# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 1. What this repository is

This repo (`gjung-group/grabnes-docs`, formerly `grabnes.github.com`) is the **source of the GRABNES project website**, published via GitHub Pages. It does **not** contain the Fortran code itself (that lives in the separate `grabnes` code repository, sibling `../grabnes`, `github.com/gjung-group/grabnes`).

GRABNES (**GRA**phene/**B**N **E**lectronic **S**tructure) is a Fortran tight-binding package for layered 2D materials — graphene, hBN, twisted bilayer and multilayer graphene, graphene on hBN, etc. Key capabilities (from the old docs, `index.rst`):

- Builds commensurate moiré supercells with controllable twist angle and layer sliding (Hermann `n1 n2 n3 n4` indices); interfaces with LAMMPS for relaxation (`.mol` in / relaxed `.xyz` out).
- Observables: band structures, DOS (Lanczos recursion + exact diagonalization), unfolded spectral functions (ARPES comparison), LDOS, probability density, Kubo–Greenwood conductivity, magnetic-field (Landau-level) DOS with disorder.
- TB models: F2G2 (intralayer, from MLWFs), reparametrized two-center (TC) models for interlayer, "hybrid" F2G2+TC models, and the SHE model (TC variant tuned so the magic angle lands at a chosen value).
- OMP parallelization; tested with Intel compilers; built with a `make.sys` makefile (`make clean && make`, needs an empty `.version` file).

## 2. Commands

```bash
uv sync                                                   # create .venv from pyproject/uv.lock
uv run sphinx-build -b html . _build                      # local preview: open _build/index.html
uv run sphinx-build -b html -W --keep-going . _build      # what CI runs; must give zero warnings
uv run python tools/sync_from_code_repo.py [--check]      # sync mirrored files with upstream main
uv run python tools/gen_api_reference.py [--src PATH] [--out PATH]   # regenerate reference/units.md + reference/api/ (sync runs it)
```

**Sync with the code repo.** The source of truth is `main` of `github.com/gjung-group/grabnes` (never a fork or the local `../grabnes`): `sync_from_code_repo.py` shallow-clones it with GitPython and mirrors `docs/development`, `docs/user-guide`, example inputs (→ `assets/downloads/examples/`), reference figures (→ `assets/images/examples/`) and regenerates the API reference (`reference/units.md`, `reference/api/`). `--check` only reports drift (exit 1). Hand-written pages derived from upstream (`development/index.md`, `theory/tapw-procedure.md`, `examples/*.md`) are tracked by upstream object hashes in `tools/sync-state.json`; the script prints `MANUAL` when their source changed — update them by hand, verbatim, then re-run to record the new baseline. The sync is run by hand (there is no automatic sync workflow). Last synced: `7b24d66`.

There are no tests or linters; "passes" means the `-W` Sphinx build succeeds.

CI (`.github/workflows/docs.yml`): push to `main` → `uv sync` → `uv run sphinx-build -b html -W --keep-going . public` → `upload-pages-artifact` → GitHub Pages (Settings → Pages → "GitHub Actions"). Also builds on PRs; deploys only from `main` (push or `workflow_dispatch`). Live site: <https://gjung-group.github.io/grabnes-docs/>.

## 3. Current contents of this repo

```
README.md                  # intent of the site
grabnes.tar.gz             # 79 MB archive of the OLD sphinx tree — duplicate of grabnes/**, do not use
grabnes/var/www/sphinx/grabnesDocs/    # the OLD (2022) Sphinx docs — raw material ONLY
├── index.rst              # description, install, illustration gallery (some sections are empty stubs)
├── grabnes.rst            # Fortran API stubs (f:automodule — sources NOT in this repo)
├── tbModels.rst           # hybrid F2G2–TC model slides (images only, incomplete)
├── tutorial.rst, workshop.rst   # thin wrappers pointing at notebooks
├── conf.py                # old config (sphinxfortran + nbsphinx, classic theme)
├── figures/               # 10 PNGs
├── notebooks/             # the real content, see below
└── _build/                # stale generated HTML — never edit or reference
```

**Do not** build the old Sphinx tree in place, and do not add new pages to it. It is gitignored, read-only input for the migration. Never touch `grabnes.tar.gz` or `_build/` output; they will be removed once migration is done.

### The notebook content (primary source of prose)

- `notebooks/Twistronics2023.ipynb` — the flagship tutorial (~25k chars of markdown): graphene (build cell, bands, DOS) → AB-stacked bilayer & bulk graphite → twisted bilayer graphene (commensurate cells, Hamiltonian, Lanczos DOS, flat bands) → graphene on hBN (input flags, Hamiltonian visualization, magnetic-field DOS with/without Anderson disorder). Colab-oriented (`drive.mount`, Intel oneAPI setup) — strip that scaffolding when migrating.
- `notebooks/grabnes2.ipynb`, `grabnes3.ipynb` — input-file tutorials (`Gendata_graphene.in`, `Gendata_moire.in`, `ReadXYZ` for relaxed structures).
- `notebooks/results.ipynb` — plotting recipes (bands, DOS) in Python.
- Supporting files worth migrating next to the tutorial pages: `Gendata.in`, `BLBL.mol`, `BLBL.frac/.cart`, `moire.fdf`, `sublattices.dat`, `GenMoire.f90_tBG_template.f90`, `PyToGrabnes.py`, `createXYZ.py`, `fracToCart.py`, `replaceFrac.py`, `graphene/` sample outputs. Skip binaries/`a.out`, `__pycache__`, `.ipynb_checkpoints`, `.DS_Store`.

Known external links: Colab notebook `https://colab.research.google.com/drive/12_ofrjJi4pr6U9j-ER1WocYJkqxEffs-`, related code `https://github.com/gjung-group/JeilJungGroupCodes.git`, `https://github.com/qtm-iisc/Twister`, ARPES paper `https://www.nature.com/articles/s41567-020-0974-x`. Author/copyright in old conf.py: Nicolas Leconte (2022), group: gjung-group (G. Jung, U. Liège).

## 4. Target website (agreed design decisions)

- **Stack: modernized Sphinx** — MyST-Markdown sources (`myst-parser`), `myst-nb` off (notebooks are converted, not embedded), `sphinx-design`, `sphinxcontrib-bibtex` if references grow, **Furo** theme (as set in `conf.py`/`pyproject.toml`), MathJax for equations. Build via `sphinx-build`; deploy with GitHub Actions to GitHub Pages. `conf.py` also defines custom `{task}` and `{todo}` admonition directives (styled in `assets/static/grabnes.css`).
- **Notebooks → Markdown pages**: convert markdown cells to MyST prose, keep representative code snippets (fenced, trimmed of Colab plumbing), reference static images from `figures/` instead of embedded base64 outputs. Keep the original `.ipynb` files downloadable under `downloads/` (or attach on pages).
- **Layout**: the **repository root is the Sphinx source directory** — no `docs/` folder, no symlinks; every section is a real top-level folder:

```
conf.py                    # project config (furo theme, myst, math, links)
index.md                   # landing page: what GRABNES is + feature gallery
installation.md            # compile (make.sys, Intel/gfortran, OMP) + Colab
pyproject.toml             # deps (sphinx, furo, myst-parser, sphinx-design, ford); uv sync
assets/                    # ALL binary/support files (single source of truth)
├── images/                # PNGs from grabnes/.../figures/ + examples/*/reference/
├── downloads/             # sample inputs, scripts, notebooks, example folders
│   └── examples/          # per-example inputs/scripts mirrored from the code repo
└── static/                # css/js/logo (served under _static/ by Sphinx)
theory/                    # models.md, moire-cells.md, observables.md, tapw-procedure.md
examples/                  # index + getting-started (01–04), moire (05–09), arpes (10–11, spectral functions)
user-guide/                # input-file, input-keys (generated table), tapw-soc-input
tutorials/                 # graphene, bilayer-graphite, tbg, graphene-on-hbn,
                           # input-reference, plotting (+ index)
benchmarks/                # benchmarks section sources
development/               # code-structure guide + documents copied from the code
                           # repo (functionality-status, validation, conventions…)
reference/index.md         # "API Reference" entry page (unit tables, links into units)
reference/units.md         # generated Fortran unit reference (overview) — never hand-edit
reference/api/             # generated: one page per Fortran unit — never hand-edit
tools/gen_api_reference.py # regenerates reference/units.md + reference/api/ (Ford + Doxygen comments)
.github/workflows/docs.yml # build + deploy to GitHub Pages
```

  Non-content markdown (`README.md`, `CLAUDE.md`), the old `grabnes/` tree and everything under `assets/downloads/` (its `README.md` files are data, not pages) are excluded in `conf.py`'s `exclude_patterns`.

- Markdown pages cross-link with `{doc}` roles; images are referenced as `assets/images/...` (root pages) or `../assets/images/...` (section pages); downloads as `assets/downloads/...`.
- Site tone: scientific documentation; every tutorial page ends with "Download this tutorial (.ipynb / input files)" links where sources exist.

## 5. Migration map (old → new)

| Old source | New location | Notes |
|---|---|---|
| `index.rst` "Description" | `index.md` | rewrite, add feature cards (sphinx-design grid) |
| `index.rst` "Getting started"/"Installation" | `installation.md` | keep Colab + compile paths |
| `index.rst` "Illustrations" (tBG, t20G, ARPES) | `benchmarks/index.md` (+ pages) | empty stubs (gap estimation, supermoire, impurities) → marked *coming soon*, do not invent content |
| `tbModels.rst` + `GBNtwoLayers*.png` | `theory/models.md` | slides are image-only; write prose around them from notebook theory |
| `grabnes.rst` (f:automodule stubs) | `reference/index.md` | module list + `codeStructure.png` + link to code repo; sphinxfortran is dead, drop it |
| `Twistronics2023.ipynb` §Graphene | `tutorials/graphene.md` | |
| `Twistronics2023.ipynb` §Bernal/graphite | `tutorials/bilayer-graphite.md` | |
| `Twistronics2023.ipynb` §tBG | `tutorials/tbg.md` | merge `grabnes3.ipynb` (ReadXYZ workflow) here |
| `Twistronics2023.ipynb` §Graphene on hBN + magnetic DOS | `tutorials/graphene-on-hbn.md`, `magnetic-field.md` | |
| `grabnes2.ipynb` | `tutorials/input-reference.md` + graphene tutorial | input-flag documentation |
| `results.ipynb` | `tutorials/plotting.md` | Python post-processing recipes |
| `figures/*.png` | `assets/images/` | rename to kebab-case when unambiguous |
| `notebooks/*.{in,mol,dat,f90,py}` | `assets/downloads/` | sample inputs/scripts |
| code repo `examples/*/README.md` + figures | `examples/{getting-started,moire,arpes}.md` + `assets/{images,downloads}/examples/` | mirrored October 2026; reference `.dat` data stays in the code repo |
| code repo `docs/user-guide/*.md` | `user-guide/` | `input-keys.md` is generated from source — regenerate, never hand-edit |
| code repo `docs/development/*.md` | `development/` | verbatim copies; `README.md` folded into `index.md` |
| code repo `docs/theory/tapw-procedure.tex` | `theory/tapw-procedure.md` | LaTeX → MyST, formulas verbatim |

## 6. Working rules

1. **Never fabricate or modify existing information for any system.** All theory, parameters, formulas, flags, and code snippets must appear exactly as in the old docs/notebooks (reformatting to MyST is fine; changing values, formulas, or comments is not). If a source looks like a typo (e.g. the `i^2+i^2+ij` denominator in the α formula), keep the original verbatim and flag it in an admonition — never silently "fix" it. Empty stub sections stay marked "coming soon".
2. Markdown (MyST) for all new pages; LaTeX math via `$...$`/`$$...$$`; cross-page links via `{doc}` roles or relative `.md` links; headings must keep implicit slugs stable once published.
3. Images: reference `assets/images/...` (root pages) or `../assets/images/...` (section pages), always with alt text. No base64 blobs in Markdown.
4. Keep pages buildable: `uv run sphinx-build -b html -W --keep-going . _build` (from the repo root) must succeed with zero warnings before committing.
5. Do not commit `_build/`, `public/`, `__pycache__`, `.ipynb_checkpoints`, `.DS_Store` (see `.gitignore`).
6. The old tree under `grabnes/` stays read-only until migration is verified; delete it (and `grabnes.tar.gz`) only in a final, separate commit.
7. Python tooling: declare deps in `pyproject.toml` (`sphinx`, `furo`, `myst-parser`, `sphinx-design`, `sphinx-copybutton`, `ford`, `gitpython`); `uv sync` builds `.venv` from `uv.lock`, and CI installs the same way.
8. `reference/units.md` and `reference/api/*.md` are generated (Ford over upstream `main`, run on a comment-normalized temp copy, plus the Doxygen `@brief`/`@param` blocks and the `!! - \`Key\`:` input-key items of the sources, quoted verbatim): after upstream changes run `uv run python tools/sync_from_code_repo.py` and commit the result; never hand-edit these files.
9. Commits: small, imperative-mood messages ("Add theory/models page…").

## 7. Open questions / follow-ups

- [ ] Canonical URL of the Fortran code repo (for Installation/Reference links) — likely `github.com/gjung-group/grabnes`; confirm before linking.
- [x] `README.md` mentioned `grabnes/examples/*` — resolved: the example files are mirrored from the code repo into `examples/` and `assets/downloads/examples/`.
- [ ] Fill empty illustration stubs (G/hBN gap, supermoire, impurity states) — needs content from maintainers.
- [x] Logo/branding: `assets/static/logo1.png` (wordmark banner, added by the maintainers) and `logo-icon.png` (square icon cropped from it, also the site favicon); referenced from `README.md` and set as `html_logo`/`html_favicon` in `conf.py`.
- [ ] Remove `grabnes/` and `grabnes.tar.gz` after final migration commit.
