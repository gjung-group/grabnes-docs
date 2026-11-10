(api-cell)=
# `cell`

:Kind: Module
:Source: [`lanczosKuboCode/Src/cell.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/cell.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`constants <api-constants>`, {ref}`math <api-math>`, {ref}`mio <api-mio>`, {ref}`name <api-name>`
:Used by: {ref}`atoms <api-atoms>`, {ref}`calc <api-calc>`, {ref}`diag <api-diag>`, {ref}`gauss <api-gauss>`, {ref}`grabnes <api-grabnes>`, {ref}`ham <api-ham>`, {ref}`hybrid <api-hybrid>`, {ref}`interface <api-interface>`, {ref}`magf <api-magf>`, {ref}`moireBLShift <api-moireblshift>`, {ref}`neigh <api-neigh>`, {ref}`scf <api-scf>`, {ref}`tbpar <api-tbpar>`
:Public interface: 1 procedure, 8 variables
:Input keys: 14 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`CellGet <api-cell-cellget>`
  - —
```

## Procedures

(api-cell-cellget)=
### `CellGet`

```fortran
subroutine CellGet()
```

```{rubric} Input keys read (14)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Structure.LatticeParameter`
  - Graphene lattice constant aG \[Angstrom\]; the cells built by the code are multiples of it.
* - `Structure.LatticeParameterBN`
  - hBN lattice constant \[Angstrom\] (cells built from Structure.MoireCellParameters set it from the indices).
* - `Run.TypeOfSystem`
  - Kind of structure: built by the code (Graphene, BoronNitride, Ribbons, TwistedBilayerBasedOnMoireCell, ...) or read from a file (ReadXYZ). It selects the cell, the atoms and parts of the Hamiltonian.
* - `Structure.CellHeight`
  - Length of the third (out-of-plane) cell vector \[Angstrom\] for the cells built by the code.
* - `Structure.SuperCell`
  - Repeat the cell N x N in the plane (the atoms are copied, no reordering: copy 0 holds the original atoms). Equivalent to an N x N k-sampling of the original cell for local quantities.
* - `Structure.SuperCellAsymmetric`
  - Repeat the cell Structure.SuperCell times along a1 and Structure.SuperCellY times along a2.
* - `Structure.SuperCellY`
  - Structure.SuperCellAsymmetric: number of copies along the second lattice vector.
* - `Structure.BasedOnMoireCellParameters`
  - Graphene / BoronNitride / TwistedBilayer cells: build the commensurate cell from the four indices of Structure.MoireCellParameters instead of CellSize x CellSize graphene cells.
* - `Structure.MoireCellParameters`
  - Four integers m1 m2 m3 m4 of the commensurate moire cell: a1 = m1 a + m2 b on the first lattice, (m3, m4) on the second; the twist angle and lattice ratio follow from them and are printed.
* - `Structure.CellSize`
  - Number of graphene cells along each lattice vector of a cell built by the code (TypeOfSystem Graphene, BoronNitride); the cell is CellSize\*SuperCell graphene cells on a side.
* - `Structure.RibbonType`
  - TypeOfSystem Ribbons: edge of the ribbons, Zigzag or Armchair.
* - `Structure.GrapheneWidth`
  - TypeOfSystem Ribbons: width of the graphene ribbon, in rows of the ribbon cell.
* - `Structure.BNWidth`
  - TypeOfSystem Ribbons: width of the hBN ribbon, in rows of the ribbon cell.
* - `Structure.XYZFile`
  - TypeOfSystem ReadXYZ: structure file. Its first three lines are the lattice vectors \[Angstrom\], the atoms follow.
```

Defined in [`lanczosKuboCode/Src/cell.F90, line 16`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/cell.F90#L16).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `aBN`
  - `real(dp), save`
  - —
* - `aG`
  - `real(dp), save`
  - —
* - `area`
  - `real(dp), save`
  - —
* - `rcell`
  - `real(dp), dimension(3,3), save`
  - —
* - `sCell`
  - `integer, save`
  - —
* - `sCell2`
  - `integer, save`
  - —
* - `ucell`
  - `real(dp), dimension(3,3), save`
  - —
* - `volume`
  - `real(dp), save`
  - —
```
