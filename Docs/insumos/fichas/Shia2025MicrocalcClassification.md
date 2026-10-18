# Shia2025MicrocalcClassification · Deep learning-based classification of benign and malignant breast microcalcifications in mammography

- Autores y año: Shia (2025)
- DOI comprobado en la página 1: Sí
- Versión leída: Docs/fuentes/pdf/Shia2025MicrocalcClassification.pdf · publicada · 14 páginas
- Tipo: experimental

## Respuestas a las preguntas
1. Modelos comparados y validación — Comparó variantes de EfficientNet (B0 a B4) frente a ResNet-50 y ResNet-101 mediante validación cruzada de cinco pliegues — «Each cell represents the p-value of the test between the model listed on the row and the model on the column, based on five-fold cross-validation results.» (p. 8)
2. Superioridad estadística en F1 — La prueba t pareada indica diferencias significativas a favor de EfficientNet sobre ResNet-50/101, pero la prueba no paramétrica de Wilcoxon no confirmó significancia (p > 0.05) ante la no normalidad de las distribuciones — «t-test suggests that there is a significant difference between the F1-score of all EfficientNet variants (from B0 to B4) used in this study and ResNet50/101, but the Wilcoxon test did not confirm its significance (p > 0.05).» (p. 8)
3. Validación externa en CBIS-DDSM — EfficientNet-B3 mantuvo la superioridad frente a ResNet-50 y ResNet-101, alcanzando la mayor exhaustividad (recall) tanto para clases benignas como malignas — «As illustrated in Fig. 8, EfficientNet-B3 maintained its superiority in classification performance compared to ResNet-50 and ResNet-101, achieving the highest recall for both benign and malignant classes.» (p. 9)
4. Origen de los datos de entrenamiento — Conjunto retrospectivo de pacientes del Changhua Christian Hospital en Taiwán, seleccionando para entrenamiento 869 casos benignos categorizados como BI-RADS 1–2 y 660 malignos con BI-RADS 5–6, confirmados histopatológicamente — «For model training, 869 benign cases (BI-RADS 1–2) and 660 malignant cases (BI-RADS 5–6) were randomly selected from the calcification-positive group.» (p. 4)

## Qué concluye la obra
- Entre los modelos evaluados, EfficientNet-B3 alcanzó el desempeño más alto de clasificación, mientras que B0 ofreció precisión similar con requerimientos computacionales notablemente menores: «Among the models evaluated, EfficientNet-B3 achieved the highest classification performance; however, EfficientNet-B0 provided comparable accuracy and F1-score while exhibiting significantly lower computational demands.» (p. 11)
- Los modelos clásicos ResNet-50 y ResNet-101 mostraron claras limitaciones para distinguir casos malignos de benignos, en particular en exhaustividad y desbalance de clases: «In contrast, traditional models such as ResNet-50 and ResNet-101 demonstrated clear limitations in distinguishing malignant from benign cases, particularly in relation to recall and class imbalance.» (p. 11)
- EfficientNet demostró solidez técnica y valor clínico potencial como sistema de apoyo a la decisión para radiólogos en la clasificación de microcalcificaciones: «EfficientNet, with its compound scaling approach, has demonstrated strong performance in this context, offering both technical robustness and potential clinical value as a decision-support system for radiologists in the classification of mammographic calcifications.» (p. 12)

## Qué deja como trabajo futuro o limitación declarada
- Señala como limitación que los datos provienen de una única institución, restringiendo la generalización hacia otras poblaciones y sistemas: «One limitation is that all data were obtained from a single institution, which may restrict the model’s generalisability to other populations or imaging systems.» (p. 12)
- Plantea abordar el riesgo de generalización limitada mediante estudios multicéntricos a gran escala que incorporen diversidad de sistemas y pacientes: «First, the risk of limited generalizability must be addressed through large-scale, multi-center studies that incorporate diverse imaging systems and patient populations.» (p. 12)
