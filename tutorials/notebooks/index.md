# Original notebooks

The tutorials in this section were written from these Jupyter notebooks. They
are shown here unchanged, with the outputs and figures saved in them, so you
can read them without running anything.

To run a notebook, open it in Google Colab, or download it and run it on a
machine where GRABNES is compiled. The notebooks were written for Colab: their
first cells mount Google Drive and set up the Intel compilers, and they use
the Python driver
[`PyToGrabnes.py`](../../assets/downloads/PyToGrabnes.py).

::::{grid} 1 1 2 2
:gutter: 3
:class-container: notebook-cards

:::{grid-item-card} {octicon}`mortar-board` Twistronics 2023 workshop
:link: Twistronics2023
:link-type: doc

The full workshop tutorial: graphene, Bernal bilayer and graphite, twisted
bilayer graphene, and graphene on hBN with the magnetic-field DOS.
+++
`Twistronics2023.ipynb` · 17 figures
:::

:::{grid-item-card} {octicon}`file-code` Input files
:link: grabnes2
:link-type: doc

Writing input files with the built-in structure methods and with `ReadXYZ`
for graphene, graphene on hBN and twisted bilayer graphene.
+++
`grabnes2.ipynb`
:::

:::{grid-item-card} {octicon}`stack` Twisted bilayer graphene input
:link: grabnes3
:link-type: doc

Twisted bilayer graphene from the built-in methods and from an external
structure file, and twisted bilayer graphene on hBN.
+++
`grabnes3.ipynb`
:::

:::{grid-item-card} {octicon}`graph` Plotting results
:link: results
:link-type: doc

Python recipes for plotting band structures and densities of states.
+++
`results.ipynb` · 6 figures
:::

::::

The Twistronics 2023 notebook is also shared as a ready-to-run
[Google Colab notebook](https://colab.research.google.com/drive/12_ofrjJi4pr6U9j-ER1WocYJkqxEffs-?usp=sharing).

```{toctree}
:hidden:

Twistronics2023
grabnes2
grabnes3
results
```
