(api-input)=
# `input`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/input.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/input.F90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: {ref}`debug <api-debug>`, {ref}`file <api-file>`, {ref}`io <api-io>`, {ref}`mem <api-mem>`, {ref}`mpi <api-mpi>`, `omp_lib`, {ref}`options <api-options>`, {ref}`parser <api-parser>`, {ref}`precision <api-precision>`, {ref}`string <api-string>`, {ref}`sys <api-sys>`, {ref}`timer <api-timer>`
:Used by: {ref}`mio <api-mio>`
:Public interface: 4 procedures, 4 generic interfaces

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`InputAddAlias <api-input-inputaddalias>`
  - —
* - {ref}`InputClose <api-input-inputclose>`
  - —
* - {ref}`InputInit <api-input-inputinit>`
  - —
* - {ref}`InputSearchLabel <api-input-inputsearchlabel>`
  - —
```

## Generic interfaces

```{list-table}
:header-rows: 1
:class: api-table
:widths: 30 70

* - Interface
  - Specific procedures
* - `InputBlock`
  - `InputBl_i`, `InputBl_r`, `InputBl_d`, `InputBl_l`, `InputBl_s`, `InputBl_im`, `InputBl_rm`, `InputBl_dm`, `InputBl_lm`, `InputBl_imi`, `InputBl_rmi`, `InputBl_dmi`, `InputBl_lmi`
* - `InputFindBlock`
  - `InputFindBl`, `InputFindBl_i`, `InputFindBl_s`
* - `InputParameter`
  - `InputPar_i`, `InputPar_d`, `InputPar_r`, `InputPar_l`, `InputPar_s`, `InputPar_is`, `InputPar_ds`, `InputPar_rs`, `InputPar_ls`
* - `InputParameterVariable`
  - `InputPar_i_variable`
```

## Procedures

(api-input-inputaddalias)=
### `InputAddAlias`

```fortran
subroutine InputAddAlias(newName, oldName)
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
* - `newName`
  - `character(len=*), intent(in)`
  - —
* - `oldName`
  - `character(len=*), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/input.F90, line 1518`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/input.F90#L1518).

(api-input-inputclose)=
### `InputClose`

```fortran
subroutine InputClose()
```

Defined in [`lanczosKuboCode/Src/MIO/input.F90, line 301`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/input.F90#L301).

(api-input-inputinit)=
### `InputInit`

```fortran
subroutine InputInit(success)
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

Defined in [`lanczosKuboCode/Src/MIO/input.F90, line 95`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/input.F90#L95).

(api-input-inputsearchlabel)=
### `InputSearchLabel`

```fortran
function InputSearchLabel(label, str, lineid) result(found)
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
* - `label`
  - `character(len=*), intent(in)`
  - —
* - `str`
  - `character(len=*), intent(out), optional`
  - —
* - `lineid`
  - `integer, intent(out), optional`
  - —
```

```{rubric} Returns
```

`found`: `logical`

Defined in [`lanczosKuboCode/Src/MIO/input.F90, line 1451`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/input.F90#L1451).
