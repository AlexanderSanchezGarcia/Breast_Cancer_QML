# Informe T1 · Grupo D: Fundamentos citados en el reporte

- **Trabajador:** Dispatch `ctx_1411714dcf61` (Task `task_f06837108dfe`, Terminal `term_10e826f6-5f39-4e03-b7cd-44b5999e2dca`)
- **Grupo asignado:** Grupo D (8 obras de fundamentos citados en el reporte técnico y bitácora)
- **Fecha:** 2026-10-14
- **Repositorio:** `/Users/alexander_san/TT`

---

## 1. Resumen ejecutivo

Se completaron las 8 fichas de lectura asignadas al Grupo D en `Docs/insumos/fichas/`, siguiendo rigurosamente el formato estándar de `Docs/insumos/noche/T1_fichas.md` y las reglas éticas y metodológicas de `Docs/insumos/noche/reglas.md`. Se verificaron de forma literal 108 citas textuales en el idioma original contra las páginas correspondientes de los archivos de texto extraídos de los PDF en `Docs/fuentes/txt/<Clave>/`. La prueba automatizada de aceptación `python3 Code/tools/verificar_citas_fichas.py` se ejecutó satisfactoriamente para todas y cada una de las 8 fichas, alcanzando un 100 % de éxito sin fallos ni discrepancias textuales.

---

## 2. Archivos creados y modificados

Se crearon exclusivamente los 8 archivos de fichas asignados y el presente informe:

1. `Docs/insumos/fichas/Mari2020Transfer.md` (12 citas verificadas)
2. `Docs/insumos/fichas/Lee2017CBISDDSM.md` (20 citas verificadas)
3. `Docs/insumos/fichas/Preskill2018NISQ.md` (17 citas verificadas)
4. `Docs/insumos/fichas/McClean2018Barren.md` (13 citas verificadas)
5. `Docs/insumos/fichas/Schuld2021Encoding.md` (10 citas verificadas)
6. `Docs/insumos/fichas/Hubregtsen2022.md` (10 citas verificadas)
7. `Docs/insumos/fichas/Guyon2003.md` (14 citas verificadas)
8. `Docs/insumos/fichas/Zwanenburg2020IBSI.md` (12 citas verificadas)
9. `Docs/insumos/noche/informe_T1_D.md` (Informe final del Grupo D)

*Nota de propiedad:* No se modificó ningún archivo fuera de los asignados (no se editó `Docs/Technical_Report.tex`, `Docs/Technical_Report.bib`, `CLAUDE.md`, `Other/bitacora_decisiones.md`, notebooks ni archivos bajo `Data/`). No se realizaron operaciones de git.

---

## 3. Salida de las pruebas de aceptación

Ejecución del script canónico `python3 Code/tools/verificar_citas_fichas.py`:

```
$ python3 Code/tools/verificar_citas_fichas.py Docs/insumos/fichas/Mari2020Transfer.md Docs/insumos/fichas/Lee2017CBISDDSM.md Docs/insumos/fichas/Preskill2018NISQ.md Docs/insumos/fichas/McClean2018Barren.md Docs/insumos/fichas/Schuld2021Encoding.md Docs/insumos/fichas/Hubregtsen2022.md Docs/insumos/fichas/Guyon2003.md Docs/insumos/fichas/Zwanenburg2020IBSI.md
Mari2020Transfer.md: OK · 12/12 citas verificadas
Lee2017CBISDDSM.md: OK · 20/20 citas verificadas
Preskill2018NISQ.md: OK · 17/17 citas verificadas
McClean2018Barren.md: OK · 13/13 citas verificadas
Schuld2021Encoding.md: OK · 10/10 citas verificadas
Hubregtsen2022.md: OK · 10/10 citas verificadas
Guyon2003.md: OK · 14/14 citas verificadas
Zwanenburg2020IBSI.md: OK · 12/12 citas verificadas

8/8 fichas pasan.
```

Total general en las fichas del Grupo D: **108 citas verificadas exitosamente sobre 108 citas declaradas (100 %)**. Asimismo, al ejecutar `python3 Code/tools/verificar_citas_fichas.py` sin argumentos, pasan las 24/24 fichas existentes en el repositorio.

---

## 4. Tabla de discrepancias y hallazgos críticos

A continuación se resume el contraste detallado entre lo que el proyecto atribuye a cada obra y lo que la fuente declara literalmente:

