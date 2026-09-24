# Borrador de reemplazo · Secciones 4.1, 4.4, 4.7, 4.8 y 4.9

> Texto propuesto para sustituir las partes del reporte que quedaron desactualizadas por las
> decisiones D-008 a D-018. **No está aplicado al `.tex`**: reescríbelo con tus palabras antes
> de integrarlo. Cada bloque indica qué decisión lo origina.

---

## §4.1 · Descripción general del proceso (diagrama y pie)

**Qué cambia.** El diagrama actual contradice el texto y varias decisiones (revisión del 2026-09-24):

- La separabilidad aparece como una caja sin número entre M5 y M6, con una flecha que sugiere que la clasificación depende de ella. Con **D-030**, la separabilidad pasa a ser el **M6**, la clasificación el **M7** y la evaluación comparativa el **M8**. El flujo es M5 → {M6, M7} → M8.
- M2 dice «Normalización · 224×224» (D-009, D-022). M4 dice «MinMaxScaler» (D-024, D-025). Las cajas cuánticas dicen «VQC» sin aclarar que θ está fijo (D-014) y no muestran K_Q (D-017). C2 aparece como «Baseline lineal» (D-016). M6 menciona «TorchConnector» (D-014). Falta indicar que masas y calcificaciones son subproblemas independientes (D-005).

Usa los mismos estilos del preámbulo (`blkGray`, `blkTeal`, `cond`, `condQ`, `blkAmber`, `blkCoral`, `arr`, `colGray`) y las librerías `positioning` y `calc`.

