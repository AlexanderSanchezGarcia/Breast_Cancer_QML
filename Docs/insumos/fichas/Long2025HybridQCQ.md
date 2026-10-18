# Long2025HybridQCQ · A hybrid quantum-classical-quantum convolutional neural network with high expressiveness and noise resilience

- Autores y año: Long et al. (2025)
- DOI comprobado en la página 1: Sí (10.1038/s41598-025-13417-1)
- Versión leída: Docs/fuentes/pdf/Long2025HybridQCQ.pdf · publicada · 17 páginas
- Tipo: experimental

## Respuestas a las preguntas
1. Definición de circuito cuántico variacional y de PQC — Definen los PQC como circuitos con puertas parametrizadas que producen transformaciones complejas con poca profundidad, y los circuitos cuánticos variacionales (VQC) como una clase particular de PQC cuyos parámetros se optimizan variacionalmente minimizando una función de coste mediante un esquema híbrido clásico-cuántico — «With limited shallow quantum circuit depth, PQCs can produce highly complex outputs through the direct combination of control gates and quantum rotation gates35.» (p. 3), «Variational Quantum Circuits (VQC)10 are a specific type of PQC, typically combining quantum circuits with classical optimizers, and are widely use in quantum algorithms.» (p. 1), «Among various types of PQCs, Variational Quantum Circuits (VQCs) specifically refer to parameterized quantum circuits whose parameters are optimized through variational methods, typically by minimizing a cost function via hybrid quantum-classical optimization.» (p. 3) y «A VQC is generally constructed using a feature embedding circuit and a trainable structure known as an ansatz, a parameterized template composed of rotation gates and entangling gates.» (p. 3)

## Qué concluye la obra
- Proponen la arquitectura híbrida cuántico-clásica-cuántica QCQ-CNN, integrando filtros convolucionales cuánticos, capas CNN clásicas y un clasificador QNN entrenable al final: «In summary, we proposed and evaluated a hybrid quantum-classical-quantum convolutional neural network (QCQ-CNN), which integrates quantum convolutional filters, classical CNN layers, and a trainable quantum neural network (QNN) classifier.» (p. 15)
- El análisis de la profundidad del ansatz variacional demuestra que profundidades moderadas ofrecen un equilibrio óptimo entre expresividad y estabilidad del entrenamiento, evitando barren plateaus: «We conducted a systematic investigation of the impact of quantum ansatz depth and found that circuits of moderate depth provide a favorable trade-off between model expressivity and training stability.» (p. 15)

## Qué deja como trabajo futuro o limitación declarada
- Señala como limitaciones que la evaluación se realizó en simulaciones y sobre circuitos de escala reducida, lo que no generaliza directamente a tareas de gran escala: «Nonetheless, this work has several limitations. Our evaluations are still constrained to simulated environments and relatively small-scale circuits, which may not directly generalize to large-scale, high-dimensional tasks.» (p. 15)
- Destaca que la sobrecarga computacional de los modelos híbridos y las restricciones de los simuladores limitan la exploración de arquitecturas más complejas y conjuntos mayores: «In addition, the computational overhead of hybrid models and the current limitations of quantum simulators restrict our ability to explore more complex architectures or larger datasets.» (p. 15)
