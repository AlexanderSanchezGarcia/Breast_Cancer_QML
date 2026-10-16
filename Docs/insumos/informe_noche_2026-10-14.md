# Informe de la noche · 2026-10-14

Siete tareas delegadas a Gemini (8 trabajadores, `gemini-3.8-flash-high` vía Orca), todas terminadas, verificadas con scripts y revisadas a mano. Nada se versionó: todo está en el árbol de trabajo para que lo revises. `Technical_Report.tex` no se tocó.

**Borrador completo para leer:** `Docs/insumos/noche/borrador_completo_2026-10-14.pdf` (140 pp.: §2 nuevo, §3, §4 EDA, §5 Metodología, §6 Resultados y Anexos, con el preámbulo y la bibliografía reales). Compila sin errores ni referencias sin resolver.

## 1. Lo más importante para ti

1. **Azevedo et al. (2022) sí respalda la tesis, literalmente** (p. 12): «separate the dataset into masses and calcifications and only then perform classification» y «see how the data appears in our Hilbert space. Ideally, both classes would appear very separately in it, as tight clusters». La atribución de §1.3 es correcta.
2. **El §1 tiene paráfrasis sin citar, ya localizadas con la fuente exacta:**
   - l. 561–563 («Quantum embeddings como mecanismo…») traduce a **Mari et al. (2020), p. 3**.
   - l. 587 («la aplicación práctica… más allá de problemas de prueba específicamente construidos…») y l. 591 («resultados mixtos… elección cuidadosa del feature map… hiperparametrización») traducen el resumen de **Álvarez-Estévez (2024)**, que está en tu bibliografía sin ningún `\cite`.
   - Más casos en `Docs/insumos/auditoria_s1_s2.md` (89 incidencias, 42 de gravedad alta; las 10 prioritarias al principio).
3. **Lee et al. (2017) confirma que la partición train/test se hizo por categoría BI-RADS** (p. 5): «The data were split into a training set and a testing set based on the BI-RADS category». La frase que quitamos de RNF-03 por no estar verificada se puede recuperar, ahora con cita. Además, **el reporte no citaba el CBIS-DDSM ni TCIA**: sus `\bibitem` están en `bibitems_noche.tex`.
4. **Parigi et al. no dice lo que pensábamos atribuirle.** Concluye que los kernels de imagen dan una exactitud *comparable* a un kernel lineal con exponencialmente menos almacenamiento. Lo que sí dice es que cargar datos exactos cuesta O(2ⁿ) compuertas, y eso es lo que usa §2.1.8.
5. **IBSI recomienda el número fijo de *bins*** con intensidades arbitrarias y desaconseja el ancho fijo. Respalda D-008, pero el manual no menciona la mamografía ni fija el 32: eso es decisión tuya.

## 2. Qué se produjo

| Tarea | Salida | Verificación | Correcciones mías tras revisar |
|---|---|---|---|
| T1A–T1D · fichas | `Docs/insumos/fichas/` (24 fichas, 446 citas literales con página) | 24/24 pasan `verificar_citas_fichas.py` | IBSI: «exige» → recomienda; no menciona mamografía. BCDR: el artículo usa las dos formas («Breast Cancer Data Repository» y, en la bibliografía, «Breast cancer digital repository») |
| T3 · auditoría §1–§2 y Abstract | `Docs/insumos/auditoria_s1_s2.md` | 17/17 citas; muestreo de líneas correcto | Atribuyó la paráfrasis de l. 591 a Shaydulin; es de Álvarez-Estévez, y había otra en l. 587 (añadido al final del archivo) |
| T4 · anexos A–E | `Docs/capitulos/A_Anexos/`, `Docs/codigo/` (15 listados), `Docs/tablas/anexo_*.tex` (11), `Code/tools/tablas_anexos.py` | 15/15 listados idénticos a sus celdas; las 11 tablas se regeneran byte a byte; versiones = `conda list` | «Sin binarios en conda-forge para la arquitectura» → no existe paquete en conda-forge |
| T5 · EDA como cap. 4 | `Docs/capitulos/4_EDA/`, `A.3.2_figuras_eda.tex`, `Docs/insumos/referencias_cruzadas.md` | compila; cifras del cuerpo sin cambios (diff) | ninguna |
| T6 · §5.11 y §6 | `5.11_experimentos_complementarios.tex`; añadidos en 6.1, 6.2, 6.6; nuevos `6.7_lecciones_implementacion.tex` y `6.8_sintesis.tex`; `Docs/insumos/lenguaje_s6.md` (14 frases que sobreafirman) | sin `SIN_FUENTE` ni `NO_ENCONTRADO` nuevos; compila | IDs D/H visibles quitados; párrafo de deprecación de `PauliFeatureMap` reescrito (decía «módulo de algoritmos antiguos»); «millones de mediciones por par» solo vale para C5 (C4: decenas de miles) |
| T7 · §2 nuevo | `Docs/capitulos/2_Antecedentes/` (2.1.6 tabla ampliada, 2.1.7 límites de la ventaja, 2.1.8 imágenes cuánticas, 2.1.9 revisión crítica) | 79/79 respaldos verificados; compila | **«16 instancias» de prueba en El Hafidi: inventadas** (el artículo no describe la partición), eliminadas. **Tamaño de las mamografías: Gemini usó 2,048×2,048**; corregido a 5,037×2,960 (NEQR: 42 qubits, ~1.4×10¹⁰ operaciones). Calibrado: Huang 2021 «demostraron… invariablemente» → «observaron… siempre»; Xiang P3 sin «fuga de información», con su cita; cierre de 2.1.7 sin «la teoría establece que solo» |

