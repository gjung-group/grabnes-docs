(api-random)=
# `random` (`random.F90`)

:Kind: Module
:Source: [`lanczosKuboCode/Src/random.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/random.F90#L1)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`mio <api-mio>`, {ref}`name <api-name>`
:Used by: {ref}`gauss <api-gauss>`, {ref}`ham <api-ham>`
:Public interface: 2 procedures, 1 derived type
:Input keys: 2 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`RandSeedFromInput <api-random-randseedfrominput>`
  - Seed the intrinsic random-number generator for the disorder models.
* - {ref}`RandTest <api-random-randtest>`
  - —
```

## Procedures

(api-random-randseedfrominput)=
### `RandSeedFromInput`

```fortran
subroutine RandSeedFromInput()
```

Seed the intrinsic random-number generator for the disorder models.

With setSeed .true. the seed is seedValue, so that a disordered Hamiltonian can be reproduced; otherwise it comes from the system clock, as before.

```{rubric} Input keys read (2)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Kubo.SetSeed`
  - Here: also seeds the random numbers of the disorder models (RandSeedFromInput) with Kubo.SeedValue.
* - `Kubo.SeedValue`
  - Here: seed of the random numbers of the disorder models when Kubo.SetSeed is set.
```

Defined in [`lanczosKuboCode/Src/random.F90, line 31`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/random.F90#L31).

(api-random-randtest)=
### `RandTest`

```fortran
subroutine RandTest(rng, n)
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
* - `rng`
  - `type(rand_t), intent(inout)`
  - —
* - `n`
  - `integer, intent(in)`
  - —
```

Defined in [`lanczosKuboCode/Src/random.F90, line 74`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/random.F90#L74).

## Derived types

(api-random-type-rand_t)=
### `rand_t`

```{list-table}
:header-rows: 1
:class: api-table
:widths: 24 46 30

* - Component
  - Declaration
  - Default
* - `state`
  - `integer, dimension(ns)`
  - `default_seed`
```
