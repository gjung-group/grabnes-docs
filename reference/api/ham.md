(api-ham)=
# `ham`

Tight-binding Hamiltonian module for twisted bilayer graphene and related 2D materials.

Provides routines to initialize on-site terms and compute hopping integrals for tight-binding Hamiltonians, including moiré strain, Zeeman terms, and interlayer coupling models. Parallelization via OpenMP/MPI is supported.

:Kind: Module
:Source: [`lanczosKuboCode/Src/ham.F90`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L27)
:Group: {ref}`Solver <api-group-solver>`
:Uses: {ref}`atoms <api-atoms>`, {ref}`cell <api-cell>`, {ref}`constants <api-constants>`, {ref}`gauss <api-gauss>`, `ieee_arithmetic`, {ref}`interface <api-interface>`, {ref}`magf <api-magf>`, {ref}`math <api-math>`, {ref}`mio <api-mio>`, {ref}`moireBLShift <api-moireblshift>`, {ref}`name <api-name>`, {ref}`neigh <api-neigh>`, {ref}`parallel <api-parallel>`, {ref}`random <api-random>`, {ref}`tbpar <api-tbpar>`
:Used by: {ref}`calc <api-calc>`, {ref}`diag <api-diag>`, {ref}`scf <api-scf>`
:Public interface: 8 procedures, 32 variables
:Input keys: 449 reads (see the procedures below)

## Procedure summary

```{list-table}
:header-rows: 1
:class: api-table
:widths: 36 64

* - Procedure
  - Description
* - {ref}`HaldaneEnabledForLayer <api-ham-haldaneenabledforlayer>`
  - Check if Haldane should be applied to a specific layer
* - {ref}`HamHopping <api-ham-hamhopping>`
  - Assemble hopping integrals (intra/inter-layer) into hopp(:,:).
* - {ref}`HamInit <api-ham-haminit>`
  - Initialize Hamiltonian parameters and neighbor lists.
* - {ref}`HamInputEnergyEV <api-ham-haminputenergyev>`
  - —
* - {ref}`HamOnSite <api-ham-hamonsite>`
  - Compute and add on-site energy terms to H0.
* - {ref}`HamPeierlsPeriodicGauge <api-ham-hampeierlsperiodicgauge>`
  - —
* - {ref}`SOCEnabledForLayer <api-ham-socenabledforlayer>`
  - —
* - {ref}`ZeemanEnabledForLayer <api-ham-zeemanenabledforlayer>`
  - Check if SOC should be applied to a specific layer
```

## Procedures

(api-ham-haldaneenabledforlayer)=
### `HaldaneEnabledForLayer`

```fortran
function HaldaneEnabledForLayer(layerIndex) result(enabled)
```

Check if Haldane should be applied to a specific layer

```{rubric} Arguments
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 18 40 42

* - Name
  - Declaration
  - Description
* - `layerIndex`
  - `integer, intent(in)`
  - Layer index to check
```

```{rubric} Returns
```

`enabled`: `logical`. True if Haldane should be applied to this layer

Defined in [`lanczosKuboCode/Src/ham.F90, line 13632`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L13632).

(api-ham-hamhopping)=
### `HamHopping`

```fortran
subroutine HamHopping()
```

Assemble hopping integrals (intra/inter-layer) into hopp(:,:).

Computes hopping amplitudes using selected bilayer/single-layer models, including twist angles, strain/bubble effects, and optional magnetic phases. Supports OpenMP for performance.

```{note}
Works with parameters set in HamInit and structures from neigh/atoms.
```

```{rubric} Input keys read (183)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Strain.ShellsFromRigidPositions`
  - GBNtwoLayers: take the shell of every intralayer bond from its in-plane length in a rigid reference structure (Strain.ShellsRigidFile, same atom order); the strain law keeps the 3-D length.
* - `Moire.Strain`
  - Here: the moire-strain hopping law is applied in HamHopping.
* - `MagField.FrankMagneticField`
  - Peierls phases from a bond-direction gauge for a rectangular graphene cell (HamHopMagneticField), with MagField.Integer flux quanta.
* - `MagField.Integer`
  - Here: number of flux quanta of MagField.FrankMagneticField.
* - `Interlayer.ChangeLatticeParameterForSrivaniModel`
  - BLSrivani: compute rbar with aG = 2.43898 Angstrom, the lattice constant of the fit.
* - `Intralayer.RemoveF2G2Flag`
  - Switch Intralayer.F2G2Model off (use the 8-shell parameter set).
* - `Intralayer.F2G2Model`
  - Here: F2G2 intralayer hoppings (otherwise the 8-shell parameter set).
* - `Stack.ThreeLayerShort`
  - Three-layer stacks: short-range interlayer model with hoppings tB1A2 (atoms on top of each other) and tA1A2 / tA1B2 (first ring).
* - `TBG.OffDiag`
  - Here: the tBG bond term is added in HamHopping.
* - `TBG.OffDiagPRB`
  - TBG.OffDiag: alternative parameter set (see HamHopping).
* - `Moire.LatticePercent`
  - Here: lattice mismatch of the moire bond terms.
* - `Moire.PotCab`
  - Here: amplitude of the off-diagonal moire term on graphene bonds \[eV\].
* - `Moire.PotCabBN`
  - Amplitude of the off-diagonal moire term on hBN bonds \[eV\].
* - `Interlayer.BilayerOneParameter`
  - Bernal bilayer with one interlayer hopping, Intralayer.BilayertAB1 (default 0.361 eV).
* - `Intralayer.BilayerThreeParameters`
  - Bernal bilayer with three interlayer hoppings tAB1, tAB3, tAB4.
* - `Moire.BfactorCab`
  - Moire.DistanceDependentEffectiveModel: decay B of Cab \[1/Angstrom\].
* - `Structure.InterlayerDistance`
  - Here: reference distance z0 of the distance-dependent Cab \[Angstrom\].
* - `Intralayer.BilayertAB1`
  - Bernal-bilayer hopping t\_AB1 (first set: one-parameter model) \[eV\] of the bilayer F2G2 / few-parameter models; the default depends on the parameter set read here.
* - `Intralayer.BilayertAB3`
  - Bernal-bilayer hopping t\_AB3 \[eV\] of the bilayer F2G2 / few-parameter models; the default depends on the parameter set read here.
* - `Intralayer.BilayertAB4`
  - Bernal-bilayer hopping t\_AB4 \[eV\] of the bilayer F2G2 / few-parameter models; the default depends on the parameter set read here.
* - `Intralayer.BilayertAA1`
  - Bernal-bilayer hopping t\_AA1 \[eV\] of the bilayer F2G2 / few-parameter models; the default depends on the parameter set read here.
* - `Intralayer.BilayertAA3`
  - Bernal-bilayer hopping t\_AA3 \[eV\] of the bilayer F2G2 model (stored as tAA2).
* - `Intralayer.BilayertBA0`
  - Bernal-bilayer hopping t\_BA0 (dimer) \[eV\] of the bilayer F2G2 / few-parameter models; the default depends on the parameter set read here.
* - `Intralayer.BilayertBA2`
  - Bernal-bilayer hopping t\_BA2 \[eV\] of the bilayer F2G2 / few-parameter models; the default depends on the parameter set read here.
* - `Intralayer.BilayertBA5`
  - Bernal-bilayer hopping t\_BA5 \[eV\] of the bilayer F2G2 / few-parameter models; the default depends on the parameter set read here.
* - `Trilayer.Gamma3`
  - Trilayer.FanZhang: gamma3 \[eV\]; also the former source of gamma1 when Trilayer.Gamma1 is absent (warning).
* - `Trilayer.Gamma1`
  - Trilayer.FanZhang: vertical dimer hopping gamma1 \[eV\].
* - `Trilayer.Gamma4`
  - Trilayer.FanZhang: gamma4 \[eV\].
* - `Trilayer.Gamma2`
  - Trilayer.FanZhang: gamma2 \[eV\].
* - `Moire.PotPhiab`
  - Here: phase of the off-diagonal moire bond term \[rad\].
* - `Moire.PotPhiabG`
  - Phase of the off-diagonal moire term on graphene bonds \[degrees\] (0 with TBG.OffDiag).
* - `Moire.PotPhiabBN`
  - Phase of the off-diagonal moire term on hBN bonds \[degrees\].
* - `Interlayer.TypeOfBL`
  - Here: selects the interlayer hopping branch of HamHopping.
* - `Interlayer.TypeOfSL`
  - Intralayer model name for single-layer systems (same names as Interlayer.TypeOfBL, e.g. HTC).
* - `Interlayer.AddExponentialDecayForDihedral`
  - Multiply the interlayer hopping of that branch by exp(-(d - Structure.InterlayerDistance) / Interlayer.BLdelta), d = 3-D bond length.
* - `Interlayer.MinDelta`
  - Read but not used at present.
* - `Interlayer.TwistedBLtbt`
  - Interlayer AA amplitude t\_bt of the analytic twisted-bilayer interlayer model \[eV\].
* - `Intralayer.KoshinoIntralayer`
  - Moon-Koshino intralayer hopping (Vpppi0 also used in-plane; its default becomes 2.7 eV).
