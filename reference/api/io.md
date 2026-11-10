(api-io)=
# `io`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/io.f90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/io.f90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: —
:Used by: {ref}`debug <api-debug>`, {ref}`file <api-file>`, {ref}`format <api-format>`, {ref}`input <api-input>`, {ref}`mio <api-mio>`, {ref}`options <api-options>`, {ref}`parser <api-parser>`, {ref}`string <api-string>`, {ref}`sys <api-sys>`
:Public interface: 8 variables

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `maxfnlen`
  - `integer, parameter`
  - `60`
* - `maxinputl`
  - `integer, parameter`
  - `512`
* - `maxlinel`
  - `integer, parameter`
  - `80`
* - `stderr`
  - `integer, save`
  - `0`
* - `stdin`
  - `integer, save`
  - `5`
* - `stdout`
  - `integer, save`
  - `6`
* - `udebug`
  - `integer, parameter`
  - `10`
* - `unit0`
  - `integer, parameter`
  - `11`
```
