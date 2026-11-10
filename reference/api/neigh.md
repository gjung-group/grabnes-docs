(api-neigh)=
# `neigh`

:Kind: Module
:Source: [`lanczosKuboCode/Src/neigh.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`atoms <api-atoms>`, {ref}`cell <api-cell>`, {ref}`constants <api-constants>`, {ref}`math <api-math>`, {ref}`mio <api-mio>`, {ref}`parallel <api-parallel>`, {ref}`tbpar <api-tbpar>`
:Used by: {ref}`calc <api-calc>`, {ref}`diag <api-diag>`, {ref}`gauss <api-gauss>`, {ref}`ham <api-ham>`, {ref}`interface <api-interface>`, {ref}`kubosubs <api-kubosubs>`, {ref}`scf <api-scf>`
:Public interface: 9 procedures, 18 variables
:Input keys: 16 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`fastNN <api-neigh-fastnn>`
  - —
* - {ref}`fastNNnotsquare <api-neigh-fastnnnotsquare>`
  - —
* - {ref}`fastNNnotsquareBulk <api-neigh-fastnnnotsquarebulk>`
  - —
* - {ref}`fastNNnotsquareBulkSmall <api-neigh-fastnnnotsquarebulksmall>`
  - —
* - {ref}`fastNNnotsquareNotRectangle <api-neigh-fastnnnotsquarenotrectangle>`
  - —
* - {ref}`fastNNnotsquareSmall <api-neigh-fastnnnotsquaresmall>`
  - —
* - {ref}`NeighList <api-neigh-neighlist>`
  - —
* - {ref}`NeighShellCutoff2 <api-neigh-neighshellcutoff2>`
  - Squared in-plane search radius that contains the first nshell neighbour shells of a honeycomb lattice with bond length aCC.
* - {ref}`NeighShellWarn2 <api-neigh-neighshellwarn2>`
  - Squared in-plane length beyond which an intralayer pair is closer to the search radius of NeighShellCutoff2 than a rigid lattice allows: the last quarter of the interval between the last requested shell and the radius. Pairs found there belong to a strained structure.
```

## Procedures

(api-neigh-fastnn)=
### `fastNN`

```fortran
subroutine fastNN(natoms, x, y, z, aCC, cutoff, A1, A2, maxnn)
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
* - `natoms`
  - `integer`
  - —
* - `x`
  - `double precision, dimension(natoms)`
  - —
* - `y`
  - `double precision, dimension(natoms)`
  - —
* - `z`
  - `double precision, dimension(natoms)`
  - —
* - `aCC`
  - `double precision`
  - —
* - `cutoff`
  - `double precision`
  - —
* - `A1`
  - `real(dp), dimension(3), intent(in)`
  - —
* - `A2`
  - `real(dp), dimension(3), intent(in)`
  - —
* - `maxnn`
  - `integer`
  - —
```

Defined in [`lanczosKuboCode/Src/neigh.F90, line 2414`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L2414).

(api-neigh-fastnnnotsquare)=
### `fastNNnotsquare`

```fortran
subroutine fastNNnotsquare(natoms, x, y, z, cutoff2, cutoff2bis, A1, A2)
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
* - `natoms`
  - `integer, intent(in)`
  - —
* - `x`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `y`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `z`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `cutoff2`
  - `real(dp), intent(in)`
  - —
* - `cutoff2bis`
  - `real(dp), intent(in)`
  - —
* - `A1`
  - `real(dp), dimension(3), intent(in)`
  - —
* - `A2`
  - `real(dp), dimension(3), intent(in)`
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
* - `Output.ReadDataFiles`
  - Here: the neighbour lists are read from the files v, dx, dy, dz instead of searched.
* - `Interlayer.AddSecondLayerInteractions`
  - Also pair atoms two layers apart (4.5 \< \|dz\| \< 7.5 Angstrom) in the neighbour search, for the models with next-layer hoppings.
```

Defined in [`lanczosKuboCode/Src/neigh.F90, line 1433`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L1433).

(api-neigh-fastnnnotsquarebulk)=
### `fastNNnotsquareBulk`

```fortran
subroutine fastNNnotsquareBulk(natoms, x, y, z, cutoff2, cutoff2bis, A1, A2, A3)
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
* - `natoms`
  - `integer, intent(in)`
  - —
* - `x`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `y`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `z`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `cutoff2`
  - `real(dp), intent(in)`
  - —
* - `cutoff2bis`
  - `real(dp), intent(in)`
  - —
* - `A1`
  - `real(dp), dimension(3), intent(in)`
  - —
* - `A2`
  - `real(dp), dimension(3), intent(in)`
  - —
* - `A3`
  - `real(dp), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/neigh.F90, line 1904`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L1904).

(api-neigh-fastnnnotsquarebulksmall)=
### `fastNNnotsquareBulkSmall`

```fortran
subroutine fastNNnotsquareBulkSmall(natoms, x, y, z, cutoff2, cutoff2bis, A1, A2, A3)
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
* - `natoms`
  - `integer, intent(in)`
  - —
* - `x`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `y`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `z`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `cutoff2`
  - `real(dp), intent(in)`
  - —
* - `cutoff2bis`
  - `real(dp), intent(in)`
  - —
* - `A1`
  - `real(dp), dimension(3), intent(in)`
  - —
* - `A2`
  - `real(dp), dimension(3), intent(in)`
  - —
* - `A3`
  - `real(dp), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/neigh.F90, line 1942`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L1942).

