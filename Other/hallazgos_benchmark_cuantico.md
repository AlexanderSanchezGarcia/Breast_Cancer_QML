# Hallazgos del Benchmark Cuántico y Análisis Metodológico · TT 2026-B039

Este documento presenta los hallazgos técnicos y el análisis empírico derivados de la caracterización de transformaciones cuánticas variacionales sobre las mamografías del dataset CBIS-DDSM. El análisis se divide en ocho secciones técnicas orientadas a sustentar las decisiones metodológicas y la viabilidad computacional del proyecto.

---

## 1. Complejidad del circuito

La complejidad del circuito cuántico se evaluó en función del número de qubits ($k \in \{8, 12, 16\}$) y las repeticiones del ansatz ($reps \in \{1, 2, 3\}$) para las configuraciones de mapa de características `ZZFeatureMap` (`zz`) y `PauliFeatureMap` (`pauli_z_zz`).

### Resultados de complejidad computacional
Los datos provienen del archivo `Code/5_benchmark_complejidad.csv`.

| feature_map | k | reps | n_weights | depth_raw | depth_transpiled | n_cx | n_gates |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `zz` | 8 | 1 | 16 | 50 | 58 | 63 | 187 |
| `zz` | 8 | 2 | 24 | 53 | 64 | 70 | 226 |
| `zz` | 8 | 3 | 32 | 56 | 70 | 77 | 265 |
| `zz` | 12 | 1 | 24 | 78 | 86 | 143 | 353 |
| `zz` | 12 | 2 | 36 | 81 | 92 | 154 | 412 |
| `zz` | 12 | 3 | 48 | 84 | 98 | 165 | 471 |
| `zz` | 16 | 1 | 32 | 106 | 114 | 255 | 567 |
| `zz` | 16 | 2 | 48 | 109 | 120 | 270 | 646 |
| `zz` | 16 | 3 | 64 | 112 | 126 | 285 | 725 |
| `pauli_z_zz` | 8 | 1 | 16 | 50 | 58 | 63 | 187 |
| `pauli_z_zz` | 8 | 2 | 24 | 53 | 64 | 70 | 226 |
| `pauli_z_zz` | 8 | 3 | 32 | 56 | 70 | 77 | 265 |
| `pauli_z_zz` | 12 | 1 | 24 | 78 | 86 | 143 | 353 |
| `pauli_z_zz` | 12 | 2 | 36 | 81 | 92 | 154 | 412 |
| `pauli_z_zz` | 12 | 3 | 48 | 84 | 98 | 165 | 471 |
| `pauli_z_zz` | 16 | 1 | 32 | 106 | 114 | 255 | 567 |
| `pauli_z_zz` | 16 | 2 | 48 | 109 | 120 | 270 | 646 |
| `pauli_z_zz` | 16 | 3 | 64 | 112 | 126 | 285 | 725 |

### Análisis del número de puertas CX
El número de puertas de dos qubits de tipo controlado-NOT ($n_{cx}$) en el circuito transpilado responde de manera exacta a la expresión:

$$n_{cx} = 2 \cdot C(k, 2) + reps \cdot (k - 1)$$

donde $C(k, 2) = \frac{k(k-1)}{2}$ es el número de pares de características interactuantes en el mapa de características (ZZFeatureMap), requiriendo 2 puertas CX por par ($2 \cdot C(k,2) = k(k-1)$), mientras que $reps \cdot (k - 1)$ representa las puertas entrelazadoras del ansatz variacional con entrelazamiento lineal. Por ejemplo:
- Para $k=8, reps=1$: $2 \cdot 28 + 1 \cdot 7 = 56 + 7 = 63$ puertas CX.
- Para $k=16, reps=3$: $2 \cdot 120 + 3 \cdot 15 = 240 + 45 = 285$ puertas CX.

---

## 2. Coste del entrenamiento conjunto (Arquitectura A)

La Arquitectura A corresponde a la integración acoplada del circuito cuántico variacional (VQC) con la red perceptrón multicapa (MLP) optimizados punto a punto *end-to-end*. En esta configuración, la actualización de los parámetros variacionales $\theta$ requiere la regla de desplazamiento de parámetros (*parameter-shift rule*), la cual evalúa el circuito cuántico dos veces por cada parámetro individual por muestra y por época:

