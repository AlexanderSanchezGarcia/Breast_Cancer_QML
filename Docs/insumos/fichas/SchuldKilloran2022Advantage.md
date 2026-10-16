# SchuldKilloran2022Advantage · Is quantum advantage the right goal for quantum machine learning?

- Autores y año: Schuld, M., & Killoran, N. (2022).
- Versión leída: Docs/fuentes/pdf/SchuldKilloran2022Advantage.pdf · versión publicada (PRX Quantum, 3(3), 030101 / arXiv:2203.01340) · 13 páginas
- Tipo: revisión conceptual y perspectiva metodológica

## Qué concluye
- Cuestionan abiertamente si la narrativa hegemónica de buscar ventaja cuántica y «vencer» al aprendizaje automático clásico debe continuar dominando la literatura: «We argue that these challenges call for a critical debate on whether quantum advantage and the narrative of “beating” classical machine learning should continue to dominate the literature the way it does, and highlight examples for how other perspectives in existing research provide an important alternative to the focus on advantage.» (p. 1)
- La investigación en QML enfrenta la paradoja de intentar superar algoritmos clásicos consolidados y masivos en problemas conceptualmente intratables desde el punto de vista teórico: «To state it in simple terms, quantum machine learning research is trying to beat large, high-performing algorithms for problems that are conceptually hard to study.» (p. 1)
- Las herramientas disponibles en computación cuántica para fundamentar ventajas (demostraciones asintóticas o prototipos ruidosos de escala minúscula) son severamente limitadas en el contexto de machine learning: «At the same time, the tools that quantum computing offers to think about advantages – essentially, experiments on prototype quantum devices and over 30 years’ worth of knowledge on provable asymptotic speedups – are severely limited.» (p. 1)
- Centrarse de forma excluyente en la ventaja cuántica obliga a restringir la investigación a un conjunto sesgado y artificial de modelos y problemas abordables bajo esas limitaciones extremas: «Focusing on quantum advantage therefore means focusing only on a biased subset of models, datasets and theoretical approaches, namely the ones we can tackle under these difficult conditions – a fact that we should discuss more critically.» (p. 1)
- Juzgar el valor de una investigación exclusivamente bajo el prisma de las aceleraciones computacionales puede frenar la emergencia de áreas esenciales y sofocar la innovación: «But judging the value of research from the limited lens of speedups could prevent important research areas from emerging, and in the worst case, it may even hinder the innovation needed to find use cases for quantum computers in the future.» (p. 1)
- La interrogante de si las computadoras cuánticas desempeñarán un papel real en aplicaciones prácticas de aprendizaje automático sigue completamente abierta: «In our view, the question about whether quantum computers can really play a role in identifying practical machine learning applications is therefore still wide open» (p. 6)

## Qué deja como trabajo futuro o limitación declarada
- Proponen orientar la disciplina hacia una pregunta fundacional más constructiva: cómo preparar el software cuántico para aplicaciones de aprendizaje automático: «driven by an advantage from the very beginning, but by the question How can we make quantum software ready for machine learning applications?.» (p. 2)
- Señalan que para explorar con sentido los beneficios futuros del QML se requiere desarrollar tres pilares esenciales: modelos adecuados, herramientas teóricas para analizarlos y software escalable: «We believe that all three ingredients – the right quantum models to study, theoretical tools with which we can study them, and software solutions to scale experiments – are important for a meaningful attempt to explore the benefit of quantum computing for machine learning in future.» (p. 2)
- Previenen contra la tentación de volcar la atención hacia «datos cuánticos» únicamente porque se ajustan con mayor comodidad a las técnicas tradicionales de prueba analítica: «we should ask ourselves if switching our attention to “quantum data” is subconsciously motivated by the hope that it suits our traditional proof techniques better, rather than providing a mature use-case.» (p. 6)
- Llaman a tener el valor científico de resistir las narrativas comerciales que prometen supremacías millonarias o acuñan términos pegajosos sin sustento riguroso: «asking more fundamental questions may be a very good use of our time, but require a bit of courage to withstand the narrative of trying to find the billiondollar quantum “supremacy”» (p. 9)

## Diseño experimental (solo obras experimentales)
No aplica: la obra es un artículo de perspectiva conceptual y discusión metodológica en *PRX Quantum*; no incluye experimentos numéricos sobre conjuntos de datos cuantitativos ni comparaciones empíricas de benchmarks.

## Las cuatro preguntas de H-046 (solo obras que reportan una ventaja o un resultado cuántico frente a clásico)
No aplica: el trabajo no reporta una ventaja cuántica. Al contrario, formula una crítica metodológica rigurosa contra la pretensión de exigir evidencia inmediata de ventaja cuántica frente a algoritmos clásicos de estado del arte en tareas prácticas de machine learning.

