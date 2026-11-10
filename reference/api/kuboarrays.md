(api-kuboarrays)=
# `kuboarrays`

:Kind: Module
:Source: [`lanczosKuboCode/Src/kuboarrays.f90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kuboarrays.f90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`mio <api-mio>`
:Used by: {ref}`calc <api-calc>`, {ref}`kubosubs <api-kubosubs>`
:Public interface: 12 variables

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `a`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `b`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `c`
  - `complex(dp), dimension(:), pointer`
  - `NULL()`
* - `H`
  - `complex(dp), dimension(:), pointer`
  - `NULL()`
* - `Psi`
  - `complex(dp), dimension(:), pointer`
  - `NULL()`
* - `Psin`
  - `complex(dp), dimension(:), pointer`
  - `NULL()`
* - `Psinm1`
  - `complex(dp), dimension(:), pointer`
  - `NULL()`
* - `tempD`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `tempZ`
  - `complex(dp), dimension(:), pointer`
  - `NULL()`
* - `XpnPsi`
  - `complex(dp), dimension(:), pointer`
  - `NULL()`
* - `XpnPsim1`
  - `complex(dp), dimension(:), pointer`
  - `NULL()`
* - `ZUPsi`
  - `complex(dp), dimension(:), pointer`
  - `NULL()`
```
