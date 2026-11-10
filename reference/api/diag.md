(api-diag)=
# `diag`

:Kind: Module
:Source: [`lanczosKuboCode/Src/diag.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`atoms <api-atoms>`, {ref}`cell <api-cell>`, {ref}`constants <api-constants>`, {ref}`ham <api-ham>`, {ref}`interface <api-interface>`, `iso_fortran_env`, {ref}`magf <api-magf>`, {ref}`math <api-math>`, {ref}`mio <api-mio>`, {ref}`name <api-name>`, {ref}`neigh <api-neigh>`, `omp_lib`, {ref}`scf <api-scf>`, {ref}`tbpar <api-tbpar>`
:Used by: {ref}`calc <api-calc>`
:Public interface: 16 procedures, 32 variables
:Input keys: 63 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`Diag3DBands <api-diag-diag3dbands>`
  - —
* - {ref}`DiagBands <api-diag-diagbands>`
  - —
* - {ref}`DiagBandsAroundK <api-diag-diagbandsaroundk>`
  - —
* - {ref}`DiagBandsG <api-diag-diagbandsg>`
  - —
* - {ref}`DiagBandsRashba <api-diag-diagbandsrashba>`
  - —
* - {ref}`DiagChern <api-diag-diagchern>`
  - —
* - {ref}`DiagDOS <api-diag-diagdos>`
  - —
* - {ref}`DiagInit <api-diag-diaginit>`
  - —
* - {ref}`DiagPDOS <api-diag-diagpdos>`
  - —
* - {ref}`DiagSpectralFunction <api-diag-diagspectralfunction>`
  - —
* - {ref}`DiagSpectralFunctionKGrid <api-diag-diagspectralfunctionkgrid>`
  - —
* - {ref}`DiagSpectralFunctionKGridInequivalent <api-diag-diagspectralfunctionkgridinequivalent>`
  - —
* - {ref}`DiagSpectralFunctionKGridInequivalent_v2 <api-diag-diagspectralfunctionkgridinequivalent_v2>`
  - —
* - {ref}`DiagSpectralFunctionKGridInequivalentEnergyCut <api-diag-diagspectralfunctionkgridinequivalentenergycut>`
  - —
* - {ref}`DiagSpectralFunctionKGridInequivalentEnergyCut_v2 <api-diag-diagspectralfunctionkgridinequivalentenergycut_v2>`
  - —
* - {ref}`DiagSpectralFunctionKGridInequivalentEnergyCutNickDale <api-diag-diagspectralfunctionkgridinequivalentenergycutnickdale>`
  - —
```

## Procedures

(api-diag-diag3dbands)=
### `Diag3DBands`

```fortran
subroutine Diag3DBands()
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 498`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L498).

(api-diag-diagbands)=
### `DiagBands`

```fortran
subroutine DiagBands()
```

```{rubric} Input keys read (13)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Bands.NumPoints`
  - k-points on the first leg of Bands.Path; the other legs get points in proportion to their length (all the same with Bands.UseSameNumberOfPoints).
* - `Bands.SparseNeig`
  - Diag.SparseSolver: number of eigenvalues computed per k-point.
* - `Bands.UseDifferentLatticeVectors`
  - Set ucell(1,2) and rcell(2,1) to zero before the path is built (rectangular-cell variant; see DiagBands).
* - `Bands.UseSameNumberOfPoints`
  - Every leg of Bands.Path gets Bands.NumPoints points, whatever its length.
* - `Output.KeepWaveFunction`
  - Dense diagonalisation that also writes the eigenvectors. Refused together with TAPW.Use or Diag.SparseSolver (it replaced those paths silently before).
* - `Diag.SparseSolver`
  - Bands by sparse ARPACK diagonalisation (DiagHamSparse): Bands.SparseNeig levels nearest E = 0, or nearest Diag.SparseSetShift with Diag.SparseUseShift. Cannot be combined with TAPW.Use.
* - `TAPW.Use`
  - Bands in the valley-projected plane-wave basis (TAPW): H is projected on plane waves around one graphene valley (Diag.N\_G, Diag.MoireAngle, Diag.UseKprimeValley); far fewer states than atoms.
* - `TAPW.UseDenseMatrix`
  - TAPW: project a dense N x N Hamiltonian (memory 16 N^2 bytes) instead of the sparse one; the sparse path is the one for large cells.
* - `TAPW.BlockMatrixFree`
  - Spinful block TAPW without the dense 2N x 2N block (matrix-free H\*X): much faster, little memory.
