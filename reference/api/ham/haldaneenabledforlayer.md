(api-ham-haldaneenabledforlayer)=
# `HaldaneEnabledForLayer`

```{index} single: HaldaneEnabledForLayer (function in ham)
```

```fortran
function HaldaneEnabledForLayer(layerIndex) result(enabled)
```

:Module: {ref}`ham <api-ham>`
:Kind: Function
:Source: [`lanczosKuboCode/Src/ham.F90, line 13632`](https://github.com/gjung-group/grabnes/blob/1e390c6ead7c835389ae89a599cb1f39e3fc691e/lanczosKuboCode/Src/ham.F90#L13632)

Check if Haldane should be applied to a specific layer

```{rubric} Parameters
```

`layerIndex` : `integer, intent(in)`
: Layer index to check

```{rubric} Returns
```

`enabled` : `logical`
: True if Haldane should be applied to this layer

```{rubric} Called by
```

{ref}`HamHopping <api-ham-hamhopping>`
