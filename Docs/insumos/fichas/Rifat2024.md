# Rifat2024 · Enhanced Hybrid Quantum Neural Network for Breast Cancer Detection

- Autores y año: Rifat et al. (2024)
- DOI comprobado en la página 1: Sí (10.1109/iccit64611.2024.11021989; según la especificación, obra de pago consultada únicamente mediante su resumen público)
- Versión leída: Docs/fuentes/txt/Rifat2024/p001.txt · resumen público de IEEE Xplore · 1 página
- Tipo: experimental / propuesta de modelo híbrido

## Respuestas a las preguntas
1. Conjunto de datos y accuracy reportados en el resumen — Utiliza el conjunto BreastMNIST, compuesto por 780 muestras que el resumen describe como «full-image mammogram samples» (aunque en realidad MedMNIST v2 define BreastMNIST como ultrasonido mamario), reportando una exactitud (*accuracy*) del 69 % — «We collected the BreastMNIST dataset of 780 benign and malignant full-image mammogram samples.» (p. 1) y «Our architecture proved superior to other state-of-the-art hybrid methods, achieving an accuracy of 69% against 67%.» (p. 1)
2. Con qué lo compara — Compara el rendimiento con otros métodos híbridos representativos del estado del arte, superando su exactitud del 67 % con un 69 % — «Our architecture proved superior to other state-of-the-art hybrid methods, achieving an accuracy of 69% against 67%.» (p. 1)

## Qué concluye la obra
- Propone un modelo híbrido clásico-cuántico para predicción de cáncer de mama combinando ResNet-50 modificado como extractor de características y una Red Neuronal Cuántica (QNN): «Therefore, we proposed a novel hybrid classical-quantum machine learning model for breast cancer prediction.» (p. 1) y «The proposed method employs a modified ResNet50 as a feature extractor and a Quantum Neural Network to train on that feature and generate desired predictions.» (p. 1)
- Emplea una capa convolucional intermedia para reducción dimensional de las características generadas por ResNet-50 antes de introducirlas a la QNN: «A Convolutional layer is applied as a dimension-reduction technique for features generated through ResNet50.» (p. 1)

## Qué deja como trabajo futuro o limitación declarada
- El resumen señala la limitación actual del cómputo cuántico debido a recursos restringidos y complejidad, reconociendo que aún debe demostrar mejoras significativas pero confiando en su potencial de reducción de complejidad: «Although quantum computing has yet to show any significant improvement in machine learning due to its limited resources and complexity, it may reduce the computational complexity of machine learning in the future.» (p. 1)
- No declara trabajo futuro explícito más allá de abrir el camino para la investigación en modelos híbridos para clasificación de imágenes médicas (revisado el resumen público completo en `Docs/fuentes/txt/Rifat2024/p001.txt`).
