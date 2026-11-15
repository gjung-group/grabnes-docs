(api-format-num2stri)=
# `num2stri`

```{index} single: num2stri (function in format)
```

```fortran
elemental function num2stri(num) result(string)
```

:Module: {ref}`format <api-format>`
:Kind: Function
:Source: [`lanczosKuboCode/Src/MIO/format.f90, line 54`](https://github.com/gjung-group/grabnes/blob/1e390c6ead7c835389ae89a599cb1f39e3fc691e/lanczosKuboCode/Src/MIO/format.f90#L54)

```{rubric} Parameters
```

`num` : `integer, intent(in)`
: —

```{rubric} Returns
```

`string` : `character(len=strlen)`
: —

```{rubric} Called by
```

{ref}`num2bytes <api-format-num2bytes>`
