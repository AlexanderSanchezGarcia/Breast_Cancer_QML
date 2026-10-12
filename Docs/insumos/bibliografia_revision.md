# Revisión bibliográfica — TT 2026-B039 (Technical_Report.tex)

Insumo para el autor. **No se editó** `Docs/Technical_Report.tex` ni `Docs/Technical_Report.bib`. Las entradas propuestas están en [`bibitems_nuevos.tex`](bibitems_nuevos.tex); las respuestas crudas, en `Docs/insumos/fuentes_bib/`. Los números de línea se refieren a `Docs/Technical_Report.tex` tal como estaba el 2026-10-11 (3870 líneas; `\begin{thebibliography}{99}` en la línea 3595).

Criterio de formato: se imitó el estilo APA del reporte (autores «Apellido, I.», año entre paréntesis, título en minúsculas tipo oración, revista en `\textit`, volumen(número), páginas con `--` o número de artículo, `\url{https://doi.org/...}`). El paso del título a minúsculas tipo oración es el único cambio de forma respecto a la fuente; las palabras, los autores y los números se copiaron de la respuesta cruda.

---

## 1. Tabla por entrada

| # | Clave | DOI o URL | Archivo crudo | Discrepancias con la lista del encargo / notas |
|---|---|---|---|---|
| a | `TandFOnline2021` | 10.1080/08839514.2021.2001177 | `Docs/insumos/fuentes_bib/TandFOnline2021.json` | Sin discrepancias con la lista (Zebari et al., 2021). **Contra la plantilla actual del reporte (líneas 3701–3703)**: la plantilla dice `\textit{AI Magazine}, 42(4)`, pero Crossref da *Applied Artificial Intelligence*, 35(15), 2157–2203. Título: «Systematic Review of Computing Approaches for Breast Cancer Detection Based Computer Aided Diagnosis Using Mammogram Images». 7 autores. Publicada en línea el 2021-12-02 (impresa 2021-12-15). |
| b | `Bray2024GLOBOCAN` | 10.3322/caac.21834 | `Docs/insumos/fuentes_bib/Bray2024GLOBOCAN.json` | Sin discrepancias. *CA: A Cancer Journal for Clinicians*, 74(3), 229–263; 7 autores. |
| c | `huang2021power` | 10.1038/s41467-021-22539-9 | `Docs/insumos/fuentes_bib/huang2021power.json` | Sin discrepancias con la lista. **Comparado con el `\bibitem{huang2021power}` actual (líneas 3843–3846)**: los 7 autores, sus iniciales, el título, la revista, el volumen 12, el artículo 2631, el año y el DOI coinciden. La única diferencia es que Crossref da número (issue) 1; la entrada nueva escribe `12(1), 2631`. Se puede dejar la actual tal cual (es correcta) o usar la nueva para incluir el número. |
| d | `Cortes2012` | https://jmlr.org/papers/v13/cortes12a.html (sin DOI) | `Docs/insumos/fuentes_bib/Cortes2012.html` (+ `Cortes2012.bib`, BibTeX oficial de jmlr.org) | Sin discrepancias. La página da además el número `13(28)` (`citation_issue` = 28; `number = {28}` en el BibTeX oficial), que se incluyó. |
| e | `Cristianini2001` | https://proceedings.neurips.cc/paper/2001/hash/1f71e393b3809197ed66df836fe833e5-Abstract.html (sin DOI) | `Docs/insumos/fuentes_bib/Cristianini2001.html` (+ `Cristianini2001.bib` y `Cristianini2001_metadata.json`, oficiales de proceedings.neurips.cc) | Sin discrepancias con la lista. Año 2001 («Advances in Neural Information Processing Systems 14 (NIPS 2001)»); editores T. Dietterich, S. Becker y Z. Ghahramani; MIT Press (BibTeX oficial); páginas 367–373 (`Metadata.json`). Nota: el texto visible de la página escribe «Jaz S. Kandola», pero las etiquetas meta y el BibTeX dicen «Kandola, Jaz»; se usó «Kandola, J.». **Duplicado probable**: el reporte ya tiene `\bibitem{cristianini2002kernel}` (líneas 3801–3804), la misma obra con año 2002 y sin editores ni páginas; se cita en la línea 1728. El autor debe quedarse con una sola de las dos claves. |
| f | `Thanasilp2024` | 10.1038/s41467-024-49287-w | `Docs/insumos/fuentes_bib/Thanasilp2024.json` | Sin discrepancias. Título: «Exponential concentration in quantum kernel methods»; autores Thanasilp, S., Wang, S., Cerezo, M., Holmes, Z.; 15(1), 5200; 2024. |
| g | `Schuld2021Encoding` | 10.1103/PhysRevA.103.032430 | `Docs/insumos/fuentes_bib/Schuld2021Encoding.json` | Sin discrepancias. Número 3. (Crossref devuelve el DOI en minúsculas, `physreva`; los DOI no distinguen mayúsculas.) |
| h | `Liu2021Speedup` | 10.1038/s41567-021-01287-z | `Docs/insumos/fuentes_bib/Liu2021Speedup.json` | Sin discrepancias. Número 9. |
| i | `Glick2024Covariant` | 10.1038/s41567-023-02340-9 | `Docs/insumos/fuentes_bib/Glick2024Covariant.json` | Sin discrepancias. 7 autores (Glick, Gujarati, Córcoles, Kim, Kandala, Gambetta, Temme); número 3; publicada en línea el 2024-01-19. |
| j | `Huang2022Experiments` | 10.1126/science.abn7293 | `Docs/insumos/fuentes_bib/Huang2022Experiments.json` | Sin discrepancias. 11 autores; número 6598; 2022. |
| k | `Hubregtsen2022` | 10.1103/PhysRevA.106.042431 | `Docs/insumos/fuentes_bib/Hubregtsen2022.json` | Sin discrepancias. 6 autores; número 4; 2022. |
| l | `Guyon2003` | https://jmlr.org/papers/v3/guyon03a.html (sin DOI) | `Docs/insumos/fuentes_bib/Guyon2003.html` | Sin discrepancias. La página da `3(Mar)`: el «número» es el mes, así que se omitió (volumen 3, sin número). |
| m | `ElHafidi2025` | arXiv:2506.03272 (https://doi.org/10.48550/arXiv.2506.03272) | `Docs/insumos/fuentes_bib/ElHafidi2025_datacite_verificado.json` (DataCite) y la página https://arxiv.org/abs/2506.03272 | Completada por el coordinador, porque la API de arXiv limitó al trabajador. Título, tres autores y año coinciden en DataCite y en las etiquetas `citation_*` de arXiv (2025-06-03). Ambos registran al primer autor como «Hafidi, My Youssef El»; la entrada usa «El Hafidi, M. Y.», a confirmar en el PDF. El resumen menciona 309 registros (39 sin cáncer y 270 con cáncer) y seis subconjuntos balanceados; las cifras de la línea 783 (ZZ 0.91, Pauli 0.96) siguen sin confirmar en el PDF. |
| n | `Arrasmith2021` | 10.22331/q-2021-10-05-558 | `Docs/insumos/fuentes_bib/Arrasmith2021.json` (DOI hallado con `Arrasmith2021_search.json`) | Sin discrepancias. DOI hallado con la búsqueda bibliográfica de Crossref (primer resultado, título exacto). Autores: Arrasmith, A., Cerezo, M., Czarnik, P., Cincio, L., Coles, P. J. Crossref escribe «Lukasz» (sin «Ł»); solo afecta al nombre de pila, que la entrada abrevia a «L.». |

---

## 2. Duplicados del reporte

### 2.1 `Schuld2019QuantumML` frente a `schuld2019quantum`

| | `Schuld2019QuantumML` | `schuld2019quantum` |
|---|---|---|
| Línea del `\bibitem` | 3757 (texto en 3758–3760) | 3831 (texto en 3832–3834) |
| Comentario | `% --- Referencia 28 ...` (línea 3756) | `% --- Referencia 41 ...` (línea 3830) |

Texto de ambos (idéntico carácter por carácter salvo la clave):

```latex
Schuld, M., \& Killoran, N. (2019). Quantum machine learning in feature {H}ilbert spaces.
\textit{Physical Review Letters}, 122(4), 040504.
\url{https://doi.org/10.1103/PhysRevLett.122.040504}
```

**¿Misma obra?** Sí: mismos autores, título, revista, volumen, número, artículo y DOI. Aparecen dos veces en la bibliografía impresa.

Líneas con `\cite`:

- `Schuld2019QuantumML` — línea **756**: «Esta formalización sentó las bases teóricas de todo el campo del QML moderno y es la justificación fundamental del presente trabajo: si el espacio de Hilbert de $2^n$ dimensiones generado por $n$ qubits ofrece una geometría más favorable para la separación de clases morfológicas mamográficas, entonces la proyección cuántica aporta valor real al pipeline de clasificación. \cite{Schuld2019QuantumML}»
- `schuld2019quantum` — línea **1221**: «… y $W(\boldsymbol{\theta})$ es el \textit{ansatz} variacional que introduce correlaciones entre qubits mediante compuertas entrenables \cite{schuld2019quantum}.» (la frase empieza en la línea 1215).
- `schuld2019quantum` — línea **1253**: «El mapeo $\phi$ introduce correlaciones de orden superior entre las componentes de $\mathbf{x}$ que los métodos de codificación clásicos no capturan \cite{schuld2019quantum, havlicek2019supervised}.» (la frase empieza en la línea 1250).

Para unificarlas habría que cambiar 1 `\cite` (línea 756) o 2 (líneas 1221 y 1253) y borrar uno de los dos `\bibitem`.

### 2.2 `GlobalCancerStatistics2024` frente a `GlobalCancerStatistics2024_2`

| | `GlobalCancerStatistics2024` | `GlobalCancerStatistics2024_2` |
|---|---|---|
| Línea del `\bibitem` | 3621 (texto en 3622–3623) | 3656 (texto en 3657–3658) |
| Comentario | `% --- Referencia 5: Global Cancer Statistics ---` | `% --- Referencia 12: American Cancer Society - Global Cancer Statistics 2024 ---` |

Texto:

```latex
% GlobalCancerStatistics2024 (3622-3623)
American Cancer Society. (2024). Global cancer statistics. Retrieved from
\url{https://pressroom.cancer.org/GlobalCancerStatistics2024}

% GlobalCancerStatistics2024_2 (3657-3658)
American Cancer Society. (2024, April). Global cancer statistics 2024. Retrieved from
\url{https://pressroom.cancer.org/GlobalCancerStatistics2024}
```

**¿Misma obra?** Sí: mismo autor corporativo, mismo año y **misma URL**. Solo cambian el mes («April») y el título («Global cancer statistics» frente a «Global cancer statistics 2024»). La URL no se descargó en esta revisión; el título y la fecha exactos de la nota de prensa quedan por confirmar.

Líneas con `\cite`:

- `GlobalCancerStatistics2024` — línea **486**: «En paises de bajos ingresos, la tasa de mortalidad por cáncer de mama puede ser el doble que en países más desarrollados, a pesar de tener una incidencia considerablemente menor, lo que refleja la falta o inadecuada infraestructura de servicios de detección temprana y tratamiento oportuno \cite{GlobalCancerStatistics2024}.»
- `GlobalCancerStatistics2024_2` — línea **527**: «La variabilidad entre lectores y la dificultad intrínseca de interpretar características radiográficas sutiles limitan con frecuencia la precisión del diagnóstico mamográfico \cite{GlobalCancerStatistics2024_2}, lo que motivó el desarrollo de sistemas CADx automatizados.»

> **Ojo (contenido):** la afirmación de la línea 527 (variabilidad entre radiólogos en la lectura de mamografías) no parece corresponder a una nota de prensa de estadísticas globales de cáncer. Conviene que el autor confirme si esa fuente respalda la frase o si debe citarse otra obra.

---

## 3. Los 10 `\bibitem` sin `\cite`

Comprobación con grep sobre `Docs/Technical_Report.tex`: para cada clave se contaron sus apariciones totales y las apariciones dentro de cualquier comando `\…cite…{…}` (incluidos los `\cite` con varias claves). Las 10 aparecen **una sola vez** (en su `\bibitem`) y **0 veces** en un `\cite`.

| Clave | Línea del `\bibitem` | Apariciones / en `\cite` | Menciones en el texto sin `\cite` (línea: frase completa) |
|---|---|---|---|
| `WHO2025` | 3598 | 1 / 0 | Ninguna (no hay «World Health Organization», «WHO», «OMS» ni «Organización Mundial» fuera de la bibliografía). |
| `NBCF2026_Facts` | 3641 | 1 / 0 | Ninguna. (La línea 509 cita `NBCF2026_EarlyDetection`, que es otra entrada.) |
| `Wang2020DeepLearning` | 3661 | 1 / 0 | **529**: «El estudio de Wang et al. (2020), publicado en el Journal of the American College of Radiology, es uno de los trabajos más citados al respecto.» · **740**: «Wang et al. (2020) realizaron el análisis más sistemático de este fenómeno, evaluando seis modelos sobre cuatro datasets diferentes.» · **873**: «Wang et al. (2020)» (fila de la Tabla `tab:estado_arte`, «Comparativa de trabajos relacionados en el estado del arte», línea 842). |
| `Xiang2024QuantumCNN` | 3675 | 1 / 0 | **559**: «El trabajo de Xiang et al. (2024), ilustra esta dirección.» · **805**: «En el dominio de la mamografía, Xiang et al. (2024) propusieron el modelo QCCNN evaluado sobre datasets tabulares (GBSG, SEER, WDBC), reportando mejoras de hasta 5\% en accuracy respecto a CNN y regresión logística clásicas.» · **927**: «Xiang et al. (2024)» (fila de la Tabla `tab:estado_arte`). |
| `Azevedo2022QuantumTransfer` | 3682 | 1 / 0 | **613**: «Tercero, retoma y ejecuta las dos líneas de trabajo futuro identificadas por Azevedo et al. (2022) como pendientes: la separación del análisis por tipo de hallazgo mamográfico y la evaluación de la distribución de datos en el espacio cuántico resultante.» · **825**: «El trabajo más cercano en el dominio del QML aplicado a mamografías es el de Azevedo et al. (2022), que implementa quantum transfer learning mediante redes neuronales híbridas clásico-cuánticas con angle embedding sobre el dataset BCDR (Barcelona Digital Breast Cancer Dataset), obteniendo 84\% de accuracy y señalando como trabajo futuro explícito la necesidad de evaluar la distribución de los datos en el espacio de Hilbert resultante para verificar la separabilidad de clases.» · **939**: «Azevedo et al. (2022)» (fila de la Tabla `tab:estado_arte`). |
| `SaezOrtuño2026QuantumKernel` | 3688 | 1 / 0 | Ninguna (no hay «Sáez», «Saez» ni «Ortuño» fuera de la bibliografía). Nota: la clave lleva «ñ», un carácter no ASCII. Funciona con pdfLaTeX + `inputenc` utf8, pero conviene evitarlo si se cita. |
| `AlvarezEstevez2024QuantumKernelBench` | 3695 | 1 / 0 | Ninguna (no hay «Alvarez», «Álvarez» ni «Estevez» fuera de la bibliografía). |
| `Gao2023MammographyReview` | 3706 | 1 / 0 | Ninguna (no hay «Gao» fuera de la bibliografía). |
| `Baccouche2022ResidualNN` | 3745 | 1 / 0 | **821**: «Baccouche et al. (2022) propusieron un ensemble de modelos ResNet (ResNet50V2, ResNet101V2, ResNet152V2) que alcanzó una accuracy de 95.13\% en clasificación de patología y 90.02\% en clasificación de forma sobre CBIS-DDSM, demostrando la ventaja del aprendizaje por ensemble para superar las metodologías de deep learning individuales más recientes.» · **883**: «Baccouche et al. (2022)» (fila de la Tabla `tab:estado_arte`). |
| `ibmquantum2024learning` | 3861 | 1 / 0 | Ninguna (no hay «IBM Quantum Learning» ni «Basics of quantum information» fuera de la bibliografía; las demás menciones de «IBM Quantum» están en las entradas `ibmquantum2024docs` y `qiskitml2024`). |

Resumen: 4 obras se nombran en el texto sin `\cite` (Wang, Xiang, Azevedo, Baccouche) y 6 no se nombran en ningún lugar (WHO2025, NBCF2026_Facts, SaezOrtuño2026QuantumKernel, AlvarezEstevez2024QuantumKernelBench, Gao2023MammographyReview, ibmquantum2024learning). El autor decide si añade el `\cite` o elimina la entrada.

Fuera de la lista: en las mismas filas de la tabla aparecen «Bilal et al. (2025)», «Singh et al. (2025)» y «Ajlouni et al. (2023)», y en la línea 821 «Shen et al. (2019)». No se revisaron en este encargo.

---

## 4. `GLOBOCAN2022` (Freihat et al., 2025)

`\bibitem{GLOBOCAN2022}` en la línea **3604** (texto en 3605–3608):

```latex
Freihat, O., Sipos, D., \& Kovacs, A. (2025). Global burden and projections of
breast cancer incidence and mortality to 2050: a comprehensive analysis of
GLOBOCAN data. \textit{Frontiers in Public Health}, 13, 1622954.
\url{https://doi.org/10.3389/fpubh.2025.1622954}
```

Se cita **una sola vez**, en la línea **484**:

> «Según los datos de GLOBOCAN 2022 de la Agencia Internacional para la Investigación sobre el Cáncer (IARC), en 2022 se registraron aproximadamente 2.3 millones casos nuevos de cáncer de mama y una mortalidad de alrededor de 670,000 mujeres a nivel mundial \cite{GLOBOCAN2022}.»

Problema: la frase atribuye los datos a «GLOBOCAN 2022 de la IARC», pero la clave apunta a un análisis secundario de 2025 (Freihat et al.). La clave sugiere la fuente primaria y el texto la nombra, pero la referencia es otra. Opciones para el autor:

1. **Citar la fuente primaria**: cambiar el `\cite` de la línea 484 a `\cite{Bray2024GLOBOCAN}` (entrada b de `bibitems_nuevos.tex`). Si Freihat et al. ya no se cita en otro lugar, eliminar o renombrar el `\bibitem`.
2. **Conservar Freihat et al.**: renombrar la clave (p. ej., `Freihat2025GLOBOCAN`) para que no se confunda con la fuente primaria, y ajustar la redacción de la línea 484 para que no atribuya directamente los datos a la IARC.
3. **Ambas**: `\cite{Bray2024GLOBOCAN}` para las cifras de 2022 y Freihat et al. solo para las proyecciones a 2050, si se usan.

No se verificó en esta revisión que las cifras «2.3 millones» y «670,000» aparezcan en ninguna de las dos fuentes (solo se descargaron metadatos).
