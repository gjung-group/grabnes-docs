# grabnes-docs

<p align="center">
  <img src="assets/static/logo1.png" alt="GRABNES logo" width="480">
</p>

Source of the documentation website for **GRABNES**, published with GitHub
Pages at <https://gjung-group.github.io/grabnes-docs/>. The Fortran code itself
lives in the separate [code repository](https://github.com/gjung-group/grabnes).

## About GRABNES

GRABNES (**GRA**phene/**B**N **E**lectronic **S**tructure) is a Fortran
tight-binding package from the
[gjung-group](https://github.com/gjung-group) for layered 2D materials:
graphene, hBN, twisted bilayer and multilayer graphene, graphene on hBN, and
related heterostructures.

- **Moiré supercells:** builds commensurate cells with controllable twist
  angle and layer sliding, and interfaces with LAMMPS for structural
  relaxation.
- **Observables:** band structures, density of states (Lanczos recursion and
  exact diagonalization), unfolded spectral functions for comparison with
  ARPES, LDOS, probability densities, Kubo–Greenwood conductivity, and
  magnetic-field (Landau-level) DOS with disorder.
- **Tight-binding models:** F2G2 intralayer models from maximally localized
  Wannier functions, reparametrized two-center (TC) interlayer models, hybrid
  F2G2+TC models, and the SHE model.
- **Performance:** OpenMP parallelization.

## What the website covers

- Installation: compiling the code, or running it in the browser via Colab.
- Theory of the implemented models and observables.
- Worked examples (the supported examples 01–11 of the code repository) and
  step-by-step tutorials.
- A user guide: the input file, writing it in YAML or JSON, stacking
  displacements, TAPW + SOC input, and the complete input-key reference with
  a description of every key.
- Benchmark studies (some still marked "coming soon").
- A development guide and a generated Fortran API reference: one page per
  unit with signatures, arguments, descriptions from the source comments,
  dependencies, source links, and the input keys each routine reads.

## Current state

The site is a Sphinx documentation tree whose **source directory is the
repository root**, built with MyST-Markdown, the Furo theme, sphinx-design and
sphinx-copybutton, and deployed to GitHub Pages by a GitHub Actions workflow.
The look is customized in `assets/static/grabnes.css` (Inter font, brand
colours from the logo, landing-page hero, cards and tables, light and dark
mode), `assets/static/grabnes.js` (line breaks for long identifiers in tables)
and `_templates/sidebar/` (logo with subtitle, source-code and issue links).
Content comes from two sources: the old (2022) Sphinx docs and notebooks
(kept locally under the gitignored `grabnes/` tree as read-only migration
input, to be removed once the migration is verified), and `main` of the
[GRABNES code repository](https://github.com/gjung-group/grabnes)
(`docs/` and `examples/`; last synced at upstream commit `1e390c6`).

Sections:

| Folder | Content |
| --- | --- |
| `conf.py` | Sphinx configuration (theme options, extensions, `{task}`/`{todo}` directives) |
| `index.md`, `installation.md` | landing page, compile & Colab instructions |
| `theory/` | tight-binding models, moiré supercells, observables, TAPW procedure |
| `examples/` | the supported examples of the code repository (01–11: getting started, moiré, ARPES) with figures and downloadable inputs |
| `tutorials/` | graphene, bilayer/graphite, twisted bilayer, graphene on hBN, input flags, plotting |
| `user-guide/` | input-file format, YAML/JSON input converter, input-key reference (generated upstream, with descriptions), stacking displacements, TAPW + SOC input |
| `benchmarks/` | benchmark studies; empty illustration stubs are marked "coming soon" |
| `development/` | code structure, functionality status, validation, coding conventions, `job.out` output style, known issues, SOC/TAPW notes, release readiness, licensing |
| `reference/` | API reference entry page + generated Fortran unit reference (overview `units.md`, one page per unit in `api/`) |
| `assets/` | images, downloadable inputs/scripts/notebooks, logo, fonts, CSS and JS |
| `_templates/` | Furo sidebar templates (brand, repository links) |
| `tools/` | sync script for the code repository (`sync_from_code_repo.py`, state in `sync-state.json`) and the API-reference generator (`gen_api_reference.py`) |
| `.github/workflows/` | `docs.yml` (build and deploy), `sync-upstream.yml` (automatic sync) |

## Syncing with the code repository

Part of the content is mirrored from `main` of the code repository
(`docs/development`, `docs/user-guide`, example inputs and figures), and
`reference/units.md` and `reference/api/` are generated from its sources with
Ford, plus the Doxygen (`@brief`, `@param`, ...) and `!!` input-key comments of
the sources, quoted verbatim. Never hand-edit mirrored files or the generated
reference.

```bash
uv run python tools/sync_from_code_repo.py [--check]   # --check only reports drift (exit 1)
uv run python tools/gen_api_reference.py               # regenerate reference/units.md + reference/api/
```

Hand-written pages derived from upstream are tracked in
`tools/sync-state.json`; the script prints `MANUAL` when their source changed.

The sync also runs automatically: `.github/workflows/sync-upstream.yml` checks
twice a day, at 05:17 and 17:17 UTC (or on demand from the Actions tab), for
the newest commit on the code repository's `main` whose `regression` workflow
passed. A clean sync that
builds with `-W` is committed to `main` and deployed; a sync with `MANUAL`
items or a failing build is opened as a pull request from `sync/upstream`
instead, and no further syncs run until it is merged or closed.

## Building locally

```bash
uv sync                                        # creates .venv from pyproject/uv.lock
uv run sphinx-build -b html . _build           # build into _build/
python3 -m http.server 8000 -d _build          # preview at http://127.0.0.1:8000/
```

The CI build treats warnings as errors; check with
`uv run sphinx-build -b html -W --keep-going . _build` before committing.

## Deployment

The live site is at <https://gjung-group.github.io/grabnes-docs/>.
`.github/workflows/docs.yml` builds the site to `public/` on every push to
`main` (and when the sync workflow dispatches it) and deploys it to GitHub
Pages (Settings → Pages → "GitHub Actions"). Pull requests are built too
(with `-W`) but not deployed.
