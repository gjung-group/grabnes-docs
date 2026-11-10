(api-moireblshift)=
# `moireBLShift`

:Kind: Module
:Source: [`lanczosKuboCode/Src/moireBLShift.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/moireBLShift.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`cell <api-cell>`, {ref}`mio <api-mio>`, {ref}`name <api-name>`
:Used by: {ref}`calc <api-calc>`, {ref}`ham <api-ham>`
:Public interface: 2 procedures, 7 variables
:Input keys: 15 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`moireBLShiftInit <api-moireblshift-moireblshiftinit>`
  - —
* - {ref}`moireBLShiftValue <api-moireblshift-moireblshiftvalue>`
  - —
```

## Procedures

(api-moireblshift-moireblshiftinit)=
### `moireBLShiftInit`

```fortran
subroutine moireBLShiftInit()
```

```{rubric} Input keys read (3)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Moire.BLShiftDefinedValues`
  - moireBLShift.Calc: one calculation with the shifts Moire.Bilayer{Bottom,Top}{X,Y}Shift.
* - `Moire.BLShiftRange`
  - moireBLShift.Calc: sweep each shift from its Moire.Bilayer\*Min to \*Max in Moire.BLShiftRangeSteps steps.
* - `Moire.BLShiftRangeSteps`
  - Moire.BLShiftRange: number of steps of the shift sweep.
```

Defined in [`lanczosKuboCode/Src/moireBLShift.F90, line 17`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/moireBLShift.F90#L17).

(api-moireblshift-moireblshiftvalue)=
### `moireBLShiftValue`

```fortran
subroutine moireBLShiftValue(mS)
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
* - `mS`
  - `integer, intent(in)`
  - —
```

```{rubric} Input keys read (12)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Moire.BilayerBottomXShift`
  - Moire.BLShiftDefinedValues: x shift of the bottom layer (written into the output prefix).
* - `Moire.BilayerBottomYShift`
  - Moire.BLShiftDefinedValues: y shift of the bottom layer.
* - `Moire.BilayerTopXShift`
  - Moire.BLShiftDefinedValues: x shift of the top layer.
* - `Moire.BilayerTopYShift`
  - Moire.BLShiftDefinedValues: y shift of the top layer.
* - `Moire.BilayerBottomXMin`
  - Moire.BLShiftRange: first x shift of the bottom layer.
* - `Moire.BilayerBottomXMax`
  - Moire.BLShiftRange: last x shift of the bottom layer.
* - `Moire.BilayerBottomYMin`
  - Moire.BLShiftRange: first y shift of the bottom layer.
* - `Moire.BilayerBottomYMax`
  - Moire.BLShiftRange: last y shift of the bottom layer.
* - `Moire.BilayerTopXMin`
  - Moire.BLShiftRange: first x shift of the top layer.
* - `Moire.BilayerTopXMax`
  - Moire.BLShiftRange: last x shift of the top layer.
* - `Moire.BilayerTopYMin`
  - Moire.BLShiftRange: first y shift of the top layer.
* - `Moire.BilayerTopYMax`
  - Moire.BLShiftRange: last y shift of the top layer.
```

Defined in [`lanczosKuboCode/Src/moireBLShift.F90, line 55`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/moireBLShift.F90#L55).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `mSf`
  - `integer, save`
  - `0`
* - `mSi`
  - `integer, save`
  - `0`
* - `mSStep`
  - `integer, save`
  - `1`
* - `tauX1`
  - `real(dp), save`
  - —
* - `tauX2`
  - `real(dp), save`
  - —
* - `tauY1`
  - `real(dp), save`
  - —
* - `tauY2`
  - `real(dp), save`
  - —
```
