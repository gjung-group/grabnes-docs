(api-qsort)=
# `qsort`

:Kind: Module
:Source: [`lanczosKuboCode/Src/math/qsort.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/math/qsort.F90#L13)
:Group: {ref}`Math library <api-group-math>`
:Uses: —
:Used by: —
:Public interface: 1 procedure

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`QuickSort <api-qsort-quicksort>`
  - —
```

## Procedures

(api-qsort-quicksort)=
### `QuickSort`

```fortran
recursive subroutine QuickSort(array)
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
* - `array`
  - `real(dp), dimension(:), intent(inout)`
  - —
```

Defined in [`lanczosKuboCode/Src/math/qsort.F90, line 35`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/math/qsort.F90#L35).