| Clave | Atribución previa del proyecto / Ubicación | Qué dice realmente la fuente (con cita) | Veredicto | Acción recomendada para el autor |
|---|---|---|---|---|
| `Mari2020Transfer` | `Docs/Technical_Report.tex:561-564` contiene la descripción casi textual: "la red cuántica completa ... mapea un espacio vectorial clásico a otro ... funcionalmente análoga a una red clásica profunda", pero **sin cita bibliográfica**. | En p. 3: «The full network is a map from a classical vector space to a classical vector space depending on classical weights. Therefore, even though it may contain a quantum computation hidden in the quantum circuit, if considered from a global point of view, Q is simply a black-box analogous to the classical deep network deﬁned in Eq. (2).» (Mari2020Transfer, p. 3). | **Sí**, la fuente sostiene la afirmación palabra por palabra, pero falta la cita formal. | Añadir la cita `\cite{Mari2020Transfer}` en `Docs/Technical_Report.tex:564`. Calibrar que su comparador clásico fue solo un «presented just as a qualitative benchmark» (Mari2020Transfer, p. 6) y no prueba de ventaja cuántica. |
| `Lee2017CBISDDSM` | `Docs/Technical_Report.tex:622` y `2583` afirma "Sus 1,566 participantes, partición train/test por categoría BI-RADS...". | En p. 5: «The data were split into a training set and a testing set based on the BI-RADS category.» (Lee2017CBISDDSM, p. 5) (20 % test, 80 % train). En p. 1 y Tabla 3: reporta **753 casos de calcificaciones y 891 de masas (total 1\,644 casos)**. La cifra de **1\,566 participantes no aparece** en el texto del artículo de Lee et al. | **Parcial**. La partición estratificada por BI-RADS sí la sostiene. La cifra de 1\,566 participantes es del repositorio TCIA (`bitacora_decisiones.md:957`), no del artículo. | Aclarar en el reporte que 1\,644 son los casos de patología reportados por Lee et al. (2017) y que 1\,566 es el número de sujetos únicos (`PatientID`) alojados en TCIA. |
| `Lee2017CBISDDSM` | `Docs/Technical_Report.tex:817` refiere a la licencia como "CC BY 3.0". | El artículo en *Scientific Data* está bajo **CC BY 4.0** («Open Access This article is licensed under a Creative Commons Attribution 4.0 International License» (Lee2017CBISDDSM, p. 9)). Los archivos de TCIA se distribuyen bajo **CC BY 3.0**. | **Sí / Precisión**. | Mantener CC BY 3.0 para el conjunto de datos de TCIA y citar CC BY 4.0 si se refiere al artículo *Data Descriptor*. |
| `Preskill2018NISQ` | `Docs/Technical_Report.tex:684, 762` define NISQ (50 a cientos de qubits ruidosos sin corrección de errores). | «Noisy Intermediate-Scale Quantum (NISQ) technology will be available in the near future.» (Preskill2018NISQ, p. 1); «we cannot be nearly so conﬁdent about the commercial potential of quantum technology in the near term, say the next ﬁve to ten years» (Preskill2018NISQ, p. 1); «NISQ is not likely to change the world all by itself.» (Preskill2018NISQ, p. 15). | **Sí**. Sostiene plenamente la definición. | Mantener el tono calibrado del reporte: Preskill advierte explícitamente que la ventaja cuántica práctica a corto plazo es incierta y que muchos algoritmos de QML son demasiado costosos para NISQ. |
| `McClean2018Barren` | `Docs/Technical_Report.tex:786-788` describe el decaimiento exponencial del gradiente con la profundidad y qubits en VQC. | «the probability that the gradient along any reasonable direction is non-zero to some ﬁxed precision is exponentially small as a function of the number of qubits» (McClean2018Barren, p. 1). Ocurre cuando subcircuitos forman un **2-diseño unitario** (segundo momento de Haar) a profundidad modesta $O(n^{1/d})$. La estimación requiere mediciones crecientes, haciendo que el descenso de gradiente degenere en una caminata aleatoria. | **Sí**. Sostiene plenamente la limitación teórica. | Reforzar en §2.1.4 que las mesetas áridas ocurren por concentración de medida (lema de Lévy) en cuanto se alcanza un 2-diseño unitario, justificando el uso de circuitos cortos de 1 y 2 repeticiones. |
| `Schuld2021Encoding` | `Other/verificacion/referencias_por_revisar.md:70` atribuye a Schuld et al. explicar los VQC como series de Fourier y fundamentar el escalado angular a $[0, \pi]$. | En p. 1: «We show that one can naturally write a quantum model as a partial Fourier series in the data, where the accessible frequencies are determined by the nature of the data encoding gates in the circuit.» (Schuld2021Encoding, p. 1). En p. 4: el espectro de frecuencias $\Omega$ depende exclusivamente de los autovalores de los hamiltonianos de codificación. En p. 10: exige reescalado de datos para acotarlos al periodo de las funciones aprendibles: «Quantum models naturally learn periodic functions in the data. One should therefore consider appropriate data re-scaling strategies, to make sure the data lies within the period of the function class.» (Schuld2021Encoding, p. 10). | **Sí**. Sostiene plenamente la formulación de series de Fourier y el reescalado angular. | Incorporar la cita formal `\cite{Schuld2021Encoding}` en §1.1.2 y §5.4 para respaldar teóricamente el escalado angular al rango $[0, \pi]$ (D-004). |
| `Hubregtsen2022` | `Other/verificacion/referencias_por_revisar.md:71` y bitácora (H-044, X6) plantean kernels cuánticos entrenables con KTA como trabajo futuro. | Define QEK entrenables mediante KTA: «We focus on quantum embedding kernels with variational parameters. These variational parameters are optimized for a given dataset by increasing the kernel-target alignment, a heuristic connected to the achievable classiﬁcation accuracy.» (Hubregtsen2022, p. 1). Advierten del costo computacional cuadrático $O(N^2)$ (p. 2) y la posibilidad de *barren plateaus* en el entrenamiento del kernel (p. 13). | **Sí**. Sostiene el marco metodológico de QEK y optimización por KTA. | Citar en §1.2 y en las perspectivas de trabajo futuro como el antecedente directo de optimización de *feature maps* guiada por KTA. |
| `Guyon2003` | `Other/bitacora_decisiones.md:1681` (H-030) explica por qué 12 características radiómicas elegidas por F no superan a 12 al azar. | «methods that score variables individually and independently of each other are at loss to determine which combination of variables would give best performance.» (Guyon2003, p. 9); «By itself one variable is “useless”. Still, the two dimensional separation is better than the separation using the “useful” variable alone. Therefore, a variable that is completely useless by itself can provide a signiﬁcant performance improvement when taken with others.» (Guyon2003, p. 9); «Two variables that are useless by themselves can be useful together.» (Guyon2003, p. 9). | **Sí**. Sostiene plenamente la insuficiencia del filtrado univariante frente a interacciones multivariadas. | Citar a Guyon & Elisseeff (2003) en la discusión de resultados de selección de características radiómicas para fundamentar por qué ANOVA F-value (`SelectKBest`) no supera a una muestra aleatoria diversa. |
| `Zwanenburg2020IBSI` | `Other/bitacora_decisiones.md:186` y `1425` justifica D-008 (`binCount=32`) por tener intensidades arbitrarias no calibradas. | En el manual de referencia (p. 24): «However, it introduces a normalising eﬀect which may be beneﬁcial when intensity units are arbitrary (e.g. raw MRI data and many spatial ﬁlters), and where contrast is considered important.» (Zwanenburg2020IBSI, p. 24). En p. 25: «When the re-segmentation range is not or cannot be deﬁned (e.g. arbitrary intensity units), the use of the FBS algorithm is not recommended.» (Zwanenburg2020IBSI, p. 25). | **Sí plenamente**. El manual de IBSI proscribe el ancho fijo (FBS) y recomienda número fijo (FBN) para intensidades arbitrarias. | Citar el manual de referencia de IBSI en §5.3 para respaldar normativamente la configuración de `binCount=32` frente a opciones de `binWidth`. |