* - `Interlayer.Vpppi0`
  - Two-centre V\_pp\_pi^0 \[eV\]: pi part of the interlayer hopping in every two-centre model, and the intralayer first-neighbour hopping with KoshinoIntralayer. Default 2.7 with KoshinoIntralayer, 3.5 otherwise.
* - `Interlayer.Vppsigma0`
  - Two-centre V\_pp\_sigma^0 of the interlayer hopping \[eV\].
* - `Interlayer.BLdelta`
  - Two-centre decay length delta of the interlayer hopping \[Angstrom\] (default 0.184 aG).
* - `Interlayer.CorrugatedInterlayerTwoCenter`
  - Two-centre interlayer hopping with local p\_z axes (corrugated sheets) instead of the global z.
* - `Structure.InterlayerDistance`
  - Here: interlayer distance of the Mayou model's q\_sigma \[Angstrom\].
* - `Intralayer.UseOldGrapheneF2G2`
  - Older graphene F2G2 parameter set (nonzero t4).
* - `Interlayer.DeactivateInterlayer`
  - Drop the interlayer bonds of the model branches that test it.
* - `Interlayer.DeactivateInterlayer12`
  - Drop the interlayer bonds between layers 1 and 2.
* - `Interlayer.DeactivateInterlayer23`
  - Drop the interlayer bonds between layers 2 and 3.
* - `Interlayer.DeactivateInterlayer34`
  - Drop the interlayer bonds between layers 3 and 4.
* - `Interlayer.DeactivateInterlayert2GBN1to2`
  - Stack.T2GBN: drop the interlayer bonds between layers 1 and 2.
* - `Interlayer.DeactivateInterlayert2GBN2to3`
  - Stack.T2GBN: drop the interlayer bonds between layers 2 and 3.
* - `Interlayer.DeactivateInterlayert2BG2to3`
  - Stack.T2BG: drop the interlayer bonds between layers 2 and 3.
* - `Interlayer.DeactivateInterlayert3BG1to2`
  - Stack.T3BG: drop the interlayer bonds between layers 1 and 2.
* - `Interlayer.DeactivateInterlayert3BG2to3`
  - Stack.T3BG: drop the interlayer bonds between layers 2 and 3.
* - `Interlayer.DeactivateInterlayert3BG3to4`
  - Stack.T3BG: drop the interlayer bonds between layers 3 and 4.
* - `Interlayer.DeactivateInterlayert3BG4to5`
  - Stack.T3BG: drop the interlayer bonds between layers 4 and 5.
* - `Interlayer.DeactivateInterlayert3BG5to6`
  - Stack.T3BG: drop the interlayer bonds between layers 5 and 6.
* - `Interlayer.DeactivateInterlayerBG`
  - Drop the interlayer bonds between layers 2 and 3 (bilayer-graphene branch).
* - `Interlayer.DeactivateInterlayerTwisted`
  - Drop the bonds between adjacent layers in the twisted-stack branch.
* - `Strain.PeriodicStrainPeriod`
  - Number of periods of the periodic strain / strained moire in the moire cell.
* - `Strain.StrainedMoireMaxDisplacement`
  - Strain.StrainedMoire: amplitude u\_max of the sinusoidal displacement \[Angstrom\].
* - `Strain.StrainedMoire`
  - Interlayer distances computed with a sinusoidal in-plane displacement u\_max sin(2 pi n x / L\_moire).
* - `Structure.SuperCell`
  - Here: the moire length is \|a1\| / SuperCell.
* - `Structure.TwistedBLAddShift`
  - Here: read for the interlayer branch of shifted bilayers.
* - `Intralayer.ForceBilayerF2G2Intralayer`
  - Here: the intralayer hoppings take the Bernal-bilayer F2G2 set below.
* - `Intralayer.Bilayert2KA`
  - F2G2 intralayer hopping t2 on sublattice A (second shell) \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.Bilayert2KB`
  - F2G2 intralayer hopping t2 on sublattice B (second shell) \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.Bilayert3K`
  - F2G2 intralayer hopping t3 (third shell) \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.Bilayert4K`
  - F2G2 intralayer hopping t4 (fourth shell) \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.Bilayert5KA`
  - F2G2 intralayer hopping t5 on sublattice A (fifth shell) \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.Bilayert5KB`
  - F2G2 intralayer hopping t5 on sublattice B (fifth shell) \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.BilayertK6A`
  - F2G2 intralayer hopping t6 (sixth shell) \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.BilayertK7A`
  - F2G2 intralayer hopping t7 (seventh shell) \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.BilayertK8A`
  - F2G2 intralayer hopping t8 (eighth shell) \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Stack.T3BG`
  - Here: selects the T3BG intralayer parameter set.
* - `Neigh.LayerDistFactor`
  - Here: read by the hopping set-up.
* - `Interlayer.KaxirasCutoff`
  - BLKaxiras / BLSrivani: cut-off of the interlayer hopping (compared as a squared length).
* - `Moire.OffDiag`
  - Here: the off-diagonal moire bond term is added in HamHopping.
* - `GBN.OffDiag`
  - Here: the G/hBN off-diagonal bond term is added in HamHopping.
* - `Structure.AddDisplacements`
  - Here: read for the bond terms.
* - `Moire.OffDiagMidpoint`
  - Here: the bond term is evaluated at the bond midpoint.
* - `Interlayer.AddPressureDependence`
  - BLKaxiras / BLSrivani: pressure (interlayer-distance) dependent parameters of Carr et al. (default .true.).
* - `Interlayer.SwitchV3Sign`
  - BLKaxiras / BLSrivani: change the sign of the V3 term.
* - `Interlayer.OldParameterSet`
  - BLKaxiras / BLSrivani: older parameter set of the fitting functions.
* - `Interlayer.DeactivateV6`
  - BLKaxiras / BLSrivani: drop the V6 term.
* - `Interlayer.DeactivateV3`
  - BLKaxiras / BLSrivani: drop the V3 term.
* - `Intralayer.MayouIntralayer`
  - Intralayer hoppings of the Mayou model.
* - `Interlayer.LegacyAngleSearch`
  - BLKaxiras / BLSrivani: bond angles from the index-based search with a 1.43 Angstrom cut-off used before November 2026 (non-Hermitian on relaxed cells).
* - `Stack.EncapsulatedFourLayersF2G2`
  - Stack.EncapsulatedFourLayers: Bernal F2G2 coupling between the two graphene layers (2-3).
* - `Interlayer.OnlyV0`
  - BLKaxiras / BLSrivani: keep only the V0 term (V3, V6 set to zero).
* - `TBG.Angle`
  - Here: twist angle of the analytic tBG bond terms \[degrees\].
* - `Structure.RotationAngle`
  - Rotation angle \[degrees\] of the interlayer model branches that use it.
* - `Interlayer.FindThetasGeometrically`
  - BLKaxiras / BLSrivani: bond angles theta12, theta21 from the geometry of the bond.
* - `Interlayer.RenormalizeHoppingFactorAAp`
  - Factor on AA' interlayer hoppings; overwritten per bond by the distance law in GBNtwoLayers.
* - `Interlayer.RenormalizeHoppingFactorBBp`
  - Factor on BB' interlayer hoppings; overwritten per bond by the distance law in GBNtwoLayers.
* - `Interlayer.RenormalizeHoppingFactorABp`
  - Factor on AB' interlayer hoppings; overwritten per bond by the distance law in GBNtwoLayers.
* - `Interlayer.RenormalizeHoppingFactorBAp`
  - Factor on BA' interlayer hoppings; overwritten per bond by the distance law in GBNtwoLayers.
* - `Interlayer.NewFittingFunctions`
  - BLKaxiras / BLSrivani: sublattice-resolved fitting functions a exp(-((r-b)/c)^4) cos(d r - h).
* - `Interlayer.RenormalizeCoupling`
  - Multiply the interlayer hoppings by Interlayer.CouplingFactor.
* - `Interlayer.CouplingFactor`
  - Interlayer.RenormalizeCoupling: factor on every interlayer hopping. 0.895 puts the magic angle of relaxed tBG at 1.08 deg; a rigid lattice needs about 1.008.
* - `Interlayer.CouplingFactor2`
  - Interlayer.DifferentCouplings: factor on the 2-3 interface (CouplingFactor on 1-2 and 3-4).
* - `Interlayer.DifferentCouplings`
  - Use Interlayer.CouplingFactor2 for the 2-3 interface of a four-layer stack.
* - `Interlayer.KoshinoSR`
  - Koshino two-centre interlayer hopping scaled per bond by exp((\|dz\| - 3.25)/1.34).
* - `Interlayer.Onlyvppsigma`
  - Two-centre interlayer hopping without the pi term (V\_pp\_pi = 0).
* - `Structure.BernalReadXYZ`
  - ReadXYZ Bernal bilayer: use the Bernal interlayer branch (dimer sites get the F2G2 AB set).
* - `Intralayer.DeactivateIntrasublattice`
  - Drop the hoppings between sites of the same sublattice.
* - `Intralayer.DeactivateIntersublattice`
  - Drop the hoppings between sites of different sublattices.
* - `Intralayer.DeactivateIntraSublatticeForC`
  - Drop same-sublattice hoppings between carbon atoms.
* - `Intralayer.T2Value`
  - Read but not used at present.
* - `Hopping.tA1B2`
  - Multilayer interlayer hopping t\_A1B2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1A2`
  - Multilayer interlayer hopping t\_A1A2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tB1B2`
  - Multilayer interlayer hopping t\_B1B2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1A3`
  - Multilayer interlayer hopping t\_A1A3 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tB1A3`
  - Multilayer interlayer hopping t\_B1A3 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1B2_2`
  - Multilayer interlayer hopping t\_A1B2\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1A2_2`
  - Multilayer interlayer hopping t\_A1A2\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tB1B2_2`
  - Multilayer interlayer hopping t\_B1B2\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1A3_2`
  - Multilayer interlayer hopping t\_A1A3\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tB1A3_2`
  - Multilayer interlayer hopping t\_B1A3\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1B3`
  - Multilayer interlayer hopping t\_A1B3 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tB1A2`
  - Multilayer interlayer hopping t\_B1A2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1A1_1`
  - Multilayer interlayer hopping t\_A1A1\_1 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tB1B1_1`
  - Multilayer interlayer hopping t\_B1B1\_1 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA2A2_1`
  - Multilayer interlayer hopping t\_A2A2\_1 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1B3_1`
  - Multilayer interlayer hopping t\_A1B3\_1 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tB1A2_1`
  - Multilayer interlayer hopping t\_B1A2\_1 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1A1_2`
  - Multilayer interlayer hopping t\_A1A1\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tB1B1_2`
  - Multilayer interlayer hopping t\_B1B1\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA2A2_2`
  - Multilayer interlayer hopping t\_A2A2\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tA1B3_2`
  - Multilayer interlayer hopping t\_A1B3\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Hopping.tB1A2_2`
  - Multilayer interlayer hopping t\_B1A2\_2 \[eV\] (sublattice and layer index; \_1/\_2: further neighbour shells) of the stack models in HamHopping.