$$\frac{\partial f(\theta)}{\partial \theta_i} = \frac{f(\theta + \frac{\pi}{2} e_i) - f(\theta - \frac{\pi}{2} e_i)}{2}$$

A diferencia del algoritmo de retropropagación (*backpropagation*) clásico —cuyo coste computacional es independiente del número de parámetros—, el gradiente por *parameter-shift* escala linealmente con la dimensión del vector $\theta$ ($2 \cdot n_{weights}$ evaluaciones de circuito por muestra).

### Tiempos de entrenamiento medidos y proyectados (50 épocas)
Los tiempos presentados a continuación se obtuvieron del archivo `Code/5_benchmark_resultados.csv`. El dataset de entrenamiento comprende el subconjunto de masas ($n = 1318$ muestras) y el subconjunto de calcificaciones ($n = 1546$ muestras), sumando 50 épocas completas.

| feature_map | k | reps | n_weights | fwd_per_sample_s | bwd_per_sample_s | step_per_sample_s | train_mass_h | train_calcification_h | total_both_h |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `zz` | 8 | 1 | 16 | 0.01657912499649683 | 0.5874025522498414 | 0.6039816772463382 | 11.05622014737047 | 12.968828791983874 | 24.025048939354342 |
| `zz` | 8 | 2 | 24 | 0.020854697744653095 | 0.9751019374962198 | 0.9959566352408729 | 18.231539517325977 | 21.385402195588743 | 39.61694171291472 |
| `zz` | 8 | 3 | 32 | 0.019811625003057998 | 1.3785148957467754 | 1.3983265207498334 | 25.597143810392783 | 30.025177792767256 | 55.62232160316004 |
| `zz` | 12 | 1 | 24 | 0.09345908325485652 | 4.704788208247919 | 4.798247291502776 | 87.83458236389804 | 103.02903212032349 | 190.86361448422153 |
| `zz` | 12 | 2 | 36 | 0.10066919775272254 | 7.357923572752043 | 7.458592770504765 | 136.53368432674 | 160.15256143333843 | 296.68624576007846 |
| `zz` | 12 | 3 | 48 | 0.11266686450107954 | 10.654111687501427 | 10.766778552002506 | 197.0918629380459 | 231.1866616860538 | 428.2785246240997 |
| `zz` | 16 | 1 | 32 | 1.0564151562502957 | 65.61640860424814 | 66.67282376049843 | 1220.4830793935685 | 1431.6136879684802 | 2652.096767362049 |
| `zz` | 16 | 2 | 48 | 1.1008739167446038 | 110.5639918645029 | 111.6648657812475 | 2044.0874041622808 | 2397.692812469564 | 4441.780216631845 |
| `zz` | 16 | 3 | 64 | 1.2224377602542518 | 149.67461418749735 | 150.8970519477516 | 2762.25436759912 | 3240.095032100333 | 6002.349399699453 |
| `pauli_z_zz` | 8 | 1 | 16 | 0.01626435400248738 | 0.563500416748866 | 0.5797647707513534 | 10.612916220142829 | 12.448837994188782 | 23.06175421433161 |
| `pauli_z_zz` | 8 | 2 | 24 | 0.01767575000121724 | 0.9273638957456569 | 0.9450396457468742 | 17.299475737421947 | 20.29210128228705 | 37.59157701970899 |
| `pauli_z_zz` | 8 | 3 | 32 | 0.019528604003426153 | 1.3489848749959492 | 1.3685134789993754 | 25.051399518349676 | 29.385025535181033 | 54.43642505353071 |
| `pauli_z_zz` | 12 | 1 | 24 | 0.08551465624623233 | 4.453566989504907 | 4.539081645751139 | 83.09041123750002 | 97.46416978237863 | 180.55458101987864 |
| `pauli_z_zz` | 12 | 2 | 36 | 0.13800558324874146 | 7.387892666753032 | 7.525898250001774 | 137.7657485208658 | 161.5977596458714 | 299.36350816673723 |
| `pauli_z_zz` | 12 | 3 | 48 | 0.12057063524844125 | 11.63389558349445 | 11.754466218742891 | 215.172034393099 | 252.39451075245154 | 467.56654514555055 |
| `pauli_z_zz` | 16 | 1 | 32 | 1.0726530937463394 | 74.50803975000599 | 75.58069284375233 | 1383.5465717786885 | 1622.8854324505708 | 3006.4320042292593 |
| `pauli_z_zz` | 16 | 2 | 48 | 2.0018371354963165 | 144.94461935424624 | 146.94645648974256 | 2689.93652296501 | 3155.2669685158608 | 5845.203491480871 |
| `pauli_z_zz` | 16 | 3 | 64 | 1.8982974062528228 | 215.26668735424755 | 217.16498476050037 | 3975.325693254715 | 4663.014811662966 | 8638.340504917682 |