---

## 5. Preguntas específicas respondidas por obra

1. **Mari2020Transfer:**
   - *Dressed quantum circuit:* Circuito cuántico variacional parametrizado acoplado a dos capas clásicas entrenables: $\tilde{Q} = L_{n_q \to n_{out}} \circ Q \circ L_{n_{in} \to n_q}$ (p. 3). La primera capa realiza la adaptación dimensional de entrada clásica a los $n_q$ qubits, y la capa final mapea los valores esperados medidos hacia el espacio de salida.
   - *Frase en §1.1.3 de Technical_Report.tex:* La frase en líneas 561–564 ("la red cuántica completa, incluyendo la capa de embedding inicial y la medición final, mapea un espacio vectorial clásico a otro espacio vectorial clásico dependiente de pesos clásicos, y aunque contiene un cómputo cuántico oculto en el circuito cuántico, es funcionalmente análoga a una red clásica profunda") es traducción directa y literal de Mari et al. (2020), p. 3 («The full network is a map from a classical vector space to a classical vector space depending on classical weights. Therefore, even though it may contain a quantum computation hidden in the quantum circuit, if considered from a global point of view, Q is simply a black-box analogous to the classical deep network deﬁned in Eq. (2).» (Mari2020Transfer, p. 3)).

2. **Lee2017CBISDDSM:**
   - *Número de casos/estudios:* DDSM original: 2\,620 estudios escaneados (p. 2). CBIS-DDSM: 753 casos de calcificaciones y 891 casos de masas (1\,644 casos en total, 2\,015 anormalidades en Tabla 3, p. 7). La cifra de 1\,566 participantes no aparece en el texto del artículo; es el conteo de `PatientID` únicos del repositorio TCIA. Se excluyeron 339 imágenes de masas dudosas (p. 4).
   - *Construcción de ROI:* Masas mediante contornos activos deformables (*level sets* locales modificados a partir de Chan-Vese, p. 4) validados con 118 casos por radiólogo experto (Dice 0.792 vs 0.398 original). Calcificaciones conservaron las anotaciones curadas del DDSM (no se aplicó level set, p. 4). Recortes generados con rectángulos envolventes.
   - *Partición train/test:* Sí está estratificada por categoría BI-RADS («The data were split into a training set and a testing set based on the BI-RADS category.» (Lee2017CBISDDSM, p. 5)) y dividida en 80 % train y 20 % test independientemente para masas y calcificaciones.
   - *Licencia:* Artículo en *Scientific Data* bajo CC BY 4.0 («Open Access This article is licensed under a Creative Commons Attribution 4.0 International License» (Lee2017CBISDDSM, p. 9)); datos en TCIA bajo CC BY 3.0.

