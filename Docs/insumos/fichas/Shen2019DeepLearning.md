# Shen2019DeepLearning · Deep Learning to Improve Breast Cancer Detection on Screening Mammography

- Autores y año: Shen et al. (2019)
- DOI comprobado en la página 1: Sí
- Versión leída: Docs/fuentes/pdf/Shen2019DeepLearning.pdf · publicada · 12 páginas
- Tipo: experimental

## Respuestas a las preguntas
1. AUC por imagen del mejor modelo individual sobre test de CBIS-DDSM — La red híbrida Resnet-VGG alcanzó un AUC medio de 0.88 con predicción aumentada (0.87 sin aumento) — «The two hybrid networks achieved mean AUCs of 0.87 and 0.85, respectively, and were among the best performing models (Tables 2 and 3).» (p. 6)
2. AUC del promedio de cuatro modelos, sensibilidad y especificidad — El ensamble promedio de los cuatro mejores modelos obtuvo un AUC de 0.91 en CBIS-DDSM, con especificidad de 80.1 % al evaluar a una sensibilidad de 86.1 % — «Figure 3a shows the Receiver Operating Characteristic (ROC) curves of the four best models and the ensemble model, which yielded an AUC of 0.91.» (p. 6)
3. Comparación con radiólogos — Sí, comparan el rendimiento tomando como referencia el benchmark de sensibilidad media de radiólogos en EE. UU. (86 %), y señalan que se requerirán conjuntos curados por paneles de radiólogos para comparaciones directas futuras — «Therefore, we evaluated model performance using a sensitivity of 86% as a benchmark based upon the estimated average for U.S. radiologists3, and determined the model specificity to be 80.1% at a similar sensitivity of 86.1%.» (p. 6)
4. Arquitecturas usadas — Emplearon ResNet-50 y VGG16 como clasificadores de parches, combinados con bloques ResNet y VGG en las capas superiores — «Two of the four best models used Resnet50 and VGG16 as patch classifiers and Resnet and VGG blocks as top layers, respectively (referred to as Resnet-Resnet and VGG-VGG); and the remaining two were hybrid models (referred to as Resnet-VGG and VGG-Resnet).» (p. 6)

## Qué concluye la obra
- Demuestra que se logra una clasificación precisa de mamografías de tamizaje mediante un modelo de aprendizaje profundo entrenado de extremo a extremo que solo requiere anotaciones ROI clínicas en la etapa inicial: «This study shows that accurate classification of screening mammograms can be achieved with a deep learning model trained in an end-to-end fashion that relies on clinical ROI annotations only in the initial stage.» (p. 9)
- Comprueba que una vez construido el clasificador de imagen completa, este puede ajustarse finamente usando conjuntos de datos que carecen de anotaciones de lesiones: «Once the whole image classifier is built, it can be fine-tuned using additional datasets that lack ROI annotations, even if the pixel intensity distributions differ as is often the case for datasets assembled from heterogeneous mammography platforms.» (p. 9)
- El modelo ensemble combinando los cuatro mejores modelos alcanzó un AUC de 0.98 al transferirse a INbreast con sensibilidad de 86.7 % y especificidad de 96.1 %: «The ensemble model based on averaging the four best models improved the AUC to 0.98 with a corresponding sensitivity of 86.7% and specificity of 96.1% (Fig. 3b).» (p. 9)

## Qué deja como trabajo futuro o limitación declarada
- Advierte que CBIS-DDSM e INbreast no son muestras representativas nacionales y sus métricas no son directamente comparables con estimaciones nacionales de radiólogos: «Finally, the CBIS-DDSM and INbreast datasets were not nationally representative samples and performance metrics in these datasets are not directly comparable to national estimates of radiologists’ sensitivity and specificity.» (p. 10)
- Indica que las comparaciones directas futuras entre algoritmos y radiólogos se facilitarán al compartir públicamente el código y contar con conjuntos de prueba representativos: «Future direct comparisons between algorithms and radiologists will be facilitated by public sharing of the code and greater availability of representative benchmarking datasets.» (p. 10)
