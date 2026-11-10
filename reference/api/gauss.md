(api-gauss)=
# `gauss`

:Kind: Module
:Source: [`lanczosKuboCode/Src/gauss.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/gauss.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`atoms <api-atoms>`, {ref}`cell <api-cell>`, {ref}`mio <api-mio>`, {ref}`neigh <api-neigh>`, {ref}`parallel <api-parallel>`, {ref}`random <api-random>`
:Used by: {ref}`ham <api-ham>`
:Public interface: 3 procedures
:Input keys: 7 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`GaussHeight <api-gauss-gaussheight>`
  - —
* - {ref}`GaussPot <api-gauss-gausspot>`
  - —
* - {ref}`GaussPotDefinedPositions <api-gauss-gausspotdefinedpositions>`
  - —
```

## Procedures

(api-gauss-gaussheight)=
### `GaussHeight`

```fortran
subroutine GaussHeight()
```

```{rubric} Input keys read (3)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Strain.GaussHeightPercentage`
  - RandomStrain (refused at present): percentage of atoms that carry a Gaussian bump.
* - `Strain.GaussHeightRange`
  - RandomStrain (refused at present): width sigma of each bump \[Angstrom\].
* - `Strain.GaussHeightStrength`
  - RandomStrain (refused at present): height amplitude of the bumps (added to z) \[Angstrom\].
```

Defined in [`lanczosKuboCode/Src/gauss.F90, line 217`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/gauss.F90#L217).

(api-gauss-gausspot)=
### `GaussPot`

```fortran
subroutine GaussPot(H, strength)
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
* - `H`
  - `real(dp), dimension(inode1:), intent(inout)`
  - —
* - `strength`
  - `real(dp), intent(in)`
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
* - `Disorder.GaussPotPercentage`
  - Gaussian disorder: percentage of the atoms that carry a Gaussian impurity potential.
* - `Disorder.GaussPotRange`
  - Gaussian disorder: width sigma of each impurity, exp(-r^2/(2 sigma^2)) \[Angstrom\]; random amplitudes in \[-w/2, w/2\].
```

Defined in [`lanczosKuboCode/Src/gauss.F90, line 18`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/gauss.F90#L18).

(api-gauss-gausspotdefinedpositions)=
### `GaussPotDefinedPositions`

```fortran
subroutine GaussPotDefinedPositions(H)
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
* - `H`
  - `real(dp), dimension(inode1:), intent(inout)`
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
* - `Strain.BubbleGaussPotRange`
  - Strain.BubbleGaussian: width sigma of the Gaussian potential at each bubble \[Angstrom\].
* - `Strain.BubbleGaussPotStrength`
  - Strain.BubbleGaussian: amplitude of the Gaussian potential at each bubble \[units of g0\].
```

Defined in [`lanczosKuboCode/Src/gauss.F90, line 145`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/gauss.F90#L145).