* - `Interlayer.SetnLayersToZero`
  - Set the number of layers to 0 (small-bulk neighbour search on a non-bulk system).
* - `Moire.PotCabG`
  - Amplitude of the off-diagonal moire term on graphene bonds in the stack models \[eV\].
* - `Interlayer.LegacyBernalTAB1`
  - Bernal interlayer branch: the coupling used before November 2026 (gamma1 = F2G2 tAB1 = 0.1391 eV and nothing else) instead of the full Bernal F2G2 interlayer set.
* - `Strain.RealStrain`
  - Intralayer hoppings t exp(-beta (d/d\_ref - 1)), d = 3-D bond length (Pereira et al., PRB 80 045401); d\_ref per shell from Strain.RealStrainReferenceLatticeConstant(BN). Off: constant hoppings.
* - `Strain.OnlyFirstNeighborRealStrain`
  - Strain.RealStrain on the first-neighbour bonds only.
* - `Strain.RealStrainBeta`
  - Strain.RealStrain: decay exponent beta (default 3.37).
* - `Strain.PeriodicStrain`
  - Sinusoidal periodic strain of the hoppings (Strain.PeriodicStrainU0, PeriodicStrainPeriod).
* - `Strain.RealisticBubbles`
  - Strain bubbles with in-plane strain and an on-site shift (Strain.Bubble\* keys).
* - `Moire.Fourier`
  - Here: bond part of the Moire.Fourier term, added before the Peierls phase.
* - `Output.WriteDataFiles`
  - Here: write the hopping and on-site tables (generate.e, \<prefix>.s.mag, ...).
```

**`HamHopHaldane`** (internal procedure of `HamHopping`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L7043))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Haldane.PaperOrientation`
  - Haldane: multiply the model's own second-neighbour hoppings by exp(+-i phi) (otherwise add T2 exp(+-i phi)).
* - `Haldane.T2Complex`
  - Haldane: imaginary second-neighbour amplitude (see HamHopHaldane).
* - `Haldane.T2`
  - Haldane second-neighbour amplitude T2 \[eV\] (units of g0 before 2026-10-14); not used with Haldane.PaperOrientation.
* - `Haldane.OppositePhase`
  - Haldane: opposite sign of the phase phi.
* - `Haldane.BothLayers`
  - Deprecated (use Haldane.LayerControl / HaldaneLayers): the Haldane term on every layer.
* - `Haldane.Flux`
  - Haldane.SpecifyFlux: flux giving the phase 2 pi Flux / Phi\_0 (2 pi Flux / (pi/3) with Haldane.SetFluxQ).
* - `Haldane.SetFluxQ`
  - Haldane.SpecifyFlux: the phase is 2 pi Haldane.Flux / (pi/3).
* - `Haldane.Phase`
  - Haldane.SpecifyPhase: Haldane phase phi \[rad\].
```

**`HamHopRealisticBubbles`** (internal procedure of `HamHopping`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L7229))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Strain.BigBubble`
  - Strain.RealisticBubbles: one big bubble.
* - `Strain.ManyBubbles`
  - Strain.RealisticBubbles: many bubbles at random positions (Strain.BubblePercentage).
* - `Strain.BubbleInPlaneStrain`
  - Strain.RealisticBubbles: include the in-plane strain of each bubble.
* - `Strain.BubblePercentage`
  - Strain.ManyBubbles: percentage of the atoms that are bubble centres.
* - `Strain.BubbleGaussian`
  - Strain.RealisticBubbles: add a Gaussian potential at each bubble (Strain.BubbleGaussPot\*).
* - `Strain.BubbleSigmaR`
  - Strain.RealisticBubbles: width of the bubble profile \[Angstrom\].
* - `Strain.BubbleC`
  - Strain.RealisticBubbles: amplitude C of the in-plane strain.
* - `Strain.BubbleShift`
  - Strain.RealisticBubbles: on-site shift inside a bubble \[eV\] (units of g0 before 2026-11-07).
* - `Strain.BubbleRadius`
  - Strain.RealisticBubbles: radius of a bubble \[Angstrom\]. !fprimex(i) = NeighD(3,j,i)/(aG/2.0\_dp) fprimex(i) = (Rat(3,NList(j,i)) - Rat(3,i))/(aG/2.0\_dp) !else !    fprimex(i) = -(Rat(3,NList(j,i)) - Rat(3,i))/(aG/2.0\_dp) end if
```

**`HamHopPeriodicStrain`** (internal procedure of `HamHopping`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L7444))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Strain.PeriodicStrainU0`
  - Strain.PeriodicStrain: amplitude u0 of the displacement \[Angstrom\].
```

**`HamHopRealStrain`** (internal procedure of `HamHopping`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L7500))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Strain.RealStrainReferenceLatticeConstant`
  - Strain.RealStrain: graphene lattice constant of the reference bond lengths \[Angstrom\]; the lattice of the hopping fit, 2.4389777651302801 for the F2G2 sets.
* - `Strain.RealStrainReferenceLatticeConstantBN`
  - Strain.RealStrain: hBN lattice constant of the reference bond lengths \[Angstrom\].
* - `Strain.RealStrainLegacyFourthShell`
  - Strain.RealStrain: fixed 3.75696 Angstrom reference for the fourth shell, as before November 2026.
```

**`HamHopShellsFromRigid`** (internal procedure of `HamHopping`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L7693))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Strain.ShellsRigidFile`
  - Strain.ShellsFromRigidPositions: rigid reference structure (xyz, same atom order).
```

**`HamHopInterlayerParameters`** (internal procedure of `HamHopping`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L7911))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Interlayer.UseBNGSrivani`
  - BLSrivani: the G/hBN parameter set.
* - `Interlayer.Oppositedxdy`
  - BLKaxiras / BLSrivani: opposite sign of the bond vector in the angle calculation.
* - `Interlayer.SublatticeDependent`
  - BLKaxiras / BLSrivani: sublattice-dependent parameters.
* - `Interlayer.UseThetaIJ`
  - BLKaxiras / BLSrivani: angle variant theta\_ij (see HamHopInterlayerParameters).
* - `Interlayer.UseTheta`
  - BLKaxiras / BLSrivani: angle variant theta (see HamHopInterlayerParameters).
* - `Interlayer.SublatticeIndependent`
  - BLKaxiras / BLSrivani: sublattice-independent parameters.
* - `Interlayer.UseOnlyVAB`
  - BLKaxiras / BLSrivani: use the V\_AB parameters for every sublattice pair.
