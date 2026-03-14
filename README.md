# Modelo de Transformación Cuántica Variacional para un Sistema Híbrido de Prediagnóstico de Cáncer de Mama

**Trabajo Terminal No. 2026-B039**  
Licenciatura en Ciencia de Datos — ESCOM, Instituto Politécnico Nacional

**Alumno:** Sánchez García Miguel Alexander  

---

## Descripción

Este proyecto explora el uso de transformaciones cuánticas variacionales (VQC) implementadas
en Qiskit como mecanismo de codificación de características extraídas de mamografías digitales,
integrando dichas representaciones cuánticas como entrada de una red neuronal clásica (PyTorch)
para la clasificación binaria de cáncer de mama (benigno / maligno).

El dataset utilizado es el **CBIS-DDSM** (Curated Breast Imaging Subset of Digital Database
for Screening Mammography), disponible públicamente en The Cancer Imaging Archive (TCIA).

> ⚠️ Este proyecto es un prototipo de investigación académica.
> No constituye un dispositivo de diagnóstico médico certificado.

---

## Estructura del repositorio
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
│   ├── manifest-*/               # Manifest NBIA para descarga de imágenes DICOM
│   ├── mass_case_description_train_set.csv
│   ├── mass_case_description_test_set.csv
│   ├── calc_case_description_train_set.csv
│   └── calc_case_description_test_set.csv
│   # ⚠️ Las imágenes DICOM NO están incluidas en este repositorio.
│   # Descárgalas desde TCIA (ver sección Dataset).
├── Docs/
│   ├── Logos/
│   ├── Technical_Report.tex      # Reporte técnico principal (LaTeX)
│   └── Technical_Report.pdf      # Versión compilada
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Dataset

Las imágenes mamográficas **no están incluidas** en este repositorio por su tamaño (163 GB)
y por las condiciones de uso de TCIA.

Para reproducir los experimentos:

1. Crea una cuenta gratuita en [The Cancer Imaging Archive](https://www.cancerimagingarchive.net)
2. Descarga el [NBIA Data Retriever](https://wiki.cancerimagingarchive.net/display/NBIA/Downloading+TCIA+Images)
3. Abre el archivo `Data/manifest-*/` con el NBIA Data Retriever
4. Los archivos CSV de metadatos ya están incluidos en `Data/`

**Cita obligatoria del dataset (licencia CC BY 3.0):**
> Sawyer-Lee, R., Gimenez, F., Hoogi, A., & Rubin, D. (2016).
> Curated Breast Imaging Subset of Digital Database for Screening Mammography (CBIS-DDSM).
> The Cancer Imaging Archive. https://doi.org/10.7937/K9/TCIA.2016.7O02S9CY

---

## Instalación del entorno

### Prerequisitos
- Python 3.10
- Anaconda o Miniconda

### Pasos
```bash
# 1. Clonar el repositorio
git clone https://github.com/tu-usuario/TT-2026-B039.git
cd TT-2026-B039

# 2. Crear el entorno virtual
conda create -n qml_cancer python=3.10 -y
conda activate qml_cancer

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Registrar el kernel en VSCode / Jupyter
python -m ipykernel install --user --name qml_cancer --display-name "QML Cancer"
```

---

## Stack tecnológico

| Herramienta | Versión | Rol |
|---|---|---|
| Python | 3.10 | Lenguaje principal |
| pydicom | 3.0.1 | Lectura de archivos DICOM |
| pandas | 2.3.3 | Manipulación de metadatos CSV |
| numpy | 1.26.4 | Operaciones matriciales |
| OpenCV | 4.13.0 | Preprocesamiento de imagen (CLAHE, recorte ROI) |
| scikit-learn | — | PCA, métricas de evaluación |
| PyRadiomics | — | Extracción de features radiómicas |
| qiskit | 2.3.0 | Circuitos cuánticos variacionales |
| qiskit-aer | 0.17.2 | Simulador cuántico local |
| qiskit-machine-learning | 0.9.0 | EstimatorQNN, TorchConnector |
| PyTorch | 2.10.0 | Red neuronal clásica downstream |
| matplotlib / seaborn | — | Visualización |

---

## Pipeline del sistema
```
CBIS-DDSM (DICOM + CSV)
        │
        ▼
[Módulo 1] Lectura DICOM + Metadatos CSV
        │
        ▼
[Módulo 2] Normalización → CLAHE → Recorte ROI
        │
        ▼
[Módulo 3] Extracción de features (PyRadiomics / CNN encoder)
        │
        ▼
[Módulo 4] Reducción dimensional PCA → vector x ∈ ℝⁿ (n = 8–32)
        │
        ▼
[Módulo 5] Quantum Embedding U(x, θ) → ⟨Z_i⟩   ← Qiskit VQC
        │
        ▼
[Módulo 6] Red Neuronal Clásica (MLP) → P(maligno)
        │
        ▼
[Módulo 7] Evaluación → AUC-ROC | F1 | Accuracy
```

---

## Metodología

Este proyecto sigue la metodología **CRISP-DM** adaptada a cómputo cuántico,
con las siguientes fases:

1. **Comprensión del negocio** — Definición del problema de prediagnóstico
2. **Comprensión de los datos** — Análisis exploratorio del CBIS-DDSM
3. **Preparación de los datos** — Preprocesamiento y extracción de features
4. **Modelado** — Implementación VQC en Qiskit + red clásica en PyTorch
5. **Evaluación** — Comparación clásico vs. cuántico con métricas estándar
6. **Despliegue** — Reporte técnico y registro INDAUTOR

---

## Resultados esperados

- Embeddings cuánticos generados para todos los casos del split de prueba
- Comparación de AUC-ROC entre modelo baseline clásico y modelo híbrido cuántico
- Análisis de separabilidad de clases en el espacio cuántico
- Documentación de restricciones prácticas del simulador Qiskit Aer

---

## Licencia

El código fuente de este repositorio está bajo la licencia **MIT**.
Consulta el archivo [LICENSE](LICENSE) para más detalles.

Las imágenes del dataset CBIS-DDSM están bajo licencia **CC BY 3.0** de TCIA
y deben descargarse directamente desde su fuente oficial.

---

## Contacto

**Alumno:** Sánchez García Miguel Alexander — msanchezg1904@alumno.ipn.mx  
**Institución:** Escuela Superior de Cómputo (ESCOM) — IPN, México