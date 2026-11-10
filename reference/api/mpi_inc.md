(api-mpi_inc)=
# `mpi_inc`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/MPI/mpi_inc.f90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpi_inc.f90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: —
:Used by: {ref}`mpi <api-mpi>`
:Public interface: 5 variables

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `defPNode`
  - `integer, parameter`
  - `0`
* - `IsPNode`
  - `logical, save`
  - `.true.`
* - `Node`
  - `integer, save`
  - `0`
* - `nProc`
  - `integer, save`
  - `1`
* - `rankPNode`
  - `integer, save`
  - `defPNode`
```
