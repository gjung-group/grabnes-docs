(api-debug)=
# `debug`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/debug.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/debug.F90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: {ref}`file <api-file>`, {ref}`io <api-io>`, {ref}`mpi <api-mpi>`
:Used by: {ref}`input <api-input>`, {ref}`mio <api-mio>`
:Public interface: 3 procedures

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`DebugClose <api-debug-debugclose>`
  - —
* - {ref}`DebugInit <api-debug-debuginit>`
  - —
* - {ref}`DebugPrint <api-debug-debugprint>`
  - —
```

## Procedures

(api-debug-debugclose)=
### `DebugClose`

```fortran
subroutine DebugClose()
```

Defined in [`lanczosKuboCode/Src/MIO/debug.F90, line 97`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/debug.F90#L97).

(api-debug-debuginit)=
### `DebugInit`

```fortran
subroutine DebugInit()
```

Defined in [`lanczosKuboCode/Src/MIO/debug.F90, line 37`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/debug.F90#L37).

(api-debug-debugprint)=
### `DebugPrint`

```fortran
subroutine DebugPrint(subroutine, i)
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
* - `subroutine`
  - `character(len=*), intent(in)`
  - —
* - `i`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/debug.F90, line 62`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/debug.F90#L62).
