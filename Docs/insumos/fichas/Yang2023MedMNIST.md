# Yang2023MedMNIST · MedMNIST v2 - A large-scale lightweight benchmark for 2D and 3D biomedical image classification

- Autores y año: Yang et al. (2023)
- DOI comprobado en la página 1: Sí (10.1038/s41597-022-01721-8)
- Versión leída: Docs/fuentes/pdf/Yang2023MedMNIST.pdf · publicada · 10 páginas
- Tipo: descriptivo / conjunto de datos y benchmark

## Respuestas a las preguntas
1. Modalidad de imagen y conjunto original de BreastMNIST — BreastMNIST proviene de ultrasonido mamario (breast ultrasound), no de mamografía, y se construyó a partir del conjunto público de Al-Dhabyani et al. (Dataset of breast ultrasound images) — «BreastMNIST. The BreastMNIST is based on a dataset25 of 780 breast ultrasound images.» (p. 4) y «BreastMNIST Al-Dhabyani et al.25 Breast Ultrasound BC (2) 780 546/78/156» (p. 4)
2. Número de imágenes y resolución — Contiene 780 imágenes en total con una resolución reducida de 28×28 píxeles en escala de grises ($1 \times 28 \times 28$), particionadas en proporciones 7:1:2 (546 de entrenamiento, 78 de validación y 156 de prueba) — «BreastMNIST. The BreastMNIST is based on a dataset25 of 780 breast ultrasound images.» (p. 4) y «We split the source dataset with a ratio of 7:1:2 into training, validation and test set. The source images of 1 × 500 × 500 are resized into 1 × 28 × 28.» (p. 5)

## Qué concluye la obra
- Presenta MedMNIST v2 como una colección estandarizada de imágenes biomédicas en formato ligero similar a MNIST para tareas de clasificación en 2D y 3D: «We introduce MedMNIST v2, a large-scale MNIST-like dataset collection of standardized biomedical images, including 12 datasets for 2D and 6 datasets for 3D.» (p. 1)
- Estandariza todas las imágenes a dimensiones compactas de 28×28 (2D) o 28×28×28 (3D) para facilitar la investigación y docencia en visión por computadora y aprendizaje automático sin requerir conocimientos médicos especializados: «All images are pre-processed into a small size of 28 × 28 (2D) or 28 × 28 × 28 (3D) with the corresponding classification labels so that no background knowledge is required for users.» (p. 1)

## Qué deja como trabajo futuro o limitación declarada
- Advierte expresamente como limitación que el conjunto de datos no está destinado para uso clínico, pues la reducción drástica de resolución puede eliminar características esenciales de patologías médicas: «Please note that this dataset is NOT intended for clinical use, as substantially reducing the resolution of medical images might result in images that are insufficient to represent and capture different disease pathologies.» (p. 8)
