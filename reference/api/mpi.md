(api-mpi)=
# `mpi`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/MPI/mpi.f90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpi.f90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: `mpi_c`, `mpi_d`, `mpi_i`, {ref}`mpi_inc <api-mpi_inc>`, `mpi_l`, `mpi_r`, `mpi_s`, `mpi_z`, {ref}`mpitime <api-mpitime>`
:Used by: {ref}`debug <api-debug>`, {ref}`file <api-file>`, {ref}`input <api-input>`, {ref}`mio <api-mio>`, {ref}`sys <api-sys>`, {ref}`timer <api-timer>`
:Public interface: 5 procedures

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`MPIBarrier <api-mpi-mpibarrier>`
  - —
* - {ref}`MPIFin <api-mpi-mpifin>`
  - —
* - {ref}`MPIGetNodes <api-mpi-mpigetnodes>`
  - —
* - {ref}`MPIIni <api-mpi-mpiini>`
  - —
* - {ref}`MPIIsPNode <api-mpi-mpiispnode>`
  - —
```

## Procedures

(api-mpi-mpibarrier)=
### `MPIBarrier`

```fortran
subroutine MPIBarrier()
```

Defined in [`lanczosKuboCode/Src/MIO/MPI/mpi.f90, line 108`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpi.f90#L108).

(api-mpi-mpifin)=
### `MPIFin`

```fortran
subroutine MPIFin()
```

Defined in [`lanczosKuboCode/Src/MIO/MPI/mpi.f90, line 64`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpi.f90#L64).

(api-mpi-mpigetnodes)=
### `MPIGetNodes`

```fortran
subroutine MPIGetNodes(n, tn)
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
* - `n`
  - `integer, intent(out)`
  - —
* - `tn`
  - `integer, intent(out)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/MPI/mpi.f90, line 79`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpi.f90#L79).

(api-mpi-mpiini)=
### `MPIIni`

```fortran
subroutine MPIIni()
```

Defined in [`lanczosKuboCode/Src/MIO/MPI/mpi.f90, line 44`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpi.f90#L44).

(api-mpi-mpiispnode)=
### `MPIIsPNode`

```fortran
function MPIIsPNode() result(is)
```

```{rubric} Returns
```

`is`: `logical`

Defined in [`lanczosKuboCode/Src/MIO/MPI/mpi.f90, line 97`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/MPI/mpi.f90#L97).
