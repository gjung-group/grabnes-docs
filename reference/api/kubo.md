(api-kubo)=
# `kubo`

:Kind: Module
:Source: [`lanczosKuboCode/Src/kubo.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubo.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`atoms <api-atoms>`, {ref}`constants <api-constants>`, {ref}`kubosubs <api-kubosubs>`, {ref}`mio <api-mio>`, {ref}`name <api-name>`, {ref}`parallel <api-parallel>`
:Used by: {ref}`calc <api-calc>`
:Public interface: 6 procedures
:Input keys: 4 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`KuboDOS <api-kubo-kubodos>`
  - —
* - {ref}`KuboInitWF <api-kubo-kuboinitwf>`
  - —
* - {ref}`KuboInitWFLayerAndSpeciesDOS <api-kubo-kuboinitwflayerandspeciesdos>`
  - —
* - {ref}`KuboInitWFLayerDOS <api-kubo-kuboinitwflayerdos>`
  - —
* - {ref}`KuboInitWFPDOS <api-kubo-kuboinitwfpdos>`
  - —
* - {ref}`KuboTEvol <api-kubo-kubotevol>`
  - —
```

## Procedures

(api-kubo-kubodos)=
### `KuboDOS`

```fortran
subroutine KuboDOS(Psi, Psin, Psinm1, a, b, H, H0, hopp, NList, nRecurs, eps, nEn, Emin, Emax)
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
* - `Psi`
  - `complex(dp), dimension(inode1:), intent(out)`
  - —
* - `Psin`
  - `complex(dp), dimension(inode1:), intent(out)`
  - —
* - `Psinm1`
  - `complex(dp), dimension(inode1:), intent(out)`
  - —
* - `a`
  - `real(dp), dimension(nRecurs), intent(out)`
  - —
* - `b`
  - `real(dp), dimension(nRecurs), intent(out)`
  - —
* - `H`
  - `complex(dp), dimension(inode1:), intent(out)`
  - —
* - `H0`
  - `real(dp), dimension(inode1:), intent(in)`
  - —
* - `hopp`
  - `complex(dp), dimension(:,inode1:), intent(in)`
  - —
* - `NList`
  - `integer, dimension(1:,inode1:), intent(in)`
  - —
* - `nRecurs`
  - `integer, intent(in)`
  - —
* - `eps`
  - `real(dp), intent(in)`
  - —
* - `nEn`
  - `integer, intent(in)`
  - —
* - `Emin`
  - `real(dp)`
  - —
* - `Emax`
  - `real(dp)`
  - —
```

Defined in [`lanczosKuboCode/Src/kubo.F90, line 276`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubo.F90#L276).

(api-kubo-kuboinitwf)=
### `KuboInitWF`

```fortran
subroutine KuboInitWF(Psi)
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
* - `Psi`
  - `complex(dp), dimension(inode1:), intent(out)`
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
* - `Kubo.SetSeed`
  - Seed the random-phase start vector with Kubo.SeedValue; otherwise from the clock (runs not reproducible).
* - `Kubo.SeedValue`
  - Kubo.SetSeed: seed of the random-phase start vector; use different values to average over vectors.
```

Defined in [`lanczosKuboCode/Src/kubo.F90, line 24`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubo.F90#L24).

(api-kubo-kuboinitwflayerandspeciesdos)=
### `KuboInitWFLayerAndSpeciesDOS`

```fortran
subroutine KuboInitWFLayerAndSpeciesDOS(Psi, layerNumber, speciesNumber, numberOfLayers, numberOfAtomsInLayer)
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
* - `Psi`
  - `complex(dp), dimension(inode1:), intent(out)`
  - —
* - `layerNumber`
  - `integer`
  - —
* - `speciesNumber`
  - `integer`
  - —
* - `numberOfLayers`
  - `integer`
  - —
* - `numberOfAtomsInLayer`
  - `integer`
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
* - `Kubo.SeedSet`
  - Seed of the random-phase start vector of a layer-and-species DOS (Kubo.PDOSLayerAndSpecies).
```

Defined in [`lanczosKuboCode/Src/kubo.F90, line 214`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubo.F90#L214).

(api-kubo-kuboinitwflayerdos)=
### `KuboInitWFLayerDOS`

```fortran
subroutine KuboInitWFLayerDOS(Psi, layerNumber, numberOfLayers, numberOfAtomsInLayer)
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
* - `Psi`
  - `complex(dp), dimension(inode1:), intent(out)`
  - —
* - `layerNumber`
  - `integer`
  - —
* - `numberOfLayers`
  - `integer`
  - —
* - `numberOfAtomsInLayer`
  - `integer`
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
* - `Kubo.SeedSet`
  - Seed of the random-phase start vector of a layer DOS (Kubo.PDOSLayer); always used, not the clock.
```

Defined in [`lanczosKuboCode/Src/kubo.F90, line 140`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubo.F90#L140).

(api-kubo-kuboinitwfpdos)=
### `KuboInitWFPDOS`

```fortran
subroutine KuboInitWFPDOS(Psi, PDOSAtomNumber)
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
* - `Psi`
  - `complex(dp), dimension(inode1:), intent(out)`
  - —
* - `PDOSAtomNumber`
  - `integer`
  - —
```

Defined in [`lanczosKuboCode/Src/kubo.F90, line 87`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubo.F90#L87).

(api-kubo-kubotevol)=
### `KuboTEvol`

```fortran
subroutine KuboTEvol(Psi, ZUPsi, Psin, Psinm1, XpnPsi, XpnPsim1, c, dT, nT, az, bz, H, H0, hopp, NList, NeighD, ac, bc, nEn, Emin, Emax, eps, nRecurs, nPol, nWr)
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
* - `Psi`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `ZUPsi`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `Psin`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `Psinm1`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `XpnPsi`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `XpnPsim1`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `c`
  - `complex(dp), dimension(nPol), intent(in)`
  - —
* - `dT`
  - `real(dp), intent(in)`
  - —
* - `nT`
  - `integer, intent(in)`
  - —
* - `az`
  - `real(dp), dimension(nRecurs), intent(inout)`
  - —
* - `bz`
  - `real(dp), dimension(nRecurs), intent(inout)`
  - —
* - `H`
  - `complex(dp), dimension(inode1:), intent(out)`
  - —
* - `H0`
  - `real(dp), dimension(inode1:), intent(in)`
  - —
* - `hopp`
  - `complex(dp), dimension(:,inode1:), intent(in)`
  - —
* - `NList`
  - `integer, dimension(1:,inode1:), intent(in)`
  - —
* - `NeighD`
  - `real(dp), dimension(1:,1:,inode1:), intent(in)`
  - —
* - `ac`
  - `real(dp), intent(in)`
  - —
* - `bc`
  - `real(dp), intent(in)`
  - —
* - `nEn`
  - `integer, intent(in)`
  - —
* - `Emin`
  - `real(dp), intent(in)`
  - —
* - `Emax`
  - `real(dp), intent(in)`
  - —
* - `eps`
  - `real(dp), intent(in)`
  - —
* - `nRecurs`
  - `integer, intent(in)`
  - —
* - `nPol`
  - `integer, intent(in)`
  - —
* - `nWr`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/kubo.F90, line 321`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubo.F90#L321).