* - `Zeeman.Term`
  - Zeeman shift of the two spin sectors (needs Zeeman.SpinPolarized .true.; no effect, with a warning, in a one-spin run).
* - `Zeeman.PseudoTerm`
  - Pseudo-Zeeman term: not implemented, no effect (a warning is printed).
* - `TAPW.aG`
  - TAPW: graphene lattice constant of the plane-wave basis \[Angstrom\]; default 2.46019, the cells often use 2.46.
* - `Diag.SparseSetShift`
  - Here: copied for the TAPW path, which does not use it at present.
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 602`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L602).

(api-diag-diagbandsaroundk)=
### `DiagBandsAroundK`

```fortran
subroutine DiagBandsAroundK()
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 1821`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L1821).

(api-diag-diagbandsg)=
### `DiagBandsG`

```fortran
subroutine DiagBandsG()
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 1952`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L1952).

(api-diag-diagbandsrashba)=
### `DiagBandsRashba`

```fortran
subroutine DiagBandsRashba()
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 1686`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L1686).

(api-diag-diagchern)=
### `DiagChern`

```fortran
subroutine DiagChern()
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 1561`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L1561).

(api-diag-diagdos)=
### `DiagDOS`

```fortran
subroutine DiagDOS()
```

```{rubric} Input keys read (5)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Diag.KGrid`
  - Number of k-points along each reciprocal lattice vector (three integers) of the k-grid of the DOS, projected DOS, 3-D bands and spectral cuts; Monkhorst-Pack points for the DOS.
* - `Kubo.Epsilon`
  - Diagonalisation DOS: width of the Gaussian broadening of every level \[eV\].
* - `Kubo.NumberofEnergyPoints`
  - Diagonalisation DOS: number of points of the energy grid from DOS.Emin to DOS.Emax.
* - `DOS.Emin`
  - Lower end of the energy grid of the diagonalisation DOS \[eV\].
* - `DOS.Emax`
  - Upper end of the energy grid of the diagonalisation DOS \[eV\].
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 178`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L178).

(api-diag-diaginit)=
### `DiagInit`

```fortran
subroutine DiagInit(N)
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
* - `N`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 143`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L143).

(api-diag-diagpdos)=
### `DiagPDOS`

```fortran
subroutine DiagPDOS()
```

```{rubric} Input keys read (1)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Kubo.NumberOfLayers`
  - Here (DiagPDOS): number of layers onto which the DOS is projected.
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 345`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L345).

(api-diag-diagspectralfunction)=
### `DiagSpectralFunction`

```fortran
subroutine DiagSpectralFunction()
```

```{rubric} Input keys read (3)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Spectral.NumPoints`
  - k-points on the first leg of Spectral.Path; the other legs in proportion to their length.
* - `Kubo.NumberofEnergyPoints`
  - Spectral function: number of points of the energy grid from Spectral.Emin to Spectral.Emax.
* - `Spectral.GaussianConvolution`
  - Spectral function: write the weights convolved with a Gaussian of width Kubo.Epsilon.
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 2132`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L2132).

(api-diag-diagspectralfunctionkgrid)=
### `DiagSpectralFunctionKGrid`

```fortran
subroutine DiagSpectralFunctionKGrid()
```

```{rubric} Input keys read (1)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Structure.CellSize`
  - Here: the graphene-lattice path is divided by CellSize to give the k of the cell.
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 2333`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L2333).

(api-diag-diagspectralfunctionkgridinequivalent)=
### `DiagSpectralFunctionKGridInequivalent`

```fortran
subroutine DiagSpectralFunctionKGridInequivalent()
```

```{rubric} Input keys read (14)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Spectral.WeiKu`
  - Unfolded spectral weight per layer and sublattice on a graphene reference lattice (Wei Ku method), files \<prefix>.spectral\<layer>\<A\|B>.
* - `Spectral.UseGaussianBroadening`
  - Spectral.WeiKu: spread each level over the energy grid with a Gaussian of width Kubo.Epsilon.
* - `Spectral.WeiKuOld`
  - Spectral.WeiKu: use the older weight routine (A and B weights only).
* - `Spectral.Nishi`
  - Unfolding weights of the Nishi routine (sub-cell translations).
* - `Spectral.Lee`
  - Unfolding weights of the Lee routine.
* - `Spectral.FoldByOne`
  - Fold the graphene-lattice k into the cell's zone by subtracting G10 + G01.
* - `Spectral.FoldByZero`
  - Do not fold the graphene-lattice k (use it as it is).
* - `Spectral.UseCoordinates`
  - Spectral.Path points in Cartesian coordinates \[1/Angstrom\] instead of reciprocal-lattice units.
* - `Structure.MoireCellParameters`
  - Here: sets the angle of Spectral.RotateReferenceSystem.
* - `Spectral.RotateReferenceSystem`
  - Rotate the graphene reference lattice by the angle of Structure.MoireCellParameters.
* - `Spectral.AlignReferenceSystem`
  - Rotate the graphene reference lattice by Spectral.AlignmentAngle (a layer unfolds under its own orientation).
* - `Spectral.AlignmentAngle`
  - Spectral.AlignReferenceSystem: orientation of the reference lattice \[degrees\].
* - `Spectral.topBottomRatio`
  - Passed to the unfolding weight routines, which do not use it at present.
* - `Spectral.energyGridResolution`
  - A level adds its weight to every energy point closer than this \[eV\]: points further apart than twice it lose levels (a warning is printed).
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 2572`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L2572).

