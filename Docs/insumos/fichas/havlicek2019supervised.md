# havlicek2019supervised · Supervised learning with quantum enhanced feature spaces

- Autores y año: Havlíček et al. (2019)
- DOI comprobado en la página 1: Sí (publicado en Nature 10.1038/s41586-019-0980-2; leído en preprint arXiv:1804.11326)
- Versión leída: Docs/fuentes/pdf/havlicek2019supervised.pdf · preprint arXiv:1804.11326 · 22 páginas
- Tipo: experimental

## Respuestas a las preguntas
1. Qué dos métodos proponen — Proponen un clasificador variacional cuántico (quantum variational classifier) que optimiza un circuito variacional como hiperplano separador, y un estimador de kernel cuántico (quantum kernel estimator) que calcula directamente el kernel cuántico para optimizar un clasificador clásico — «Here, we propose and experimentally implement two novel methods on a superconducting processor.» (p. 1) y «One method, the quantum variational classiﬁer builds on [1, 2] and operates through using a variational quantum circuit to classify a training set in direct analogy to conventional SVMs. In the second, a quantum kernel estimator, we estimate the kernel function and optimize the classiﬁer directly.» (p. 1)
2. En qué procesador y con cuántos qubits los ejecutan — Implementan los métodos en un procesador superconductor de 5 qubits de IBM, ejecutando los experimentos con 2 qubits (Q0 y Q1) — «Schematic of the 5-qubit quantum processor. The experiment was performed on qubits Q0 and Q1, highlighted in the image.» (p. 3)
3. Qué dicen sobre la ventaja cuántica — No afirman una ventaja incondicional, sino que la establecen expresamente como condición: solo puede lograrse si el mapeo de características genera un kernel computacionalmente intratable o difícil de estimar por medios clásicos — «To obtain an advantage over classical approaches we need to implement a map based on circuits that are hard to simulate classically.» (p. 2) y «To see why a quantum advantage can only be obtained for feature maps with a classically hard to estimate kernel, we point out the following: The decision rule py(⃗x) > p−y(⃗x) −yb can be restated as ˜m(⃗x) = sign(⟨Φ(⃗x) |W †(⃗θ)fW(⃗θ)| Φ(⃗x)⟩+ b).» (p. 4)
4. Forma del circuito de codificación que proponen — Utilizan un mapeo unitario de n qubits alternado con capas Hadamard y operadores diagonales con coeficientes de datos $\phi_S(x)$, en particular para 2 qubits con $\phi_{\{i\}}(x) = x_i$ y $\phi_{\{1,2\}}(x) = (\pi - x_1)(\pi - x_2)$ — «We use the map for n = d = 2 - qubits in Fig. 1(b) with φ{i}(⃗x) = xi and φ{1,2}(⃗x) = (π −x1)(π −x2).» (p. 2)

## Qué concluye la obra
- Demuestran experimentalmente un clasificador cuántico que mapea datos en un espacio de Hilbert grande aprovechando estados cuánticos: «Both methods represent the feature space of a classiﬁcation problem by a quantum state, taking advantage of the large dimensionality of quantum Hilbert space to obtain an enhanced solution.» (p. 1)
- Concluyen que demostraron experimentalmente un clasificador con kernel cuántico conjeturado como difícil de estimar clásicamente, logrando hasta 100 % de éxito incluso ante ruido: «Conclusions: We have experimentally demonstrated a classiﬁer that exploits a quantum feature space. The kernel of this feature space has been conjectured to be hard to estimate classically.» (p. 6)

## Qué deja como trabajo futuro o limitación declarada
- Identifican la búsqueda de feature maps adecuados con ventaja cuántica demostrable y mejoras sobre datos reales: «In the future it becomes intriguing to ﬁnd suitable feature maps for this technique with provable quantum advantages while providing signiﬁcant improvement on real world data sets.» (p. 6)