```

**`HamHopF2G2sParameters`** (internal procedure of `HamHopping`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L8253))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Intralayer.SingleLayert2KSL`
  - F2G2 intralayer hopping t2, second shell \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.SingleLayert3K`
  - F2G2 intralayer hopping t3, third shell \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.SingleLayert4K`
  - F2G2 intralayer hopping t4, fourth shell \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.SingleLayert5KSL`
  - F2G2 intralayer hopping t5, fifth shell \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.hBNt2B`
  - F2G2 intralayer hopping t2 of hBN on boron \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.hBNt2N`
  - F2G2 intralayer hopping t2 of hBN on nitrogen \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.hBNt3`
  - F2G2 intralayer hopping t3 of hBN \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.hBNt4`
  - F2G2 intralayer hopping t4 of hBN \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.hBNt5B`
  - F2G2 intralayer hopping t5 of hBN on boron \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.hBNt5N`
  - F2G2 intralayer hopping t5 of hBN on nitrogen \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.hBNt6`
  - F2G2 intralayer hopping t6 of hBN \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.hBNt7`
  - F2G2 intralayer hopping t7 of hBN \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
* - `Intralayer.hBNt8`
  - F2G2 intralayer hopping t8 of hBN \[eV\]; the default depends on the parameter set read here (graphene, hBN, G/hBN fits).
```

**`HamHopBondTermsTBG`** (internal procedure of `HamHopping`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L12444))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Moire.PotCabG`
  - Here (tBG bond terms): amplitude of the off-diagonal term on graphene bonds \[eV\].
```

Defined in [`lanczosKuboCode/Src/ham.F90, line 5373`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L5373).

(api-ham-haminit)=
### `HamInit`

```fortran
subroutine HamInit()
```

Initialize Hamiltonian parameters and neighbor lists.

Reads input parameters (strain, Zeeman terms, models), prepares neighbor lists and internal arrays, and sets module state. On-site terms are computed in HamOnSite; hopping is assembled elsewhere.

```{rubric} Input keys read (46)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Zeeman.Term`
  - Spin Zeeman shift +-Zeeman.Factor x Zeeman.Bmag on the spin sector Zeeman.Spin; with Zeeman.SpinPolarized both sectors. Follows SOC.LayerControl unless Zeeman.FollowSOCLayers .false.
* - `Zeeman.PseudoTerm`
  - Pseudo-Zeeman term (Zeeman.PseudoFactor): not implemented, no effect.
* - `Zeeman.Spin`
  - Zeeman.Term in a one-spin run: spin sector computed, 1 (up) or -1 / 2 (down).
* - `Zeeman.Factor`
  - Zeeman.Term: Zeeman energy per tesla \[eV/T\]; the shift is Factor x Zeeman.Bmag.
* - `Zeeman.PseudoFactor`
  - Zeeman.PseudoTerm: factor \[eV/T\] (the term is not implemented).
* - `Zeeman.SpinPolarized`
  - Two spin sectors (nspin = 2), needed by the spinful terms (Zeeman, SOC). Refused unless Hubbard.EnableSCF .false.
* - `SOC.Intrinsic`
  - Spin-independent sublattice mass +-SOC.LambdaI (not Kane-Mele, see SOC.KaneMele).
* - `SOC.LambdaI`
  - SOC.Intrinsic: amplitude \[eV\].
* - `SOC.Ising`
  - Ising (valley-Zeeman) spin-orbit term +-SOC.LambdaIsing.
* - `SOC.LambdaIsing`
  - SOC.Ising: amplitude \[eV\].
* - `SOC.Rashba`
  - Rashba spin-orbit term on the first-neighbour bonds (spinful block TAPW path).
* - `SOC.LambdaR`
  - SOC.Rashba: amplitude \[eV\]; the K-point splitting is 3 LambdaR (2/3 of the Gmitra lambda\_R).
* - `SOC.PIA`
  - Pseudospin-inversion-asymmetry SOC term (Gmitra), spinful TAPW only.
* - `SOC.LambdaPIA`
  - SOC.PIA: amplitude for both sublattices \[eV\].
* - `SOC.LambdaPIAA`
  - SOC.PIA: amplitude on sublattice A \[eV\] (default SOC.LambdaPIA).
* - `SOC.LambdaPIAB`
  - SOC.PIA: amplitude on sublattice B \[eV\] (default SOC.LambdaPIA).
* - `SOC.RashbaConsistentPhase`
  - .true. (default since 2026-10-16): spinful bond terms carry the same Bloch phase as the hopping. .false. restores the former Rashba phase, exact only at K and Gamma (warning printed).
* - `SOC.RashbaAngle`
  - SOC.Rashba: rotation of the Rashba spin texture (radial component) \[degrees\].
* - `SOC.KaneMele`
  - Kane-Mele intrinsic spin-orbit term on second-neighbour bonds, SOC.LambdaKM.
* - `SOC.LambdaKM`
  - SOC.KaneMele: amplitude lambda\_KM \[eV\] (gap 2 lambda\_KM in a single layer).
* - `SOC.Interlayer`
  - Interlayer spin-orbit term lambda\_4 between same-sublattice sites of adjacent untwisted graphene layers, i (lambda/3) c\_ij sgn(dz) (d x s)\_z.
* - `SOC.LambdaInterlayer`
  - SOC.Interlayer: amplitude \[eV\].
* - `Zeeman.FollowSOCLayers`
  - With SOC.LayerControl: the Zeeman term acts on the same layers as SOC (.false.: every layer).
* - `SOC.LayerControl`
  - Apply the SOC terms only to the layers listed in SOCLayers (e.g. 'SOCLayers 1 5'); otherwise every layer.
* - `Haldane.LayerControl`
  - Apply the Haldane term only to the layers listed in HaldaneLayers; otherwise see Haldane.NNN.
* - `Haldane.NNN`
  - Haldane second-neighbour term (Haldane.\* keys) on every layer.
* - `Neigh.fastNN`
  - Neighbour search fastNN: refused (it reads past the end of its bins).
* - `Neigh.fastNNnotsquare`
  - Binned neighbour search, the default and best tested one; .false. selects NeighList (see Neigh.CompareAll).
* - `Neigh.fastNNnotsquareNotRectangle`
  - Neighbour search fastNNnotsquareNotRectangle: refused (it reads past the end of its bins).
* - `Neigh.CutAtNN3`
  - Deprecated: limits the search to three intralayer shells; use TB.NeighLevels 3.
* - `Neigh.IntralayerRadius`
  - In-plane radius of the intralayer neighbour search \[Angstrom\], replacing the shell table's: for strained or corrugated cells (strained cells need 5.1134 to reproduce the search before October 2026).
* - `Intralayer.F2G2Model`
  - F2G2 intralayer model (5 shells); .false.: the 8-shell parameter set. A warning lists shells not searched.
* - `Neigh.LayerNeighbors`
  - Search interlayer neighbours (any value but 0); 0: no interlayer pairs.
* - `Stack.Bulk`
  - The cell is periodic along z too (graphite-like stack): interlayer pairs across the z boundary are kept. DiagHamSparse samples k\_z = 0 only.
* - `Stack.BulkSmall`
  - Stack.Bulk: neighbour search for small cells (fastNNnotsquareBulkSmall).
* - `Stack.NonBulkSmall`
  - Slab (non-periodic z) with the neighbour search for small cells.
* - `Structure.InterlayerDistance`
  - Here: read by the neighbour search set-up.
* - `Neigh.LayerDistFactor`
  - In-plane radius of the interlayer neighbour search: 1.1 aG/sqrt(3) times this factor.
* - `Output.ReadDataFiles`
  - Here: the on-site energies are read from generate.e (units of g0) instead of computed.
* - `Moire.Strain`
  - Modify the hoppings by a model moire strain (Moire.StrainFactor, Moire.HeightAmp).
* - `Moire.StrainFactor`
  - Moire.Strain: beta of the hopping law t = exp(-beta (d/d\_CC - 1)).
* - `Moire.HeightAmp`
  - Moire.Strain: amplitude of the height modulation \[Angstrom\].
* - `Strain.RandomStrain`
  - Random Gaussian height bumps (Strain.GaussHeight\*): refused at present.
* - `Output.PrintBubble`
  - Strain bubble diagnostic around a hard-coded atom: refused at present.
* - `Strain.BubbleSigmaR`
  - Output.PrintBubble (refused): Gaussian width of the height bump \[Angstrom\].
* - `Strain.BubbleHeight`
  - Output.PrintBubble (refused): height of the Gaussian bump \[Angstrom\].
```

Defined in [`lanczosKuboCode/Src/ham.F90, line 242`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L242).

(api-ham-haminputenergyev)=
### `HamInputEnergyEV`

```fortran
subroutine HamInputEnergyEV(key, value, defaultG0, since)
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
* - `key`
  - `character(len=*), intent(in)`
  - —
* - `value`
  - `real(dp), intent(out)`
  - —
* - `defaultG0`
  - `real(dp), intent(in)`
  - —
* - `since`
  - `character(len=*), intent(in), optional`
  - —
