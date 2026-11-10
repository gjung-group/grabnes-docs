(api-version)=
# `version`

:Kind: Module
:Source: [`lanczosKuboCode/Src/version.f90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/version.f90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: —
:Used by: —
:Public interface: 2 procedures

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`VersionGet <api-version-versionget>`
  - —
* - {ref}`VersionUpdate <api-version-versionupdate>`
  - —
```

## Procedures

(api-version-versionget)=
### `VersionGet`

```fortran
function VersionGet() result(res)
```

```{rubric} Returns
```

`res`: `character(len=len)`

Defined in [`lanczosKuboCode/Src/version.f90, line 21`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/version.f90#L21).

(api-version-versionupdate)=
### `VersionUpdate`

```fortran
function VersionUpdate() result(res)
```

```{rubric} Returns
```

`res`: `character(len=len)`

Defined in [`lanczosKuboCode/Src/version.f90, line 41`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/version.f90#L41).