(api-neigh-fastnnnotsquarenotrectangle)=
### `fastNNnotsquareNotRectangle`

```fortran
subroutine fastNNnotsquareNotRectangle(natoms, x, y, z, aCC, cutoff2, cutoff2bis, A1, A2, maxnn)
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
* - `natoms`
  - `integer, intent(in)`
  - —
* - `x`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `y`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `z`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `aCC`
  - `real(dp)`
  - —
* - `cutoff2`
  - `real(dp)`
  - —
* - `cutoff2bis`
  - `real(dp)`
  - —
* - `A1`
  - `real(dp), dimension(3)`
  - —
* - `A2`
  - `real(dp), dimension(3)`
  - —
* - `maxnn`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/neigh.F90, line 1983`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L1983).

(api-neigh-fastnnnotsquaresmall)=
### `fastNNnotsquareSmall`

```fortran
subroutine fastNNnotsquareSmall(natoms, x, y, z, aCC, cutoff2, cutoff2bis, A1, A2, maxnn)
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
* - `natoms`
  - `integer, intent(in)`
  - —
* - `x`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `y`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `z`
  - `real(dp), dimension(natoms), intent(in)`
  - —
* - `aCC`
  - `real(dp), intent(in)`
  - —
* - `cutoff2`
  - `real(dp), intent(in)`
  - —
* - `cutoff2bis`
  - `real(dp), intent(in)`
  - —
* - `A1`
  - `real(dp), dimension(3), intent(in)`
  - —
* - `A2`
  - `real(dp), dimension(3), intent(in)`
  - —
* - `maxnn`
  - `integer, intent(in)`
  - —
```

```{rubric} Input keys read (1)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Neigh.Only000Cell`
  - fastNNnotsquareSmall: keep only the first-neighbour image in the home cell when assigning image cells.
```

Defined in [`lanczosKuboCode/Src/neigh.F90, line 1477`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L1477).

(api-neigh-neighlist)=
### `NeighList`

```fortran
subroutine NeighList()
```

```{rubric} Input keys read (9)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Structure.InterlayerDistance`
  - Here (NeighList): sets the interlayer neighbour radius sqrt((1.1 aBN)^2/3 + d^2).
* - `Neigh.LayerNeighbors`
  - NeighList (Neigh.fastNNnotsquare .false.): interlayer neighbours per atom reserved in the list.
* - `Neigh.LayerDistFactor`
  - NeighList with Neigh.BLInPlaneInteractionRadius: in-plane cutoff 1.1 aG/sqrt(3) times this factor.
* - `Neigh.CompareAll`
  - NeighList: compare every pair of atoms (with the 3 x 3 neighbouring cells). Without it NeighList is known to give wrong bands; a warning is printed.
* - `Neigh.CompareAll.UltraSmall`
  - NeighList: as Neigh.CompareAll with the 7 x 7 neighbouring cells, for cells of fewer than ~36 atoms.
* - `Neigh.BLInPlaneInteractionRadius`
  - NeighList: select neighbours by their in-plane distance (z ignored) within the in-plane cutoff.
* - `Neigh.SafetyCheck`
  - NeighList: list the atoms with fewer than Neigh.ExpectedNumber neighbours.
* - `Neigh.ExpectedNumber`
  - Neigh.SafetyCheck: minimum expected number of neighbours per atom.
* - `Neigh.Print`
  - Print the neighbour list (atom, neighbour, slot, image cell) in the output; atoms without 3 entries are marked.
```

