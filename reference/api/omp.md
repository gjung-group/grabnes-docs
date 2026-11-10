(api-omp)=
# `omp`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/omp.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/omp.F90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: `omp_lib`
:Used by: {ref}`mio <api-mio>`
:Public interface: 1 procedure, 5 variables

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`OmpInit <api-omp-ompinit>`
  - —
```

## Procedures

(api-omp-ompinit)=
### `OmpInit`

```fortran
subroutine OmpInit()
```

Defined in [`lanczosKuboCode/Src/MIO/omp.F90, line 31`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/omp.F90#L31).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `minCy`
  - `integer, save`
  - —
* - `Node`
  - `integer, save`
  - `0`
* - `nProc`
  - `integer, save`
  - `1`
* - `nThread`
  - `integer, save`
  - `0`
* - `numThreads`
  - `integer, save`
  - `1`
```
