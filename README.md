# grabnes-docs

<p align="center">
  <img src="assets/static/logo1.png" alt="GRABNES logo" width="480">
</p>

The source of the [GRABNES](https://github.com/gjung-group/grabnes) project
website (GRAphene/BN Electronic Structure, a Fortran tight-binding package for
layered 2D materials), published with GitHub Pages. The Fortran code itself
lives in the separate code repository.

The website features:
- Theory of the implemented models and observables.
- Worked examples and step-by-step tutorials.
- A user guide with the complete input-key reference.
- Benchmark studies (some still marked "coming soon").
- A development guide and a generated Fortran API reference.

## Current state

The site is a Sphinx documentation tree whose **source directory is the
repository root**, built with MyST-Markdown, the Furo theme, and
sphinx-design, and deployed to GitHub Pages by a GitHub Actions workflow.
Content comes from two sources: the old (2022) Sphinx docs and notebooks
(kept locally under the gitignored `grabnes/` tree as read-only migration
input, to be removed once the migration is verified), and `main` of the
[GRABNES code repository](https://github.com/gjung-group/grabnes)
(`docs/` and `examples/`; last synced at upstream commit `a3d2767`).

Sections:

| Folder | Content |
| --- | --- |
| `index.md`, `installation.md` | landing page, compile & Colab instructions |
| `theory/` | tight-binding models, moiré supercells, observables, TAPW procedure |
| `examples/` | the supported examples of the code repository (01–11: getting started, moiré, ARPES) with figures and downloadable inputs |
| `tutorials/` | graphene, bilayer/graphite, twisted bilayer, graphene on hBN, input flags, plotting |
| `user-guide/` | input-file format, the complete input-key reference, TAPW + SOC input |
| `benchmarks/` | benchmark studies; empty illustration stubs are marked "coming soon" |
| `development/` | code structure, functionality status, validation, coding conventions, known issues, SOC/TAPW notes, release readiness, licensing |
| `reference/` | API reference entry page + generated Fortran unit reference |
| `assets/` | images, downloadable inputs/scripts/notebooks, logo, fonts, and CSS |
| `tools/` | sync script for the code repository and the API-reference generator |

## Syncing with the code repository

Part of the content is mirrored from `main` of the code repository
(`docs/development`, `docs/user-guide`, example inputs and figures), and
`reference/units.md` is generated from its sources. Never hand-edit mirrored
files or `reference/units.md`.

```bash
uv run python tools/sync_from_code_repo.py [--check]   # --check only reports drift (exit 1)
uv run python tools/gen_api_reference.py               # regenerate reference/units.md
```

Hand-written pages derived from upstream are tracked in
`tools/sync-state.json`; the script prints `MANUAL` when their source changed.

## Building locally

```bash
uv sync                                        # creates .venv from pyproject/uv.lock
uv run sphinx-build -b html . _build           # open _build/index.html
```

The CI build treats warnings as errors; check with
`uv run sphinx-build -b html -W --keep-going . _build` before committing.

## Deployment

The live site is at <https://gjung-group.github.io/grabnes-docs/>.
`.github/workflows/docs.yml` builds the site to `public/` on every push to
`main` and deploys it to GitHub Pages (Settings → Pages → "GitHub Actions").
Pull requests are built too (with `-W`) but not deployed.