```latex
\begin{figure}[H]
\centering
\begin{tikzpicture}[every node/.style={scale=0.7}, node distance=0.5cm and 0.3cm]

\node[blkGray] (ds) {%
  \textbf{CBIS-DDSM Dataset}\\[2pt]
  {\normalfont\scriptsize
  1{,}566 pacientes $\cdot$ 3{,}568 lesiones $\cdot$
  DICOM $+$ CSV $\cdot$ masas y calcificaciones como subproblemas independientes}%
};

\node[blkTeal, below=of ds] (m1) {%
  \textbf{M1 $\cdot$ Lectura de datos}\\[2pt]
  {\normalfont\scriptsize
  \texttt{pydicom} $\cdot$ \texttt{pandas} $\cdot$ DICOM + CSV unificados}%
};

\node[blkTeal, below=of m1] (m2) {%
  \textbf{M2 $\cdot$ Preprocesamiento}\\[2pt]
  {\normalfont\scriptsize
  Alineación y limpieza de máscaras $\cdot$
  Recorte ROI a resolución original $\cdot$ intensidades de 16 bits}%
};

\node[blkTeal, below=of m2] (m3) {%
  \textbf{M3 $\cdot$ Extracción de características}\\[2pt]
  {\normalfont\scriptsize
  PyRadiomics: primer orden, forma, GLCM, GLRLM
  $\rightarrow \mathbf{x} \in \mathbb{R}^{67}$}%
};

\node[blkTeal, below=of m3] (m4) {%
  \textbf{M4 $\cdot$ Selección y escalado}\\[2pt]
  {\normalfont\scriptsize
  F-test con restricción $|r| \le 0.95$ ($k = 12$)
  $+$ cuantiles $\rightarrow \mathbf{x} \in [0,\pi]^{12}$}%
};

\node[font=\tiny\color{colGray}, below=0.25cm of m4] (lm5) {%
  M5 $\cdot$ Transformación (5 condiciones experimentales)%
};
\coordinate (fork) at ($(lm5.south) + (0,-0.2cm)$);

\node[cond, anchor=north] at ($(fork) + (-6.2cm, -0.1cm)$) (c1){%
  \textbf{C1 $\cdot$ Sin}\\ \textbf{transf.}\\[4pt]
  {\normalfont\tiny Baseline}\\ {\normalfont\tiny crudo}%
};
\node[cond, anchor=north] at ($(fork) + (-3.1cm, -0.1cm)$) (c2){%
  \textbf{C2 $\cdot$ PCA}\\ \textbf{lineal}\\[4pt]
  {\normalfont\tiny Control}\\ {\normalfont\tiny nulo}%
};
\node[cond, anchor=north] at ($(fork) + (0cm, -0.1cm)$) (c3){%
  \textbf{C3 $\cdot$ Kernel}\\ \textbf{PCA (RBF)}\\[4pt]
  {\normalfont\tiny Baseline}\\ {\normalfont\tiny no lineal}%
};
\node[condQ, anchor=north] at ($(fork) + (3.2cm, -0.1cm)$) (c4){%
  \textbf{C4 $\cdot$ Qiskit}\\ \textit{ZZ feature map}\\[4pt]
  {\normalfont\tiny ansatz con $\theta$ fijo}\\
  {\normalfont\tiny$\langle Z_i\rangle \in [-1,1]^{12}$ $\cdot$ $K_Q$}%
};
\node[condQ, anchor=north] at ($(fork) + (6.3cm, -0.1cm)$) (c5){%
  \textbf{C5 $\cdot$ Qiskit}\\ \textit{Pauli feature map} $(X, ZZ)$\\[4pt]
  {\normalfont\tiny ansatz con $\theta$ fijo}\\
  {\normalfont\tiny$\langle Z_i\rangle \in [-1,1]^{12}$ $\cdot$ $K_Q$}%
};

%% Convergencia centrada bajo C3 y a la altura de las cajas cuánticas, que son las más altas
\coordinate (merge) at ($(c3.south |- c5.south) + (0,-0.5cm)$);
\coordinate (mergeL) at (merge -| c1);
\coordinate (mergeR) at (merge -| c5);

%% M6 y M7 en paralelo: ambos consumen la salida de M5
\node[blkAmber, anchor=north, text width=5.6cm, minimum height=1.9cm]
  at ($(merge) + (-2.9cm, -0.6cm)$) (m6){%
  \textbf{M6 $\cdot$ Análisis de separabilidad}\\[2pt]
  {\normalfont\scriptsize
  KTA $\cdot$ \textit{geometric difference} $g_{CQ}$ $\cdot$
  Davies-Bouldin $\cdot$ Fisher $\cdot$ t-SNE}%
};
\node[blkCoral, anchor=north, text width=5.6cm, minimum height=1.9cm]
  at ($(merge) + (2.9cm, -0.6cm)$) (m7){%
  \textbf{M7 $\cdot$ Clasificación (MLP)}\\[2pt]
  {\normalfont\scriptsize
  Mismo MLP en las 5 condiciones $\cdot$
  validación cruzada 5-fold $\cdot$ test oficial}%
};

\node[blkCoral, anchor=north, text width=12cm]
  at ($(m6.south -| merge) + (0,-0.6cm)$) (m8){%
  \textbf{M8 $\cdot$ Evaluación comparativa}\\[2pt]
  {\normalfont\scriptsize
  AUC-ROC $\cdot$ F1 $\cdot$ Accuracy $\cdot$
  correlación separabilidad--clasificación $\cdot$
  masas vs.\ calcificaciones $\cdot$ restricciones del simulador}%
};

\node[blkGray, below=of m8, text width=12cm] (res) {%
  \textbf{Informe de resultados}\\[2pt]
  {\normalfont\scriptsize
  Separabilidad $\cdot$ Clasificación $\cdot$
  Viabilidad práctica del simulador Qiskit Aer}%
};

%% ── Flechas
\foreach \a/\b in {ds/m1, m1/m2, m2/m3, m3/m4, m8/res}
  \draw[arr] (\a.south) -- (\b.north);
\draw[color=colGray, line width=0.4pt] (m4.south) -- (lm5.north);
\draw[color=colGray, line width=0.4pt] (lm5.south) -- (fork);
\draw[color=colGray, line width=0.4pt] (fork -| c1.north) -- (fork -| c5.north);
\foreach \c in {c1, c2, c3, c4, c5}
  \draw[arr] (fork -| \c.north) -- (\c.north);
\foreach \c in {c1, c2, c3, c4, c5}
  \draw[color=colGray, line width=0.4pt] (\c.south) -- (\c.south |- merge);
\draw[color=colGray, line width=0.4pt] (mergeL) -- (mergeR);
\draw[arr] (merge -| m6.north) -- (m6.north);
\draw[arr] (merge -| m7.north) -- (m7.north);
\draw[arr] (m6.south) -- (m6.south |- m8.north);
\draw[arr] (m7.south) -- (m7.south |- m8.north);

\end{tikzpicture}

\caption{%
  Pipeline del sistema híbrido cuántico-clásico para prediagnóstico de cáncer de mama.
  Masas y calcificaciones recorren el pipeline como subproblemas independientes.
  El módulo M4 selecciona 12 características por F-test con una restricción de
  redundancia y las transforma en ángulos en $[0,\pi]$ mediante una transformación por
  cuantiles, ajustada solo sobre el conjunto de entrenamiento; el mismo vector alimenta las
  cinco condiciones. En C4 y C5 los parámetros del \textit{ansatz} se fijan con una semilla
  y no se entrenan, y el kernel de fidelidad $K_Q$ se calcula con el \textit{feature map}
  solo. C4 combina una codificación de primer orden en $Z$ con el acoplamiento $ZZ$; en C5,
  con una repetición, el término en $X$ actúa sobre un autoestado y solo añade una fase global,
  de modo que C5 codifica únicamente el acoplamiento $ZZ$ [PENDIENTE Q-012]. La salida de M5 alimenta en paralelo el análisis de
  separabilidad (M6) y la clasificación (M7), que el módulo M8 compara.%
}
\label{fig:pipeline_sistema}
\end{figure}
```

