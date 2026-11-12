# Configuration file for the Sphinx documentation builder.
#
# For the full list of options:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = "GRABNES"
copyright = "2022-2026, Nicolas Leconte and the GRABNES developers"
author = "Nicolas Leconte"

# The full version, including alpha/beta/rc tags
release = "0.1"

# -- General configuration ---------------------------------------------------

extensions = [
    # myst_nb includes myst_parser and also renders the original Jupyter
    # notebooks under tutorials/notebooks/ (stored outputs, never executed).
    "myst_nb",
    "sphinx_design",
    "sphinx.ext.mathjax",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
]

# Copy buttons on code blocks: strip shell prompts and Python REPL prompts.
copybutton_prompt_text = r"\$ |>>> |\.\.\. "
copybutton_prompt_is_regexp = True
copybutton_exclude = ".linenos, .gp, .go"

myst_enable_extensions = [
    "colon_fence",
    "tasklist",  # "- [ ]" task lists of the notebooks, as Jupyter shows them
    "dollarmath",
    "amsmath",
    "fieldlist",
]

# The tutorial pages are notebooks shown as saved: they need Google Colab,
# Google Drive and the compiled code, so they are never executed here.
nb_execution_mode = "off"
# Keep the outputs exactly as saved and in their order (merging would reorder
# stderr and trim text); consecutive streams are joined visually in the CSS.
nb_merge_streams = False

templates_path = ["_templates"]

# The repository root is the Sphinx source directory, so everything that is
# not website content must be excluded: build output, the README/CLAUDE docs,
# and the old (2022) sphinx tree kept for reference until migration ends.
exclude_patterns = [
    "_build",
    "public",
    # myst-nb writes notebook images next to the build folder, i.e. here
    "jupyter_execute",
    ".venv/*",
    "grabnes/*",
    "README.md",
    "CLAUDE.md",
    # README.md files inside downloadable example folders are data, not pages
    "assets/downloads/**",
    "Thumbs.db",
    ".DS_Store",
    "**/.ipynb_checkpoints",
    # the original notebooks are downloads; their cells are rendered on the
    # tutorial pages (tools/notebook_pages.py)
    "tutorials/notebooks/*.ipynb",
]

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "GRABNES documentation"
html_short_title = "GRABNES"
# assets/ holds images, sample inputs and static files; its static/ subfolder
# is served under _static/ by Sphinx.
html_static_path = ["assets/static"]
html_css_files = ["grabnes.css"]
html_js_files = ["grabnes.js"]
html_logo = "assets/static/logo1.png"
html_favicon = "assets/static/logo-icon.png"

_GITHUB_ICON = (
    '<svg stroke="currentColor" fill="currentColor" stroke-width="0" viewBox="0 0 16 16">'
    '<path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 '
    '0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 '
    '1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15'
    '-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82'
    '.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93'
    '-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path></svg>'
)

html_theme_options = {
    # Brand colours: the blue of the GRABNES wordmark, lightened for dark mode.
    "light_css_variables": {
        "color-brand-primary": "#1d4fb8",
        "color-brand-content": "#1d5bd6",
        "color-brand-visited": "#5a3fb0",
    },
    "dark_css_variables": {
        "color-brand-primary": "#8cb0ff",
        "color-brand-content": "#8cb0ff",
        "color-brand-visited": "#b9a4ff",
    },
    # "View source" button on every page, pointing to the page on GitHub.
    "source_repository": "https://github.com/gjung-group/grabnes-docs/",
    "source_branch": "main",
    "source_directory": "",
    "top_of_page_buttons": ["view"],
    "navigation_with_keys": True,
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/gjung-group/grabnes",
            "html": _GITHUB_ICON,
            "class": "",
        },
    ],
}

# Repository link buttons right below the brand (logo + title), above the search box.
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/repo-links.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}

# External links that should not be checked during builds
nitpick_ignore = []

# -- Custom directives ---------------------------------------------------------
# {task}  : exercise/exercise box used in the tutorials
# {todo}  : work-in-progress marker
# Both render as titled admonitions (styled in assets/static/grabnes.css).

from docutils import nodes
from docutils.parsers.rst import Directive


class _TitledAdmonition(Directive):
    has_content = True
    name = ""

    def run(self):
        node = nodes.admonition(classes=[self.name])
        node += nodes.title(self.name.title(), self.name.title())
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class Task(_TitledAdmonition):
    name = "task"


class Todo(_TitledAdmonition):
    name = "todo"


# -- Tutorial pages cut from the original notebooks ----------------------------
# tutorials/<page>.ipynb are verbatim runs of cells of the original notebooks
# in tutorials/notebooks/ (written and checked by tools/notebook_pages.py).
# They are rendered with their saved outputs. Each page gets its title (see
# PAGES) and a toolbar naming the original notebook and its cells, with
# "Open in Colab" and "Download" links to the original.

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).parent / "tools"))
import notebook_pages as _nbp  # noqa: E402

_NB_RANGES = _nbp.cell_ranges()


def _prompt(text, kind):
    return nodes.raw("", f'<div class="jp-prompt jp-{kind}prompt">{text}</div>', format="html")