## 3. Preparación (hecha por mí, sin Gemini)

- Carpetas renombradas con `git mv`: `5_EDA` → `4_EDA` y `4_Metodologia` → `5_Metodologia`, con archivos `4.x` y `5.x`. Etiquetas `sec:metodologia` y `sec:modulo1`…`sec:modulo8` añadidas.
- `Docs/fuentes/` (ignorada en git): 24 PDF y su texto por página. 7 tuyos y 17 de acceso abierto.
- `Docs/insumos/bibitems_noche.tex`: 14 `\bibitem` nuevos generados desde Crossref, DataCite y arXiv. Incluye Lee 2017, Clark 2013 (TCIA), IBSI, Preskill, McClean, Mari, Schuld y Killoran, Shaydulin, Canatar, Kübler, Bowles, FRQI, NEQR y Parigi. Parigi ya está publicado: *AVS Quantum Science* 8(1), 013801 (2026).
- `Docs/insumos/preambulo_extra.tex`: configuración de `listings`, con traducción de acentos y letras griegas.
- `compilar_prueba.sh`: ahora encuentra pdflatex, carga el preámbulo extra y `bibitems_noche.tex`.
- Scripts nuevos en `Code/tools/`: `verificar_citas_fichas.py`, `extraer_codigo.py`, `verificar_listados.py`.

## 4. Pendientes y decisiones tuyas

1. **Integrar en `Technical_Report.tex`**, cuando quieras:
   - el preámbulo extra (`listings`);
   - los `\bibitem` de `bibitems_noche.tex` y `bibitems_nuevos.tex`;
   - los `\input` de las carpetas;
   - `\appendix` antes de los anexos.
2. **§1:** pendiente de redactar contigo, con las tres preguntas PI-1 a PI-3 y la auditoría de T3.
3. **§3:** faltan las subsecciones nuevas (radiómica, PCA/KPCA, SVM/QSVM, kernel proyectado, ancho de banda). Las ecuaciones las escribo y verifico yo, no Gemini.
4. **`Docs/insumos/lenguaje_s6.md`:** 14 frases de §6 que sobreafirman, con propuesta de redacción. No las cambié; decide tú.
5. **`Docs/insumos/referencias_cruzadas.md`:** referencias escritas a mano («sección 4.x») fuera del EDA. Hay que corregirlas y añadir a la bitácora una nota de equivalencias (§4 de antes → §5).
6. **Lo que el verificador de cifras aún marca:**
   - 67 `SIN_FUENTE` en borradores anteriores de §5, sobre todo 5.1 y 5.8;
   - 17 `NO_ENCONTRADO` del EDA de TT1;
   - 1 «Qiskit 2.1», que es una versión, no una cifra.

   No son de esta noche, pero conviene limpiarlos.
7. **Rifat 2024 (BreastMNIST)** sigue sin PDF y queda fuera de §2. Radhi 2025 tampoco se evaluó: no hay PDF.
8. **En el entorno `radiomics`, PyRadiomics aparece como versión `0.1.dev1`** aunque es el mismo commit `8ed5793`. Es la etiqueta de `setuptools_scm`, como explica H-029. El Anexo D lo muestra tal cual.
9. **Nada está en un commit.** Sugiero revisarlo y versionarlo por partes: preparación y herramientas; capítulos 2, 4, 5 y 6; anexos; fichas y auditoría.

## 5. Lecciones de esta noche para delegar

- Las pruebas automáticas atraparon cero errores de cita: Gemini respetó el formato y las citas literales. **Los errores reales fueron de contenido y no los ve ningún script.** Hubo tres tipos: datos inventados (las 16 instancias), datos del proyecto mal tomados (2,048×2,048) y verbos que exageran. Todos aparecieron en la redacción libre (§2, §6.8), no en las fichas.
- **Yo también me equivoqué una vez:** «corregí» BCDR sin ver que el artículo usa las dos formas, y rompí una cita. El verificador lo detectó y lo deshice.
