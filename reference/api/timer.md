(api-timer)=
# `timer`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/timer.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/timer.F90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: {ref}`mem <api-mem>`, {ref}`mpi <api-mpi>`, {ref}`precision <api-precision>`, {ref}`sys <api-sys>`
:Used by: {ref}`input <api-input>`, {ref}`mio <api-mio>`
:Public interface: 3 procedures

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`TimerCount <api-timer-timercount>`
  - —
* - {ref}`TimerPrint <api-timer-timerprint>`
  - —
* - {ref}`TimerStop <api-timer-timerstop>`
  - —
```

## Procedures

(api-timer-timercount)=
### `TimerCount`

```fortran
subroutine TimerCount(module)
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
* - `module`
  - `character(len=*), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/timer.F90, line 57`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/timer.F90#L57).

(api-timer-timerprint)=
### `TimerPrint`

```fortran
subroutine TimerPrint()
```

Defined in [`lanczosKuboCode/Src/MIO/timer.F90, line 167`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/timer.F90#L167).

(api-timer-timerstop)=
### `TimerStop`

```fortran
subroutine TimerStop(module)
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
* - `module`
  - `character(len=*), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/timer.F90, line 121`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/timer.F90#L121).