### Conclusión de viabilidad
A partir de los datos observados, ninguna configuración para $k \ge 12$ cabe dentro de un presupuesto de cómputo razonable. En particular, para $k=16$ y $reps=3$, el tiempo total requerido de entrenamiento alcanza $6002.35$ horas ($\approx 250$ días) para `zz` y $8638.34$ horas ($\approx 360$ días) para `pauli_z_zz`. Incluso para la configuración más pequeña $k=8, reps=1$, se requieren más de $23$ horas completas de cómputo. Por lo tanto, el entrenamiento conjunto bajo la Arquitectura A resulta inalcanzable de manera práctica.

---

## 3. Coste con embedding precomputado (Arquitectura B)

La Arquitectura B propone fijar los parámetros del ansatz $\theta$ mediante una semilla estocástica determinada, transformando la componente cuántica en una proyección de características determinista y fija. Bajo este enfoque, el *embedding* cuántico se evalúa una única vez por muestra durante la fase de extracción de datos, almacenando los vectores resultantes en caché para alimentar posteriormente el clasificador clásico mediante retropropagación convencional.

### Comparativa entre Arquitectura A y Arquitectura B
Los datos provienen del archivo `Code/5_benchmark_arquitectura.csv`.

| k | fwd_ms | arch_A_hours | arch_B_hours | speedup |
| :---: | :---: | :---: | :---: | :---: |
| 8 | 16.46547656309849 | 48.050097878708684 | 0.03263823354285301 | 1472.2027715017225 |
| 12 | 100.51643231236085 | 381.72722896844306 | 0.1992459058280575 | 1915.8598385347038 |
| 16 | 1241.6323906254547 | 5304.193534724098 | 2.461191316528679 | 2155.1325567836207 |

### Análisis de aceleración
El desacoplamiento del gradiente cuántico reduce los tiempos de cómputo sobre el dataset completo desde miles de horas a lapsos sumamente eficientes:
- A $k=8$, la extracción completa se realiza en apenas $0.0326$ horas ($\approx 1.95$ minutos), representando un factor de aceleración (*speedup*) de $1472.20\times$.
- A $k=16$, la extracción requiere $2.4612$ horas ($\approx 2.46$ horas), obteniendo una aceleración de $2155.13\times$ respecto a la Arquitectura A (que exigiría $5304.19$ horas).

---

## 4. Cuello de botella del kernel de fidelidad

El cálculo de la matriz de kernel cuántico de fidelidad se define como:

$$K(x, x') = |\langle \phi(x) | \phi(x') \rangle|^2$$

Para evaluar la separabilidad cuántica y la ventaja geométrica, se requiere la construcción de 4 matrices complejas de kernel (correspondientes a 2 mapas de características $\times$ 2 subconjuntos: masas y calcificaciones), considerando una muestra estandarizada de $N=200$ elementos. La complejidad temporal para evaluar una matriz de pares escala cuadráticamente como $O(N^2)$, con un total de $\frac{N(N-1)}{2}$ pares únicos.

### Mediciones de cómputo empírico para kernels
Los datos provienen del archivo `Code/5_benchmark_kernel.csv`.

