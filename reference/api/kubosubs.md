(api-kubosubs)=
# `kubosubs`

:Kind: Module
:Source: [`lanczosKuboCode/Src/kubosubs.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubosubs.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`atoms <api-atoms>`, {ref}`constants <api-constants>`, {ref}`kuboarrays <api-kuboarrays>`, {ref}`math <api-math>`, {ref}`mio <api-mio>`, {ref}`name <api-name>`, {ref}`neigh <api-neigh>`
:Used by: {ref}`calc <api-calc>`, {ref}`kubo <api-kubo>`
:Public interface: 7 procedures
:Input keys: 1 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`KuboChebyshevEvolve <api-kubosubs-kubochebyshevevolve>`
  - —
* - {ref}`KuboCn <api-kubosubs-kubocn>`
  - —
* - {ref}`KuboEvol <api-kubosubs-kuboevol>`
  - —
* - {ref}`KuboFermi <api-kubosubs-kubofermi>`
  - —
* - {ref}`KuboFrac <api-kubosubs-kubofrac>`
  - —
* - {ref}`KuboInterval <api-kubosubs-kubointerval>`
  - —
* - {ref}`KuboRecursion <api-kubosubs-kuborecursion>`
  - —
```

## Procedures

(api-kubosubs-kubochebyshevevolve)=
### `KuboChebyshevEvolve`

```fortran
subroutine KuboChebyshevEvolve(Z, Psin, Psinm1, c, H0, hopp, NList, ac, bc, nPol)
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
* - `Z`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `Psin`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `Psinm1`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `c`
  - `complex(dp), dimension(nPol), intent(in)`
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
* - `ac`
  - `real(dp), intent(in)`
  - —
* - `bc`
  - `real(dp), intent(in)`
  - —
* - `nPol`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/kubosubs.F90, line 557`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubosubs.F90#L557).

(api-kubosubs-kubocn)=
### `KuboCn`

```fortran
subroutine KuboCn(dT, ac, bc, nPol, c)
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
* - `dT`
  - `real(dp), intent(in)`
  - —
* - `ac`
  - `real(dp), intent(in)`
  - —
* - `bc`
  - `real(dp), intent(in)`
  - —
* - `nPol`
  - `integer, intent(in)`
  - —
* - `c`
  - `complex(dp), dimension(nPol), intent(out)`
  - —
```

Defined in [`lanczosKuboCode/Src/kubosubs.F90, line 352`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubosubs.F90#L352).

(api-kubosubs-kuboevol)=
### `KuboEvol`

```fortran
subroutine KuboEvol(Psi, ZUPsi, Psin, Psinm1, XpnPsi, XpnPsim1, c, H0, hopp, NList, NeighD, ac, bc, nPol, prnt, dir)
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
* - `nPol`
  - `integer, intent(in)`
  - —
* - `prnt`
  - `logical, intent(in)`
  - —
* - `dir`
  - `integer, intent(in), optional`
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
* - `Kubo.TimeEvolutionInYDirection`
  - Kubo time evolution: position operator along y instead of x.
```

Defined in [`lanczosKuboCode/Src/kubosubs.F90, line 438`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubosubs.F90#L438).

(api-kubosubs-kubofermi)=
### `KuboFermi`

```fortran
subroutine KuboFermi(npts)
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
* - `npts`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/kubosubs.F90, line 677`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubosubs.F90#L677).

(api-kubosubs-kubofrac)=
### `KuboFrac`

```fortran
subroutine KuboFrac(a, b, nRecurs, norm, eps, nEn, Emin, Emax, name, name2)
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
* - `a`
  - `real(dp), dimension(nRecurs), intent(in)`
  - —
* - `b`
  - `real(dp), dimension(nRecurs), intent(in)`
  - —
* - `nRecurs`
  - `integer, intent(in)`
  - —
* - `norm`
  - `real(dp), intent(in)`
  - —
* - `eps`
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
* - `name`
  - `character(len=*), intent(in)`
  - —
* - `name2`
  - `character(len=*), intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/kubosubs.F90, line 222`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubosubs.F90#L222).

(api-kubosubs-kubointerval)=
### `KuboInterval`

```fortran
subroutine KuboInterval(nRecurs, a, b, ac, bc)
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
* - `nRecurs`
  - `integer, intent(in)`
  - —
* - `a`
  - `real(dp), dimension(nRecurs), intent(in)`
  - —
* - `b`
  - `real(dp), dimension(nRecurs), intent(in)`
  - —
* - `ac`
  - `real(dp), intent(out)`
  - —
* - `bc`
  - `real(dp), intent(out)`
  - —
```

Defined in [`lanczosKuboCode/Src/kubosubs.F90, line 290`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubosubs.F90#L290).

(api-kubosubs-kuborecursion)=
### `KuboRecursion`

```fortran
subroutine KuboRecursion(Psi, Psin, Psinm1, nRecurs, a, b, H, H0, hopp, NList, wr, name, store, overlapWith, overlaps)
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
* - `Psin`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `Psinm1`
  - `complex(dp), dimension(inode1:), intent(inout)`
  - —
* - `nRecurs`
  - `integer, intent(in)`
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
* - `wr`
  - `logical, intent(in)`
  - —
* - `name`
  - `character(len=*), intent(in), optional`
  - —
* - `store`
  - `complex(dp), dimension(:,:), intent(out), optional`
  - —
* - `overlapWith`
  - `complex(dp), dimension(inode1:), intent(in), optional`
  - —
* - `overlaps`
  - `complex(dp), dimension(nRecurs), intent(out), optional`
  - —
```

Defined in [`lanczosKuboCode/Src/kubosubs.F90, line 26`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/kubosubs.F90#L26).