(api-diag-diagspectralfunctionkgridinequivalent_v2)=
### `DiagSpectralFunctionKGridInequivalent_v2`

```fortran
subroutine DiagSpectralFunctionKGridInequivalent_v2()
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 3156`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L3156).

(api-diag-diagspectralfunctionkgridinequivalentenergycut)=
### `DiagSpectralFunctionKGridInequivalentEnergyCut`

```fortran
subroutine DiagSpectralFunctionKGridInequivalentEnergyCut()
```

```{rubric} Input keys read (2)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Spectral.RotateOpposite`
  - Spectral.RotateReferenceSystem: rotate by the opposite angle.
* - `Spectral.KGridCut`
  - Constant-energy cuts: half side of the k box around graphene K = (2/3,1/3) \[1/Angstrom\], sampled by Diag.KGrid.
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 3673`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L3673).

(api-diag-diagspectralfunctionkgridinequivalentenergycut_v2)=
### `DiagSpectralFunctionKGridInequivalentEnergyCut_v2`

```fortran
subroutine DiagSpectralFunctionKGridInequivalentEnergyCut_v2()
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 4150`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L4150).

(api-diag-diagspectralfunctionkgridinequivalentenergycutnickdale)=
### `DiagSpectralFunctionKGridInequivalentEnergyCutNickDale`

```fortran
subroutine DiagSpectralFunctionKGridInequivalentEnergyCutNickDale()
```

```{rubric} Input keys read (3)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Spectral.KGridCutX`
  - NickDale cut: length of the kx line from graphene K \[1/Angstrom\].
* - `Spectral.KGridCutY`
  - NickDale cut: the line is at ky = K\_y + KGridCutY \[1/Angstrom\].
* - `Spectral.KGridLowerGridHalf`
  - NickDale cut: the kx line runs from K\_x - KGridCutX to K\_x instead of K\_x to K\_x + KGridCutX.
```

Defined in [`lanczosKuboCode/Src/diag.F90, line 4698`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L4698).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `calculate3DTAPWBands`
  - `logical, save`
  - `.false.`
* - `calculateChern`
  - `logical, save`
  - `.false.`
* - `checkTAPWUnitary`
  - `logical, save`
  - `.false.`
* - `fermi_energy`
  - `real(dp), save`
  - `0.0_dp`
* - `forceBlockTAPW`
  - `logical, save`
  - `.false.`
* - `gammaCentred3D`
  - `logical, save`
  - `.true.`
* - `gGridRotationAngle`
  - `real(dp), save`
  - `0.0_dp`
* - `gw_b1`
  - `integer, save`
  - `0`
* - `gw_b2`
  - `integer, save`
  - `0`
* - `gw_ntop`
  - `integer, save`
  - `8`
* - `gWeightsHam`
  - `logical, save`
  - `.false.`
* - `gWeightsTAPW`
  - `logical, save`
  - `.false.`
* - `layerWeightsTAPW`
  - `logical, save`
  - `.false.`
* - `lw_b1`
  - `integer, save`
  - `0`
* - `lw_b2`
  - `integer, save`
  - `0`
* - `M_tapw`
  - `integer, save`
  - `0`
* - `moireAngle`
  - `real(dp), save`
  - `33.004491598883078_dp`
* - `nk_3D_x`
  - `integer, save`
  - `10`
* - `nk_3D_y`
  - `integer, save`
  - `10`
* - `nk_chern_x`
  - `integer, save`
  - `10`
* - `nk_chern_y`
  - `integer, save`
  - `10`