| feature_map | k | n_samples | seconds | n_pairs | s_per_pair | diag_ok |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `zz` | 8 | 30 | 5.286911832983606 | 435 | 0.012153820305709438 | True |
| `zz` | 8 | 60 | 22.43924820900429 | 1770 | 0.012677541361019373 | True |
| `zz` | 12 | 30 | 58.64821287500672 | 435 | 0.13482347787357868 | True |
| `zz` | 12 | 60 | 256.67106083297404 | 1770 | 0.14501189877569154 | True |
| `zz` | 16 | 30 | 830.0090601249831 | 435 | 1.9080668048850187 | True |
| `zz` | 16 | 60 | 3110.444323374977 | 1770 | 1.7573131770480097 | True |
| `pauli_z_zz` | 8 | 30 | 4.719015541020781 | 435 | 0.01084831158855352 | True |
| `pauli_z_zz` | 8 | 60 | 19.357756042008987 | 1770 | 0.010936585334468354 | True |
| `pauli_z_zz` | 12 | 30 | 47.324695792020066 | 435 | 0.10879240411958636 | True |
| `pauli_z_zz` | 12 | 60 | 191.96328712499235 | 1770 | 0.10845383453389398 | True |
| `pauli_z_zz` | 16 | 30 | 717.7259991659957 | 435 | 1.6499448256689557 | True |
| `pauli_z_zz` | 16 | 60 | 3011.634112208005 | 1770 | 1.7014881989875734 | True |

### Proyección de tiempo para tamaños de muestra extendidos ($N=150$ y $N=200$)
Los datos provienen del archivo `Code/5_benchmark_kernel_proyeccion.csv`.

| feature_map | k | n_samples | projected_s |
| :--- | :---: | :---: | :---: |
| `pauli_z_zz` | 8 | 150 | 121.72311155738471 |
| `pauli_z_zz` | 8 | 200 | 216.7597243840676 |
| `pauli_z_zz` | 12 | 150 | 1213.8633584763215 |
| `pauli_z_zz` | 12 | 200 | 2161.6000746021296 |
| `pauli_z_zz` | 16 | 150 | 18726.132025268358 |
| `pauli_z_zz` | 16 | 200 | 33346.75859533247 |
| `zz` | 8 | 150 | 138.74523331284723 |
| `zz` | 8 | 200 | 247.0720485839517 |
| `zz` | 12 | 150 | 1563.5801670277974 |
| `zz` | 12 | 200 | 2784.3619976602386 |
| `zz` | 16 | 150 | 20480.310649050793 |
| `zz` | 16 | 200 | 36470.53082023363 |

### Evaluación del cuello de botella
Para una muestra de $N=200$, la construcción de una sola matriz de kernel para $k=16$ requiere $36470.53$ segundos ($\approx 10.13$ horas) con `zz` y $33346.76$ segundos ($\approx 9.26$ horas) con `pauli_z_zz`. Multiplicado por las 4 matrices necesarias, la computación del kernel de fidelidad insumiría más de $38.7$ horas dedicadas exclusivamente al cómputo matricial. Este cuello de botella vuelve impracticable el uso de $k=16$ para el análisis de kernel, incluso bajo los supuestos de la Arquitectura B.

---

## 5. Equivalencia de las condiciones C4 y C5

> **Nota de origen:** Las determinaciones reportadas en esta sección provienen de verificaciones puntuales independientes y no forman parte de los archivos CSV del benchmark.

### Demostración empírica de identidad entre mapas de características
En el marco de Qiskit, la declaración de un mapa de características Pauli utilizando `pauli_feature_map(paulis=['Z','ZZ'])` (asociado a la condición C5) produce exactamente el mismo estado cuántico vectorizado que la instanciación directa de `zz_feature_map` (asociado a la condición C4).

La fidelidad cuántica entre los estados generados:

$$\mathcal{F} = |\langle \phi_{zz}(x) | \phi_{pauli\_z\_zz}(x) \rangle|^2 = 1.000000000000$$

fue verificada numéricamente de manera puntual para $k=4$ y $k=8$, obteniéndose una identidad perfecta en la amplitud de probabilidad de cada vector de estado.