> **Sin compilar.** El código reutiliza las posiciones y estilos del original. Revisa al compilar
> que las cajas de M6 y M7 no se solapen; si hace falta, ajusta los desplazamientos ±2.9 cm o
> `text width`.

---

## §4.4 · Módulo 2: Preprocesamiento de imagen

**Qué cambia.** El texto actual aplica CLAHE y normaliza a 224×224. Ambas cosas se retiran de
la ruta radiómica (D-009, D-010). Se añade la alineación verificada de las máscaras y su limpieza
(D-020, D-021, H-020, H-021) y el contrato de salida (D-022). *Actualizado el 2026-09-23 con los
resultados de `Code/2_Preprocessing.ipynb`; D-020 a D-022 siguen provisionales.*

```latex
El módulo de preprocesamiento transforma las imágenes DICOM crudas en pares
(imagen, máscara) alineados y centrados en la región de interés, adecuados para la
extracción de características del módulo siguiente.

La primera etapa resuelve la correspondencia geométrica entre imagen y máscara. En 80 de
los 3\,568 registros las dimensiones de la máscara no coinciden con las de la mamografía, y
el desajuste es de dos tipos. En 78 masas la máscara reproduce la imagen a una escala de
0.870 en ambos ejes, y se remuestrea al tamaño de la imagen por vecino más cercano, que
preserva su carácter binario. En 2 calcificaciones la diferencia es de pocas decenas de
píxeles y no es proporcional, de modo que la máscara se ancla sin escalar. Ambas reglas se
verificaron de forma independiente. Los recortes que acompañan al CBIS-DDSM coinciden, cuando
imagen y máscara están alineadas, con la caja de la máscara ampliada en 20 píxeles por lado.
Esa relación se cumple en el \SI{99.8}{\percent} de los casos verificables y confirma la regla
de anclaje; para las máscaras escaladas se empleó una prueba de contraste entre la lesión y
su entorno.

A continuación, cada máscara se reduce a su componente conexa mayor. El
\SI{86.3}{\percent} de las máscaras de masas contiene pequeñas islas desconectadas, residuos
de la rasterización del contorno, que alterarían el perímetro y el diámetro máximo calculados
sobre la región.

La segunda etapa realiza el recorte de la región de interés: la máscara identifica los
píxeles de la lesión y se extrae su rectángulo mínimo ampliado en 20 píxeles por lado,
\textbf{conservando la resolución y las intensidades originales de la imagen}. Los recortes
del CBIS-DDSM no se emplean para la extracción, porque su intensidad está reescalada por una
ganancia distinta en cada caso.

La decisión de no redimensionar el recorte a una malla común es deliberada. Las lesiones del
conjunto abarcan desde \(33\times33\) hasta \(3\,801\times2\,873\) píxeles, y las medidas de
tamaño figuran entre las características más discriminativas entre lesiones benignas y
malignas: en masas, cinco de las doce con mayor tamaño de efecto sobre el conjunto de
entrenamiento son descriptores de forma y tamaño (\(|d|\) de Cohen entre 0.40 y 0.45).
Redimensionar a una malla común iguala artificialmente la escala de las lesiones y elimina
esa señal. La normalización a \(224\times224\) correspondía a la Estrategia B
basada en un codificador convolucional, descartada en favor de la extracción radiómica.

Por la misma razón se excluye la ecualización adaptativa de histograma (CLAHE) de la ruta
de extracción. CLAHE es una transformación local dependiente del contenido, y altera la
reproducibilidad de las características de primer orden y de la matriz de co-ocurrencia
bajo el estándar IBSI. Se genera una variante con CLAHE únicamente para cuantificar su
efecto sobre las características extraídas, que se reporta en la sección de resultados.
```

