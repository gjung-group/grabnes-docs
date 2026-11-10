(api-parallel)=
# `parallel`

:Kind: Module
:Source: [`lanczosKuboCode/Src/parallel.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/parallel.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`mio <api-mio>`
:Used by: {ref}`atoms <api-atoms>`, {ref}`gauss <api-gauss>`, {ref}`grabnes <api-grabnes>`, {ref}`ham <api-ham>`, {ref}`kubo <api-kubo>`, {ref}`neigh <api-neigh>`, {ref}`random <api-random>`
:Public interface: 1 procedure, 7 variables

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`ParallelDiv <api-parallel-paralleldiv>`
  - —
```

## Procedures

(api-parallel-paralleldiv)=
### `ParallelDiv`

```fortran
subroutine ParallelDiv()
```

Defined in [`lanczosKuboCode/Src/parallel.F90, line 18`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/parallel.F90#L18).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `nDiv`
  - `integer, save`
  - —
* - `nTh`
  - `integer, dimension(:), pointer`
  - —
* - `procID`
  - `integer, save`
  - —
* - `xDiv`
  - `integer, save`
  - —
* - `xSubdiv`
  - `integer, save`
  - —
* - `yDiv`
  - `integer, save`
  - —
* - `ySubdiv`
  - `integer, save`
  - —
```
