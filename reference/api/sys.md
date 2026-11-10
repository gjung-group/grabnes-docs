(api-sys)=
# `sys`

:Kind: Module
:Source: [`lanczosKuboCode/Src/MIO/sys.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L13)
:Group: {ref}`MIO library <api-group-mio>`
:Uses: {ref}`format <api-format>`, {ref}`io <api-io>`, {ref}`mpi <api-mpi>`
:Used by: {ref}`file <api-file>`, {ref}`input <api-input>`, {ref}`mem <api-mem>`, {ref}`mio <api-mio>`, {ref}`parser <api-parser>`, {ref}`timer <api-timer>`
:Public interface: 9 procedures, 1 generic interface

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`SysDebugging <api-sys-sysdebugging>`
  - —
* - {ref}`SysKill <api-sys-syskill>`
  - —
* - {ref}`SysKillFlush <api-sys-syskillflush>`
  - —
* - {ref}`SysPrintDebug <api-sys-sysprintdebug>`
  - —
* - {ref}`SysPrintErrors <api-sys-sysprinterrors>`
  - —
* - {ref}`SysSection <api-sys-syssection>`
  - —
* - {ref}`SysSetDebug <api-sys-syssetdebug>`
  - —
* - {ref}`SysSubsection <api-sys-syssubsection>`
  - —
* - {ref}`SysWarning <api-sys-syswarning>`
  - —
```

## Generic interfaces

```{list-table}
:header-rows: 1
:class: api-table
:widths: 30 70

* - Interface
  - Specific procedures
* - `SysPrint`
  - `SysPrint_mod`, `SysPrint__`
```

## Procedures

(api-sys-sysdebugging)=
### `SysDebugging`

```fortran
logical function SysDebugging(module)
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

```{rubric} Returns
```

`SysDebugging`: `logical`

Defined in [`lanczosKuboCode/Src/MIO/sys.F90, line 450`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L450).

(api-sys-syskill)=
### `SysKill`

```fortran
subroutine SysKill(message, module, func, hold)
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
* - `message`
  - `character(len=*), intent(in)`
  - —
* - `module`
  - `character(len=*), intent(in)`
  - —
* - `func`
  - `character(len=*), intent(in), optional`
  - —
* - `hold`
  - `logical, intent(in), optional`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/sys.F90, line 72`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L72).

(api-sys-syskillflush)=
### `SysKillFlush`

```fortran
subroutine SysKillFlush()
```

Defined in [`lanczosKuboCode/Src/MIO/sys.F90, line 324`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L324).

(api-sys-sysprintdebug)=
### `SysPrintDebug`

```fortran
subroutine SysPrintDebug(message, module, force)
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
* - `message`
  - `character(len=*), intent(in)`
  - —
* - `module`
  - `character(len=*), intent(in)`
  - —
* - `force`
  - `logical, intent(in), optional`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/sys.F90, line 480`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L480).

(api-sys-sysprinterrors)=
### `SysPrintErrors`

```fortran
subroutine SysPrintErrors(final)
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
* - `final`
  - `logical, intent(in), optional`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/sys.F90, line 284`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L284).

(api-sys-syssection)=
### `SysSection`

```fortran
subroutine SysSection(title, module)
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
* - `title`
  - `character(len=*), intent(in)`
  - —
* - `module`
  - `character(len=*), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/sys.F90, line 363`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L363).

(api-sys-syssetdebug)=
### `SysSetDebug`

```fortran
subroutine SysSetDebug(on, module)
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
* - `on`
  - `logical, intent(in)`
  - —
* - `module`
  - `character(len=*), intent(in), optional`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/sys.F90, line 411`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L411).

(api-sys-syssubsection)=
### `SysSubsection`

```fortran
subroutine SysSubsection(title, module)
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
* - `title`
  - `character(len=*), intent(in)`
  - —
* - `module`
  - `character(len=*), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/sys.F90, line 391`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L391).

(api-sys-syswarning)=
### `SysWarning`

```fortran
subroutine SysWarning(message, module, func)
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
* - `message`
  - `character(len=*), intent(in)`
  - —
* - `module`
  - `character(len=*), intent(in)`
  - —
* - `func`
  - `character(len=*), intent(in), optional`
  - —
```

Defined in [`lanczosKuboCode/Src/MIO/sys.F90, line 137`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/MIO/sys.F90#L137).
