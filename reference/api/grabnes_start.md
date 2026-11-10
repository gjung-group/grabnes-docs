(api-grabnes_start)=
# `grabnes_start`

:Kind: Module
:Source: [`lanczosKuboCode/Src/grabnes_start.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/grabnes_start.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`mio <api-mio>`, {ref}`name <api-name>`
:Used by: {ref}`grabnes <api-grabnes>`
:Public interface: 1 procedure
:Input keys: 2 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`GrabnesStart <api-grabnes_start-grabnesstart>`
  - —
```

## Procedures

(api-grabnes_start-grabnesstart)=
### `GrabnesStart`

```fortran
subroutine GrabnesStart(success)
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
* - `success`
  - `logical, intent(out)`
  - —
```

```{rubric} Input keys read (2)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Run.Description`
  - Free text printed at the top of the output.
* - `Run.Prefix`
  - Prefix of the output files (\<prefix>.DOS, ...); default grabnes.
```

Defined in [`lanczosKuboCode/Src/grabnes_start.F90, line 11`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/grabnes_start.F90#L11).
