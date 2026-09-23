# Variational Quantum Transform Model for a Hybrid Breast Cancer Pre-diagnosis System

**Terminal Work No. 2026-B039**  
Bachelor of Science in Data Science — ESCOM, National Polytechnic Institute

**Student:** Sánchez García Miguel Alexander

---

## Description

This project explores the use of variational quantum transforms (VQT) implemented
in Qiskit as a feature encoding mechanism for characteristics extracted from digital mammograms,
integrating these quantum representations as input to a classical neural network (PyTorch)
for binary classification of breast cancer (benign / malignant).

The dataset used is **CBIS-DDSM** (Curated Breast Imaging Subset of Digital Database
for Screening Mammography), publicly available at The Cancer Imaging Archive (TCIA).

> ⚠️ This project is an academic research prototype.
> It does not constitute a certified medical diagnostic device.

---

## Repository Structure

```
TT/
├── Code/
│   ├── 1_EDA.ipynb
│   ├── 5_Quantum_Benchmark.ipynb
│   ├── 6_Design_Verifications.ipynb
│   ├── Test.ipynb
│   ├── env/                     # Reproducible environment definitions
│   └── results/                 # Benchmark CSV results
├── Data/                        # CBIS-DDSM CSV metadata and DICOM images (not versioned)
├── Docs/
│   ├── Figures/
│   ├── Logos/
│   ├── Technical_Report.bib
│   ├── Technical_Report.pdf
│   └── Technical_Report.tex
├── Other/
│   ├── Procedimiento del Acto Académico.pdf
│   ├── bitacora_decisiones.md
│   ├── hallazgos_benchmark_cuantico.md
│   └── plan_trabajo.html
├── .gitignore
└── README.md
```

---

## Dataset

Mammographic images **are not included** in this repository due to their size (163 GB)
and TCIA usage terms. The `Data/` directory is excluded from version control; it contains
the CBIS-DDSM metadata CSV files and locally obtained DICOM images.

To reproduce the experiments:

1. Create a free account at [The Cancer Imaging Archive](https://www.cancerimagingarchive.net).
2. Download the [NBIA Data Retriever](https://wiki.cancerimagingarchive.net/display/NBIA/Downloading+TCIA+Images).
3. Obtain the CBIS-DDSM images through TCIA and place the downloaded data in `Data/`.

**Mandatory dataset citation (CC BY 3.0 license):**
> Sawyer-Lee, R., Gimenez, F., Hoogi, A., & Rubin, D. (2016).
> Curated Breast Imaging Subset of Digital Database for Screening Mammography (CBIS-DDSM).
> The Cancer Imaging Archive. https://doi.org/10.7937/K9/TCIA.2016.7O02S9CY

---

## Environments

Environment definitions and reproduction notes are available in
[Code/env/README.md](Code/env/README.md).

---

## Documentation and Project Records

The technical report source, bibliography, compiled PDF, figures, and institutional logos
are located in `Docs/`. Academic records, the work plan, decision log, and benchmark
findings are located in `Other/`.

---

## Contact

**Student:** Sánchez García Miguel Alexander — msanchezg1904@alumno.ipn.mx  
**Institution:** Superior School of Computing (ESCOM) — IPN, Mexico
