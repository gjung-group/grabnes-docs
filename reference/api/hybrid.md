(api-hybrid)=
# `hybrid`

:Kind: Module
:Source: [`lanczosKuboCode/Src/hybrid.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/hybrid.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`cell <api-cell>`, {ref}`constants <api-constants>`, {ref}`mio <api-mio>`
:Used by: {ref}`atoms <api-atoms>`
:Public interface: 1 procedure
:Input keys: 5 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`HybridGen <api-hybrid-hybridgen>`
  - —
```

## Procedures

(api-hybrid-hybridgen)=
### `HybridGen`

```fortran
subroutine HybridGen(nAt, Rat, Species, in1, in2)
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
* - `nAt`
  - `integer, intent(in)`
  - —
* - `Rat`
  - `real(dp), dimension(3,nAt), intent(in)`
  - —
* - `Species`
  - `integer, dimension(nAt), intent(inout)`
  - —
* - `in1`
  - `integer, intent(in)`
  - —
* - `in2`
  - `integer, intent(in)`
  - —
```

```{rubric} Input keys read (5)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Hybrid.Radius`
  - TypeOfSystem Hybrid (refused at present): radius of the hBN islands in graphene \[Angstrom\].
* - `Hybrid.Percentage`
  - TypeOfSystem Hybrid (refused at present): percentage of the area covered by hBN islands.
* - `Structure.SuperCell`
  - Here (TypeOfSystem Hybrid): sets the size of the region where islands are placed.
* - `Structure.CellSize`
  - Here (TypeOfSystem Hybrid): sets the size of the region where islands are placed.
* - `Hybrid.RandomSites`
  - TypeOfSystem Hybrid (refused at present): place the islands at random sites.
```

Defined in [`lanczosKuboCode/Src/hybrid.F90, line 13`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/hybrid.F90#L13).
