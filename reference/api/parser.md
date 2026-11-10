(api-parser)=
# `parser`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/parser.f90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/parser.f90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: {ref}`format <api-format>`, {ref}`io <api-io>`, {ref}`precision <api-precision>`, {ref}`string <api-string>`, {ref}`sys <api-sys>`
:Used by: {ref}`input <api-input>`, {ref}`mio <api-mio>`
:Public interface: 2 generic interfaces

## Generic interfaces

```{list-table}
:header-rows: 1
:class: api-table
:widths: 30 70

* - Interface
  - Specific procedures
* - `ParserCheck`
  - `ParserCheck_i`, `ParserCheck_r`, `ParserCheck_d`, `ParserCheck_s`, `ParserCheck_l`
* - `ParserFindValue`
  - `ParserFindValue_i`, `ParserFindValue_d`
```