```

Defined in [`lanczosKuboCode/Src/ham.F90, line 13260`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L13260).

(api-ham-hamonsite)=
### `HamOnSite`

```fortran
subroutine HamOnSite()
```

Compute and add on-site energy terms to H0.

Controls the on-site contributions to the Hamiltonian. Values are added to H0 (never reinitialized) to preserve composition of effects (e.g., strain + gates). Handles multiple layer configurations and optional random/moire strain.

```{note}
Always update H0 additively; do not reinitialize.
```

```{rubric} Input keys read (201)
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Stack.GBNtwoLayersF2G2s`
  - Stack.GBNtwoLayers with F2G2 intralayer parameters for both graphene and hBN.
* - `Stack.GBNtwoLayers`
  - Graphene on one hBN layer (ReadXYZ cells): intralayer shells from the in-plane bond length, distance-dependent C-B and C-N interlayer hoppings.
* - `Stack.BNBNtwoLayers`
  - Two hBN layers: refused (no interlayer hopping is implemented).
* - `Stack.T2GBN`
  - Stack model flag: selects the twisted bilayer graphene on hBN (three layers) branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.T2BG`
  - Stack model flag; read here but not used in HamOnSite.
* - `Stack.T3BG`
  - Stack model flag: selects the six-layer T3BG branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.EncapsulatedThreeLayers`
  - Stack model flag: selects the hBN-encapsulated graphene (three layers) branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.EncapsulatedFourLayers`
  - Stack model flag: selects the hBN-encapsulated bilayer (four layers) branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.EncapsulatedFiveLayers`
  - Stack model flag: selects the five-layer encapsulated stack branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.EncapsulatedSixLayers`
  - Stack model flag: selects the six-layer encapsulated stack branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.EncapsulatedSevenLayers`
  - Stack model flag: selects the seven-layer encapsulated stack branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Potential.UseLayerSpecificOnsiteEnergyTerms`
  - Use the per-layer carbon on-site energies TB.OnSiteC1\_LB, C2\_LB, C1\_LT, C2\_LT.
* - `Stack.T3GwithBN`
  - Stack model flag: selects the twisted trilayer graphene with hBN branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.BNt2GBN`
  - Stack model flag: selects the hBN / twisted bilayer graphene / hBN branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Moire.DontUseInplaneMoire`
  - Skip the harmonic in-plane moire on-site term for GBNtwoLayers and the encapsulated stacks.
* - `Stack.TwoLayers`
  - Stack model flag: selects the two-layer graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.ThreeLayers`
  - Stack model flag: selects the three-layer graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.FourLayersSandwiched`
  - Stack model flag: selects the four-layer sandwiched graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.HelicalTwistedMBM`
  - Stack model flag: selects the helical-twisted four-layer (mono-bi-mono) branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.FiveLayersSandwiched`
  - Stack model flag: selects the five-layer graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.SixLayersSandwiched`
  - Stack model flag: selects the six-layer graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.SevenLayersSandwiched`
  - Stack model flag: selects the seven-layer graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.EightLayersSandwiched`
  - Stack model flag: selects the eight-layer graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.TenLayersSandwiched`
  - Stack model flag: selects the ten-layer graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Stack.TwentyLayersSandwiched`
  - Stack model flag: selects the twenty-layer graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Intralayer.ForceBilayerF2G2Intralayer`
  - Multilayer stacks: Bernal-bilayer F2G2 intralayer parameters instead of the single-layer ones.
* - `Stack.MiddleTwist`
  - Single-layer F2G2 parameters in every layer of the multilayer stacks; default .true. unless Intralayer.ForceBilayerF2G2Intralayer. A threeLayers stack then gets the averaged on-site energy.
* - `Stack.FourLayers`
  - Stack model flag: selects the four-layer graphene branches of the on-site and hopping terms (HamOnSite, HamHopping).
* - `Structure.ReadRigidXYZ`
  - Here: the rigid positions enter the on-site terms of the displacement-based models.
* - `Moire.Potential`
  - Moire on-site potential (HamOnSiteMoirePotential): the G/hBN effective model needs one of MoireH0AndHZ, MoireOnlyH0, MoireOnlyHZ, MoireNoH0AndHZ. No effect for ReadXYZ + GBNtwoLayers.
* - `Moire.PreFactor`
  - Moire.Potential: factor on the amplitudes of the moire potential.
* - `TBG.Diag`
  - Stacking-dependent on-site term of twisted bilayer graphene (from the local stacking displacements).
* - `TBG.DiagPRB`
  - TBG.Diag: use the amplitudes Interlayer.CAA, CBB, ... instead of the default set.
* - `BNBN.Diag`
  - Stacking-dependent on-site term of an hBN bilayer.
* - `Moire.LatticePercent`
  - Lattice mismatch epsilon of the moire potential, d(r) = ((1+eps) R(theta) - 1) r; commensurate G/hBN in a CellSize cell wants -1/CellSize.
* - `Moire.BilayerElectricField`
  - Layer potential (displacement field) of Moire.BilayerElectricShift; the profile follows the stack flag (e.g. Stack.FiveLayersSandwiched). Without this flag the shift does nothing.
* - `Moire.BilayerElectricShift`
  - Moire.BilayerElectricField: potential difference between the outer layers \[eV\].
* - `Moire.BilayerElectricFieldInvert`
  - Moire.BilayerElectricField: invert the field for atoms beyond half the cell in x.
* - `Structure.CellSize`
  - Here: half the cell length in x, CellSize\*SuperCell\*aG/2, for Moire.BilayerElectricFieldInvert.
* - `Trilayer.FanZhang`
  - On-site terms of the Fan-Zhang trilayer model (HamOnSiteTrilayerFanZhang).
* - `Potential.AddSublatticeMassterm`
  - Sublattice mass: Species 1 gets -m/2, Species 2 +m/2, m = Potential.SublatticeMassterm.
* - `Potential.OnlyBottomLayerMassTerm`
  - Potential.AddSublatticeMassterm on the bottom layer only.
* - `Potential.SublatticeMassterm`
  - Potential.AddSublatticeMassterm: mass m \[eV\].
* - `Potential.AddOnsiteEnergyShift`
  - Add Potential.OnsiteEnergyShift to every on-site energy.
* - `Potential.OnsiteEnergyShift`
  - Potential.AddOnsiteEnergyShift: shift \[eV\].
* - `Strain.Bubbles`
  - Disorder: shift the on-site energy by Disorder.OnsiteShift on randomly chosen cells of a CheckerDivider x CheckerDivider checkerboard (fraction Disorder.CheckerDensity).
* - `Disorder.OnsiteShift`
  - Strain.Bubbles: on-site shift of the chosen cells \[eV\] (units of g0 before 2026-10-14).
* - `Disorder.CheckerDivider`
  - Strain.Bubbles: the cell is divided into D x D checkerboard cells.
* - `Disorder.CheckerDensity`
  - Strain.Bubbles: fraction of checkerboard cells that are shifted.
* - `Potential.PNP`
  - Step p-n-p potential along x: -PNPAmp outside, +PNPAmp inside the central region (HamOnSitePNP).
* - `Potential.PNPKink`
  - Smooth p-n-p junction along x: Potential.PNPAmp x tanh steps of width Potential.PNPDelta at L/4 and 3L/4 (HamOnSitePNPKink).
* - `Potential.SinusModulation`
  - Legacy: add sin(2 pi N x / L) with amplitude 1 g0 (no amplitude key); do not use.
* - `Potential.SinusNumberOfPeriod`
  - Potential.SinusModulation: number N of periods in the cell.
* - `Potential.SinusModulationUsingPeriod`
  - Add Potential.SinusFactor x sin(2 pi x / Potential.SinusModulationPeriod); x is Cartesian, so it is lattice-periodic only for suitable periods.
* - `Potential.SinusModulationPeriod`
  - Period of the sine modulation \[Angstrom\] (absolute length, not a fraction of the cell).
* - `Potential.SinusModulationAddMassTerm`
  - Replace the sine modulation by its staggered form SinusMassTermFactor x sin(...) x (-1)^Species.
* - `Potential.SinusFactor`
  - Amplitude of the sine modulation \[eV\] (units of g0 before 2026-10-14).
* - `Potential.SinusMassTermFactor`
  - Amplitude of the staggered sine modulation \[eV\] (units of g0 before 2026-10-14).
* - `Potential.SinusModulationUsingPeriodYDirection`
  - As Potential.SinusModulationUsingPeriod, along y.
* - `Potential.CosinusModulationUsingPeriod`
  - Add Potential.CosinusFactor x cos(2 pi x / Potential.CosinusModulationPeriod).
* - `Potential.CosinusModulationPeriod`
  - Period of the cosine modulation \[Angstrom\].
* - `Potential.CosinusModulationAddMassTerm`
  - Replace the cosine modulation by CosinusMassTermFactor x cos(...) x (-1)^Species.
* - `Potential.CosinusFactor`
  - Amplitude of the cosine modulation \[eV\] (units of g0 before 2026-10-14).
* - `Potential.CosinusMassTermFactor`
  - Amplitude of the staggered cosine modulation \[eV\] (units of g0 before 2026-10-14).
* - `Potential.CosinusModulationUsingPeriodYDirection`
  - As Potential.CosinusModulationUsingPeriod, along y.
* - `Potential.SquareFunction`
  - Staggered potential -+(-1)^Species A following the sign of sin(2 pi N x/L) sin(2 pi N y/L) (HamOnSiteSquareFunction).
* - `Potential.SquareFunction2`
  - Staggered square-wave potential on honeycomb-sized regions (HamOnSiteSquareFunction2).
