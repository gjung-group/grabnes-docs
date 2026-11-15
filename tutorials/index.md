# Tutorials

Hands-on tutorials, worked out with the Python driver library
[`PyToGrabnes.py`](../assets/downloads/PyToGrabnes.py) which generates the GRABNES
input files and runs the Fortran executable in the background. The same
input files can of course be written by hand and run from the terminal —
the Python layer is only a convenience.

Every page shows the cells of one of the original Jupyter notebooks exactly as
they are, with the outputs and figures saved in them. The bar under each page
title names the notebook and the cells the page shows, and links to the
notebook in Google Colab and to its download.

```{warning}
These notebooks are a record of the 2023 workshop and the moiré course, shown
as they were run. They were written for Google Colab with shared Google Drive
folders (Intel compilers, inputs) prepared for the workshop, they use the
input key names from before October 2026 (which still work, see
{doc}`../user-guide/input-file`), and some of the links in them no longer
resolve (for example `https://scqc.uos.ac.kr/grabnes/`). For the current code,
build it as described in {doc}`../installation` and run the
{doc}`../examples/index`; {doc}`../status` lists what is supported.
```

```{toctree}
:maxdepth: 1
:caption: Twistronics 2023 workshop

introduction
graphene
bilayer-graphite
tbg
graphene-on-hbn
```

```{toctree}
:maxdepth: 1
:caption: Moiré course notebooks

input-files
tbg-input
plotting
```

```{toctree}
:maxdepth: 1

notebooks/index
```

```{tip}
These pages originate from the Twistronics 2023 workshop tutorial sessions
and from an informal moiré course among group members. The original
notebooks can be opened in Google Colab or downloaded from
{doc}`notebooks/index`.
```
