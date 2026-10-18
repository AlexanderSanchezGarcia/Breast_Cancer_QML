# Wang2020DeepLearning · Inconsistent Performance of Deep Learning Models on Mammogram Classification.

- Autores y año: Wang et al. (2020)
- DOI comprobado en la página 1: No
- Versión leída: Docs/fuentes/txt/Wang2020DeepLearning/p001.txt · resumen HTML · 1 página
- Tipo: experimental

## Respuestas a las preguntas
1. Número de modelos y conjuntos de datos — Se evaluaron seis modelos de aprendizaje profundo en cuatro conjuntos de datos de mamografía (tres públicos y uno privado) — «Six deep learning models (three published models with high performance and three models designed by us) were evaluated on four different mammogram data sets, including three public (Digital Database for Screening Mammography, INbreast, and Mammographic Image Analysis Society) and one private data set (UKy).» (p. 1)
2. Cifras de AUC en validación y conjuntos externos — Los modelos publicados reportaron auROC en validación entre 0.88 y 0.95, mientras que sobre conjuntos externos el rendimiento de los seis modelos cayó significativamente a entre 0.44 (IC 95 %: 0.43–0.45) y 0.65 (IC 95 %: 0.64–0.66) — «The three published models reported validation auROC scores between 0.88 and 0.95 on the validation data set.» (p. 1) y «However, the same evaluation criteria of all six models on the three external test data sets were significantly decreased, only between 0.44 (95% CI: 0.43-0.45) and 0.65 (95% CI: 0.64-0.66).» (p. 1)
3. Variabilidad entre lectores, cambio de dominio o conjuntos diversos — Aborda el cambio en la distribución de datos hacia dominios externos no vistos («The purpose of this study is to determine whether the high performance of deep learning on mammograms can be transferred to external data with a different data distribution.», p. 1); sobre variabilidad específica entre lectores no aparece en el texto disponible: NO_ENCONTRADO — busqué en p. 1 (resumen HTML).

## Qué concluye la obra
- Demuestra inconsistencia en el desempeño a través de distintos conjuntos de datos y modelos: «Our results demonstrate performance inconsistency across the data sets and models, indicating that the high performance of deep learning models on one data set cannot be readily transferred to unseen external data sets, and these models need further assessment and validation before being applied in clinical practice.» (p. 1)
- Los modelos diseñados por los autores alcanzaron un auROC de validación inferior a los modelos publicados previamente: «Our models achieved between 0.71 (95% confidence interval [CI]: 0.70-0.72) and 0.79 (95% CI: 0.78-0.80) auROC on the same validation data set.» (p. 1)

## Qué deja como trabajo futuro o limitación declarada
- Concluye que los modelos requieren una mayor evaluación y validación antes de su aplicación en la práctica clínica: «and these models need further assessment and validation before being applied in clinical practice.» (p. 1)