* - `Potential.Zterm1D`
  - Staggered potential that changes sign with sin(2 pi N x / L) (HamOnSiteZterm1D).
* - `Potential.Zterm1DKink`
  - Staggered potential with smooth tanh kinks along x (HamOnSiteZterm1DKink); written for two periods.
* - `Potential.SquareChecker2219`
  - Staggered checkerboard potential with fixed periods 22 x 19 in the cell (HamOnSiteSquareChecker).
* - `Disorder.SublatticeDisorder`
  - Random on-site disorder on a fraction Disorder.SublattPct of the Species-2 atoms.
* - `Disorder.SublattAmp`
  - Disorder.SublatticeDisorder: width w of the random energies \[eV\] (units of g0 before 2026-11-07).
* - `Disorder.SublattPct`
  - Disorder.SublatticeDisorder: fraction of the atoms affected.
* - `Disorder.Anderson`
  - Anderson disorder: random on-site energies of width Disorder.AndersonAmp on every atom.
* - `Disorder.AndersonAmp`
  - Disorder.Anderson: width w of the uniform distribution \[eV\] (units of g0 before 2026-11-07).
* - `Disorder.DeltaDisorder`
  - Delta-like impurity disorder (HamOnSiteDeltaDisorder; Disorder.DeltaAmp, DeltaSkewFactor).
* - `Disorder.GaussDisorder`
  - Gaussian impurities of strength Disorder.GaussPotStrength (Disorder.GaussPot\* keys).
* - `Disorder.GaussPotStrength`
  - Disorder.GaussDisorder: amplitude w of the Gaussian impurities \[eV\] (units of g0 before 2026-11-07).
* - `Potential.FourLayerOnsiteShifts`
  - Add the on-site shifts Stack.FourLayerShift1..4 to the atoms of layers 1..4 (four-layer stacks only), e.g. for a screened displacement-field profile.
* - `Stack.FourLayerShift1`
  - Potential.FourLayerOnsiteShifts: on-site shift of layer 1 \[eV\].
* - `Stack.FourLayerShift2`
  - Potential.FourLayerOnsiteShifts: on-site shift of layer 2 \[eV\].
* - `Stack.FourLayerShift3`
  - Potential.FourLayerOnsiteShifts: on-site shift of layer 3 \[eV\].
* - `Stack.FourLayerShift4`
  - Potential.FourLayerOnsiteShifts: on-site shift of layer 4 \[eV\].
* - `Potential.HelicalTwistedMBM_CDW`
  - C3-symmetric trigonal CDW, (A/3) \[cos 2 pi S f1 + cos 2 pi S f2 + cos 2 pi S (f1+f2)\] in fractional coordinates, S = SuperCell; Potential.CDWAmplitude, CDWUseMassTerm.
* - `Moire.CDW`
  - On-site CDW \[A + A\_m (-1)^Species\] (1/nQ) sum\_q cos(2 pi (h f1 + k f2)/D + phase) on every atom, q from the block moireCDW.Qvectors in units of the cell's reciprocal lattice (moireCDW.\* keys).
* - `Moire.Fourier`
  - General moire term given by Fourier components: on-site part here, bond part in HamHopping.
```

**`HamOnSiteMoireCDW`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1358))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `moireCDW.Amplitude`
  - Moire.CDW: scalar amplitude A \[eV\].
* - `moireCDW.MassAmplitude`
  - Moire.CDW: staggered amplitude A\_m, multiplied by (-1)^Species \[eV\].
* - `moireCDW.Phase`
  - Moire.CDW: phase of every cosine \[rad\].
* - `moireCDW.Denominator`
  - Moire.CDW: denominator D of the wave vectors q = (h, k)/D; the cell must be periodic for them.
* - `Structure.SuperCellX`
  - Here: checks that the moireCDW wave vectors are periodic in the supercell.
```

**`HamOnSiteTrigonalCDW`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1446))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Potential.CDWAmplitude`
  - Potential.HelicalTwistedMBM\_CDW: amplitude A \[eV\].
* - `Potential.CDWPeriod`
  - Read but not used: the trigonal CDW period is set by Structure.SuperCell.
* - `Potential.CDWUseMassTerm`
  - Potential.HelicalTwistedMBM\_CDW: multiply the CDW by (-1)^Species.
```

**`HamOnSiteDeltaDisorder`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1499))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Disorder.DeltaAmp`
  - Disorder.DeltaDisorder: amplitude w \[eV\] (units of g0 before 2026-10-14).
* - `Disorder.DeltaSkewFactor`
  - Disorder.DeltaDisorder: skew factor of the distribution.
```

**`HamOnSiteSquareChecker`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1546))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Potential.AmplitudeOfSquare`
  - Amplitude A of the staggered square / checker potentials \[eV\] (units of g0 before 2026-10-14).
```

**`HamOnSiteZterm1DKink`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1590))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Potential.Zterm1DAmp`
  - Potential.Zterm1DKink: amplitude of the tanh profile \[eV\] (units of g0 before 2026-10-14).
* - `Potential.Zterm1DDelta`
  - Potential.Zterm1DKink: width of the tanh steps \[Angstrom\].
```

**`HamOnSiteZterm1D`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1631))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Potential.AmplitudeOfSquare3`
  - Potential.Zterm1D: amplitude \[eV\] (units of g0 before 2026-10-14).
```

**`HamOnSiteSquareFunction2`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1664))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Potential.NumberOfWidthHoneycomb`
  - Potential.SquareFunction2: size of the regions in graphene cells.
* - `Potential.AmplitudeOfSquare2`
  - Potential.SquareFunction2: amplitude \[eV\] (units of g0 before 2026-10-14).
* - `Potential.PhaseOfSquareX`
  - Potential.SquareFunction2: phase of the x factor \[rad\].
* - `Potential.PhaseOfSquareY`
  - Potential.SquareFunction2: phase of the y factor \[rad\].
* - `Potential.TwoDimension`
  - Potential.SquareFunction2: modulation along x and y (otherwise x only).
* - `Potential.AddZTerm`
  - Potential.SquareFunction(2): add the staggered z term.
* - `Potential.ArmChairShape`
  - Potential.SquareFunction2: regions of armchair shape.
```

**`HamOnSiteSquareFunction`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1760))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Potential.TwoDimensional`
  - Potential.SquareFunction: modulation along x and y (otherwise x only).
```

**`HamOnSitePNPKink`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1832))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Potential.PNPAmp`
  - Amplitude of the p-n-p potential \[eV\] (units of g0 before 2026-10-14).
```

**`HamOnSiteTrilayerFanZhang`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L1939))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Trilayer.U1`
  - Trilayer.FanZhang: on-site potential of layer 1 \[eV\].
* - `Trilayer.U2`
  - Trilayer.FanZhang: on-site potential of layer 2 \[eV\].
* - `Trilayer.U3`
  - Trilayer.FanZhang: on-site potential of layer 3 \[eV\].
* - `Trilayer.Delta`
  - Trilayer.FanZhang: Delta term of the model \[eV\].
```

