# Digital Identity and Emotional Coping Among Young Adults on Instagram and TikTok

## Research Reproducibility Package

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nasirhussain92/social-media-digital-identity-jmh/blob/main/notebooks/JMH_Reproducibility_Notebook.ipynb)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-yellow.svg)](LICENSE)
[![License: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](data/DATA_LICENSE.txt)

This repository provides the complete reproducibility package for the research article:

> **Digital Identity and Emotional Coping Among Young Adults on Instagram and TikTok**

The repository contains the anonymized dataset, computational notebook, analysis scripts, and supporting resources required to reproduce the statistical analyses reported in the study.

Click the **"Open in Colab"** badge above to run the full analysis directly in your browser — no local setup required. The notebook clones this repository and installs all dependencies automatically.

---

## Repository Structure

```text
social-media-digital-identity-jmh/

├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── social_media_dataset.csv
│   ├── social_media_dataset_raw.csv
│   ├── codebook.csv
│   └── DATA_LICENSE.txt
│
├── docs/
│   └── questionnaire.pdf
│
├── notebooks/
│   └── JMH_Reproducibility_Notebook.ipynb
│
├── src/
│   ├── reliability.py
│   ├── descriptive.py
│   ├── correlation.py
│   ├── regression.py
│   ├── mediation.py
│   └── utils.py
│
└── outputs/
    ├── tables/
    │   └── .gitkeep
    └── figures/
        └── .gitkeep
```

---

## Study Overview

This study investigates the relationship between social media use and the psychological well-being of young adults using Instagram and TikTok.

The analytical framework examines the following constructs:

- **Independent Variable**
  - Social Media Usage

- **Mediating Variables**
  - Digital Identity
  - Emotional Coping
  - Social Comparison

- **Dependent Variable**
  - Self-Esteem

- **Moderator**
  - Platform Type (Instagram vs. TikTok)

---

## Statistical Analyses

The computational workflow reproduces the analyses reported in the manuscript, including:

- Data preparation
- Variable construction
- Reverse scoring
- Reliability Analysis (Cronbach's Alpha)
- Descriptive Statistics
- Pearson Correlation Analysis
- Multiple Regression Analysis
- Mediation Analysis (Baron & Kenny)
- Sobel Test
- Publication-ready tables

---

## Dataset

The repository contains an anonymized survey dataset collected from university students (N = 265).

Personally identifiable information has been removed to protect participant confidentiality.

- `social_media_dataset.csv` — cleaned dataset with short variable codes, matched to `codebook.csv`.
- `social_media_dataset_raw.csv` — the raw export with full question-text column headers, provided for transparency.
- `codebook.csv` — variable definitions, question wording, construct mapping, and reverse-scoring flags.

---

## Reproducibility

The Google Colab notebook (`notebooks/JMH_Reproducibility_Notebook.ipynb`) reproduces the complete analytical workflow directly from the dataset included in this repository.

Running the notebook (via the badge above, or `Runtime → Run all` in Colab) will reproduce the statistical analyses and outputs reported in the manuscript, including:

- `outputs/tables/descriptive_statistics.csv`
- `outputs/tables/correlation_matrix.csv`
- `outputs/tables/regression_results.csv`
- `outputs/tables/mediation_results.csv`
- `outputs/tables/group_comparison_*.csv`
- `outputs/figures/distributions.png`
- `outputs/figures/correlation_heatmap.png`

---

## Citation

Citation details will be updated following publication. In the meantime, please cite this repository using the metadata in `CITATION.cff`.

---

## Data Availability

The anonymized dataset, computational notebook, analysis scripts, and supporting documentation are openly available in this repository to facilitate transparency and reproducibility.

A permanent archived version of this repository will be released through Zenodo and assigned a citable DOI.

---

## License

**Source Code**

MIT License — see [`LICENSE`](LICENSE)

**Dataset**

Creative Commons Attribution 4.0 International (CC BY 4.0) — see [`data/DATA_LICENSE.txt`](data/DATA_LICENSE.txt)

---

## Author

**Nasir Hussain**

Assistant Registrar

Karachi Institute of Economics and Technology (KIET)

Karachi, Pakistan

GitHub: https://github.com/nasirhussain92
