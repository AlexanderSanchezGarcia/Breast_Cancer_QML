# Anez2025AIPipeline · Artificial Intelligence Pipeline for Mammography-Based Breast Cancer Detection: An Integrated Systematic Review and Large-Scale Experimental Validation

- Autores y año: Añez et al. (2025)
- DOI comprobado en la página 1: Sí
- Versión leída: Docs/fuentes/pdf/Anez2025AIPipeline.pdf · publicada · 30 páginas
- Tipo: experimental

## Respuestas a las preguntas
1. Cifras exactas de AUC-ROC y sensibilidad sobre CBIS-DDSM — ResNet-50 alcanzó AUC-ROC de 0.95 y Recall (sensibilidad) de 89 %; XGBoost alcanzó AUC-ROC de 0.90 y Recall de 74 %; SVM obtuvo AUC-ROC de 0.84 y Recall de 66 % — «The best CNN (ResNet-50) achieved an AUC-ROC of 0.95 with a Recall of 89%, while the XGBoost model reached an AUC-ROC of 0.90 with a Recall of 74%,» (p. 27)
2. Entrada recibida por SVM y XGBoost — Recibieron características estadísticas manuales extraídas directamente de las mamografías completas (intensidad media, desviación estándar, ancho y alto) — «These models were trained on handcrafted features extracted directly from full mammographic images, including mean intensity, standard deviation, width, and height.» (p. 10)
3. Partición o protocolo de evaluación — Para CNN se usó partición estratificada 64 % entrenamiento, 16 % validación y 20 % prueba; para SVM y XGBoost se usó 80 % entrenamiento con validación cruzada interna y 20 % prueba — «The dataset was partitioned into training subsets (64%), validation subsets (16%) and test subsets (20%) using stratified sampling to maintain the class and laterality balance described in Section 2.6.» (p. 10)

## Qué concluye la obra
- Desarrolló un flujo funcional y escalable para preprocesar y analizar tanto imágenes DICOM como datos clínicos estructurados: «A functional and scalable workflow was developed to preprocess and analyse both DICOM images and structured clinical data.» (p. 27)
- Evaluó múltiples modelos incluyendo arquitecturas de aprendizaje profundo y algoritmos clásicos sobre CBIS-DDSM: «Multiple models were trained and evaluated, including deep learning architectures (ResNet-50, EfficientNetB0, MobileNetV3-Small) and classical algorithms (XGBoost, SVM).» (p. 27)
- Los análisis de explicabilidad con Grad-CAM y SHAP sugieren que los modelos basaron sus decisiones en patrones médicamente relevantes: «Taken together, these techniques suggest that the models based their decisions on medically meaningful patterns rather than purely spurious correlations, and provide a basis for qualitative inspection by clinicians.» (p. 27)
- Entre los enfoques clásicos, XGBoost obtuvo el mejor rendimiento con características estadísticas simples: «Among classical ML approaches, XGBoost achieved the highest performance, indicating a strong ability to correctly identify malignant cases using simple statistical features, while SVM yielded lower but competitive results, as showing in Table 5, showing moderate performance but below both the XGBoost and the best CNN models.» (p. 18)

## Qué deja como trabajo futuro o limitación declarada
- Advierte que se requiere validación externa rigurosa en conjuntos independientes de distintos centros antes de su despliegue clínico: «Rigorous external validation on independent datasets from different centers will be essential before any clinical deployment is considered.» (p. 24)
- Señala como limitación que los modelos clásicos se entrenaron con un conjunto compacto de variables clínicas y morfológicas: «Second, the classical machine learning models (XGBoost and SVM) were trained on a relatively compact set of clinical and morphological features.» (p. 24)
