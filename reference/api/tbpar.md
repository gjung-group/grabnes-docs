(api-tbpar)=
# `tbpar`

:Kind: Module
:Source: [`lanczosKuboCode/Src/tbpar.f90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/tbpar.f90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`cell <api-cell>`, {ref}`mio <api-mio>`
:Used by: {ref}`calc <api-calc>`, {ref}`diag <api-diag>`, {ref}`ham <api-ham>`, {ref}`interface <api-interface>`, {ref}`neigh <api-neigh>`, {ref}`scf <api-scf>`
:Public interface: 1 procedure, 14 variables
:Input keys: 20 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`TBInit <api-tbpar-tbinit>`
  - —
```

## Procedures

(api-tbpar-tbinit)=
### `TBInit`

```fortran
subroutine TBInit()
```

```{rubric} Input keys read (20)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `TB.NeighLevels`
  - Number of neighbour shells of the hopping table (at least 1).
* - `TB.Hopping`
  - Nearest-neighbour hopping g0 \[eV\], the internal energy unit: every energy is divided by it. Default -3.72 aG + 12.14 (2.9887 eV at aG 2.46).
* - `TB.BNHopping`
  - Nearest-neighbour B-N hopping of hBN \[eV\] (default: TB.Hopping).
* - `TB.CBHopping`
  - Nearest-neighbour C-B hopping \[eV\].
* - `TB.CNHopping`
  - Nearest-neighbour C-N hopping \[eV\].
* - `TB.OnSiteC`
  - On-site energy of carbon \[eV\].
* - `TB.OnSiteC1`
  - On-site energy of carbon sublattice 1 (Species 1) \[eV\].
* - `TB.OnSiteC2`
  - On-site energy of carbon sublattice 2 (Species 2) \[eV\].
* - `TB.OnSiteC1_LB`
  - On-site energy of carbon sublattice 1 of the bottom layer \[eV\], for the stack models that use it.
* - `TB.OnSiteC2_LB`
  - On-site energy of carbon sublattice 2 of the bottom layer \[eV\], for the stack models that use it.
* - `TB.OnSiteC1_LT`
  - On-site energy of carbon sublattice 1 of the top layer \[eV\], for the stack models that use it.
* - `TB.OnSiteC2_LT`
  - On-site energy of carbon sublattice 2 of the top layer \[eV\], for the stack models that use it.
* - `TB.OnSiteB`
  - On-site energy of boron \[eV\].
* - `TB.OnSiteN`
  - On-site energy of nitrogen \[eV\].
* - `TB.InterLayerHopping`
  - Interlayer hopping t exp(-d/dIntLay) of the simplest interlayer branch of HamHopping, d = in-plane distance \[eV\].
* - `Haldane.T2`
  - Here: read to leave the second-neighbour table entries at zero; the Haldane term itself is added in ham.F90.
* - `Run.TypeOfSystem`
  - Here: Ribbons, Hybrid and ReadXYZ structures get the hopping table of mixed C/B/N systems.
* - `Hubbard.U_C`
  - Hubbard U of carbon \[eV\] (two-spin runs with Hubbard.EnableSCF).
* - `Hubbard.U_B`
  - Hubbard U of boron \[eV\] (two-spin runs with Hubbard.EnableSCF).
* - `Hubbard.U_N`
  - Hubbard U of nitrogen \[eV\] (two-spin runs with Hubbard.EnableSCF).
```

Defined in [`lanczosKuboCode/Src/tbpar.f90, line 20`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/tbpar.f90#L20).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `e0_B`
  - `real(dp), save`
  - —
* - `e0_C`
  - `real(dp), save`
  - —
* - `e0_C1`
  - `real(dp), save`
  - —
* - `e0_C1_LB`
  - `real(dp), save`
  - —
* - `e0_C1_LT`
  - `real(dp), save`
  - —
* - `e0_C2`
  - `real(dp), save`
  - —
* - `e0_C2_LB`
  - `real(dp), save`
  - —
* - `e0_C2_LT`
  - `real(dp), save`
  - —
* - `e0_N`
  - `real(dp), save`
  - —
* - `g0`
  - `real(dp), save`
  - —
* - `gIntLay`
  - `real(dp), save`
  - —
* - `gn`
  - `real(dp), dimension(:,:,:), pointer`
  - —
* - `tbnn`
  - `integer, save`
  - —
* - `U`
  - `real(dp), dimension(4), save`
  - —
```
