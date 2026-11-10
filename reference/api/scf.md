(api-scf)=
# `scf`

:Kind: Module
:Source: [`lanczosKuboCode/Src/scf.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/scf.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`atoms <api-atoms>`, {ref}`cell <api-cell>`, {ref}`constants <api-constants>`, {ref}`ham <api-ham>`, {ref}`mio <api-mio>`, {ref}`neigh <api-neigh>`, {ref}`tbpar <api-tbpar>`
:Used by: {ref}`calc <api-calc>`, {ref}`diag <api-diag>`
:Public interface: 2 procedures, 2 variables
:Input keys: 8 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`SCFGetCharge <api-scf-scfgetcharge>`
  - —
* - {ref}`SCFInit <api-scf-scfinit>`
  - —
```

## Procedures

(api-scf-scfgetcharge)=
### `SCFGetCharge`

```fortran
subroutine SCFGetCharge()
```

```{rubric} Input keys read (8)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Diag.KGrid`
  - Number of k-points along each reciprocal lattice vector (three integers) of the k-grid; here of the Hubbard SCF.
* - `Hubbard.SCFMaxIterations`
  - Hubbard SCF: maximum number of iterations.
* - `Hubbard.SCFTolerance`
  - Hubbard SCF: convergence threshold on the change of the charges.
* - `Hubbard.SCFMix`
  - Hubbard SCF: linear mixing, charge = (1 - mix) new + mix old.
* - `Hubbard.MOCharge`
  - Hubbard SCF: spin imbalance dq added to (and subtracted from) the starting charges of the ordered pattern.
* - `Hubbard.AFOrdering`
  - Hubbard SCF: start from an antiferromagnetic (sublattice) spin pattern.
* - `Hubbard.AFOrderingLayer`
  - Hubbard SCF: start from a pattern antiferromagnetic between layers (if Hubbard.AFOrdering is off).
* - `Hubbard.FOrderingLayer`
  - Hubbard SCF: start from a layer-ferromagnetic pattern (if the two orderings above are off).
```

Defined in [`lanczosKuboCode/Src/scf.F90, line 20`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/scf.F90#L20).

(api-scf-scfinit)=
### `SCFInit`

```fortran
subroutine SCFInit(N)
```

```{rubric} Arguments
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 18 40 42

* - Name
  - Declaration
  - Description
* - `N`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/scf.F90, line 259`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/scf.F90#L259).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `charge`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `Zch`
  - `real(dp), parameter`
  - `1.0_dp`
```