* - `physicalTwistAngle`
  - `real(dp), save`
  - `1.08_dp`
* - `skipGRotation`
  - `logical, save`
  - `.false.`
* - `socDebug`
  - `logical, save`
  - `.false.`
* - `tapwBothValleys`
  - `logical, save`
  - `.false.`
* - `tapwDebug`
  - `logical, save`
  - `.false.`
* - `tapwLowdin`
  - `logical, save`
  - `.false.`
* - `tapwNG`
  - `integer, save`
  - `180`
* - `tapwValleyDecouple`
  - `logical, save`
  - `.false.`
* - `useKprimeValley`
  - `logical, save`
  - `.false.`
* - `useRigidPositions`
  - `logical, save`
  - `.false.`
* - `useTriangularTruncation`
  - `logical, save`
  - `.false.`
```

## Input keys read by private procedures

Procedures that are not part of the public interface but read input keys.

**`DiagSpectralWindow`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L2088))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Spectral.Emin`
  - Lower end of the energy grid of the spectral function \[eV\] (units of g0 before November 2026).
* - `Spectral.Emax`
  - Upper end of the energy grid of the spectral function \[eV\] (units of g0 before November 2026).
```

**`DiagSpectralEpsilon`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L2103))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Kubo.Epsilon`
  - Spectral function: Gaussian width of Spectral.UseGaussianBroadening / GaussianConvolution \[eV\] (units of g0 before November 2026).
```

**`DiagHamSparse`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L5180))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Diag.SparseUseShift`
  - Diag.SparseSolver: shift-invert mode (MKL PARDISO), the Bands.SparseNeig levels nearest Diag.SparseSetShift; output \<prefix>.SparseEig.
* - `Diag.SparseSetShift`
  - Diag.SparseUseShift: energy around which the levels are computed \[eV\].
* - `Diag.SparseSaveRitz`
  - Diag.SparseSolver: also compute the eigenvectors (Ritz vectors) in ARPACK.
* - `Diag.SparseCount`
  - Diag.SparseUseShift: count exactly the states below the shift (so level indices are absolute) and check completeness ('complete T/F' per k in \<prefix>.SparseEig).
* - `Diag.SparseSetTol`
  - Diag.SparseSolver: ARPACK tolerance (default 1e-9 in shift-invert mode, 0.1 otherwise). ! PARDISO initialization nnn = nn !nrhs = 1 a = values ia = row\_ptr ja = col\_ind maxfct = 1 mnum = 1 msglvl = 0 error = 0
```

**`DiagH0TAPW`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L5902))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `TAPW.UseTriangularDistanceOrder`
  - Diag.TriangularTruncation: order the triangular G list by distance (default) instead of grid order.
```

**`DiagHamChern`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L10766))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Kubo.Epsilon`
  - Here (DiagHamChern, refused): regularisation of the energy denominators.
```

**`DiagSpectralWeightNishi`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L11043))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Spectral.numberOfTS`
  - Spectral.Nishi: number of sub-cell translations (set to 6 by the routine).
```

**`CalculateChernTAPW`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L12066))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Diag.ChernEnergyWindow`
  - Diag.ChernCalculation: energy window around Diag.Chern\_EF for the band selection \[eV\].
* - `Diag.ChernAllOccupiedBands`
  - Diag.ChernCalculation: sum over all bands below the Fermi energy.
* - `Diag.ChernNBands`
  - Diag.ChernCalculation: number of bands included.
* - `Diag.ChernUseOptionA`
  - Diag.ChernCalculation: Berry curvature from the velocities in the TB basis instead of the TAPW basis.
* - `Diag.ChernBandsBelowFermi`
  - Diag.ChernCalculation: bands below the Fermi energy included.
* - `Diag.ChernBandsAboveFermi`
  - Diag.ChernCalculation: bands above the Fermi energy included.
* - `Diag.ChernTargetBands`
  - Diag.ChernCalculation: number of bands closest to the Fermi energy whose Chern numbers are reported.
```

**`CalculateBerryAtKpointFromStored`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/diag.F90#L12802))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Diag.ChernEnergyThreshold`
  - Diag.ChernCalculation: pairs of levels closer than this \[units of g0\] are left out of the Kubo sum.
* - `Diag.ChernEtaEV`
  - Diag.ChernCalculation: read but not used at present.
* - `Diag.ChernEps`
  - Diag.ChernCalculation: eps in the denominator (E\_n - E\_m)^2 + eps of the Kubo sum \[units of g0^2\].
```
