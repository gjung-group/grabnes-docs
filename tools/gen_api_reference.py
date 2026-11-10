#!/usr/bin/env python3
"""Generate the Fortran API reference of GRABNES from the code repository.

Usage:
    uv run python tools/gen_api_reference.py [--src PATH] [--out PATH]

``--src`` is ``lanczosKuboCode/Src`` of a checkout of the code repository;
``--out`` is the overview page (default ``reference/units.md``). One page per
program unit is written next to it, under ``reference/api/`` (the directory is
emptied first, so units removed upstream disappear).

What is shown, and where it comes from:

* Program units, procedures, arguments, results, generic interfaces, derived
  types and module variables: parsed by Ford. Ford runs on a normalized copy in
  a temporary directory where ordinary ``!`` comments are blanked (Ford would
  otherwise mistake them for documentation); ``!!`` lines are kept. The cpp
  template fragments ``MIO/mem_temp.f90`` and ``MIO/MPI/mpi_type.f90`` are
  include files with ``[_TYPE]`` placeholders and are skipped.
* Summaries, details and argument descriptions: the Doxygen tags ``@brief``,
  ``@details``, ``@note``, ``@param`` and ``@return`` of the comment block right
  above a ``module``/``subroutine``/``function`` statement, copied verbatim.
  Ford does not read ``!>`` blocks, so they are read from the sources directly.
* Input keys: the ``!! - `Key`: description`` item that follows every line
  reading an input key (collected by Ford into the routine's ``doc_list``).
* Grouping: the object list ``OBJS`` of ``Src/Makefile`` (solver), the
  ``MIO/`` and ``math/`` directories (libraries); programs inside the library
  directories are build-time code generators; anything else is not compiled.
* Source links: the definition line in the original file, at the exact commit.

The output depends only on the sources (the date shown is the commit date), so
regenerating an unchanged commit gives an identical page.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

CODE_REPO = "https://github.com/gjung-group/grabnes"
SRC_PREFIX = "lanczosKuboCode/Src"
TEMPLATE_FRAGMENTS = {"mem_temp.f90", "mpi_type.f90"}

# ---------------------------------------------------------------------------
# Source normalization (for Ford)


def strip_comments(text: str) -> str:
    """Blank ordinary ``!`` comments; keep ``!!`` lines (Ford documentation).

    Line numbers are preserved. A ``!`` inside a quoted string does not start
    a comment.
    """
    out = []
    for line in text.splitlines():
        in_str: str | None = None
        cut = -1
        for i, ch in enumerate(line):
            if in_str:
                if ch == in_str:
                    in_str = None
            elif ch in "\"'":
                in_str = ch
            elif ch == "!":
                cut = i
                break
        if cut < 0:
            out.append(line)
        elif line.lstrip().startswith("!!"):
            out.append(line)
        elif not line[:cut].strip():
            out.append("")  # whole-line comment
        else:
            out.append(line[:cut].rstrip())  # inline comment
    return "\n".join(out) + "\n"


def fortran_files(src: Path) -> list[Path]:
    return [
        f for f in sorted(src.rglob("*"))
        if f.is_file() and f.suffix.lower() == ".f90" and f.name not in TEMPLATE_FRAGMENTS
    ]


def normalize_tree(src: Path, dst: Path) -> None:
    for f in fortran_files(src):
        target = dst / f.relative_to(src)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(strip_comments(f.read_text(errors="replace")))


# ---------------------------------------------------------------------------
# Doxygen comments and definition lines, read from the original sources

DEF_RE = re.compile(
    r"^\s*(?!end\b)(?:[\w(),=*:\s]*?\s)?(subroutine|function|module|program)\s+(\w+)\s*(?:\(|$|&|!|result\b)",
    re.IGNORECASE,
)
TAG_RE = re.compile(r"^@(\w+)(?:\[[^\]]*\])?\s*(.*)$")


@dataclass
class Doxy:
    brief: str = ""
    details: list[str] = field(default_factory=list)  # paragraphs
    notes: list[str] = field(default_factory=list)
    params: dict[str, str] = field(default_factory=dict)  # lower-case name -> text
    returns: str = ""

    def __bool__(self) -> bool:
        return bool(self.brief or self.details or self.notes or self.params or self.returns)


def parse_doxygen(block: list[str]) -> Doxy:
    """Parse ``!>``/``!!`` comment lines (top to bottom) with Doxygen tags."""
    d = Doxy()
    if not any("@" in ln for ln in block):
        return d
    target: tuple[str, str] | None = None  # (tag, param name)
    buf: list[str] = []

    def flush():
        nonlocal buf
        text = " ".join(s for s in buf if s).strip()
        buf = []
        if not target or not text:
            return
        tag, name = target
        if tag == "brief":
            d.brief = f"{d.brief} {text}".strip()
        elif tag == "details":
            d.details.append(text)
        elif tag == "note":
            d.notes.append(text)
        elif tag == "param" and name:
            d.params[name.lower()] = f"{d.params.get(name.lower(), '')} {text}".strip()
        elif tag in ("return", "returns", "retval"):
            d.returns = f"{d.returns} {text}".strip()

    prev_mark = ""
    for raw in block:
        s = raw.strip()
        if not (s.startswith("!>") or s.startswith("!!")):
            continue
        mark, s = s[:2], s[2:].strip()
        new_block = mark == "!>" and prev_mark == "!!"  # Doxygen: '!>' after '!!' opens a new block
        prev_mark = mark
        m = TAG_RE.match(s)
        if new_block and not m and s:
            flush()
            target = ("details", "") if d.brief else ("brief", "")
            buf = [s]
            continue
        if m:
            flush()
            tag, rest = m.group(1).lower(), m.group(2)
            if tag == "param":
                name, _, rest = rest.partition(" ")
                target = ("param", name.strip())
            elif tag in ("brief", "details", "note", "return", "returns", "retval"):
                target = (tag, "")
            else:
                target = None  # @file, @author, ...: not shown
            buf = [rest.strip()]
        elif not s:
            flush()  # paragraph break
            if target and target[0] == "brief":
                target = ("details", "")
        else:
            if target is None and not d.brief and not d.details:
                target = ("brief", "")
            buf.append(s)
    flush()
    return d


class SourceFile:
    """Original text of one Fortran file: definition lines and Doxygen blocks."""

    def __init__(self, path: Path):
        self.lines = path.read_text(errors="replace").splitlines()
        self.defs: dict[str, list[int]] = defaultdict(list)  # lower name -> 1-based lines
        for i, line in enumerate(self.lines, 1):
            if line.lstrip().startswith(("!", "#")):
                continue
            m = DEF_RE.match(line)
            if m and not re.match(r"^\s*module\s+procedure\b", line, re.IGNORECASE):
                self.defs[m.group(2).lower()].append(i)

    def line_of(self, name: str, after: int = 0) -> int | None:
        for ln in self.defs.get(name.lower(), []):
            if ln > after:
                return ln
        return None

    def doxygen_above(self, line: int | None) -> Doxy:
        if not line:
            return Doxy()
        i = line - 2
        block: list[str] = []
        while i >= 0 and self.lines[i].strip().startswith("!"):
            block.append(self.lines[i])
            i -= 1
        return parse_doxygen(block[::-1])

    def header_doxygen(self) -> Doxy:
        """Doxygen block at the top of the file (e.g. ``!> @file`` ... ``@brief``)."""
        block = []
        for line in self.lines:
            if line.strip().startswith("!"):
                block.append(line)
            elif line.strip():
                break
            elif block:
                break
        return parse_doxygen(block)


# ---------------------------------------------------------------------------
# Input-key items (``!! - `Key`: description``)

KEY_ITEM = re.compile(r"^-\s*`([^`]+)`:\s*(.*)$")


def key_items(p) -> list[tuple[str, str]]:
    """Input-key descriptions in a procedure's ``!!`` comments (Ford ``doc_list``).

    Upstream writes one Markdown item after every line that reads a key; its
    continuation lines are indented. Other ``!!`` lines are ignored.
    """
    items: list[list[str]] = []
    current: list[str] | None = None
    for raw in getattr(p, "doc_list", None) or []:
        m = KEY_ITEM.match(raw.strip())
        if m:
            current = [m.group(1), m.group(2).strip()]
            items.append(current)
        elif current is not None and raw.startswith("  ") and raw.strip():
            current[1] = f"{current[1]} {raw.strip()}".strip()
        else:
            current = None
    return [(k, v) for k, v in items]


# ---------------------------------------------------------------------------
# Markdown helpers


def md_text(text: str) -> str:
    """Escape what MyST would read as markup in plain text (``*``/``_`` emphasis,
    ``$`` math, ``[``/``]`` links, ``<`` HTML), outside inline code spans."""
    parts = re.split(r"(`[^`]*`)", text)
    return "".join(
        part if part.startswith("`") else re.sub(r"([*_$\[\]<])", r"\\\1", part)
        for part in parts
    )


def cell(text: str) -> str:
    """Plain text for a table cell."""
    return md_text(text).replace("|", "\\|") if text else ""


def code(text: str) -> str:
    """Inline code that survives backticks and table pipes."""
    text = str(text).replace("|", "\\|")
    return f"`` {text} ``" if "`" in text else f"`{text}`"


def table(header: list[str], rows: list[list[str]], widths: list[int]) -> list[str]:
    """A ``list-table`` with fixed relative column widths (styled by ``api-table``
    in assets/static/grabnes.css: full width, wrapping cells)."""
    out = ["```{list-table}", ":header-rows: 1", ":class: api-table",
           ":widths: " + " ".join(str(w) for w in widths), ""]
    for r in [header] + rows:
        out.append(f"* - {r[0] or ' '}")
        out += [f"  - {c or ' '}" for c in r[1:]]
    return out + ["```", ""]


def ident(name: str) -> str:
    return re.sub(r"[^a-z0-9_]+", "-", name.lower())


# ---------------------------------------------------------------------------
# Ford entities -> text


def proto_name(v) -> str:
    p = getattr(v, "proto", None)
    if not p:
        return ""
    first = p[0] if isinstance(p, (list, tuple)) else p
    return first if isinstance(first, str) else getattr(first, "name", str(first))


def type_spec(v) -> str:
    """Fortran type specification, e.g. ``real(dp)``, ``character(len=*)``."""
    t = (getattr(v, "vartype", "") or "").lower()
    if t in ("type", "class", "procedure"):
        return f"{t}({proto_name(v) or '*'})"
    if t == "character":
        ln = getattr(v, "strlen", None)
        kind = getattr(v, "kind", None)
        inner = ", ".join(x for x in [f"len={ln}" if ln else "", f"kind={kind}" if kind else ""] if x)
        return f"character({inner})" if inner else "character"
    kind = getattr(v, "kind", None)
    return f"{t}({kind})" if kind else t


def var_attribs(v, with_intent: bool = False) -> list[str]:
    attrs = []
    dim = getattr(v, "dimension", "") or ""
    if dim:
        attrs.append(f"dimension{dim}" if dim.startswith("(") else f"dimension({dim})")
    if getattr(v, "parameter", False):
        attrs.append("parameter")
    if with_intent and getattr(v, "intent", ""):
        attrs.append(f"intent({v.intent})")
    if getattr(v, "optional", False):
        attrs.append("optional")
    for a in getattr(v, "attribs", None) or []:
        a = str(a).strip()
        if a and a.lower() not in {x.lower() for x in attrs} and not a.lower().startswith(("intent", "dimension")):
            attrs.append(a)
    return attrs


def declaration(v, with_intent: bool = False) -> str:
    """Declaration as in the source, e.g. ``real(dp), dimension(3), intent(in)``."""
    return code(", ".join([type_spec(v)] + var_attribs(v, with_intent)))


def is_function(p) -> bool:
    return type(p).__name__ == "FortranFunction"


def signature(p) -> str:
    args = ", ".join(a.name for a in (getattr(p, "args", None) or []))
    prefix = " ".join(a for a in (getattr(p, "attribs", None) or []) if a.lower() in
                      ("pure", "elemental", "recursive", "impure", "module"))
    prefix = f"{prefix} " if prefix else ""
    if is_function(p):
        r = getattr(p, "retvar", None)
        rname = getattr(r, "name", p.name) if r is not None else p.name
        rtype = type_spec(r) if r is not None and getattr(r, "vartype", None) else ""
        result = f" result({rname})" if rname.lower() != p.name.lower() else ""
        typed = f"{rtype} " if rtype and not result else ""
        return f"{prefix}{typed}function {p.name}({args}){result}"
    return f"{prefix}subroutine {p.name}({args})"


def procs_of(entity) -> list:
    return list(getattr(entity, "subroutines", None) or []) + list(getattr(entity, "functions", None) or [])


def all_procs(entity, parents=()):
    """(procedure, parent names) for every procedure, nested ones included."""
    for p in procs_of(entity):
        yield p, parents
        yield from all_procs(p, parents + (p.name,))


def use_names(d) -> list[str]:
    if isinstance(d, str):
        head = d.split(",")[0].split("(")[0].strip()
        return [] if not head or head.lower().startswith("only") else [head]
    if isinstance(d, (list, tuple, set)):
        return [n for x in d for n in use_names(x)]
    return [getattr(d, "name", str(d)).strip()]


# ---------------------------------------------------------------------------
# Model


@dataclass
class Unit:
    kind: str  # "program" | "module"
    obj: object
    path: str  # relative to Src, posix
    group: str
    label: str = ""
    page: str = ""
    uses: list[str] = field(default_factory=list)
    used_by: list[str] = field(default_factory=list)

    @property
    def name(self) -> str:
        return self.obj.name


GROUPS = [
    ("solver", "Solver", "The `grabnes` program and the modules compiled into it (the object list `OBJS` of `Src/Makefile`)."),
    ("mio", "MIO library", "Memory, input and output library (`MIO/`, built as `libMIO.a`): input parsing, messages, files, timers, OpenMP and MPI support."),
    ("math", "Math library", "Numerical routines (`math/`, built as `libmath.a`)."),
    ("generator", "Build-time code generators", "Programs compiled and run by the makefiles of the libraries to generate Fortran sources before the build."),
    ("unbuilt", "Sources not in the solver build", "Files in `Src/` that are not in the object list of `Src/Makefile` and are therefore not compiled into `grabnes`."),
]


def makefile_objects(src: Path) -> set[str]:
    mk = src / "Makefile"
    if not mk.exists():
        return set()
    text = mk.read_text(errors="replace").replace("\\\n", " ")
    m = re.search(r"^OBJS\s*:?=\s*(.*)$", text, re.MULTILINE)
    return {Path(o).stem.lower() for o in m.group(1).split() if o.endswith(".o")} if m else set()


def classify(path: str, kind: str, objs: set[str]) -> str:
    top = path.split("/")[0]
    stem = Path(path).stem.lower()
    if top in ("MIO", "math"):
        return "generator" if kind == "program" else top.lower()
    if stem in objs or (kind == "program" and stem == "grabnes"):
        return "solver"
    return "unbuilt"


# ---------------------------------------------------------------------------
# Rendering


class Renderer:
    def __init__(self, units: list[Unit], sources: dict[str, SourceFile], commit: str, date: str, ford_version: str):
        self.units = units
        self.sources = sources
        self.commit = commit
        self.date = date
        self.ford_version = ford_version
        self.by_name: dict[str, Unit] = {}
        for u in units:  # first unit of a name wins (the built one sorts first)
            self.by_name.setdefault(u.name.lower(), u)

    # -- links ------------------------------------------------------------
    def src_url(self, path: str, line: int | None = None) -> str:
        if not self.commit:
            return ""
        url = f"{CODE_REPO}/blob/{self.commit}/{SRC_PREFIX}/{path}"
        return f"{url}#L{line}" if line else url

    def src_link(self, path: str, line: int | None = None, text: str | None = None) -> str:
        label = text or (f"{SRC_PREFIX}/{path}" + (f", line {line}" if line else ""))
        url = self.src_url(path, line)
        return f"[{code(label) if text is None else label}]({url})" if url else code(label)

    def unit_ref(self, name: str) -> str:
        u = self.by_name.get(name.lower())
        return f"{{ref}}`{name} <{u.label}>`" if u else code(name)

    # -- overview ---------------------------------------------------------
    def overview(self) -> str:
        stats = self.stats()
        short = self.commit[:7] if self.commit else "unknown"
        commit_link = f"[`{short}`]({CODE_REPO}/tree/{self.commit})" if self.commit else "`unknown`"
        out = [
            "(api-units)=",
            "# Fortran unit reference",
            "",
            "Reference documentation of every program unit in `lanczosKuboCode/Src/` of the",
            f"[GRABNES code repository]({CODE_REPO}): procedures with their arguments,",
            "generic interfaces, derived types, module variables, the dependencies",
            "between units, and the input keys read by each routine.",
            "",
            ":::{admonition} Provenance",
            ":class: note",
            "",
            f"Generated by `tools/gen_api_reference.py` with Ford {self.ford_version} from commit",
            f"{commit_link} of the code repository ({self.date}). Do not edit by hand; the page is",
            "regenerated whenever the synchronization with the code repository brings new sources.",
            "Descriptions are quoted verbatim from the Doxygen (`@brief`, `@param`, ...) and",
            "Ford (`!!`) comments of the sources; an entry without a description has none in the source.",
            ":::",
            "",
            "::::{grid} 2 2 4 4",
            ":gutter: 2",
            "",
        ]
        for value, what in stats:
            out += [f":::{{grid-item-card}} {value}", ":text-align: center", "", what, ":::", ""]
        out += ["::::", ""]

        for gid, title, blurb in GROUPS:
            members = [u for u in self.units if u.group == gid]
            if not members:
                continue
            out += [f"(api-group-{gid})=", f"## {title}", "", blurb, ""]
            rows = []
            for u in members:
                pubs = [p for p in self.public_procs(u)]
                nkeys = sum(len(key_items(p)) for p, _ in self.all_procs(u.obj))
                rows.append([
                    self.unit_ref(u.name) if self.by_name.get(u.name.lower()) is u else f"{{ref}}`{u.name} <{u.label}>`",
                    u.kind,
                    self.src_link(u.path, text=code(u.path)),
                    str(len(pubs)) if pubs else "—",
                    str(nkeys) if nkeys else "—",
                ])
            out += table(["Unit", "Kind", "Source", "Public procedures", "Input-key reads"], rows, [22, 12, 32, 17, 17])

        out += [
            "```{note}",
            "The cpp template fragments `MIO/mem_temp.f90` and `MIO/MPI/mpi_type.f90` are include",
            "files with `[_TYPE]` placeholders, expanded by the code generators above; they are",
            "not program units and are not listed.",
            "```",
            "",
            "```{toctree}",
            ":hidden:",
            "",
        ]
        out += [u.page for u in self.units]
        out += ["```", ""]
        return "\n".join(out)

    def stats(self) -> list[tuple[str, str]]:
        n_units = len(self.units)
        n_pub = sum(len(self.public_procs(u)) for u in self.units)
        n_if = sum(len(self.interfaces(u)) for u in self.units)
        n_keys = sum(len(key_items(p)) for u in self.units for p, _ in self.all_procs(u.obj))
        return [
            (str(n_units), "program units"),
            (str(n_pub), "public procedures"),
            (str(n_if), "generic interfaces"),
            (str(n_keys), "documented input-key reads"),
        ]

    # -- unit queries -----------------------------------------------------
    def unit_doxy(self, u: Unit) -> Doxy:
        sf = self.sources[u.path]
        d = sf.doxygen_above(sf.line_of(u.name))
        return d if d else sf.header_doxygen()

    def public_procs(self, u: Unit) -> list:
        if u.kind == "program":
            return []
        return sorted(
            (p for p in (getattr(u.obj, "pub_procs", None) or {}).values()
             if type(p).__name__ in ("FortranSubroutine", "FortranFunction")),
            key=lambda p: p.name.lower(),
        )

    def interfaces(self, u: Unit) -> list:
        if u.kind == "program":
            return []
        return sorted(
            (p for p in (getattr(u.obj, "pub_procs", None) or {}).values()
             if type(p).__name__ == "FortranInterface"),
            key=lambda p: p.name.lower(),
        )

    all_procs = staticmethod(lambda entity, parents=(): all_procs(entity, parents))

    # -- unit page --------------------------------------------------------
    def unit_page(self, u: Unit) -> str:
        sf = self.sources[u.path]
        uline = sf.line_of(u.name)
        doxy = self.unit_doxy(u)
        pubs = self.public_procs(u)
        ifaces = self.interfaces(u)
        types = sorted((getattr(u.obj, "pub_types", None) or {}).values(), key=lambda t: t.name.lower()) \
            if u.kind == "module" else []
        variables = sorted(
            (v for v in (getattr(u.obj, "pub_vars", None) or {}).values()
             if not type(v).__name__.startswith("FortranNamelist")),
            key=lambda v: v.name.lower(),
        ) if u.kind == "module" else []
        anchors = {p.name.lower(): f"{u.label}-{ident(p.name)}" for p in pubs}

        dup = sum(1 for v in self.units if v.name.lower() == u.name.lower()) > 1
        title = f"{code(u.name)} ({code(Path(u.path).name)})" if dup else code(u.name)
        out = [f"({u.label})=", f"# {title}", ""]
        if doxy.brief:
            out += [md_text(doxy.brief), ""]
        for para in doxy.details:
            out += [md_text(para), ""]
        for note in doxy.notes:
            out += ["```{note}", md_text(note), "```", ""]

        group_title = next(t for g, t, _ in GROUPS if g == u.group)
        nkeys = sum(len(key_items(p)) for p, _ in self.all_procs(u.obj))
        facts = [
            ["Kind", u.kind.capitalize()],
            ["Source", self.src_link(u.path, uline, text=code(f"{SRC_PREFIX}/{u.path}"))],
            ["Group", f"{{ref}}`{group_title} <api-group-{u.group}>`"],
            ["Uses", ", ".join(self.unit_ref(n) for n in u.uses) or "—"],
            ["Used by", ", ".join(self.unit_ref(n) for n in u.used_by) or "—"],
        ]
        if u.kind == "module":
            facts.append(["Public interface", ", ".join(x for x in [
                f"{len(pubs)} procedure{'s' if len(pubs) != 1 else ''}" if pubs else "",
                f"{len(ifaces)} generic interface{'s' if len(ifaces) != 1 else ''}" if ifaces else "",
                f"{len(types)} derived type{'s' if len(types) != 1 else ''}" if types else "",
                f"{len(variables)} variable{'s' if len(variables) != 1 else ''}" if variables else "",
            ] if x) or "none"])
        if nkeys:
            facts.append(["Input keys", f"{nkeys} reads (see the procedures below)"])
        out += [f":{k}: {v}" for k, v in facts] + [""]

        if pubs:
            out += ["## Procedure summary", ""]
            rows = []
            for p in pubs:
                d = sf.doxygen_above(sf.line_of(p.name))
                rows.append([
                    f"{{ref}}`{p.name} <{anchors[p.name.lower()]}>`",
                    cell(d.brief) or "—",
                ])
            out += table(["Procedure", "Description"], rows, [36, 64])

        if ifaces:
            out += ["## Generic interfaces", ""]
            rows = []
            for i in ifaces:
                specifics = [getattr(m, "name", str(m)) for m in (getattr(i, "modprocs", None) or [])]
                specifics += [r.name for r in (getattr(i, "routines", None) or []) if getattr(r, "name", None)
                              and r.name not in specifics]
                links = [f"{{ref}}`{s} <{anchors[s.lower()]}>`" if s.lower() in anchors else code(s) for s in specifics]
                rows.append([code(i.name), ", ".join(links) or "—"])
            out += table(["Interface", "Specific procedures"], rows, [30, 70])

        if pubs:
            out += ["## Procedures", ""]
            for p in pubs:
                out += self.procedure(u, sf, p, anchors[p.name.lower()])

        if types:
            out += ["## Derived types", ""]
            for t in types:
                tline = sf.line_of(t.name)
                out += [f"({u.label}-type-{ident(t.name)})=", f"### {code(t.name)}", ""]
                comps = list(getattr(t, "variables", None) or [])
                if comps:
                    out += table(["Component", "Declaration", "Default"], [
                        [code(c.name), declaration(c),
                         code(c.initial) if getattr(c, "initial", None) else "—"] for c in comps], [24, 46, 30])
                out += [f"Defined in {self.src_link(u.path, tline)}." if tline else "", ""]

        if variables:
            out += ["## Module variables", ""]
            out += table(["Name", "Declaration", "Initial value"], [
                [code(v.name), declaration(v),
                 code(v.initial) if getattr(v, "initial", None) else "—"] for v in variables], [26, 44, 30])

        others = [(p, parents) for p, parents in self.all_procs(u.obj)
                  if key_items(p) and not (not parents and p.name.lower() in anchors)
                  and not (parents and parents[0].lower() in anchors)]
        if others:
            out += [
                "## Input keys read by private procedures", "",
                "Procedures that are not part of the public interface but read input keys.", "",
            ]
            for p, parents in others:
                out += self.key_block(u, sf, p, parents)
        return "\n".join(out).rstrip() + "\n"

    def procedure(self, u: Unit, sf: SourceFile, p, anchor: str) -> list[str]:
        line = sf.line_of(p.name)
        d = sf.doxygen_above(line)
        out = [f"({anchor})=", f"### {code(p.name)}", "", "```fortran", signature(p), "```", ""]
        if d.brief:
            out += [md_text(d.brief), ""]
        for para in d.details:
            out += [md_text(para), ""]
        for note in d.notes:
            out += ["```{note}", md_text(note), "```", ""]
        args = list(getattr(p, "args", None) or [])
        if args:
            out += ["```{rubric} Arguments", "```", ""]
            out += table(["Name", "Declaration", "Description"], [
                [code(a.name), declaration(a, with_intent=True),
                 cell(d.params.get(a.name.lower(), "")) or "—"] for a in args], [18, 40, 42])
        if is_function(p):
            r = getattr(p, "retvar", None)
            if r is not None:
                attrs = ", ".join(code(x) for x in var_attribs(r))
                rdesc = f" {cell(d.returns)}" if d.returns else ""
                out += ["```{rubric} Returns", "```", "",
                        f"{code(r.name)}: {code(type_spec(r))}" + (f", {attrs}" if attrs else "") + (f".{rdesc}" if rdesc else ""), ""]
        own = key_items(p)
        nested = [(q, parents) for q, parents in self.all_procs(p, (p.name,)) if key_items(q)]
        if own or nested:
            n = len(own) + sum(len(key_items(q)) for q, _ in nested)
            out += [f"```{{rubric}} Input keys read ({n})", "```", ""]
            if own:
                out += table(["Key", "Description"], [[code(k), cell(v)] for k, v in own], [34, 66])
            for q, parents in nested:
                out += self.key_block(u, sf, q, parents, after=line or 0)
        if line:
            out += [f"Defined in {self.src_link(u.path, line)}.", ""]
        return out

    def key_block(self, u: Unit, sf: SourceFile, p, parents, after: int = 0) -> list[str]:
        line = sf.line_of(p.name, after)
        where = f"internal procedure of {code(parents[-1])}" if parents else (getattr(p, "permission", "") or "private")
        src = f", {self.src_link(u.path, line, text='source')}" if line else ""
        out = [f"**{code(p.name)}** ({where}{src})", ""]
        out += table(["Key", "Description"], [[code(k), cell(v)] for k, v in key_items(p)], [34, 66])
        return out


# ---------------------------------------------------------------------------


def git(src: Path, *args: str) -> str:
    try:
        return subprocess.run(["git", "-C", str(src), *args], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ""


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", default="../grabnes/lanczosKuboCode/Src")
    ap.add_argument("--out", default="reference/units.md")
    a = ap.parse_args()

    src = Path(a.src).resolve()
    if not src.is_dir():
        sys.exit(f"source directory not found: {src}")
    import ford
    from ford import ProjectSettings
    from ford.fortran_project import Project

    commit = git(src, "rev-parse", "HEAD")
    date = git(src, "log", "-1", "--format=%cs") or "unknown date"
    sources = {f.relative_to(src).as_posix(): SourceFile(f) for f in fortran_files(src)}
    objs = makefile_objects(src)

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        normalize_tree(src, tmp)
        project = Project(ProjectSettings(src_dir=[tmp], extensions=["f90"], preprocessor=""))

        units: list[Unit] = []
        for kind, objs_ in (("program", project.programs), ("module", project.modules)):
            for o in objs_:
                path = Path(o.source_file.path).relative_to(tmp).as_posix()
                units.append(Unit(kind, o, path, classify(path, kind, objs)))

        order = {g: i for i, (g, _, _) in enumerate(GROUPS)}
        units.sort(key=lambda u: (order[u.group], u.kind != "program", u.name.lower(), u.path))
        out = Path(a.out)
        api_dir = out.parent / "api"
        seen: set[str] = set()
        for u in units:
            label = f"api-{u.name.lower()}"
            if label in seen:
                label = f"api-{u.name.lower()}-{Path(u.path).stem.lower()}"
            seen.add(label)
            u.label = label
            u.page = f"api/{label.removeprefix('api-')}"
            # use statements of the unit and of every procedure in it
            entities = [u.obj] + [p for p, _ in all_procs(u.obj)]
            u.uses = sorted({n for e in entities for d in (getattr(e, "uses", None) or []) for n in use_names(d)
                             if n and n.lower() != u.name.lower()}, key=str.lower)
        names = {u.name.lower() for u in units}
        for u in units:
            for n in u.uses:
                if n.lower() in names:
                    for v in units:
                        if v.name.lower() == n.lower() and u.name not in v.used_by:
                            v.used_by.append(u.name)
                            break
        for u in units:
            u.used_by.sort(key=str.lower)

        r = Renderer(units, sources, commit, date, ford.__version__)
        if api_dir.exists():
            shutil.rmtree(api_dir)
        api_dir.mkdir(parents=True)
        for u in units:
            (out.parent / f"{u.page}.md").write_text(r.unit_page(u))
        out.write_text(r.overview())

    print(f"wrote {out} and {len(units)} unit pages in {api_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
