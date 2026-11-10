(api-random-random_old)=
# `random` (`random_old.F90`)

:Kind: Module
:Source: [`lanczosKuboCode/Src/random_old.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/random_old.F90#L1)
:Group: {ref}`Sources not in the solver build <api-group-unbuilt>`
:Uses: {ref}`mio <api-mio>`, {ref}`name <api-name>`, {ref}`parallel <api-parallel>`
:Used by: —
:Public interface: 2 procedures
:Input keys: 2 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`RandGen <api-random-random_old-randgen>`
  - —
* - {ref}`RandInit <api-random-random_old-randinit>`
  - —
```

## Procedures

(api-random-random_old-randgen)=
### `RandGen`

```fortran
function RandGen() result(rand)
```

```{rubric} Returns
```

`rand`: `real(dp)`

Defined in [`lanczosKuboCode/Src/random_old.F90, line 91`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/random_old.F90#L91).

(api-random-random_old-randinit)=
### `RandInit`

```fortran
subroutine RandInit()
```

```{rubric} Input keys read (2)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Random.Test`
  - Old random-number module (random\_old.F90, not compiled): run a test of the generator.
* - `Random.TestNumber`
  - Random.Test: number of random numbers drawn.
```

Defined in [`lanczosKuboCode/Src/random_old.F90, line 24`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/random_old.F90#L24).
