# Borrador de reemplazo · Secciones 4.4, 4.7, 4.8 y 4.9

> Texto propuesto para sustituir las partes del reporte que quedaron desactualizadas por las
> decisiones D-008 a D-018. **No está aplicado al `.tex`**: reescríbelo con tus palabras antes
> de integrarlo. Cada bloque indica qué decisión lo origina.

---

## §4.4 · Módulo 2: Preprocesamiento de imagen

**Qué cambia.** El texto actual aplica CLAHE y normaliza a 224×224. Ambas cosas se retiran de
la ruta radiómica (D-009, D-010).

```latex
El módulo de preprocesamiento transforma las imágenes DICOM crudas en pares
(imagen, máscara) alineados y centrados en la región de interés, adecuados para la
extracción de características del módulo siguiente.

La primera etapa resuelve la correspondencia geométrica entre imagen y máscara. El
\SI{2.3}{\percent} de los casos (80 de 3\,568) presenta máscaras cuyas dimensiones no
coinciden con las de la mamografía asociada; en esos casos la máscara se remuestrea al
espacio de la imagen mediante interpolación por vecino más cercano, que preserva el
carácter binario de la anotación.

La segunda etapa realiza el recorte de la región de interés: la máscara binaria identifica
los píxeles de la lesión y se extrae el rectángulo mínimo que contiene la región activa,
\textbf{conservando la resolución original de la imagen}.

La decisión de no redimensionar el recorte a una malla común es deliberada. Los recortes
del conjunto abarcan desde \(41\times65\) hasta \(1\,137\times1\,641\) píxeles, y un
análisis preliminar de los tamaños de efecto muestra que las cinco características más
discriminativas entre lesiones benignas y malignas en masas son medidas de tamaño
(\(|d|\) de Cohen entre 1.41 y 1.43). Redimensionar a una malla común iguala artificialmente
la escala de las lesiones y elimina precisamente la señal de mayor magnitud disponible. La
normalización a \(224\times224\) correspondía a la Estrategia B basada en un codificador
convolucional, descartada en favor de la extracción radiómica.

Por la misma razón se excluye la ecualización adaptativa de histograma (CLAHE) de la ruta
de extracción. CLAHE es una transformación local dependiente del contenido, y altera la
reproducibilidad de las características de primer orden y de la matriz de co-ocurrencia
bajo el estándar IBSI. Se genera una variante con CLAHE únicamente para cuantificar su
efecto sobre las características extraídas, que se reporta en la sección de resultados.
```

---

## §4.7 · Módulo 5: Transformación

**Qué cambia.** C5 deja de ser `PauliFeatureMap(Z, ZZ)` porque era idéntico a C4 (H-012,
D-015). C2 se declara control nulo (D-016). Se fija k=12 y reps=1 (D-013).

```latex
El módulo de transformación implementa las cinco condiciones experimentales. Todas parten
del mismo vector \(\mathbf{x} \in [0,\pi]^{12}\) producido por M4.

\begin{itemize}
  \item \textbf{C1 · Baseline crudo.} El vector pasa directamente al clasificador.
  \item \textbf{C2 · PCA lineal.} Control nulo, véase la nota más abajo.
  \item \textbf{C3 · Kernel PCA con núcleo RBF.} Baseline clásico no lineal.
  \item \textbf{C4 · ZZFeatureMap.} Codificación de primer orden en \(Z\) con acoplamiento
        de segundo orden \(ZZ\).
  \item \textbf{C5 · PauliFeatureMap con operadores \((X, ZZ)\).} Codificación de primer
        orden en \(X\), manteniendo el mismo acoplamiento de segundo orden.
\end{itemize}

\textbf{Sobre la condición C2.} Dado que M4 entrega un vector ya de dimensión \(k\), una
proyección PCA a \(k\) componentes no constituye una reducción de dimensionalidad sino una
rotación ortogonal, que preserva las distancias euclidianas. En consecuencia, los índices
de Davies-Bouldin y Fisher y el \textit{kernel-target alignment} son invariantes ante ella,
y el perceptrón absorbe la rotación en su primera capa lineal. C2 se conserva
deliberadamente como \textbf{control nulo}: si las métricas de separabilidad arrojaran
valores distintos para C1 y C2, ello indicaría un defecto en su implementación. El
comparador clásico sustantivo es C3.

\textbf{Sobre la elección de C5.} La biblioteca Qiskit define \texttt{ZZFeatureMap} como un
caso particular de \texttt{PauliFeatureMap} con operadores \((Z, ZZ)\); ambas construcciones
preparan el mismo estado, con fidelidad \(|\langle\phi_{ZZ}|\phi_{\text{Pauli}}\rangle|^2 = 1\).
Especificadas así, C4 y C5 no constituirían condiciones independientes. Se adopta por tanto
el conjunto \((X, ZZ)\), cuya fidelidad media respecto a la codificación \(ZZ\) es de 0.071
sobre 200 entradas aleatorias, manteniendo un número idéntico de compuertas de
entrelazamiento. La comparación entre C4 y C5 mide en consecuencia el efecto del
\textbf{eje de codificación de primer orden}, con el acoplamiento de segundo orden fijo.
```

