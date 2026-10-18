# Avci2023MammographyEnhancement · A Novel Medical Image Enhancement Algorithm for Breast Cancer Detection on Mammography Images Using Machine Learning

- Autores y año: Avcı y Karakaya (2023)
- DOI comprobado en la página 1: Sí
- Versión leída: Docs/fuentes/pdf/Avci2023MammographyEnhancement.pdf · publicada · 14 páginas
- Tipo: experimental

## Respuestas a las preguntas
1. Clasificadores comparados y características (GLCM, GLRLM) — Comparan SVM, RF, ANN, k-NN, Naive Bayes y DT, utilizando características extraídas mediante GLCM y GLRLM — «Support vector machine (SVM), random forest (RF), artiﬁcial neural network (ANN), k-Nearest Neighbour (k-NN), naive Bayes (NB), and decision tree (DT)» (p. 7)
2. Mejores clasificadores y métricas — SVM, RF y ANN obtuvieron el mejor rendimiento general en comparación con k-NN, NB y DT, alcanzando valores máximos de AUC, sensibilidad y especificidad — «In our study, SVM, RF, and ANN methods generally performed better than k-NN, NB, and DT especially in CLAHE&USM, and MF&CLAHE&USM pre-processing combinations.» (p. 11)
3. Sensibilidad al preprocesamiento — El preprocesamiento condiciona fuertemente la clasificación: CLAHE individual produce resultados bajos, mientras que combinarlo con unsharp masking (CLAHE&USM) maximiza el rendimiento — «When the CLAHE algorithm is used alone as a pre-processing method, it has been observed that it has a lower classiﬁcation performance than other pre-processing combinations.» (p. 12)
4. Conjunto de datos usado — Emplearon la base de datos pública mini-MIAS de 322 mamografías digitalizadas de 161 pacientes en vista MLO — «The open-access mini-MIAS database was used in the study [16].» (p. 4)

## Qué concluye la obra
- Compara el desempeño de clasificación de distintos métodos bajo diversas combinaciones de preprocesamiento: «At the same time, classiﬁcation performances of data mining methods in different pre-processing combinations were compared.» (p. 12)
- En clasificación de tejido normal frente a anormal, las combinaciones CLAHE&USM y MF&CLAHE&USM lograron los rendimientos más elevados: «In normal/abnormal tissue classiﬁcation, higher classiﬁcation performances were obtained in CLAHE&USM and MF&CLAHE&USM algorithms compared to other pre-processing combinations.» (p. 12)
- Los algoritmos SVM, RF, ANN, NB y DT superaron consistentemente a k-NN en ambas tareas de clasificación: «When we look at the best algorithm, in terms of classiﬁcation performance, it can be said that SVM, RF, ANN, NB, and DT classiﬁcation methods are more successful than the k-NN algorithm in both classiﬁcations.» (p. 12)
- Propone una combinación óptima de preprocesamiento debido a su impacto decisivo sobre todas las etapas del procesamiento de imagen: «At the end of this study, the appropriate combination with high classiﬁcation performances in mammography images is proposed for the pre-processing algorithms, which has a signiﬁcant impact on all steps in image processing.» (p. 12)

## Qué deja como trabajo futuro o limitación declarada
- Señala como limitación el tamaño muestral y propone validar los algoritmos en conjuntos de datos más extensos: «In the study, image processing steps were performed on 322 mammography images from 161 people obtained from the open-access database. The algorithms used can be applied to larger data sets.» (p. 12)
- Advierte la ausencia de subtipos y fenotipos tumorales en mini-MIAS, dejando su incorporación para trabajos futuros: «There is no breast cancer type and phenotype information in the mini-MIAS dataset we used. However, in future studies, it can be planned to work with data in light of this information.» (p. 12)
