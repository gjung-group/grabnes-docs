(api-sparse_matrix_module)=
# `sparse_matrix_module`

:Kind: Module
:Source: [`lanczosKuboCode/Src/test_sparse_diag.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/test_sparse_diag.F90#L1)
:Group: {ref}`Sources not in the solver build <api-group-unbuilt>`
:Uses: —
:Used by: {ref}`test_csr <api-test_csr>`
:Public interface: 2 procedures

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`convert_to_csr <api-sparse_matrix_module-convert_to_csr>`
  - —
* - {ref}`sparse_matvec <api-sparse_matrix_module-sparse_matvec>`
  - —
```

## Procedures

(api-sparse_matrix_module-convert_to_csr)=
### `convert_to_csr`

```fortran
subroutine convert_to_csr(HLoc, N, row_ptr, col_ind, values)
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
* - `HLoc`
  - `complex(16), dimension(N,N), intent(in)`
  - —
* - `N`
  - `integer, intent(in)`
  - —
* - `row_ptr`
  - `integer, dimension(:), intent(out), allocatable`
  - —
* - `col_ind`
  - `integer, dimension(:), intent(out), allocatable`
  - —
* - `values`
  - `complex(16), dimension(:), intent(out), allocatable`
  - —
```

Defined in [`lanczosKuboCode/Src/test_sparse_diag.F90, line 29`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/test_sparse_diag.F90#L29).

(api-sparse_matrix_module-sparse_matvec)=
### `sparse_matvec`

```fortran
subroutine sparse_matvec(nn, row_ptr, col_ind, values, x, y)
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
* - `nn`
  - `integer, intent(in)`
  - —
* - `row_ptr`
  - `integer, dimension(:), intent(in)`
  - —
* - `col_ind`
  - `integer, dimension(:), intent(in)`
  - —
* - `values`
  - `complex(16), dimension(:), intent(in)`
  - —
* - `x`
  - `complex(16), dimension(:), intent(in)`
  - —
* - `y`
  - `complex(16), dimension(nn), intent(out)`
  - —
```

Defined in [`lanczosKuboCode/Src/test_sparse_diag.F90, line 4`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/test_sparse_diag.F90#L4).