### Evidencia concurrente en el benchmark de complejidad
Como evidencia concurrente derivada de los datos medidos en el proyecto, las 18 filas del archivo `Code/5_benchmark_complejidad.csv` son absolutamente idénticas punto a punto entre `zz` y `pauli_z_zz` en sus métricas de `depth_raw` (50–112), `depth_transpiled` (58–126), `n_cx` (63–285) y `n_gates` (187–725).

### Implicación metodológica
Tal como están especificadas originalmente en el protocolo de pruebas, C4 y C5 constituyen una única y misma condición experimental. 

### Verificación de alternativas de Pauli con igual costo de CX
Se evaluaron construcciones de mapas de características Pauli alternativas manteniendo la misma cantidad de puertas de control CX ($n_{cx}$), midiendo la fidelidad resultante frente a `ZZFeatureMap`:
- `['Z', 'Y', 'ZZ']`: Fidelidad $= 0.000000000000$ contra ZZ.
- `['X', 'ZZ']`: Fidelidad $= 0.000000000000$ contra ZZ.
- `['Z', 'YY']`: Fidelidad $= 0.356000000000$ contra ZZ.

---

## 6. El ansatz es necesario

> **Nota de origen:** Las determinaciones reportadas en esta sección provienen de verificaciones puntuales independientes y no forman parte de los archivos CSV del benchmark.

### Comportamiento del mapa de características sin ansatz
El mapa de características `ZZFeatureMap` aplica exclusivamente una capa inicial de puertas Hadamard $H^{\otimes k}$ seguida de puertas diagonales compuestas por rotaciones de fase $R_Z$ y bloques entrelazadores diagonales $CX-R_Z-CX$. Puesto que todas las puertas posteriores a la capa Hadamard inicial son representables por matrices diagonales en la base computacional $Z$:

$$U_{\text{diag}} |x\rangle = e^{i \theta(x)} |x\rangle$$

estas alteran las fases complejas del estado pero mantienen inalterados los módulos de las amplitudes. Al partir del estado de superposición uniforme $H^{\otimes k}|0\rangle = \frac{1}{\sqrt{2^k}} \sum_{z \in \{0,1\}^k} |z\rangle$, la magnitud de cada amplitud se preserva rigurosamente en $2^{-k/2}$.

### Inobservabilidad en la base Z
Al realizar la medición en la base computacional $Z$, la probabilidad marginal de medir cero en cualquier qubit $i$ satisface:

$$P(\text{qubit}_i = 0) = \frac{1}{2}$$

lo que conduce a un valor esperado del observable $Z_i$ de:

$$\langle Z_i \rangle = P(\text{qubit}_i = 0) - P(\text{qubit}_i = 1) = 0$$

para todo vector de entrada $x$, resultado comprobado empírica y numéricamente.

Por lo tanto, la proyección del mapa de características sin un ansatz variacional carece por completo de información discriminativa si se mide en la base computacional $Z$, ya que toda la información codificada reside exclusivamente en las fases complejas y la medición en $Z$ es ciega a dichas fases.

### Consecuencia metodológica para la Arquitectura B
En la Arquitectura B, para extraer un *embedding* vectorial útil $\langle Z_i \rangle \in [-1, 1]^k$, los parámetros $\theta$ del ansatz variacional no deben eliminarse ni declararse ausentes. En su lugar, el ansatz debe incluirse con sus parámetros $\theta$ manteniendo un valor **FIJO** mediante una semilla aleatoria declarada. Las rotaciones $R_Y(\theta)$ del ansatz rotan la base de medición, proyectando las diferencias de fase a diferencias de población observables en $Z$. Por otra parte, el cálculo del kernel de fidelidad $K(x, x') = |\langle \phi(x) | \phi(x') \rangle|^2$ no sufre de esta limitación debido a que compara directamente los vectores de estado completos en el espacio de Hilbert.

---

## 7. Sensibilidad al número de shots

Para evaluar el impacto del ruido de muestreo numérico (*shot noise*) en la aproximación de los valores esperados de los observables, se evaluó la discrepancia del estimador estocástico frente al cálculo analítico exacto mediante *statevector*.

