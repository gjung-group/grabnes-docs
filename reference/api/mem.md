(api-mem)=
# `mem`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/mem_in.f90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/mem_in.f90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: {ref}`format <api-format>`, {ref}`precision <api-precision>`, {ref}`sys <api-sys>`
:Used by: {ref}`input <api-input>`, {ref}`mio <api-mio>`, {ref}`timer <api-timer>`
:Public interface: 3 procedures, 7 variables

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`MemCount <api-mem-memcount>`
  - —
* - {ref}`MemGetName <api-mem-memgetname>`
  - —
* - {ref}`MemPrint <api-mem-memprint>`
  - —
```

## Procedures

(api-mem-memcount)=
### `MemCount`

```fortran
subroutine MemCount(sz, arrname, rname)
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
* - `sz`
  - `integer(8), intent(in)`
  - —
* - `arrname`
  - `character(len=*), intent(in)`
  - —
* - `rname`
  - `character(len=*), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/mem_in.f90, line 55`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/mem_in.f90#L55).

(api-mem-memgetname)=
### `MemGetName`

```fortran
subroutine MemGetName(arrname, rname, name, routine)
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
* - `arrname`
  - `character(len=32), intent(out)`
  - —
* - `rname`
  - `character(len=32), intent(out)`
  - —
* - `name`
  - `character(len=*), intent(in), optional`
  - —
* - `routine`
  - `character(len=*), intent(in), optional`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/mem_in.f90, line 269`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/mem_in.f90#L269).

(api-mem-memprint)=
### `MemPrint`

```fortran
subroutine MemPrint()
```

Defined in [`lanczosKuboCode/Src/MIO/mem_in.f90, line 79`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/mem_in.f90#L79).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `Csz`
  - `integer, parameter`
  - `[CSZ]`
* - `Dsz`
  - `integer, parameter`
  - `[DSZ]`
* - `Isz`
  - `integer, parameter`
  - `[ISZ]`
* - `Lsz`
  - `integer, parameter`
  - `[LSZ]`
* - `Rsz`
  - `integer, parameter`
  - `[RSZ]`
* - `Ssz`
  - `integer, parameter`
  - `[SSZ]`
* - `Zsz`
  - `integer, parameter`
  - `[ZSZ]`
```
