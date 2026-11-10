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
(`docs/` and `examples/`; last synced at upstream commit `c6f4e03`).

Sections:

| Folder | Content |
| --- | --- |
| `index.md`, `installation.md` | landing page, compile & Colab instructions |
| `theory/` | tight-binding models, moiré supercells, observables, TAPW procedure |
| `examples/` | the supported examples of the code repository (01–11: getting started, moiré, ARPES) with figures and downloadable inputs |
| `tutorials/` | graphene, bilayer/graphite, twisted bilayer, graphene on hBN, input flags, plotting |
| `user-guide/` | input-file format, the complete input-key reference, TAPW + SOC input |
| `benchmarks/` | benchmark studies; empty illustration stubs are marked "coming soon" |
| `development/` | code structure, functionality status, validation, coding conventions, `job.out` output style, known issues, SOC/TAPW notes, release readiness, licensing |
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

The sync also runs automatically: `.github/workflows/sync-upstream.yml` checks
every hour (or on demand from the Actions tab) for the newest commit on the
code repository's `main` whose `regression` workflow passed. A clean sync that
builds with `-W` is committed to `main` and deployed; a sync with `MANUAL`
items or a failing build is opened as a pull request from `sync/upstream`
instead, and no further syncs run until it is merged or closed.

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