### Datos de precisión según disparos (shots)
Los datos provienen del archivo `Code/5_benchmark_shots.csv`.

| shots | mae | max_err | fwd_per_sample_s |
| :---: | :---: | :---: | :---: |
| 512 | 0.036927172305733884 | 0.1399256166365689 | 0.00367616150106187 |
| 1024 | 0.029234175402886586 | 0.10111231557339835 | 0.003635312499682186 |
| 2048 | 0.022456292071820618 | 0.09565759256062438 | 0.0035644583749672165 |
| 4096 | 0.0173911961782176 | 0.07109411078715952 | 0.0035777161247096956 |
| 8192 | 0.013870435579419173 | 0.0489699691167058 | 0.0036275234360800823 |

### Análisis de convergencia estocástica
- A 512 disparos, el error absoluto medio (MAE) es de $0.0369$ con un error máximo de $0.1399$.
- A 8192 disparos, el MAE se reduce a $0.0139$ con un error máximo de $0.0490$.

La pendiente log-log medida experimentalmente entre el número de disparos y el MAE es de $-0.357$. Esta cifra presenta una discrepancia frente a la pendiente teórica de $-0.500$ derivada del teorema del límite central y la cota $O(1/\sqrt{\text{shots}})$. 

La razón de esta desviación reside en que cada punto experimental del benchmark representa una única corrida estocástica individual. Para publicaciones o reportes académicos formalmente citables, se recomienda promediar un mínimo de 10 repeticiones independientes por cada valor de disparos.

---

## 8. Optimización sin gradiente

> **Nota de origen:** Las determinaciones reportadas en esta sección provienen de verificaciones puntuales independientes y no forman parte de los archivos CSV del benchmark.

### Evaluación del algoritmo Particle Swarm Optimization (PSO)
Se analizó la factibilidad de emplear optimización sin gradientes mediante el algoritmo de enjambre de partículas (PSO) como alternativa al esquema de gradientes por *parameter-shift*.

El costo computacional por iteración en PSO viene dado por:

$$\text{Costo}_{\text{iteración}} = N_{\text{partículas}} \times \text{Costo}_{\text{forward}}(\text{dataset})$$

### Resultados comparativos
1. **Configuración sobre dataset completo (30 partículas, 200 iteraciones):** La evaluación completa del enjambre sobre la totalidad de las muestras arroja un tiempo de cómputo y convergencia global **PEOR** que el entrenamiento por *parameter-shift*.
2. **Configuración en mini-lotes (128 muestras):** La incorporación de mini-lotes aleatorios de 128 muestras reduce el tiempo de ejecución aproximadamente $5$ veces. Sin embargo, la velocidad global se mantiene un orden de magnitud por debajo de la alternativa de fijar $\theta$ previamente (Arquitectura B sin entrenamiento de ansatz).

### Persistencia del fenómeno de mesetas áridas (Barren Plateaus)
Los métodos de optimización libres de gradiente no logran evadir el problema de las mesetas áridas (*barren plateaus*). Cuando la superficie del paisaje de costo sufre de una meseta árida, las diferencias de costo entre las distintas partículas del enjambre se vuelven exponencialmente pequeñas en función del número de qubits:

$$\text{Var}_\theta [\Delta C] \in O(2^{-k})$$

por lo que las fuerzas de atracción hacia el mejor global $g^*$ y mejor individual $p_i^*$ se anulan debido a la falta de pendiente utilizable.

*Referencia bibliográfica:* **PENDIENTE DE VERIFICAR:** Arrasmith, A., Cerezo, M., Czarnik, P., Cincio, L., & Coles, P. J. (2021). "Effect of barren plateaus on gradient-free optimization". *Quantum*, 5, 558.

### Valor único y nicho de aplicación de PSO
A pesar de su desventaja en velocidad frente a la fijación de parámetros, el valor único del algoritmo PSO reside en su capacidad para optimizar funciones de costo no diferenciables o no analíticas en el circuito cuántico, tales como la maximización directa del Área Bajo la Curva ROC (AUC-ROC), el alineamiento de kernel centrado (KTA) o la razón de discriminación de Fisher.