## Preguntas específicas
- **Su argumento central sobre por qué la ventaja cuántica no debería ser el único objetivo**:
  1. *Desfase fundamental de metodologías*: El machine learning contemporáneo avanza empíricamente a través de modelos masivos (redes neuronales profundas con millones de parámetros y grandes volúmenes de datos) cuyo comportamiento práctico excede la capacidad de las teorías matemáticas existentes. La computación cuántica, en cambio, carece de hardware maduro para contrastes empíricos a esa escala y depende de demostraciones asintóticas que no reflejan el rendimiento práctico: «To state it in simple terms, quantum machine learning research is trying to beat large, high-performing algorithms for problems that are conceptually hard to study.» (p. 1).
  2. *Deformación de la agenda científica*: Forzar la búsqueda de ventaja empuja a la comunidad a fabricar problemas artificiales o elegir problemas donde las demostraciones analíticas sean convenientes, produciendo comparaciones frágiles o hiperparámetros clásicos mal ajustados.
  3. *Inhibición de fundamentos necesarios*: Exigir que cada trabajo demuestre que «lo cuántico supera a lo clásico» frena el desarrollo de las herramientas matemáticas, representaciones y bibliotecas de software que se requieren antes de poder si quiera plantear experimentos a gran escala.
- **Qué proponen en su lugar**:
  1. *Reformulación de la meta de investigación*: Sustituir la narrativa de «vencer a lo clásico» por la construcción de fundamentos sólidos bajo la pregunta: «How can we make quantum software ready for machine learning applications?.» (p. 2).
  2. *Estudio de bloques constructivos y representaciones*: Investigar arquitecturas básicas (perceptrones cuánticos, modelos variacionales, mapas de características) desde una perspectiva dual «ventaja y no-ventaja», analizando su expresividad, sesgo inductivo y capacidad de representación.
  3. *Diferenciación automática e integración híbrida*: Desarrollar bibliotecas de software que permitan calcular gradientes exactos de circuitos cuánticos en hardware mediante la regla de desplazamiento de parámetros (*parameter-shift rule*), habilitando su acoplamiento modular con marcos clásicos como PyTorch o TensorFlow: «Armed with the ability to evaluate quantum models and compute their gradients, we can directly “plug and play” with existing deep learning tools and train quantum circuits the same way as we train neural networks.» (p. 9).
  4. *Polinización cruzada entre campos*: Adaptar herramientas teóricas y optimizadores de deep learning a circuitos cuánticos y transferir conceptos cuánticos (como redes de tensores) hacia la computación clásica.
  5. *Aceptación de resultados negativos y honestidad científica*: Fomentar que supervisores, revisores y revistas valoren los análisis descriptivos y los resultados negativos como contribuciones científicas legítimas.

## Relevancia para el TT
- Se alinea directamente con la **Regla 1 de CLAUDE.md**: respalda conceptualmente la orientación de nuestra tesis, cuyo fin es evaluar de forma objetiva la viabilidad y separabilidad de transformaciones cuánticas variacionales en datos radiómicos del CBIS-DDSM, asumiendo que un resultado negativo respecto a la ventaja cuántica es evidencia válida y rigurosa.
- Se conecta con **H-046**, **H-049** y **H-050**: aporta el respaldo metodológico para no forzar afirmaciones infundadas de «ventaja cuántica» sobre el CBIS-DDSM, donde los clasificadores clásicos (SVM con RBF) no son superados por mapas cuánticos.
- Se conecta con **§1.1** y **§6.4**: fundamenta una postura epistemológica sobria frente al exceso de expectativas infundadas en QML.
- **Qué NO se puede afirmar con esta fuente**:
  - No se puede afirmar que Schuld y Killoran descarten el potencial de la computación cuántica; proponen fundamentar rigurosamente la disciplina en vez de apresurar promesas comerciales de ventaja.
  - No se puede citar esta obra como demostración matemática de superioridad de ningún modelo cuántico específico sobre datos prácticos.

## Contraste con lo que el proyecto ya le atribuye
- `Docs/Technical_Report.tex:755,756,1221,1253,3757,3758,3831,3832`:
  - En el reporte técnico actual se cita únicamente el trabajo previo de Schuld y Killoran (2019), *Quantum machine learning in feature Hilbert spaces* (`Schuld2019QuantumML` / `schuld2019quantum`), presentándolo como justificación para proyectar datos radiómicos a espacios de Hilbert cuánticos de dimensión $2^n$.
  - En contraste, la perspectiva de Schuld y Killoran de 2022 (`SchuldKilloran2022Advantage`) fue incorporada en `Docs/insumos/bibitems_noche.tex` para moderar esa postura inicial.
  - Sostenido: La obra de 2022 sostiene directamente la decisión metodológica de nuestra tesis de no condicionar el éxito del trabajo a la existencia de una ventaja cuántica en el CBIS-DDSM, reconociendo que proyectar a espacios de Hilbert exponencialmente grandes sin sesgo inductivo no garantiza mejoras frente a métodos clásicos.
- `Other/bitacora_decisiones.md:328`:
  - «El comparador clásico real es C3: Kernel PCA con RBF de k → k es genuinamente no lineal, no una rotación. Y es el comparador conceptualmente correcto, porque el marco de Schuld contrapone kernels cuánticos contra kernels clásicos, siendo el RBF el kernel clásico de referencia.»
  - Sostenido: Sí. El estándar metodológico promovido por Schuld y Killoran exige comparar contra kernels clásicos de referencia bien calibrados.