def _jupyter_prompts(doctree, nb):
    """Add JupyterLab's prompt column: `[n]:` beside every code cell (blue)
    and beside every execute_result (red), with the execution counts saved in
    the notebook (`[ ]:` where none is saved, as Jupyter shows it)."""
    for cell in doctree.findall(nodes.container):
        if cell.get("nb_element") != "cell_code":
            continue
        source = nb["cells"][cell["cell_index"]]
        count = source.get("execution_count")
        for part in list(cell.children):
            if part.get("nb_element") == "cell_code_source":
                part.insert(0, _prompt(f"[{count if count is not None else '&nbsp;'}]:", "in"))
            elif part.get("nb_element") == "cell_code_output":
                outputs = source.get("outputs", [])
                if len(outputs) != len(part.children):
                    outputs = [{}] * len(part.children)
                rows = []
                for out, node in zip(outputs, part.children):
                    row = nodes.container(classes=["jp-output-row"])
                    if out.get("output_type") == "execute_result":
                        n = out.get("execution_count")
                        row += _prompt(f"[{n if n is not None else '&nbsp;'}]:", "out")
                    else:
                        row += _prompt("", "out")
                    row += node.deepcopy()
                    rows.append(row)
                part.children = []
                part.extend(rows)


def _notebook_page(app, doctree):
    docname = app.env.docname
    page_name = docname.removeprefix("tutorials/")
    if not docname.startswith("tutorials/") or page_name not in _nbp.PAGES:
        return
    spec = _nbp.PAGES[page_name]
    stem = spec["source"]
    first, end = _NB_RANGES[page_name]
    total = len(_nbp.load(_nbp.NB_DIR / f"{stem}.ipynb")["cells"])
    cells = "all cells" if (first, end) == (0, total) else f"cells {first + 1}&ndash;{end}"
    toolbar = nodes.raw("", (
        '<div class="notebook-toolbar">'
        f'<span class="notebook-file">{stem}.ipynb &middot; {cells}</span>'
        f'<a class="notebook-action" href="{_nbp.colab_url(stem)}" rel="noopener">'
        "Open in Colab</a>"
        f'<a class="notebook-action" href="../_downloads/notebooks/{stem}.ipynb" download>'
        "Download .ipynb</a>"
        "</div>"
    ), format="html")

    _jupyter_prompts(doctree, _nbp.load(_nbp.OUT_DIR / f"{page_name}.ipynb"))

    # Notebook metadata (docinfo) must stay a direct child of the document.
    meta = [n for n in doctree.children if isinstance(n, nodes.docinfo)]
    body = [n for n in doctree.children if not isinstance(n, nodes.docinfo)]
    if spec["title"]:
        page = nodes.section(ids=[nodes.make_id(f"tutorial-{page_name}")])
        page += nodes.title(spec["title"], spec["title"])
        page += toolbar
        page.extend(body)
    else:
        page, rest = body[0], body[1:]
        if spec["nest"]:
            page.extend(rest)  # later top-level headings become subsections
        elif rest:
            raise ValueError(f"{docname}: several top-level headings, set a title")
        page.insert(1, toolbar)
    doctree.children = []
    doctree.extend(meta)
    doctree += page


def _display_math_blocks(text):
    """Separate `$$` display-math blocks from the surrounding text.

    Jupyter shows a `$$ ... $$` block that sits inside a paragraph as display
    math; MyST only does when the block is a paragraph of its own. Blank lines
    are added before an opening and after a closing `$$` line; the text itself
    is unchanged.
    """
    out, in_math = [], False
    lines = text.split("\n")
    for k, line in enumerate(lines):
        if line.strip() == "$$":
            if not in_math and out and out[-1].strip():
                out.append("")
            out.append(line)
            if in_math and k + 1 < len(lines) and lines[k + 1].strip():
                out.append("")
            in_math = not in_math
        else:
            out.append(line)
    return "\n".join(out)


def _notebook_source(app, docname, source):
    # Rendering only; the notebook files are not changed.
    if docname.removeprefix("tutorials/") not in _nbp.PAGES:
        return
    import json

    nb = json.loads(source[0])
    for cell in nb["cells"]:
        if cell["cell_type"] != "markdown":
            continue
        text = "".join(cell["source"])
        # The notebook links to the driver library as a file next to it; on
        # the website it lives in assets/downloads/.
        text = text.replace("](./PyToGrabnes.py)", "](../assets/downloads/PyToGrabnes.py)")
        cell["source"] = _display_math_blocks(text)
    source[0] = json.dumps(nb)


def _copy_notebooks(app, exception):
    # Serve the unchanged original .ipynb files for the download links.
    if exception or app.builder.format != "html":
        return
    import shutil

    out = _Path(app.outdir, "_downloads", "notebooks")
    out.mkdir(parents=True, exist_ok=True)
    for nb in sorted(_nbp.NB_DIR.glob("*.ipynb")):
        shutil.copy2(nb, out)


def setup(app):
    app.add_directive("task", Task)
    app.add_directive("todo", Todo)
    # Before the title collector (priority 500) so the new title is used.
    app.connect("doctree-read", _notebook_page, priority=400)
    app.connect("source-read", _notebook_source)
    app.connect("build-finished", _copy_notebooks)
