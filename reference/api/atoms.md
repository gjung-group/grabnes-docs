(api-atoms)=
# `atoms`

:Kind: Module
:Source: [`lanczosKuboCode/Src/atoms.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/atoms.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`cell <api-cell>`, {ref}`constants <api-constants>`, {ref}`hybrid <api-hybrid>`, {ref}`math <api-math>`, {ref}`mio <api-mio>`, {ref}`name <api-name>`, {ref}`parallel <api-parallel>`
:Used by: {ref}`calc <api-calc>`, {ref}`diag <api-diag>`, {ref}`gauss <api-gauss>`, {ref}`grabnes <api-grabnes>`, {ref}`ham <api-ham>`, {ref}`interface <api-interface>`, {ref}`kubo <api-kubo>`, {ref}`kubosubs <api-kubosubs>`, {ref}`neigh <api-neigh>`, {ref}`scf <api-scf>`
:Public interface: 4 procedures, 33 variables
:Input keys: 119 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`AtomsPos <api-atoms-atomspos>`
  - —
* - {ref}`AtomsRotate <api-atoms-atomsrotate>`
  - —
* - {ref}`AtomsSetCart <api-atoms-atomssetcart>`
  - —
* - {ref}`AtomsSetFrac <api-atoms-atomssetfrac>`
  - —
```

## Procedures

(api-atoms-atomspos)=
### `AtomsPos`

```fortran
subroutine AtomsPos()
```

```{rubric} Input keys read (118)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Stack.EncapsulatedThreeLayers`
  - Stack model flag (ham.F90). Here: with a displacement file, each graphene atom reads two displacements (bottom and top interface, six columns).
* - `Run.TypeOfSystem`
  - Here: selects how the atoms are built or read (AtomsPos).
* - `Structure.BasedOnMoireCellParameters`
  - Here: the atoms of a Graphene / BoronNitride cell are built in the cell of Structure.MoireCellParameters.
* - `Structure.MoireCellParameters`
  - Here: indices m1 m2 m3 m4 of the commensurate cell in which the layers are built.
* - `Structure.InterlayerDistance`
  - Interlayer distance d of the stacks built by the code \[Angstrom\] (layers at +-d/2 about the cell centre); default 3.35 (3.22 before October 2026).
* - `Structure.CellSize`
  - Here: number of graphene cells along each lattice vector of the atoms built for Graphene / BoronNitride.
* - `Structure.SuperCellAsymmetric`
  - Here: the atoms are built on CellSize\*SuperCell x CellSize\*SuperCellY graphene cells.
* - `Moire.DistanceDependentEffectiveModel`
  - Here: allocates the per-atom interlayer distances (all 3.35 Angstrom) for Graphene cells.
* - `Structure.TwistedBLAddShift`
  - BilayerGraphene\_Over\_BN, TwistedBilayerBasedOnMoireCell, MoireEncapsulatedBilayerBasedOnMoireCell: shift the second layer by the Bernal (Structure.BernalShift) or bridge (Structure.BridgeShift) offset, plus Structure.BilayerShiftFactor. Without it the two layers of the moire cell form a twisted pair.
* - `Structure.BernalShift`
  - Structure.TwistedBLAddShift / TrilayerAddShift: the added shift is the Bernal (AB) offset.
* - `Structure.BridgeShift`
  - Structure.TwistedBLAddShift / TrilayerAddShift: the added shift is half the Bernal offset (bridge stacking).
* - `Structure.BilayerShiftFactor`
  - Extra shift of the second layer along a1+a2 \[Angstrom\] (in Angstrom since November 2026).
* - `Structure.CreateBLDomainBoundary`
  - TwistedBilayerBasedOnMoireCell: build a domain boundary in the bilayer: the layers are displaced in opposite directions along y over a strip starting at x = L/2.
* - `Structure.BLDomainBoundaryWidth`
  - Structure.CreateBLDomainBoundary: width of the strip over which the shift grows \[Angstrom\].
* - `Structure.BLDomainBoundaryTypeArmAA`
  - Structure.CreateBLDomainBoundary: armchair boundary of the AA type (PRB 88 115409).
* - `Structure.BLDomainBoundaryTypeArmSP`
  - Structure.CreateBLDomainBoundary: armchair boundary of the SP type (both layers moved).
* - `Structure.BLDomainBoundaryNRShifts`
  - Structure.CreateBLDomainBoundary: total shift in units of a/sqrt(3).
* - `Structure.TwistedBilayerAngle`
  - TypeOfSystem TwistedBilayer / MoireEncapsulatedBilayer: twist angle of the second layer \[degrees\].
* - `Structure.TrilayerAddShift`
  - TrilayerBasedOnMoireCell: shift a layer by the Bernal or bridge offset (Structure.BernalShift / BridgeShift), plus Structure.TrilayerShiftFactor.
* - `Structure.TrilayerShiftFactor`
  - Structure.TrilayerAddShift: extra shift along a1+a2 \[Angstrom\].
* - `Structure.RibbonType`
  - Here: Zigzag or Armchair ribbon atoms (AtomsRibbons).
* - `Structure.XYZFile`
  - Here: the atoms (symbol x y z \[Angstrom\]) are read from line 5 of the file on.
* - `Structure.UseSublatticeFile`
  - ReadXYZ: take the Species of every atom from Structure.SublatticeFile instead of the element symbol (C = 1, B = 3, N = 4).
* - `Structure.SublatticeFile`
  - Structure.UseSublatticeFile: file of the Species; its first two tokens per line are read as (index, Species), same atom order as the structure file.
* - `Structure.ReadInterlayerDistances`
  - ReadXYZ: read one interlayer distance per atom from Structure.InterlayerDistanceFile \[Angstrom\].
* - `Structure.InterlayerDistanceFile`
  - Structure.ReadInterlayerDistances: file of the distances, one per atom in file order.
* - `GBN.UseDisplacementFile`
  - G/hBN stacking-dependent on-site model from per-atom stacking displacements, read from Structure.DisplacementsFile (or computed, Structure.DisplacementsFromPositions).
* - `TBG.UseDisplacementFile`
  - Twisted-bilayer stacking-dependent on-site model from per-atom stacking displacements, read from Structure.DisplacementsFile (or computed, Structure.DisplacementsFromPositions).
* - `Structure.DisplacementsFromPositions`
  - Compute the stacking displacements of GBN/TBG.UseDisplacementFile from the rigid (generateInit.xyz) and actual structures instead of reading a file.
* - `Structure.DisplacementsFile`
  - File of the stacking displacements, one line 'dx dy d' per atom in file order.
* - `Structure.SuperCellX`
  - ReadXYZ: repetitions of the read cell along a1 (with Structure.SuperCellY; different values allowed).
* - `Structure.SuperCellY`
  - ReadXYZ: repetitions of the read cell along a2 (with Structure.SuperCellX).
* - `Structure.ReadLayerIndex`
  - Take the layer index of every atom from layerIndex.dat (one value per line, file order) instead of the z windows of the stack flags. Recommended for relaxed cells.
* - `Structure.ReadRigidXYZ`
  - ReadXYZ: also read the rigid (unrelaxed) positions from Structure.RigidPositions, same atom order.
* - `Structure.InvertDisplacements`
  - Change the sign of the in-plane stacking displacements read from the file.
* - `Structure.RigidPositions`
  - Structure.ReadRigidXYZ: file of the rigid positions (xyz format, same atom order).
* - `Stack.FourLayers`
  - Stack model flag (ham.F90). Here: layer index from the z windows Stack.FourLayersZ1..Z4.
* - `Stack.FourLayersSandwiched`
  - Stack model flag (ham.F90). Here: layer index from Stack.FourLayersZ1..Z4.
* - `Stack.HelicalTwistedMBM`
  - Stack model flag (ham.F90). Here: layer index from Stack.FourLayersZ1..Z4.
* - `Stack.FiveLayersSandwiched`
  - Stack model flag (ham.F90). Here: layer index from Stack.FiveLayersZ1..Z5.
* - `Stack.SixLayersSandwiched`
  - Stack model flag (ham.F90). Here: layer index from Stack.SixLayersZ1..Z6.
* - `Stack.SevenLayersSandwiched`
  - Stack model flag (ham.F90). Here: layer index from Stack.SevenLayersZ1..Z7.
* - `Stack.EightLayersSandwiched`
  - Stack model flag (ham.F90). Here: layer index from Stack.EightLayersZ1..Z8.
* - `Stack.TenLayersSandwiched`
  - Stack model flag (ham.F90). Here: layer index from Stack.TenLayersZ1..Z10.
* - `Stack.TwentyLayersSandwiched`
  - Stack model flag (ham.F90). Here: layer index from Stack.TwentyLayersZ1..Z20.
* - `Stack.ThreeLayers`
  - Stack model flag (ham.F90). Here: layer index from Stack.ThreeLayersZ1..Z3.
* - `Stack.OneLayer`
  - Stack model flag (ham.F90). Here: every atom in layer 1.
* - `Stack.TwoLayers`
  - Stack model flag (ham.F90). Here: layer index from Stack.TwoLayersZ1..Z2.
* - `Stack.TwoLayersZ1`
  - z centre of layer 1 \[Angstrom\] for the stack flags that use the Stack.TwoLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwoLayersZ2`
  - z centre of layer 2 \[Angstrom\] for the stack flags that use the Stack.TwoLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.ThreeLayersZ1`
  - z centre of layer 1 \[Angstrom\] for the stack flags that use the Stack.ThreeLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.ThreeLayersZ2`
  - z centre of layer 2 \[Angstrom\] for the stack flags that use the Stack.ThreeLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.ThreeLayersZ3`
  - z centre of layer 3 \[Angstrom\] for the stack flags that use the Stack.ThreeLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.FourLayersZ1`
  - z centre of layer 1 \[Angstrom\] for the stack flags that use the Stack.FourLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.FourLayersZ2`
  - z centre of layer 2 \[Angstrom\] for the stack flags that use the Stack.FourLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.FourLayersZ3`
  - z centre of layer 3 \[Angstrom\] for the stack flags that use the Stack.FourLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.FourLayersZ4`
  - z centre of layer 4 \[Angstrom\] for the stack flags that use the Stack.FourLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.FiveLayersZ1`
  - z centre of layer 1 \[Angstrom\] for the stack flags that use the Stack.FiveLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.FiveLayersZ2`
  - z centre of layer 2 \[Angstrom\] for the stack flags that use the Stack.FiveLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.FiveLayersZ3`
  - z centre of layer 3 \[Angstrom\] for the stack flags that use the Stack.FiveLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.FiveLayersZ4`
  - z centre of layer 4 \[Angstrom\] for the stack flags that use the Stack.FiveLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.FiveLayersZ5`
  - z centre of layer 5 \[Angstrom\] for the stack flags that use the Stack.FiveLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SixLayersZ1`
  - z centre of layer 1 \[Angstrom\] for the stack flags that use the Stack.SixLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SixLayersZ2`
  - z centre of layer 2 \[Angstrom\] for the stack flags that use the Stack.SixLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SixLayersZ3`
  - z centre of layer 3 \[Angstrom\] for the stack flags that use the Stack.SixLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SixLayersZ4`
  - z centre of layer 4 \[Angstrom\] for the stack flags that use the Stack.SixLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SixLayersZ5`
  - z centre of layer 5 \[Angstrom\] for the stack flags that use the Stack.SixLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SixLayersZ6`
  - z centre of layer 6 \[Angstrom\] for the stack flags that use the Stack.SixLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SevenLayersZ1`
  - z centre of layer 1 \[Angstrom\] for the stack flags that use the Stack.SevenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SevenLayersZ2`
  - z centre of layer 2 \[Angstrom\] for the stack flags that use the Stack.SevenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SevenLayersZ3`
  - z centre of layer 3 \[Angstrom\] for the stack flags that use the Stack.SevenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SevenLayersZ4`
  - z centre of layer 4 \[Angstrom\] for the stack flags that use the Stack.SevenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SevenLayersZ5`
  - z centre of layer 5 \[Angstrom\] for the stack flags that use the Stack.SevenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SevenLayersZ6`
  - z centre of layer 6 \[Angstrom\] for the stack flags that use the Stack.SevenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.SevenLayersZ7`
  - z centre of layer 7 \[Angstrom\] for the stack flags that use the Stack.SevenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.EightLayersZ1`
  - z centre of layer 1 \[Angstrom\] for the stack flags that use the Stack.EightLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.EightLayersZ2`
  - z centre of layer 2 \[Angstrom\] for the stack flags that use the Stack.EightLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.EightLayersZ3`
  - z centre of layer 3 \[Angstrom\] for the stack flags that use the Stack.EightLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.EightLayersZ4`
  - z centre of layer 4 \[Angstrom\] for the stack flags that use the Stack.EightLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.EightLayersZ5`
  - z centre of layer 5 \[Angstrom\] for the stack flags that use the Stack.EightLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.EightLayersZ6`
  - z centre of layer 6 \[Angstrom\] for the stack flags that use the Stack.EightLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.EightLayersZ7`
  - z centre of layer 7 \[Angstrom\] for the stack flags that use the Stack.EightLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.EightLayersZ8`
  - z centre of layer 8 \[Angstrom\] for the stack flags that use the Stack.EightLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ1`
  - z centre of layer 1 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ2`
  - z centre of layer 2 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ3`
  - z centre of layer 3 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ4`
  - z centre of layer 4 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ5`
  - z centre of layer 5 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ6`
  - z centre of layer 6 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ7`
  - z centre of layer 7 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ8`
  - z centre of layer 8 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ9`
  - z centre of layer 9 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TenLayersZ10`
  - z centre of layer 10 \[Angstrom\] for the stack flags that use the Stack.TenLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ1`
  - z centre of layer 1 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ2`
  - z centre of layer 2 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ3`
  - z centre of layer 3 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ4`
  - z centre of layer 4 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ5`
  - z centre of layer 5 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ6`
  - z centre of layer 6 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ7`
  - z centre of layer 7 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ8`
  - z centre of layer 8 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ9`
  - z centre of layer 9 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ10`
  - z centre of layer 10 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ11`
  - z centre of layer 11 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ12`
  - z centre of layer 12 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ13`
  - z centre of layer 13 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ14`
  - z centre of layer 14 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ15`
  - z centre of layer 15 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ16`
  - z centre of layer 16 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ17`
  - z centre of layer 17 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ18`
  - z centre of layer 18 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ19`
  - z centre of layer 19 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.TwentyLayersZ20`
  - z centre of layer 20 \[Angstrom\] for the stack flags that use the Stack.TwentyLayersZ\* windows; an atom goes to the layer whose window holds it (only the midpoints between neighbouring centres matter).
* - `Stack.GBNtwoLayers`
  - Stack model flag (ham.F90). Here: graphene (Species 1, 2) is layer 1, everything else layer 2.
* - `Stack.T2GBN`
  - Stack model flag (ham.F90). Here: layer index from Stack.ThreeLayersZ1..Z3.
* - `Stack.T2BG`
  - Stack model flag (ham.F90); read here but not used for the layer index.
* - `Stack.T3BG`
  - Stack model flag (ham.F90). Here: layer index from Stack.SixLayersZ1..Z6.
* - `Stack.EncapsulatedFourLayers`
  - Stack model flag (ham.F90). Here: layer index from Stack.FourLayersZ1..Z4.
```

Defined in [`lanczosKuboCode/Src/atoms.F90, line 69`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/atoms.F90#L69).

(api-atoms-atomsrotate)=
### `AtomsRotate`

```fortran
subroutine AtomsRotate(angle)
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
* - `angle`
  - `real(dp), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/atoms.F90, line 37`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/atoms.F90#L37).

(api-atoms-atomssetcart)=
### `AtomsSetCart`

```fortran
subroutine AtomsSetCart()
```

Defined in [`lanczosKuboCode/Src/atoms.F90, line 1762`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/atoms.F90#L1762).

(api-atoms-atomssetfrac)=
### `AtomsSetFrac`

```fortran
subroutine AtomsSetFrac()
```

Defined in [`lanczosKuboCode/Src/atoms.F90, line 1790`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/atoms.F90#L1790).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `dIntLay`
  - `real(dp)`
  - —
* - `displacements`
  - `real(dp), dimension(:,:), pointer`
  - `NULL()`
* - `displacements_b`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `displacements_t`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `frac`
  - `logical, save`
  - `.true.`
* - `in1`
  - `integer, save`
  - —
* - `in2`
  - `integer, save`
  - —
* - `indxDiv`
  - `integer, dimension(:), pointer`
  - —
* - `indxNode`
  - `integer, dimension(:), pointer`
  - —
* - `inode1`
  - `integer, save`
  - —
* - `inode2`
  - `integer, save`
  - —
* - `interlayerDistances`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `layerIndex`
  - `integer, dimension(:), pointer`
  - —
* - `nAt`
  - `integer, save`
  - —
* - `nAtBN`
  - `integer, save`
  - —
* - `nAtC`
  - `integer, save`
  - —
* - `nAtC1`
  - `integer, save`
  - —
* - `nAtC2`
  - `integer, save`
  - —
* - `nAtC3`
  - `integer, save`
  - —
* - `nEl`
  - `real(dp)`
  - —
* - `phiForEffectiveModel`
  - `real(dp)`
  - —
* - `procAt`
  - `integer, dimension(:), pointer`
  - —
* - `Rat`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `RatBN`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `RatC`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `RatC1`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `RatC2`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `RatC3`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `RatInit`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `RatTemp`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `secAt`
  - `integer, dimension(:), pointer`
  - —
* - `Species`
  - `integer, dimension(:), pointer`
  - —
* - `SpeciesTemp`
  - `integer, dimension(:), pointer`
  - —
```

## Input keys read by private procedures

Procedures that are not part of the public interface but read input keys.

**`AtomsOrder`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/atoms.F90#L1890))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Structure.AtomsOrderDeactivated`
  - Keep the atoms in input order (default). .false. reorders them in spatial bins for the parallel decomposition; refused for ReadXYZ, whose per-atom files are in file order.
```