> **Antes de integrarlo.** El \(|d|\) de 1.41–1.43 de H-003 venía de solo 20 masas y ya no se
> cita: las cifras de arriba son del conjunto de entrenamiento completo (H-023). La hipótesis de
> que 0.870 = 43.5/50 µm entre digitalizadores del DDSM está sin verificar: no incluirla sin fuente.

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
entrelazamiento. \textbf{[Corregir según Q-012, ver H-034]} Con una repetición, el término en $X$ actúa
sobre el estado $|+\rangle$, que es autoestado de $X$, y solo añade una fase global: C5 equivale
a un \textit{feature map} con únicamente el acoplamiento $ZZ$. La comparación entre C4 y C5 mide
por tanto el efecto de incluir o no una codificación de primer orden.
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
- **Q-004** quedó cerrada (D-019): Azevedo et al. (2022). Falta añadir el `\cite` en §1.3 y §2.1.5.
- **§4.5** promete «entre 100 y 300 características»: con las cuatro familias sobre la imagen
  original son **67** (D-023).
- **D-030, renumeración de módulos:** el M6 pasa a ser la separabilidad, el M7 la clasificación y el M8 la
  evaluación comparativa. Hay que renumerar las secciones de módulos (con una nueva sección para M6),
  reagrupar la tabla de requisitos (RF-15 a RF-17 en M6 y los de clasificación en M7), rehacer la tabla CRISP-DM
  y revisar cualquier mención de «M6» o «M7» en el texto.
- **H-033, fórmula de la *geometric difference* (§3.4.2 y RF-16):** K_C y K_Q están invertidos respecto a Huang et al.
  (2021), ec. 5. La forma correcta es g_CQ = √‖√K_Q · K_C⁻¹ · √K_Q‖∞, con Tr(K) = N.
- **RF-14** dice «PauliFeatureMap (operadores X, Y, Z)»; C5 usa (X, ZZ) (D-015).
- **RF-04, RF-05 y RF-06** (tabla de requisitos del Módulo 2) siguen pidiendo normalizar a [0,1], aplicar
  CLAHE y redimensionar a 224×224. Hay que reescribirlos en línea con D-009, D-010 y D-022.