3. **Preskill2018NISQ:**
   - *Definición de NISQ y rango de qubits:* «Noisy Intermediate-Scale Quantum (NISQ) technology will be available in the near future.» (Preskill2018NISQ, p. 1). Rango de 50 a cientos de qubits con el hito de 50 qubits por superar la simulación clásica directa por fuerza bruta («50 qubits is a signiﬁcant milestone, because that’s beyond what can be simulated by brute force using the most powerful existing digital supercomputers.» (Preskill2018NISQ, p. 5)). Compuertas ruidosas no protegidas por corrección de errores («When I speak of the NISQ era, I’m imagining quantum computers with noisy gates unprotected by quantum error correction.» (Preskill2018NISQ, p. 5)).
   - *Ventaja a corto plazo:* Preskill concluye que la ventaja práctica a corto plazo es incierta («Perhaps NISQ will allow us to speed up the time to solution for problems of broad interest in the near future, but we don’t know yet whether that will happen.» (Preskill2018NISQ, p. 15)), que no hay certidumbre comercial para los próximos 5 a 10 años («we cannot be nearly so conﬁdent about the commercial potential of quantum technology in the near term, say the next ﬁve to ten years» (Preskill2018NISQ, p. 1)), y que «NISQ is not likely to change the world all by itself.» (Preskill2018NISQ, p. 15).

4. **McClean2018Barren:**
   - *Enunciado del barren plateau:* El valor esperado del gradiente de la función objetivo respecto a los parámetros angulares es cero en promedio y su varianza decae exponencialmente con el número de qubits $n$. Como consecuencia de la concentración de medida (lema de Lévy), la probabilidad de que el gradiente supere un umbral fijo $\epsilon$ es exponencialmente pequeña: «Speciﬁcally, we show that for a wide class of reasonable parameterized quantum circuits, the probability that the gradient along any reasonable direction is non-zero to some ﬁxed precision is exponentially small as a function of the number of qubits.» (McClean2018Barren, p. 1).
   - *Condiciones:* Ansätze aleatorios parametrizados (RPQC) de profundidad suficiente para que el bloque anterior o posterior forme un 2-diseño unitario respecto a la medida de Haar: «As a result, if a circuit is of suﬃcient depth such that for any ∂kE, either U−or U+ forms a 2-design, then with high probability one will produce an ansatz state on a barren plateau of the quantum landscape, with no interesting search directions in sight.» (McClean2018Barren, p. 3). La profundidad requerida es modesta: $O(n^{1/d})$ en arreglos espaciales $d$-dimensionales.

