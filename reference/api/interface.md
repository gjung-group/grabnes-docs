(api-interface)=
# `interface`

:Kind: Module
:Source: [`lanczosKuboCode/Src/interface.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/interface.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`atoms <api-atoms>`, {ref}`cell <api-cell>`, {ref}`constants <api-constants>`, {ref}`math <api-math>`, {ref}`mio <api-mio>`, {ref}`neigh <api-neigh>`, {ref}`tbpar <api-tbpar>`
:Used by: {ref}`diag <api-diag>`, {ref}`ham <api-ham>`
:Public interface: 2 procedures, 7 variables
:Input keys: 13 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`InterfacePot1 <api-interface-interfacepot1>`
  - —
* - {ref}`InterfacePot2 <api-interface-interfacepot2>`
  - —
```

## Procedures

(api-interface-interfacepot1)=
### `InterfacePot1`

```fortran
subroutine InterfacePot1()
```

```{rubric} Input keys read (13)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Interlayer.InterfaceClambda`
  - Edge potential A exp(-r/lambda)/r of a graphene/hBN interface: decay length lambda on carbon \[Angstrom\]. InterfacePot1, which reads it, is not called at present.
* - `Interlayer.InterfaceBNlambda`
  - Edge potential: decay length lambda on B and N \[Angstrom\] (InterfacePot1, not called).
* - `Interlayer.InterfaceClambda_B`
  - Edge potential: lambda on carbon from a B edge \[Angstrom\] (InterfacePot1, not called).
* - `Interlayer.InterfaceClambda_N`
  - Edge potential: lambda on carbon from an N edge \[Angstrom\] (InterfacePot1, not called).
* - `Interlayer.InterfaceBNlambda_B`
  - Edge potential: lambda on BN from a B edge \[Angstrom\] (InterfacePot1, not called).
* - `Interlayer.InterfaceBNlambda_N`
  - Edge potential: lambda on BN from an N edge \[Angstrom\] (InterfacePot1, not called).
* - `Interlayer.InterfaceAmpN`
  - Edge potential: amplitude A of N edges \[eV Angstrom\] (InterfacePot1, not called).
* - `Interlayer.InterfaceAmpB`
  - Edge potential: amplitude A of B edges \[eV Angstrom\] (InterfacePot1, not called).
* - `Interlayer.InterfaceAmpCN`
  - Edge potential: amplitude of N edges on carbon \[eV Angstrom\] (InterfacePot1, not called).
* - `Interlayer.InterfaceAmpCB`
  - Edge potential: amplitude of B edges on carbon \[eV Angstrom\] (InterfacePot1, not called).
* - `Interface.EdgeHopping`
  - Edge hopping correction at a graphene/hBN interface (InterfacePot1, not called at present).
* - `Interface.EdgeHoppingAmp`
  - Interface.EdgeHopping: amplitude (InterfacePot1, not called at present).
* - `Interface.EdgeHoppingDamp`
  - Interface.EdgeHopping: damping (InterfacePot1, not called at present).
```

Defined in [`lanczosKuboCode/Src/interface.F90, line 25`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/interface.F90#L25).

(api-interface-interfacepot2)=
### `InterfacePot2`

```fortran
subroutine InterfacePot2(H, Nneigh, NList, neighCell, neighD, Species, Nradii)
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
* - `Nneigh`
  - `integer, dimension(inode1:), intent(in)`
  - —
* - `NList`
  - `integer, dimension(1:maxNeigh,inode1:inode2), intent(in)`
  - —
* - `neighCell`
  - `integer, dimension(1:3,1:maxNeigh,inode1:inode2), intent(in)`
  - —
* - `neighD`
  - `real(dp), dimension(:,:,:), intent(in)`
  - —
* - `Species`
  - `integer, dimension(inode1:), intent(in)`
  - —
* - `Nradii`
  - `real(dp), dimension(:,:), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/interface.F90, line 120`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/interface.F90#L120).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `edgeH`
  - `real(dp), dimension(:,:), pointer`
  - —
* - `edgeHopp`
  - `logical, save`
  - —
* - `edgeIndx`
  - `integer, dimension(:), pointer`
  - —
* - `NedgeCell`
  - `integer, dimension(:,:,:), pointer`
  - —
* - `nEdgeN`
  - `integer, dimension(:), pointer`
  - —
* - `NeI`
  - `integer, dimension(:,:), pointer`
  - —
* - `nQ`
  - `integer, save`
  - —
```
