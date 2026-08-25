# Mass-dependent optical behavior of carbonaceous aerosols in Amazonian biomass-burning plumes

[![Issues](https://img.shields.io/github/issues/thiago-vg/SAMBBA-data-analysis)](https://github.com/thiago-vg/SAMBBA-data-analysis/issues)
[![Downloads](https://img.shields.io/github/downloads/thiago-vg/SAMBBA-data-analysis/total)](https://github.com/thiago-vg/SAMBBA-data-analysis/releases)

This repository contains the scripts developed for the manuscript:

> **Mass-dependent optical behavior of carbonaceous aerosols in Amazonian biomass-burning plumes**

*Manuscript in preparation.*

------------------------------------------------------------------------

# Overview

This repository contains the complete workflow used to process, analyze
and visualize observations collected during the **South American Biomass
Burning Analysis (SAMBBA)** aircraft campaign.

The workflow combines aircraft measurements of aerosol chemical
composition, optical properties and ancillary variables to investigate
the relationship between aerosol composition and light scattering and
absorption in biomass burning plumes.

The scripts reproduce the preprocessing, statistical analyses and
publication-quality figures presented in the manuscript.

------------------------------------------------------------------------

# Repository structure

``` text
.
├── README.md
├── data
│   └── Download_files_all_sambba_edited.ipynb
└── processing and output
    ├── flights_io_commented.py
    ├── flight_processing_commented.py
    ├── Flight_plot_example.ipynb
    ├── Summary_stats.ipynb
    ├── Correlation_plots_documented.ipynb
    └── RF_and_PDP.ipynb
```

------------------------------------------------------------------------

# Prerequisites

These scripts were developed using the **Pangeo Notebook** Docker image.

-   https://hub.docker.com/r/pangeo/pangeo-notebook
-   https://www.pangeo.io/

Ensure Docker is installed before running the notebooks.

------------------------------------------------------------------------

# Installation

1.  Pull the Docker image

``` bash
docker pull pangeo/pangeo-notebook:latest
```

2.  Run the container

``` bash
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work --rm pangeo/pangeo-notebook
```

3.  Clone the repository

``` bash
git clone https://github.com/thiago-vg/REPOSITORY_NAME.git
cd REPOSITORY_NAME
```

4.  Open JupyterLab at `http://localhost:8888`.

------------------------------------------------------------------------

# Scripts and workflow

The scripts should be executed in the order shown below.

## 1. Data download

-   **data/Download_files_all_sambba_edited.ipynb**

Downloads the complete SAMBBA dataset from the CEDA Archive and
organizes the directory structure required by the subsequent analyses.

## 2. Data preprocessing

-   **processing and output/flights_io_commented.py**

Matches the files corresponding to each research flight across the
different instrument datasets.

-   **processing and output/flight_processing_commented.py**

Loads, quality-controls and harmonizes the measurements from the FAAM
core dataset, AMS, SP2, nephelometer and PCASP.

These modules are imported automatically by the analysis notebooks.
## 3. Exploratory analysis and visualization

-   **Flight_plot_example.ipynb**
-   **Flight_track_plot.ipynb**

Generates publication-quality figures illustrating flight tracks and vertical profiles used to inspect the harmonized SAMBBA dataset. This notebook produces **Figure 1 and 2** of the manuscript.

## 4. Summary statistics

-   **Summary_stats.ipynb**

Computes descriptive statistics of the aerosol optical and chemical properties, generating the summary tables and composition figures used throughout the study. This notebook produces **Table 2** of the manuscript and **Figures S1–S11** of the Supporting Information.

## 5. Correlation analysis

-   **Correlation_plots_documented.ipynb**

Investigates the relationships between aerosol chemical, physical, and optical properties through correlation matrices and pairwise scatter plots. This notebook produces **Figures S12 and S13** of the Supporting Information.

## 6. Random Forest analysis

-   **RF_and_PDP.ipynb**

Implements the Random Forest analysis presented in the manuscript, including model training, performance evaluation, feature importance analysis, and Partial Dependence Profiles (PDPs) of the most influential predictors. This notebook produces **Figures 3–7** of the manuscript.

------------------------------------------------------------------------

# Data sources

The analyses use observations collected during the **SAMBBA aircraft
campaign**.

The original datasets can be obtained from the **CEDA Archive**.

Additional ancillary datasets include:

-   MODIS(2012) MCD12C1 Land Cover Type product
-   Avaliable at: [![MCD12C1](https://img.shields.io/badge/NASA-Earthdata-orange?logo=nasa)](https://www.earthdata.nasa.gov/data/catalog?keyword=MCD12C1)
------------------------------------------------------------------------

# Workflow

``` mermaid
graph TD;
A["Download_files_all_sambba_edited.ipynb"] --> B["flights_io_commented.py"];
B --> C["flight_processing_commented.py"];
C --> D["Flight_plot_example.ipynb"];
C --> E["Flight_track_plot.ipynb"];
C --> F["Summary_stats.ipynb"];
C --> G["Correlation_plots_documented.ipynb"];
C --> H["RF_and_PDP.ipynb"];
```

------------------------------------------------------------------------

# Citation

If you use these scripts in your research, please cite:

> **Carbonaceous aerosol controls light scattering and absorption in
> Amazonian biomass burning plumes: effective optical efficiencies and
> their concentration-dependent limits**

*Manuscript in preparation.*

Once the manuscript is published, the citation and DOI will be updated.

------------------------------------------------------------------------

# Contact

Questions, suggestions and contributions are welcome through GitHub
Issues.
