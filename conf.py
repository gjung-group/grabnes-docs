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
    "dollarmath",
    "amsmath",
    "fieldlist",
]

# Notebooks are shown as saved: they need Google Colab, Google Drive and the
# compiled code, so they are never executed during the build.
nb_execution_mode = "off"
# Plots are stored as PNG and the notebooks' HTML outputs as text: prefer the
# image, then plain text.
nb_mime_priority_overrides = [("html", "text/html", None)]
nb_merge_streams = True

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


# -- Original notebooks (tutorials/notebooks/) --------------------------------
# The notebooks are rendered verbatim. Several of them have more than one
# top-level heading, so the page title comes from this table instead: the
# notebook's own sections are nested below it. Every notebook page also gets a
# toolbar with "Open in Colab" and "Download" links.

NOTEBOOKS = {
    "Twistronics2023": "Twistronics 2023 workshop notebook",
    "grabnes2": "Input files notebook",
    "grabnes3": "Twisted bilayer graphene input notebook",
    "results": "Plotting results notebook",
}
_NB_DIR = "tutorials/notebooks/"
_COLAB = (
    "https://colab.research.google.com/github/gjung-group/grabnes-docs/blob/main/"
)


def _notebook_page(app, doctree):
    docname = app.env.docname
    if not docname.startswith(_NB_DIR) or docname[len(_NB_DIR):] not in NOTEBOOKS:
        return
    stem = docname[len(_NB_DIR):]
    title = NOTEBOOKS[stem]
    page = nodes.section(ids=[nodes.make_id(f"notebook-{stem}")])
    page += nodes.title(title, title)
    toolbar = (
        '<div class="notebook-toolbar">'
        f'<span class="notebook-file">{stem}.ipynb</span>'
        f'<a class="notebook-action" href="{_COLAB}{docname}.ipynb" rel="noopener">'
        "Open in Colab</a>"
        f'<a class="notebook-action" href="../../_downloads/notebooks/{stem}.ipynb" download>'
        "Download .ipynb</a>"
        "</div>"
    )
    page += nodes.raw("", toolbar, format="html")
    # Notebook metadata (docinfo) must stay a direct child of the document.
    meta = [n for n in doctree.children if isinstance(n, nodes.docinfo)]
    page.extend(n for n in doctree.children if not isinstance(n, nodes.docinfo))
    doctree.children = []
    doctree.extend(meta)
    doctree += page


def _notebook_links(app, docname, source):
    # The notebooks link to the driver library as a file next to them; on the
    # website it lives in assets/downloads/. Only the rendered page changes.
    if docname.startswith(_NB_DIR):
        source[0] = source[0].replace(
            "](./PyToGrabnes.py)", "](../../assets/downloads/PyToGrabnes.py)"
        )


def _copy_notebooks(app, exception):
    # Serve the unchanged .ipynb files at a stable URL for the download links.
    if exception or app.builder.format != "html":
        return
    import shutil
    from pathlib import Path

    out = Path(app.outdir, "_downloads", "notebooks")
    out.mkdir(parents=True, exist_ok=True)
    for stem in NOTEBOOKS:
        shutil.copy2(Path(app.srcdir, _NB_DIR, f"{stem}.ipynb"), out)


def setup(app):
    app.add_directive("task", Task)
    app.add_directive("todo", Todo)
    # Before the title collector (priority 500) so the new title is used.
    app.connect("doctree-read", _notebook_page, priority=400)
    app.connect("source-read", _notebook_links)
    app.connect("build-finished", _copy_notebooks)
