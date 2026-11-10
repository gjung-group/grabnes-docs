(api-mpitime)=
# `mpitime`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/MPI/mpitime.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpitime.F90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: {ref}`mpikinds <api-mpikinds>`
:Used by: {ref}`mpi <api-mpi>`
:Public interface: 2 procedures

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`MPITimer <api-mpitime-mpitimer>`
  - —
* - {ref}`MPITimerGet <api-mpitime-mpitimerget>`
  - —
```

## Procedures

(api-mpitime-mpitimer)=
### `MPITimer`

```fortran
subroutine MPITimer(action)
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
* - `action`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/MPI/mpitime.F90, line 42`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpitime.F90#L42).

(api-mpitime-mpitimerget)=
### `MPITimerGet`

```fortran
subroutine MPITimerGet(t, nc)
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
* - `t`
  - `real(dp), intent(out)`
  - —
* - `nc`
  - `integer, intent(out)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/MPI/mpitime.F90, line 78`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpitime.F90#L78).
