# Carbox*E. coli*

Source code for data analysis and figures from "Functional reconstitution of a bacterial CO<sub>2</sub> concentrating mechanism in *E. coli*" by Avi I. Flamholz, Eli Dugan, Cecilia Blikstad, Shmuel Gleizer, Roee Ben-Nissan, Shira Amram, Niv Antonovsky, Sumedha Ravishankar, Elad Noor, Arren Bar-Even, Ron Milo, and David F. Savage. This codebase assumes you are running Python 3+ and have Jupyter Notebook and/or Jupyter Lab installed. 

## Dependencies

This codebase depends on cobrapy, matplotlib, numpy, pandas, scipy, seaborn as well as several other commonly-used python libraries. In addition, it depends on the [optslope](https://pypi.org/project/optslope/) algorithm developed by Elad Noor during his time in the Milo. To install all dependencies locally, run

```
pip install cobra jupyterlab matplotlib numpy optslope pandas scipy seaborn statannot
```

## Before Generating Figures

### Running OptSlope

First run the OptSlope algorthm. This is necessary to generate Figure S1 diagramming the design of the CCMB1 strain. The `optslope_rubisco/` directory contains all the relevant models and code. From the root directory run `python optslope_rubisco/rubisco_dependence.py`. This will generate the tabular output file `optslope_rubisco/results.csv`.

### Analysis of LC-MS Data

The notebook titled `00_LCMS_calcs` (in the `notebooks` folder) reads the LCMS data and performs calculations required to generate the figures, for example inferrence of the intracellular <sup>12</sup>CO<sub>2</sub> concentration and the relative flux through rubisco. Choose "Restart Kernall and Run All Cells" to run the entire notebook. This will save a number of output files into the `data/LCMS` directory.

### Flux Balance Analysis

The notebook titled `01_FBA_rubisco_flux_prediction` use Flux Balance Analysis to predict the relative flux through rubisco in the complemented CCMB1 strain.  Choose "Restart Kernall and Run All Cells" to run the entire notebook. This will save a number of output files into the `data/FBA` directory.

## Generating Figures

Each figure has an associated notebook - the titles begin with the appropriate figure number. Having installed all the dependencies and run the prerequisite scripts you should now be able to generate all the figures.