---

## §4.8 · Módulo 6: Clasificación

**Qué cambia.** Desaparece `TorchConnector` y la optimización conjunta (D-014). Entra la
validación cruzada (D-018).

```latex
La transformación cuántica se aplica como una etapa de codificación determinista. Los
parámetros variacionales \(\boldsymbol{\theta}\) del \textit{ansatz} se fijan mediante una
semilla declarada (42) y no se optimizan. Los \textit{quantum embeddings}
\(\langle Z_i\rangle\) se calculan una sola vez para la totalidad del conjunto, se almacenan
en disco, y el clasificador se entrena sobre esa matriz como sobre cualquier conjunto de
datos tabular.

Esta arquitectura responde a dos consideraciones independientes. La primera es de validez
interna: las condiciones C2 y C3 son transformaciones no supervisadas, de modo que permitir
que la condición cuántica ajustara \(\boldsymbol{\theta}\) contra las etiquetas le otorgaría
una ventaja de la que los baselines carecen, y cualquier mejora observada en separabilidad
sería atribuible al ajuste supervisado y no a la codificación. La segunda es de viabilidad:
el cálculo del gradiente por \textit{parameter-shift} requiere dos evaluaciones del circuito
por parámetro, frente al coste independiente del número de parámetros que caracteriza a la
retropropagación clásica, lo que sitúa el entrenamiento conjunto en un régimen impracticable.

Es necesario precisar que el \textit{ansatz} no puede suprimirse. El \textit{feature map}
aplica exclusivamente compuertas de Hadamard y compuertas diagonales, que modifican las
fases de las amplitudes pero no sus magnitudes. Partiendo del estado
\(H^{\otimes k}|0\rangle\), toda amplitud conserva magnitud \(2^{-k/2}\), de donde
\(P(\text{qubit}_i = 0) = 1/2\) exactamente y \(\langle Z_i\rangle = 0\) para toda entrada.
La información codificada reside en las fases, a las que una medición en la base \(Z\) es
insensible; el \textit{ansatz} es el mecanismo que las rota hacia poblaciones medibles. En
consecuencia, \(\boldsymbol{\theta}\) constituye un parámetro reportable del diseño
experimental y no un detalle de implementación.

El clasificador es un perceptrón multicapa idéntico en las cinco condiciones. Se emplea
validación cruzada estratificada de cinco pliegues sobre el conjunto de entrenamiento,
preservando intacta la partición de prueba oficial del CBIS-DDSM como evaluación final.
```

---

## §4.9 · Módulo 7: Evaluación comparativa

**Qué cambia.** Se precisa sobre qué objeto se calcula la *geometric difference* (D-017) y se
anticipa la discrepancia entre familias de métricas (H-013).

```latex
El análisis de separabilidad opera sobre dos objetos distintos, y la distinción es
consecuente para la interpretación de los resultados.

El \textit{kernel-target alignment} y la \textit{geometric difference} se calculan sobre el
núcleo cuántico de fidelidad \(K_Q(\mathbf{x},\mathbf{x}') =
|\langle\phi(\mathbf{x})|\phi(\mathbf{x}')\rangle|^2\), evaluado mediante
\texttt{FidelityQuantumKernel} sobre el \textit{feature map} exclusivamente, sin
\textit{ansatz}. La \textit{geometric difference} está definida entre dos núcleos, por lo
que no admite ser calculada sobre los vectores \(\langle Z_i\rangle\). Dado su coste
cuadrático en el número de muestras, se evalúa sobre submuestras de 150 a 200 casos por
subconjunto.

Los índices de Davies-Bouldin y Fisher, la visualización \textit{t-SNE} y el clasificador
operan en cambio sobre los vectores \(\langle Z_i\rangle\).

Ambas familias de métricas no son equivalentes: el núcleo de fidelidad compara estados
completos, incluida su información de fase, mientras que los valores de expectativa en la
base \(Z\) son insensibles a ella. Es por tanto posible observar un alineamiento elevado
del núcleo junto a un desempeño clasificatorio moderado, y tal discrepancia constituye
información sobre la naturaleza de la codificación antes que una inconsistencia.
```

---

## Pendiente que no cubre este borrador

- **§5.1** afirma cobertura DICOM del 100 %. Era falso al escribirse (97.6 %) y es cierto
  desde el 2026-09-21. Conviene una nota sobre la recuperación de las 84 series.
- **§5.4** documenta que `Manufacturer` es UNKNOWN, pero no extrae la consecuencia: al faltar
  también `PixelSpacing`, las características de forma quedan en píxeles sin escala física.
- **El cronograma** no contempla M2 ni M3 como actividades y hay que rehacerlo.
- **Q-004**: la atribución a Azevedo o a Incudini sigue sin resolverse.
