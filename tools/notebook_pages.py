"""Tutorial pages cut from the original Jupyter notebooks.

The original notebooks live unchanged in ``tutorials/notebooks/``. Every
tutorial page is a notebook ``tutorials/<page>.ipynb`` holding a contiguous
run of cells of one original notebook, copied byte for byte (source, outputs,
metadata), so the site shows exactly what the notebooks contain.

    uv run python tools/notebook_pages.py           # (re)write the pages
    uv run python tools/notebook_pages.py --check   # exit 1 if a page differs

A page starts at the cell whose source is exactly ``start`` (``None``: the
first cell) and runs up to the start of the next page cut from the same
notebook, or to the end of the notebook. conf.py imports PAGES to give each
page its title and its "Open in Colab" / "Download" toolbar.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NB_DIR = ROOT / "tutorials" / "notebooks"
OUT_DIR = ROOT / "tutorials"

# Colab links of the originals. The Twistronics notebook has its own shared
# Colab copy; the others open the file of this repository.
COLAB = {
    "Twistronics2023": "https://colab.research.google.com/drive/12_ofrjJi4pr6U9j-ER1WocYJkqxEffs-?usp=sharing",
}
COLAB_GITHUB = (
    "https://colab.research.google.com/github/gjung-group/grabnes-docs/blob/main/"
    "tutorials/notebooks/{stem}.ipynb"
)

# page -> source notebook, first cell, and how to title the page:
#   title=None: the first heading of the page is its title; later top-level
#               headings of the page are nested under it (nest=True).
#   title="..": the page has several top-level headings; they are nested
#               under this title.
PAGES = {
    "introduction": dict(source="Twistronics2023", start="# Introduction",
                         title=None, nest=True),
    "graphene": dict(source="Twistronics2023", start="# Graphene",
                     title=None, nest=False),
    "bilayer-graphite": dict(source="Twistronics2023",
                             start="# Bernal stacked bilayer graphene: bilayer and bulk graphite",
                             title=None, nest=False),
    "tbg": dict(source="Twistronics2023", start="# Twisted Bilayer Graphene",
                title=None, nest=False),
    "graphene-on-hbn": dict(source="Twistronics2023", start="# Graphene on h-BN",
                            title=None, nest=True),
    "input-files": dict(source="grabnes2", start=None,
                        title="Input files", nest=False),
    "tbg-input": dict(source="grabnes3", start=None,
                      title="Twisted bilayer graphene input files", nest=False),
    "plotting": dict(source="results", start=None,
                     title="Plotting results", nest=False),
}


def colab_url(stem: str) -> str:
    return COLAB.get(stem, COLAB_GITHUB.format(stem=stem))


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def cell_ranges() -> dict[str, tuple[int, int]]:
    """page -> (first, end) cell indices (end exclusive) in its source."""
    ranges = {}
    by_source: dict[str, list[tuple[int, str]]] = {}
    for page, spec in PAGES.items():
        nb = load(NB_DIR / f"{spec['source']}.ipynb")
        cells = nb["cells"]
        if spec["start"] is None:
            first = 0
        else:
            hits = [i for i, c in enumerate(cells)
                    if "".join(c["source"]).strip() == spec["start"]]
            if len(hits) != 1:
                sys.exit(f"{page}: start cell {spec['start']!r} found {len(hits)} times "
                         f"in {spec['source']}.ipynb")
            first = hits[0]
        by_source.setdefault(spec["source"], []).append((first, page))
    for source, starts in by_source.items():
        n = len(load(NB_DIR / f"{source}.ipynb")["cells"])
        starts.sort()
        for k, (first, page) in enumerate(starts):
            end = starts[k + 1][0] if k + 1 < len(starts) else n
            ranges[page] = (first, end)
    return ranges


def page_notebook(page: str, rng: tuple[int, int]) -> dict:
    spec = PAGES[page]
    nb = load(NB_DIR / f"{spec['source']}.ipynb")
    out = {k: v for k, v in nb.items() if k != "cells"}
    out["cells"] = nb["cells"][rng[0]:rng[1]]
    return out


def dump(nb: dict) -> str:
    return json.dumps(nb, indent=1, ensure_ascii=False) + "\n"


def main(argv: list[str]) -> int:
    check = "--check" in argv
    bad = 0
    for page, rng in cell_ranges().items():
        want = page_notebook(page, rng)
        path = OUT_DIR / f"{page}.ipynb"
        src = PAGES[page]["source"]
        if check:
            have = load(path) if path.exists() else None
            if have != want:
                print(f"DIFFERS  {path.relative_to(ROOT)} (cells {rng[0] + 1}-{rng[1]} of {src}.ipynb)")
                bad += 1
            else:
                print(f"ok       {path.relative_to(ROOT)} = cells {rng[0] + 1}-{rng[1]} of {src}.ipynb")
        else:
            path.write_text(dump(want), encoding="utf-8")
            print(f"wrote    {path.relative_to(ROOT)} = cells {rng[0] + 1}-{rng[1]} of {src}.ipynb")
    # every cell of every original notebook is on exactly one page
    for source in {s["source"] for s in PAGES.values()}:
        n = len(load(NB_DIR / f"{source}.ipynb")["cells"])
        covered = sorted(r for p, r in cell_ranges().items() if PAGES[p]["source"] == source)
        if covered[0][0] != 0 or covered[-1][1] != n or any(
                a[1] != b[0] for a, b in zip(covered, covered[1:])):
            print(f"GAP      {source}.ipynb: pages do not cover all {n} cells")
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
