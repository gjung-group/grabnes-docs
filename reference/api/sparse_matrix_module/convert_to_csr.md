(api-sparse_matrix_module-convert_to_csr)=
# `convert_to_csr`

```{index} single: convert_to_csr (subroutine in sparse_matrix_module)
```

```fortran
subroutine convert_to_csr(HLoc, N, row_ptr, col_ind, values)
```

:Module: {ref}`sparse_matrix_module <api-sparse_matrix_module>`
:Kind: Subroutine
:Source: [`lanczosKuboCode/Src/test_sparse_diag.F90, line 29`](https://github.com/gjung-group/grabnes/blob/1e390c6ead7c835389ae89a599cb1f39e3fc691e/lanczosKuboCode/Src/test_sparse_diag.F90#L29)

```{rubric} Parameters
```

`HLoc` : `complex(16), dimension(N,N), intent(in)`
: —

`N` : `integer, intent(in)`
: —

`row_ptr` : `integer, dimension(:), intent(out), allocatable`
: —

`col_ind` : `integer, dimension(:), intent(out), allocatable`
: —

`values` : `complex(16), dimension(:), intent(out), allocatable`
: —

```{rubric} Calls
```

{ref}`MIO_Debug <api-mio-interface-mio_debug>`

```{rubric} Called by
```

{ref}`test_csr <api-test_csr>` (program)