**`HamOnSiteMoirePotential`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L2082))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Moire.Sachs`
  - Moire potential of Sachs et al., PRB 84, 195414 (2011), amplitudes Moire.PotA, PotB, PotC.
* - `Moire.PotA`
  - Moire.Sachs: amplitude A \[eV\].
* - `Moire.PotB`
  - Moire.Sachs: amplitude B \[eV\].
* - `Moire.PotC`
  - Moire.Sachs: constant term C \[eV\].
* - `Moire.Jeil`
  - G/hBN moire potential of Jung et al., PRB 89, 205414 (2014): amplitudes Moire.PotC0, PotCz, PotCab and phases Moire.PotPhi0, PotPhiz, PotPhiab (the effective model).
* - `Moire.PreFactor`
  - Here: factor on Moire.PotC0, PotCz, PotCab.
* - `Moire.PotC0`
  - Moire.Jeil: amplitude C0 of the scalar moire term \[eV\].
* - `Moire.PotCz`
  - Moire.Jeil: amplitude Cz of the mass (sublattice-odd) term \[eV\].
* - `Moire.PotCab`
  - Moire.Jeil: amplitude Cab of the off-diagonal (bond) term \[eV\].
* - `Moire.PotPhi0`
  - Moire.Jeil: phase of the C0 term \[rad\].
* - `Moire.PotPhiz`
  - Moire.Jeil: phase of the Cz term \[rad\].
* - `Moire.PotPhiab`
  - Moire.Jeil: phase of the Cab term \[rad\].
* - `Moire.DistanceDependentEffectiveModel`
  - Moire.Jeil amplitudes scaled with the local interlayer distance z: C(z) = C exp(-B (z - z0)).
* - `Moire.BfactorC0`
  - Moire.DistanceDependentEffectiveModel: decay B of C0 \[1/Angstrom\].
* - `Moire.BfactorCz`
  - Moire.DistanceDependentEffectiveModel: decay B of Cz \[1/Angstrom\].
* - `Structure.InterlayerDistance`
  - Here: reference distance z0 of Moire.DistanceDependentEffectiveModel \[Angstrom\].
* - `Potential.SublatticeBasis`
  - Moire potential from the AA/BB sublattice form (diagoH0FromAABB) instead of the C0/phase form.
* - `Structure.AddDisplacements`
  - Add the stacking displacements read from the file to the analytic ones (needs a displacement file).
* - `Moire.Trilayer`
  - Two moire potentials of a trilayer (needs Moire.Sachs; Moire.PotA1..B2, Moire.Trin1/m1/n2/m2).
* - `Moire.RemoveTopMoireInL2`
  - Leave out the moire term from the top interface in layer 2 (see HamOnSiteMoirePotential).
* - `BNBN.UseDisplacementFile`
  - BNBN.Diag with per-atom stacking displacements from Structure.DisplacementsFile.
* - `GBN.UseHarmonicApprox`
  - Stack.GBNtwoLayers: harmonic (first-shell) G/hBN on-site moire term; TBG.Diag and BNBN.Diag are then switched off.
* - `GBN.Angle`
  - Twist angle of the analytic G/hBN stacking displacements \[degrees\].
* - `Stack.GlobalTwist`
  - Rotate the stacking displacements read from the file by this angle before use \[degrees\].
* - `Stack.GlobalTwist2`
  - As Stack.GlobalTwist, for the second set of displacements \[degrees\].
* - `Stack.GlobalPhiL1`
  - Rotation of the displacements of layer 1 \[degrees\] (layer-resolved stacks).
* - `Stack.GlobalPhiL2`
  - Rotation of the displacements of layer 2 \[degrees\].
* - `Stack.GlobalPhiL2a`
  - Rotation of the bottom-interface displacements of layer 2 \[degrees\] (encapsulated layers).
* - `Stack.GlobalPhiL2b`
  - Rotation of the top-interface displacements of layer 2 \[degrees\].
* - `Stack.GlobalPhiL3`
  - Rotation of the displacements of layer 3 \[degrees\].
* - `Structure.RotationAngle`
  - Rotation angle \[degrees\] used by the hopping terms (HamHopping); read here but not used.
* - `TBG.SwitchDxDy`
  - TBG.Diag: exchange the x and y components of the stacking displacement.
* - `Interlayer.CAA`
  - Stacking-dependent on-site term (TBG.Diag, BNBN.Diag, or the G/hBN default set): amplitude C\_AA on sublattice A of layer 1 \[eV\]; the defaults depend on the model.
* - `Interlayer.CBB`
  - Stacking-dependent on-site term (TBG.Diag, BNBN.Diag, or the G/hBN default set): amplitude C\_BB on sublattice B of layer 1 \[eV\]; the defaults depend on the model.
* - `Interlayer.CAA0`
  - Stacking-dependent on-site term (TBG.Diag, BNBN.Diag, or the G/hBN default set): constant part C\_AA0 on sublattice A of layer 1 \[eV\]; the defaults depend on the model.
* - `Interlayer.CBB0`
  - Stacking-dependent on-site term (TBG.Diag, BNBN.Diag, or the G/hBN default set): constant part C\_BB0 on sublattice B of layer 1 \[eV\]; the defaults depend on the model.
* - `Interlayer.CApAp`
  - Stacking-dependent on-site term (TBG.Diag, BNBN.Diag, or the G/hBN default set): amplitude C\_A'A' on sublattice A of layer 2 \[eV\]; the defaults depend on the model.
* - `Interlayer.CBpBp`
  - Stacking-dependent on-site term (TBG.Diag, BNBN.Diag, or the G/hBN default set): amplitude C\_B'B' on sublattice B of layer 2 \[eV\]; the defaults depend on the model.
* - `Interlayer.CApAp0`
  - Stacking-dependent on-site term (TBG.Diag, BNBN.Diag, or the G/hBN default set): constant part on sublattice A of layer 2 \[eV\]; the defaults depend on the model.
* - `Interlayer.CBpBp0`
  - Stacking-dependent on-site term (TBG.Diag, BNBN.Diag, or the G/hBN default set): constant part on sublattice B of layer 2 \[eV\]; the defaults depend on the model.
* - `Interlayer.PhiAA`
  - Stacking-dependent on-site term: phase of the AA harmonic \[degrees\]; the defaults depend on the model.
* - `Interlayer.PhiBB`
  - Stacking-dependent on-site term: phase of the BB harmonic \[degrees\]; the defaults depend on the model.
* - `Interlayer.PhiApAp`
  - Stacking-dependent on-site term: phase of the A'A' harmonic \[degrees\]; the defaults depend on the model.
* - `Interlayer.PhiBpBp`
  - Stacking-dependent on-site term: phase of the B'B' harmonic \[degrees\]; the defaults depend on the model.
* - `TBG.Angle`
  - Twist angle of the analytic tBG stacking displacements \[degrees\] (on-site and bond terms).
* - `TBG.LegacyAnalyticOnSite`
  - Analytic tBG on-site term as before November 2026 (GBN.Angle, d in Angstrom); warning printed.
* - `Output.WriteDataFiles`
  - Here: also writes the moire on-site terms to Hjj1, Hjj2.
* - `Moire.PotA1`
  - Moire.Trilayer: amplitude A of the first moire \[eV\] (default Moire.PotA).
* - `Moire.PotB1`
  - Moire.Trilayer: amplitude B of the first moire \[eV\] (default Moire.PotB).
* - `Moire.PotA2`
  - Moire.Trilayer: amplitude A of the second moire \[eV\] (default Moire.PotA).
* - `Moire.PotB2`
  - Moire.Trilayer: amplitude B of the second moire \[eV\] (default Moire.PotB).
* - `Moire.Trin1`
  - Moire.Trilayer: n1 of the moire periods n1 aG/m1 and n1 n2 aG/m2.
* - `Moire.Trim1`
  - Moire.Trilayer: m1 of the first period n1 aG/m1 (non-zero).
* - `Moire.Trin2`
  - Moire.Trilayer: n2 of the second period n1 n2 aG/m2.
* - `Moire.Trim2`
  - Moire.Trilayer: m2 of the second period n1 n2 aG/m2 (non-zero).
* - `Structure.SingleLayerXYZ`
  - ReadXYZ: the structure is a single layer (selects the single-layer branch of the moire potential).
* - `Trilayer.FanZhang`
  - Here: selects the trilayer branch of the moire potential.
* - `Moire.OnlyH0`
  - Moire potential: apply only the scalar term H0 (one of OnlyH0, OnlyHZ, NoH0AndHZ, H0AndHZ is required).
* - `Moire.OnlyHZ`
  - Moire potential: apply only the mass term HZ.
* - `Moire.NoH0AndHZ`
  - Moire potential: apply neither H0 nor HZ (bond terms only).
* - `Moire.H0AndHZ`
  - Moire potential: apply both the scalar H0 and the mass HZ terms.
* - `Moire.BilayerTopAngle`
  - Encapsulated bilayer: twist angle of the top hBN relative to the graphene \[degrees\].
* - `Moire.BilayerBottomAngle`
  - Encapsulated bilayer: twist angle of the bottom hBN relative to the graphene \[degrees\].
* - `Moire.BLDeactivateUpperLayer`
  - Encapsulated bilayer: no moire term on layer 2.
* - `Moire.TDBLDeactivateUpperLayers`
  - Multilayer: no moire term on any layer above layer 1.
* - `Moire.Kekule`
  - Kekule-type moire on-site term (HamOnSiteMoireKekule; Moire.KekuleAngle, KekuleEpsFactor).
* - `Moire.AddSecondMoire`
  - Second moire on the same graphene (effective model): same amplitudes and phases, slot 2 = Moire.Twisted2, TwistAngle2, LatticePercent x LatticePercentFactor, SecondMoireMassFactor.
* - `Moire.LatticePercentFactor`
  - Moire.AddSecondMoire: lattice mismatch of the second moire = Moire.LatticePercent x this factor.
* - `Moire.SwitchHzjj`
  - Read but not used at present.
* - `Moire.TwistAngle`
  - Moire.Twisted: twist angle theta of the first moire, d(r) = ((1+eps) R(theta) - 1) r \[degrees\].
* - `Moire.TwistAngle2`
  - Moire.Twisted2: twist angle of the second moire (Moire.AddSecondMoire) \[degrees\].
* - `Moire.Twisted`
  - The first moire includes the twist Moire.TwistAngle (otherwise lattice mismatch only).
* - `Moire.Twisted2`
  - The second moire includes the twist Moire.TwistAngle2.
* - `Intralayer.DeactivateASubLattice`
  - Moire potential: skip the moire term on the Species-2 atoms.
* - `Intralayer.DeactivateBSubLattice`
  - Moire potential: skip the moire term on the Species-1 atoms.
* - `Moire.LayerShift1`
  - Moire potential: added to the y component of the stacking displacement of the first (bottom) moire \[Angstrom\].
* - `Moire.LayerShift2`
  - Moire potential: shift of the second moire pattern \[Angstrom\].
* - `Moire.SecondMoireRotateFirst`
  - Moire.AddSecondMoire: build the displacement with the rotation applied first (default).
* - `Moire.SecondMoireMassFactor`
  - Moire.AddSecondMoire: factor (sign) of the mass term of the second moire; \< 0 flips BN to NB.
* - `Moire.FirstMoireMassFactor`
  - Factor (sign) of the mass term of the first moire; \< 0 flips BN to NB.
* - `Potential.MinZ`
  - Read but not used at present.
* - `Moire.SymmetricPot`
  - Symmetric moire potential with amplitudes Moire.SymmA, Moire.SymmB.
* - `Moire.SymmA`
  - Moire.SymmetricPot: amplitude A \[eV\].
* - `Moire.SymmB`
  - Moire.SymmetricPot: amplitude B \[eV\].
```

