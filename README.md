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
│   ├── modulo1_lectura_datos/
│   │   └── modulo1_lectura_datos.ipynb
│   ├── modulo2_preprocesamiento/
│   │   └── modulo2_preprocesamiento.ipynb
│   ├── modulo3_extraccion_features/
│   │   └── modulo3_extraccion_features.ipynb
│   ├── modulo4_reduccion_pca/
│   │   └── modulo4_reduccion_pca.ipynb
│   ├── modulo5_quantum_embedding/
│   │   └── modulo5_quantum_embedding.ipynb
│   ├── modulo6_red_neuronal/
│   │   └── modulo6_red_neuronal.ipynb
│   └── modulo7_evaluacion/
│       └── modulo7_evaluacion.ipynb
├── Data/
│   ├── manifest-*/               # NBIA Manifest for downloading DICOM images
│   ├── mass_case_description_train_set.csv
│   ├── mass_case_description_test_set.csv
│   ├── calc_case_description_train_set.csv
│   └── calc_case_description_test_set.csv
│   # ⚠️ DICOM images are NOT included in this repository.
│   # Download them from TCIA (see Dataset section).
├── Docs/
│   ├── Logos/
│   ├── Technical_Report.tex      # Main technical report (LaTeX)
│   └── Technical_Report.pdf      # Compiled version
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Dataset

Mammographic images **are not included** in this repository due to their size (163 GB)
and TCIA usage terms.

To reproduce the experiments:

1. Create a free account at [The Cancer Imaging Archive](https://www.cancerimagingarchive.net)
2. Download the [NBIA Data Retriever](https://wiki.cancerimagingarchive.net/display/NBIA/Downloading+TCIA+Images)
3. Open the `Data/manifest-*/` file with the NBIA Data Retriever
4. Metadata CSV files are already included in `Data/`

**Mandatory dataset citation (CC BY 3.0 license):**
> Sawyer-Lee, R., Gimenez, F., Hoogi, A., & Rubin, D. (2016).
> Curated Breast Imaging Subset of Digital Database for Screening Mammography (CBIS-DDSM).
> The Cancer Imaging Archive. https://doi.org/10.7937/K9/TCIA.2016.7O02S9CY

---

## Environment Setup

### Prerequisites
- Python 3.10
- Anaconda or Miniconda

### Steps
```bash
# 1. Clone the repository
git clone https://github.com/your-username/TT-2026-B039.git
cd TT-2026-B039

# 2. Create the virtual environment
conda create -n qml_cancer python=3.10 -y
conda activate qml_cancer

# 3. Install dependencies
pip install -r requirements.txt

# 4. Register the kernel in VSCode / Jupyter
python -m ipykernel install --user --name qml_cancer --display-name "QML Cancer"
```

---

## Technology Stack

| Tool | Version | Role |
|---|---|---|
| Python | 3.10 | Main language |
| pydicom | 3.0.1 | DICOM file reading |
| pandas | 2.3.3 | CSV metadata manipulation |
| numpy | 1.26.4 | Matrix operations |
| OpenCV | 4.13.0 | Image preprocessing (CLAHE, ROI cropping) |
| scikit-learn | — | PCA, evaluation metrics |
| PyRadiomics | — | Radiomics feature extraction |
| qiskit | 2.3.0 | Variational quantum circuits |
| qiskit-aer | 0.17.2 | Local quantum simulator |
| qiskit-machine-learning | 0.9.0 | EstimatorQNN, TorchConnector |
| PyTorch | 2.10.0 | Classical downstream neural network |
| matplotlib / seaborn | — | Visualization |

---

## System Pipeline
```
CBIS-DDSM (DICOM + CSV)
        │
        ▼
[Module 1] DICOM Reading + CSV Metadata
        │
        ▼
[Module 2] Normalization → CLAHE → ROI Cropping
        │
        ▼
[Module 3] Feature extraction (PyRadiomics / CNN encoder)
        │
        ▼
[Module 4] Dimensional reduction PCA → vector x ∈ ℝⁿ (n = 8–32)
        │
        ▼
[Module 5] Quantum Embedding U(x, θ) → ⟨Z_i⟩   ← Qiskit VQT
        │
        ▼
[Module 6] Classical Neural Network (MLP) → P(malignant)
        │
        ▼
[Module 7] Evaluation → AUC-ROC | F1 | Accuracy
```

---

## Methodology

This project follows the **CRISP-DM** methodology adapted for quantum computing,
with the following phases:

1. **Business Understanding** — Definition of the pre-diagnosis problem
2. **Data Understanding** — Exploratory analysis of CBIS-DDSM
3. **Data Preparation** — Preprocessing and feature extraction
4. **Modeling** — VQT implementation in Qiskit + classical network in PyTorch
5. **Evaluation** — Comparison of classical vs. quantum with standard metrics
6. **Deployment** — Technical report and INDAUTOR registration

---

## Expected Results

- Quantum embeddings generated for all test split cases
- AUC-ROC comparison between classical baseline and hybrid quantum model
- Analysis of class separability in quantum space
- Documentation of practical limitations of Qiskit Aer simulator

---

## License

The source code in this repository is under the **MIT** license.
See the [LICENSE](LICENSE) file for more details.

The images in the CBIS-DDSM dataset are under **CC BY 3.0** license from TCIA
and must be downloaded directly from their official source.

---

## Contact

**Student:** Sánchez García Miguel Alexander — msanchezg1904@alumno.ipn.mx  
**Institution:** Superior School of Computing (ESCOM) — IPN, Mexico