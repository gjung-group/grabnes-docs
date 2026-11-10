(api-magf)=
# `magf`

:Kind: Module
:Source: [`lanczosKuboCode/Src/magf.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/magf.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`cell <api-cell>`, {ref}`constants <api-constants>`, {ref}`mio <api-mio>`, {ref}`name <api-name>`
:Used by: {ref}`calc <api-calc>`, {ref}`diag <api-diag>`, {ref}`ham <api-ham>`
:Public interface: 4 procedures, 11 variables
:Input keys: 16 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`HaldPhaseInit <api-magf-haldphaseinit>`
  - —
* - {ref}`HaldPhaseValue <api-magf-haldphasevalue>`
  - —
* - {ref}`MagfInit <api-magf-magfinit>`
  - —
* - {ref}`MagfValue <api-magf-magfvalue>`
  - —
```

## Procedures

(api-magf-haldphaseinit)=
### `HaldPhaseInit`

```fortran
subroutine HaldPhaseInit()
```

```{rubric} Input keys read (6)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Haldane.SpecifyFlux`
  - Haldane model: one phase, 2 pi Haldane.Flux / Phi\_0 (no sweep over HaldPhase.\*).
* - `Haldane.SpecifyPhase`
  - Haldane model: one phase, Haldane.Phase \[rad\] (no sweep over HaldPhase.\*).
* - `Haldane.SpecifyRange`
  - Haldane model: sweep the phase over HaldPhase.InitialInteger..FinalInteger; step m has phase m\*2\*pi/(FinalInteger - InitialInteger).
* - `HaldPhase.InitialInteger`
  - Haldane.SpecifyRange: first step of the phase sweep.
* - `HaldPhase.FinalInteger`
  - Haldane.SpecifyRange: last step of the phase sweep.
* - `HaldPhase.Step`
  - Haldane.SpecifyRange: increment of the step index.
```

Defined in [`lanczosKuboCode/Src/magf.F90, line 148`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/magf.F90#L148).

(api-magf-haldphasevalue)=
### `HaldPhaseValue`

```fortran
subroutine HaldPhaseValue(mPhi)
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
* - `mPhi`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/magf.F90, line 213`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/magf.F90#L213).

(api-magf-magfinit)=
### `MagfInit`

```fortran
subroutine MagfInit()
```

```{rubric} Input keys read (8)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `MagField.Value`
  - Perpendicular magnetic field \[T\], rounded to an integer number of flux quanta through the cell (a warning is printed when it rounds to zero). Peierls phases on every hopping.
* - `MagField.Integer`
  - Perpendicular magnetic field as m flux quanta through the whole cell: B = m Phi\_0 / A. Use MagField.Integer 0 for no field.
* - `MagField.InitialB`
  - Field sweep from MagField.InitialB to MagField.FinalB \[T\], each rounded to whole flux quanta.
* - `MagField.FinalB`
  - Last field of the sweep started by MagField.InitialB \[T\].
* - `MagField.InitialInteger`
  - Field sweep in flux quanta through the cell, from InitialInteger to FinalInteger: one calculation per value, in folders m\<m>\_B\<B>. Both 0 = no field.
* - `MagField.FinalInteger`
  - Last value of the MagField.InitialInteger sweep (flux quanta through the cell).
* - `MagField.Step`
  - Step of a field sweep \[T\], rounded to whole flux quanta (otherwise MagField.IntegerStep).
* - `MagField.IntegerStep`
  - Step of a field sweep, in flux quanta through the cell.
```

Defined in [`lanczosKuboCode/Src/magf.F90, line 20`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/magf.F90#L20).

(api-magf-magfvalue)=
### `MagfValue`

```fortran
subroutine MagfValue(mB)
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
* - `mB`
  - `integer, intent(in)`
  - —
```

```{rubric} Input keys read (2)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Zeeman.Bmag`
  - Field of the Zeeman term \[T\], separate from the orbital field; the Zeeman energy is ZeemanFactor x Zeeman.Bmag.
* - `Run.TypeOfSystem`
  - Here: used to name the output folders of a field sweep.
```

Defined in [`lanczosKuboCode/Src/magf.F90, line 100`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/magf.F90#L100).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `Bmag`
  - `real(dp), save`
  - `0.0_dp`
* - `BmagZeeman`
  - `real(dp), save`
  - `0.0_dp`
* - `HaldanePhase`
  - `real(dp), save`
  - —
* - `HaldPhase`
  - `logical, save`
  - `.false.`
* - `magfield`
  - `logical, save`
  - `.false.`
* - `mBf`
  - `integer, save`
  - `0`
* - `mBi`
  - `integer, save`
  - `0`
* - `mPhif`
  - `integer, save`
  - `0`
* - `mPhii`
  - `integer, save`
  - `0`
* - `mPhiStep`
  - `integer, save`
  - `0`
* - `mStep`
  - `integer, save`
  - `1`
```