5. **Schuld2021Encoding:**
   - *Series de Fourier:* Todo modelo cuántico variacional con codificación generada por hamiltonianos $e^{-ixH}$ se escribe como una serie parcial de Fourier: «We show that one can naturally write a quantum model as a partial Fourier series in the data, where the accessible frequencies are determined by the nature of the data encoding gates in the circuit.» (Schuld2021Encoding, p. 1).
   - *Qué determina el espectro de frecuencias:* El espectro de frecuencias $\Omega = \{\Lambda_k - \Lambda_j\}$ está gobernado de forma exclusiva por las diferencias entre sumas de autovalores de los hamiltonianos de codificación: «As a consequence, a quantum model’s frequency spectrum is solely determined by the eigenvalues of the data encoding gates, while its Fourier coeﬃcients depend on the entire circuit, as was claimed in Fig. 1.» (Schuld2021Encoding, p. 4). Codificar una vez con una rotación de Pauli da grado 1 (un solo seno); repetir la compuerta $L$ veces extiende el espectro a grado $L$.

6. **Hubregtsen2022:**
   - *Quantum embedding kernels entrenables:* Circuitos de feature map parametrizados $U(x, \theta)$ cuyos parámetros libres $\theta$ se optimizan para una tarea concreta antes de calcular el kernel de solapamiento: «We focus on quantum embedding kernels with variational parameters. These variational parameters are optimized for a given dataset by increasing the kernel-target alignment, a heuristic connected to the achievable classiﬁcation accuracy.» (Hubregtsen2022, p. 1).
   - *Entrenamiento con KTA:* Maximización del alineamiento angular en un ciclo híbrido clásico-cuántico: «With the kernel-target alignment we now have a measure that we can use as a cost function to maximize through a hybrid quantum-classical optimization loop [43].» (Hubregtsen2022, p. 6), aproximando la matriz de kernel a la matriz objetivo ideal $K^* = y y^T$.

7. **Guyon2003:**
   - *Selección univariante:* El filtrado univariante evalúa variables de forma aislada y no puede determinar combinaciones óptimas: «methods that score variables individually and independently of each other are at loss to determine which combination of variables would give best performance.» (Guyon2003, p. 9).
   - *Variables inútiles solas pero útiles juntas:* «By itself one variable is “useless”. Still, the two dimensional separation is better than the separation using the “useful” variable alone. Therefore, a variable that is completely useless by itself can provide a signiﬁcant performance improvement when taken with others.» (Guyon2003, p. 9) y «Two variables that are useless by themselves can be useful together.» (Guyon2003, p. 9).
   - *Conexión con H-030:* Explica por qué `SelectKBest` con estadístico F no supera a variables elegidas al azar en las características radiómicas del CBIS-DDSM: ignora redundancias e interacciones multivariadas.

8. **Zwanenburg2020IBSI:**
   - *Manual vs artículo:* Todas las citas corresponden al **manual de referencia técnico de IBSI** (178 pp., arXiv:1612.07003v11).
   - *Recomendación de discretización:* Para modalidades con **intensidades arbitrarias no calibradas** (como mamografía escaneada o resonancia magnética cruda), IBSI **recomienda número fijo de bins (FBN)** debido a su efecto normalizador: «However, it introduces a normalising eﬀect which may be beneﬁcial when intensity units are arbitrary (e.g. raw MRI data and many spatial ﬁlters), and where contrast is considered important.» (Zwanenburg2020IBSI, p. 24) y **desaconseja expresamente ancho fijo de bin (FBS)**: «When the re-segmentation range is not or cannot be deﬁned (e.g. arbitrary intensity units), the use of the FBS algorithm is not recommended.» (Zwanenburg2020IBSI, p. 25). Esto valida formalmente la decisión D-008 (`binCount=32`).

---

## 6. Estado de pendientes y verificaciones

- **Marcadores `[VERIFICAR]` dejados:** Cero. Todas las afirmaciones, cifras, citas y números de página fueron contrastados contra los archivos de texto fuente y validados por el verificador automatizado.
- **Limitaciones o tareas pendientes:** Ninguna para el Grupo D. El trabajo asignado está completamente terminado y listo para su consumo por el coordinador y el autor.
