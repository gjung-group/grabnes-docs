(api-format)=
# `format`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/format.f90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: {ref}`io <api-io>`, {ref}`precision <api-precision>`
:Used by: {ref}`file <api-file>`, {ref}`mem <api-mem>`, {ref}`mio <api-mio>`, {ref}`parser <api-parser>`, {ref}`sys <api-sys>`
:Public interface: 9 procedures, 1 generic interface

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`lowercase <api-format-lowercase>`
  - —
* - {ref}`num2bytes <api-format-num2bytes>`
  - —
* - {ref}`num2month <api-format-num2month>`
  - —
* - {ref}`num2strc <api-format-num2strc>`
  - —
* - {ref}`num2strd <api-format-num2strd>`
  - —
* - {ref}`num2stri <api-format-num2stri>`
  - —
* - {ref}`num2strr <api-format-num2strr>`
  - —
* - {ref}`num2strz <api-format-num2strz>`
  - —
* - {ref}`uppercase <api-format-uppercase>`
  - —
```

## Generic interfaces

```{list-table}
:header-rows: 1
:class: api-table
:widths: 30 70

* - Interface
  - Specific procedures
* - `num2string`
  - {ref}`num2stri <api-format-num2stri>`, {ref}`num2strd <api-format-num2strd>`, {ref}`num2strz <api-format-num2strz>`, {ref}`num2strr <api-format-num2strr>`, {ref}`num2strc <api-format-num2strc>`
```

## Procedures

(api-format-lowercase)=
### `lowercase`

```fortran
elemental function lowercase(str) result(lcstr)
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
* - `str`
  - `character(len=*), intent(in)`
  - —
```

```{rubric} Returns
```

`lcstr`: `character(len=maxlinel)`

Defined in [`lanczosKuboCode/Src/MIO/format.f90, line 244`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L244).

(api-format-num2bytes)=
### `num2bytes`

```fortran
elemental function num2bytes(num) result(string)
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
* - `num`
  - `integer(8), intent(in)`
  - —
```

```{rubric} Returns
```

`string`: `character(len=30)`

Defined in [`lanczosKuboCode/Src/MIO/format.f90, line 200`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L200).

(api-format-num2month)=
### `num2month`

```fortran
elemental function num2month(num) result(string)
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
* - `num`
  - `integer, intent(in)`
  - —
```

```{rubric} Returns
```

`string`: `character(len=9)`

Defined in [`lanczosKuboCode/Src/MIO/format.f90, line 169`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L169).

(api-format-num2strc)=
### `num2strc`

```fortran
elemental function num2strc(num, dec) result(string)
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
* - `num`
  - `complex(sp), intent(in)`
  - —
* - `dec`
  - `integer, intent(in), optional`
  - —
```

```{rubric} Returns
```

`string`: `character(len=strlen)`

Defined in [`lanczosKuboCode/Src/MIO/format.f90, line 92`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L92).

(api-format-num2strd)=
### `num2strd`

```fortran
elemental function num2strd(num, dec) result(string)
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
* - `num`
  - `real(dp), intent(in)`
  - —
* - `dec`
  - `integer, intent(in), optional`
  - —
```

```{rubric} Returns
```

`string`: `character(len=strlen)`

Defined in [`lanczosKuboCode/Src/MIO/format.f90, line 105`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L105).

(api-format-num2stri)=
### `num2stri`

```fortran
elemental function num2stri(num) result(string)
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
* - `num`
  - `integer, intent(in)`
  - —
```

```{rubric} Returns
```

`string`: `character(len=strlen)`

Defined in [`lanczosKuboCode/Src/MIO/format.f90, line 54`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L54).

(api-format-num2strr)=
### `num2strr`

```fortran
elemental function num2strr(num, dec) result(string)
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
* - `num`
  - `real(sp), intent(in)`
  - —
* - `dec`
  - `integer, intent(in), optional`
  - —
```

```{rubric} Returns
```

`string`: `character(len=strlen)`

Defined in [`lanczosKuboCode/Src/MIO/format.f90, line 63`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L63).

(api-format-num2strz)=
### `num2strz`

```fortran
elemental function num2strz(num, dec) result(string)
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
* - `num`
  - `complex(dp), intent(in)`
  - —
* - `dec`
  - `integer, intent(in), optional`
  - —
```

```{rubric} Returns
```

`string`: `character(len=strlen)`

Defined in [`lanczosKuboCode/Src/MIO/format.f90, line 142`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L142).

(api-format-uppercase)=
### `uppercase`

```fortran
elemental function uppercase(str) result(lcstr)
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
* - `str`
  - `character(len=*), intent(in)`
  - —
```

```{rubric} Returns
```

`lcstr`: `character(len=maxlinel)`

Defined in [`lanczosKuboCode/Src/MIO/format.f90, line 283`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/format.f90#L283).