Defined in [`lanczosKuboCode/Src/neigh.F90, line 524`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L524).

(api-neigh-neighshellcutoff2)=
### `NeighShellCutoff2`

```fortran
function NeighShellCutoff2(nshell, aCC) result(cut2)
```

Squared in-plane search radius that contains the first nshell neighbour shells of a honeycomb lattice with bond length aCC.

The radius lies halfway between shell nshell and the next one, so it tolerates moderately strained or relaxed lattices.

```{rubric} Arguments
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 18 40 42

* - Name
  - Declaration
  - Description
* - `nshell`
  - `integer, intent(in)`
  - —
* - `aCC`
  - `real(dp), intent(in)`
  - —
```

```{rubric} Returns
```

`cut2`: `real(dp)`

Defined in [`lanczosKuboCode/Src/neigh.F90, line 63`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L63).

(api-neigh-neighshellwarn2)=
### `NeighShellWarn2`

```fortran
function NeighShellWarn2(nshell, aCC) result(warn2)
```

Squared in-plane length beyond which an intralayer pair is closer to the search radius of NeighShellCutoff2 than a rigid lattice allows: the last quarter of the interval between the last requested shell and the radius. Pairs found there belong to a strained structure.

```{rubric} Arguments
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 18 40 42

* - Name
  - Declaration
  - Description
* - `nshell`
  - `integer, intent(in)`
  - —
* - `aCC`
  - `real(dp), intent(in)`
  - —
```

```{rubric} Returns
```

`warn2`: `real(dp)`

Defined in [`lanczosKuboCode/Src/neigh.F90, line 86`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L86).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `maxNeigh`
  - `integer`
  - `3`
* - `maxShells`
  - `integer, parameter`
  - `8`
* - `neighCell`
  - `integer, dimension(:,:,:), pointer`
  - —
* - `NeighD`
  - `real(dp), dimension(:,:,:), pointer`
  - —
* - `NeighIntraWarn2`
  - `real(dp), save`
  - `0.0_dp`
* - `NList`
  - `integer, dimension(:,:), pointer`
  - —
* - `NList2`
  - `integer, dimension(:,:), pointer`
  - —
* - `Nneigh`
  - `integer, dimension(:), pointer`
  - —
* - `nodeSndRcv`
  - `integer, dimension(:,:), pointer`
  - `NULL()`
* - `Nradii`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `rcvIndx`
  - `integer, dimension(:,:), pointer`
  - `NULL()`
* - `rcvList`
  - `integer, dimension(:), pointer`
  - `NULL()`
* - `rcvSz`
  - `integer`
  - —
* - `shellCount`
  - `integer, dimension(maxShells), parameter`
  - `[3, 6, 3, 6, 6, 6, 6, 3]`
* - `shellRadius`
  - `real(dp), dimension(maxShells+1), parameter`
  - `[1.0_dp, 1.7320508075688772_dp, 2.0_dp, 2.6457513110645906_dp, 3.0_dp, 3.4641016151377544_dp, 3.6055512754639891_dp, 4.0_dp, 4.3588989435406740_dp]`
* - `sndIndx`
  - `integer, dimension(:,:), pointer`
  - `NULL()`
* - `sndList`
  - `integer, dimension(:), pointer`
  - `NULL()`
* - `sndSz`
  - `integer`
  - —
```

## Input keys read by private procedures

Procedures that are not part of the public interface but read input keys.

**`NeighFinishSearch`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L319))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Output.WriteDataFiles`
  - Write the neighbour lists and the Hamiltonian to files (v, dx, dy, dz, pos, neighCell.dat, neighD.dat, \<prefix>.e, \<prefix>.s.mag, ...): a complete export of H, large for big cells.
```

**`NeighSetRadii`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L348))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Run.TypeOfSystem`
  - Here: BoronNitride uses the hBN lattice constant for every neighbour radius.
```

**`NeighReadDataFiles`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L446))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Neigh.ReadDetails`
  - With Output.ReadDataFiles: also read neighCell.dat and neighD.dat (image cell and bond vector of each pair).
```

**`NeighListOld`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/neigh.F90#L1023))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Neigh.Distance`
  - NeighListOld: first-neighbour distance \[Angstrom\]; pairs within 1.1 times it are neighbours.
```