**`HamOnSiteMoireKekule`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L3648))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Moire.KekuleAngle`
  - Moire.Kekule: angle of the Kekule pattern \[degrees\].
* - `Moire.KekuleEpsFactor`
  - Moire.Kekule: the lattice mismatch enters as Moire.LatticePercent / this factor.
```

**`HamOnSiteSpeciesEnergies`** (internal procedure of `HamOnSite`, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L3703))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Interlayer.TypeOfBL`
  - Interlayer hopping model: None, Koshino, Jeil, Mayou, BLKaxiras, BLSrivani, ... (see HamHopping); also selects matching on-site energies (e.g. BLKaxiras with Interlayer.UseBNGKaxiras).
* - `Interlayer.UseBNGKaxiras`
  - With TypeOfBL BLKaxiras: the G/hBN interlayer model (Eq. 4) with the hBN 8-shell intralayer set and its B / N on-site energies; needs a stack flag (e.g. Stack.TwoLayers).
```

Defined in [`lanczosKuboCode/Src/ham.F90, line 756`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L756).

(api-ham-hampeierlsperiodicgauge)=
### `HamPeierlsPeriodicGauge`

```fortran
subroutine HamPeierlsPeriodicGauge(flux)
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
* - `flux`
  - `real(dp), intent(in)`
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
* - `MagField.LegacyCornerPhase`
  - Peierls phases without the exp(i pi m n1 n2) term of bonds across a cell corner, as before 2026-10-22 (wrong for odd m). The run otherwise refuses a non-integer number of flux quanta.
```

Defined in [`lanczosKuboCode/Src/ham.F90, line 12834`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L12834).

(api-ham-socenabledforlayer)=
### `SOCEnabledForLayer`

```fortran
function SOCEnabledForLayer(layerIndex) result(enabled)
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
* - `layerIndex`
  - `integer, intent(in)`
  - —
```

```{rubric} Returns
```

`enabled`: `logical`

Defined in [`lanczosKuboCode/Src/ham.F90, line 13602`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L13602).

(api-ham-zeemanenabledforlayer)=
### `ZeemanEnabledForLayer`

```fortran
function ZeemanEnabledForLayer(layerIndex) result(enabled)
```

Check if SOC should be applied to a specific layer

Layers that carry the Zeeman term: the SOC layers when SOC.LayerControl is on and Zeeman.FollowSOCLayers is .true. (default), otherwise every layer

```{rubric} Arguments
```

```{list-table}
:header-rows: 1
:class: api-table
:widths: 18 40 42

* - Name
  - Declaration
  - Description
* - `layerIndex`
  - `integer, intent(in)`
  - Layer index to check
```

```{rubric} Returns
```

`enabled`: `logical`. True if SOC should be applied to this layer

Defined in [`lanczosKuboCode/Src/ham.F90, line 13589`](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L13589).

## Module variables

```{list-table}
:header-rows: 1
:class: api-table
:widths: 26 44 30

* - Name
  - Declaration
  - Initial value
* - `gZeeman`
  - `real(dp), save`
  - —
* - `H0`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `H0Bottom`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `H0Top`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `HABimag`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `HABreal`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `HaldaneLayerControl`
  - `logical, save`
  - —
* - `HaldaneLayersArray`
  - `integer, dimension(:), save, allocatable`
  - —
* - `Ho`
  - `real(dp), dimension(:), pointer`
  - `NULL()`
* - `hopp`
  - `complex(dp), dimension(:,:), pointer`
  - `NULL()`
* - `InterlayerSOCterm`
  - `logical, save`
  - `.false.`
* - `IntrinsicSOCterm`
  - `logical, save`
  - —
* - `IsingSOCterm`
  - `logical, save`
  - —
* - `KaneMeleSOCterm`
  - `logical, save`
  - `.false.`
* - `lambdaI`
  - `real(dp), save`
  - —
* - `lambdaIL`
  - `real(dp), save`
  - `0.0_dp`
* - `lambdaIsing`
  - `real(dp), save`
  - —
* - `lambdaKM`
  - `real(dp), save`
  - `0.0_dp`
* - `lambdaPIA`
  - `real(dp), save`
  - —
* - `lambdaPIAA`
  - `real(dp), save`
  - `0.0_dp`
* - `lambdaPIAB`
  - `real(dp), save`
  - `0.0_dp`
* - `lambdaR`
  - `real(dp), save`
  - —
* - `nspin`
  - `integer, save`
  - —
* - `PIASOCterm`
  - `logical, save`
  - —
* - `rashbaAngle`
  - `real(dp), save`
  - `0.0_dp`
* - `RashbaConsistentPhase`
  - `logical, save`
  - `.false.`
* - `RashbaSOCterm`
  - `logical, save`
  - —
* - `socBond`
  - `complex(dp), dimension(:,:,:,:), save, allocatable`
  - —
* - `socBondOn`
  - `logical, dimension(:,:), save, allocatable`
  - —
* - `SOCLayerControl`
  - `logical, save`
  - —
* - `SOCLayersArray`
  - `integer, dimension(:), save, allocatable`
  - —
* - `Zterm`
  - `logical, save`
  - —
```

## Input keys read by private procedures

Procedures that are not part of the public interface but read input keys.

**`HamMeasureLayerTwist`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L4124))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Stack.MeasureTwist`
  - Report the twist of every interface measured from the structure.
* - `Stack.ModelFromTwist`
  - Untwisted AB pairs found in the structure get the bilayer F2G2 intra- and interlayer model (Jung-MacDonald PRB 89 035405); AA and twisted pairs keep the two-centre model.
* - `Stack.AlignModelEnergies`
  - With Stack.ModelFromTwist: shift the AB-pair sites so their K-point energy matches the single-layer set.
* - `Stack.TwistTolerance`
  - Stack.MeasureTwist / ModelFromTwist: twists below this count as untwisted \[degrees\].
```

**`HamCheckHermiticity`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L4491))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Moire.OffDiag`
  - Off-diagonal (bond) moire term of the G/hBN effective model, Cab. Evaluated at atom i: H slightly non-Hermitian unless Moire.OffDiagMidpoint.
* - `TBG.OffDiag`
  - Off-diagonal (bond) stacking-dependent term of twisted bilayer graphene.
* - `GBN.OffDiag`
  - Off-diagonal (bond) stacking-dependent term of G/hBN, from atom i's displacement.
* - `Strain.StrainedMoire`
  - Strained-moire hopping term (checked for Hermiticity here).
* - `Moire.OffDiagMidpoint`
  - Moire.OffDiag: evaluate the bond term at the bond midpoint (one shared routine for both moire slots): Hermitian H, needed for recursion runs. Plain effective model only.
```

**`HamMoireFourierSetup`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L4894))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Structure.SuperCellX`
  - Here: input cell = simulation cell / SuperCell for the Moire.Fourier wave vectors.
* - `Moire.FourierKprime`
  - Moire.Fourier: the term U is given for the K' valley.
* - `Moire.FourierGrapheneAngle`
  - Moire.Fourier: orientation of the graphene lattice \[degrees\].
* - `Moire.FourierLatticeConstant`
  - Moire.Fourier: graphene lattice constant of the Fourier components \[Angstrom\] (default aG).
```

**`HamHopValleyZeeman`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L5061))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Valley.Zeeman`
  - Valley Zeeman term lambda i nu\_ij s\_i /(3 sqrt 3) on the graphene second-neighbour bonds of each layer (= tau\_z at the Dirac points) \[eV\]; 0 = off. Added before the Peierls phase.
```

**`HamSOCBondTables`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L12929))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Stack.TwistTolerance`
  - Here: interfaces twisted by less than this count as aligned for the SOC bond tables \[degrees\].
```

**`HamDisplacementsFromPositions`** (private, [source](https://github.com/gjung-group/grabnes/blob/7b24d6625d6373cee0d474c9abbec91499ab77e7/lanczosKuboCode/Src/ham.F90#L13132))

```{list-table}
:header-rows: 1
:class: api-table
:widths: 34 66

* - Key
  - Description
* - `Structure.DisplacementsFromPositions`
  - Here: the stacking displacements are computed from generateInit.xyz and the structure.
* - `Stack.GlobalTwist`
  - Here: refused with Structure.DisplacementsFromPositions (those displacements are already in the lab frame).
* - `Stack.EncapsulatedThreeLayers`
  - Here: graphene atoms get a bottom and a top displacement.
```
