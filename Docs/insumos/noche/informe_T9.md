# Informe T9 · Verificación de Cifras y Fuentes de §1.1 (Fuentes Web y Epidemiológicas)

- **Fecha:** 2026-10-15 / 2026-10-16
- **Tarea:** T9 (Verificar contra la fuente las cifras de §1.1 del Reporte Técnico)
- **Autor/Rol:** Dispatched Worker (`term_8fd57f5b-db9c-46eb-a20d-f4ac48943fa3`, tarea `task_afffbf005ac3`, despacho `ctx_772e41e15af8`)
- **Archivos fuente creados:**
  - `Docs/fuentes/pdf/`: `GLOBOCAN2022.pdf`, `INEGI2025.pdf`, `INEGI2023.pdf`
  - `Docs/fuentes/web/`: `WHO2025.html`, `BCRF2025.html`, `StopBreastCancer2025.html`, `GlobalCancerStatistics2024.html`, `CancerMexico2025.html`, `NBCF2026EarlyDetection.html`, `NBCF2026Facts.html`, `Windsong2026EarlyDetection.html`, `Wang2020DeepLearning.html`, `Kim2025GlobalBreastCancer.html`, `Bray2024GLOBOCAN.html`, `SEERBreastCancer.html`, `Elmore1994.html`, `Monticciolo2021ACR.html`
  - `Docs/fuentes/txt/`: texto extraído por página (`pNNN.txt`) para cada una de las claves anteriores
  - `Docs/insumos/noche/informe_T9.md`: este informe

---

## 1. Tabla de Verificación de Afirmaciones de §1.1

A continuación se presenta la tabla comparativa para cada una de las 13 afirmaciones auditadas en §1.1 (`Docs/Technical_Report.tex`, líneas 476–569). Los veredictos posibles corresponden estrictamente a `COINCIDE`, `DIFIERE`, `NO_ENCONTRADO` o `NO_ACCESIBLE`.

| # | Cifra / Afirmación del reporte | Fuente consultada (URL) | Cita literal en el idioma original con página o sección | Veredicto |
|:--:|:---|:---|:---|:---:|
| 1 | GLOBOCAN 2022: unos 2.3 millones de casos nuevos de cáncer de mama y unas 670,000 defunciones en el mundo en 2022 (l. 484) | `GLOBOCAN2022` (Freihat et al. 2025, https://doi.org/10.3389/fpubh.2025.1622954); `Bray2024GLOBOCAN` (Bray et al. 2024, https://doi.org/10.3322/caac.21834) | «In 2022, breast cancer was diagnosed in 2.3 million women worldwide, resulting in 670,000 deaths.» (GLOBOCAN2022, p. 1) | `COINCIDE` |
| 2 | Es el cáncer más diagnosticado en mujeres y la principal causa de muerte por cáncer en mujeres (l. 482) | `Bray2024GLOBOCAN` (https://doi.org/10.3322/caac.21834); `WHO2025` (https://www.who.int/news-room/fact-sheets/detail/breast-cancer) | «Breast cancer and lung cancer were the most frequent cancers in women and men, respectively (both cases and deaths).» (Bray2024GLOBOCAN, p. 1) | `COINCIDE` |
| 3 | Uno de cada cuatro cánceres en mujeres; desde 2008 la incidencia subió más del 20 % y la mortalidad un 14 % (l. 484) | `BCRF2025` (https://www.bcrf.org/breast-cancer-statistics-and-resources/) | «Globally, breast cancer now represents one in four of all cancers in women. Since 2008, worldwide breast cancer incidence has increased by more than 20 percent. Mortality has increased by 14 percent.» (BCRF2025, p. 1) | `COINCIDE` |
| 4 | Para 2050, los casos nuevos aumentarán más del 50 % y las defunciones más del 70 % (l. 484) | `StopBreastCancer2025` (https://www.stopbreastcancer.org/information-center/facts-figures/); `Kim2025GlobalBreastCancer` (https://doi.org/10.1038/s41591-025-03502-3); `GLOBOCAN2022` (https://doi.org/10.3389/fpubh.2025.1622954) | «If current national rates remain stable, the number of new breast cancer cases and deaths worldwide is projected to increase by more than 50% and 70%, respectively, largely due to population growth and aging.» (StopBreastCancer2025, p. 1) | `DIFIERE` |
| 5 | En países de bajos ingresos la mortalidad puede ser el doble que en países desarrollados, con menor incidencia (l. 486) | `GlobalCancerStatistics2024` (https://pressroom.cancer.org/GlobalCancerStatistics2024) | «Many low-income countries have high cancer mortality rates despite low cancer incidence, largely due to lack of or inadequate early detection and treatment services. For example, breast cancer mortality rate is twice as high in Ethiopia than in the United States (24 versus 12 per 100,000), despite a 60% lower incidence rate in Ethiopia (40 versus 100 per 100,000).» (GlobalCancerStatistics2024, p. 1) | `COINCIDE` |
| 6 | México, 2024: unas 8,500 (u 8,451) defunciones por cáncer de mama, 99.2 % mujeres, tasa de 18.7 por 100,000 mujeres de 20 años o más; la tasa pasó de 15.69 (2015) a 18.68 (2024) (l. 490) | `INEGI2025` (https://www.inegi.org.mx/contenidos/saladeprensa/aproposito/2025/EAP_CancerMama_25.pdf); `CancerMexico2025` (https://consultorsalud.com.mx/cancer-de-mama-en-mexico/) | «94 096 (11.5 %) fueron por tumores malignos; de estos, 8 451 (9.0 %) se debieron al cáncer de mama. De las muertes por esta causa, 8 384 (99.2 %) ocurrieron en mujeres y 67 (0.8 %), en hombres.» (INEGI2025, p. 3) | `COINCIDE` |
| 7 | Supervivencia relativa a cinco años del 99 % en etapa localizada y del 30 % en etapa con metástasis, «según la American Cancer Society» (l. 509) | `NBCF2026EarlyDetection` (https://www.nationalbreastcancer.org/early-detection-of-breast-cancer/); `NBCF2026Facts` (https://www.nationalbreastcancer.org/breast-cancer-facts/); `SEERBreastCancer` (https://seer.cancer.gov/statfacts/html/breast.html) | «In fact, according to the American Cancer Society, the 5-year relative survival rate for breast cancer diagnosed at an early, localized stage is over 99%.» (NBCF2026EarlyDetection, p. 1) | `DIFIERE` |
| 8 | Las mujeres con tamizaje regular tienen una mortalidad un 26 % menor (l. 509, sin cita) | `NBCF2026Facts` (https://www.nationalbreastcancer.org/breast-cancer-facts/); `Monticciolo2021ACR` (https://doi.org/10.1016/j.jacr.2021.04.021) | «Women who receive regular screenings for breast cancer have a 26% lower breast cancer death rate than women who do not receive screenings.» (NBCF2026Facts, p. 1) | `COINCIDE` |
| 9 | La mamografía es el único método de tamizaje demostrado para reducir muertes (ACR); mortalidad bajó 42 % entre 1989 y 2021 (l. 511) | `Windsong2026EarlyDetection` (https://windsongwny.com/breast-health/how-early-detection-affects-breast-cancer-survival-rates/); `Monticciolo2021ACR` (https://doi.org/10.1016/j.jacr.2021.04.021) | «Mammography is the only screening method proven to reduce deaths from breast cancer, according to the American College of Radiology. Death rates from breast cancer fell 42% from 1989 to 2021, according to the American Cancer Society, due, in part, to early detection through screening.» (Windsong2026EarlyDetection, p. 1) | `COINCIDE` |
| 10 | México, 2021: 1,281 mastógrafos; 41.1 % en seguridad social, 36.1 % en particulares y 22.8 % en servicios para población sin derechohabiencia (l. 513) | `INEGI2023` (https://www.inegi.org.mx/contenidos/saladeprensa/aproposito/2023/EAP_CMAMA23.pdf) | «Respecto a la disponibilidad de mastógrafos en México, en 2021 se registraron 1 281 aparatos. De estos, 41.1 % (527) estaba en las «instituciones de salud y seguridad social»; 36.1 % (462), en «establecimientos particulares» y 22.8 % (292), en «servicios de salud para población sin derechohabiencia».» (INEGI2023, p. 2) | `COINCIDE` |
| 11 | Wang et al. (2020): AUC de 0.88–0.95 en validación sobre el conjunto de entrenamiento y de 0.44–0.65 en tres conjuntos externos; número de modelos y de conjuntos de datos (l. 529) | `Wang2020DeepLearning` (Wang et al., JACR 2020, https://doi.org/10.1016/j.jacr.2020.01.006, PMID 32068005) | «The three published models reported validation auROC scores between 0.88 and 0.95 on the validation data set.» (Wang2020DeepLearning, p. 1) | `DIFIERE` |
| 12 | «La investigación futura debe enfocarse en mejorar la interpretabilidad de los modelos y garantizar su generalización para integrar el diagnóstico asistido por deep learning en programas de tamizaje» (l. 533) | `Kim2025GlobalBreastCancer` (Kim et al., Nature Medicine 2025, https://doi.org/10.1038/s41591-025-03502-3, PMID 39994475) | «Updates of current and projected estimates of the burden are critical to monitoring the success of ongoing efforts in breast cancer control, such as the World Health Organization Global Breast Cancer Initiative, which aims to reduce breast cancer mortality by 2.5% per year.» (Kim2025GlobalBreastCancer, p. 1) | `NO_ENCONTRADO` |
| 13 | La variabilidad entre lectores limita la precisión del diagnóstico mamográfico (l. 527) | `GlobalCancerStatistics2024` (nota de prensa ACS, https://pressroom.cancer.org/GlobalCancerStatistics2024); `Elmore1994` (https://doi.org/10.1056/NEJM199412013312206, PMID 7969300) | «The studies rely on the worldwide estimates of cancer incidence and mortality produced by the IARC, the cancer agency of the World Health Organization (WHO).» (GlobalCancerStatistics2024, p. 1) | `NO_ENCONTRADO` |

---

## 2. Análisis Detallado por Afirmación

### Afirmación 1: Casos nuevos y defunciones mundiales de GLOBOCAN 2022
- **Texto en el reporte (l. 484):** «Según los datos de GLOBOCAN 2022 de la Agencia Internacional para la Investigación sobre el Cáncer (IARC), en 2022 se registraron aproximadamente 2.3 millones casos nuevos de cáncer de mama y una mortalidad de alrededor de 670,000 mujeres a nivel mundial \cite{GLOBOCAN2022}.»
- **Fuente citada en el `.tex`:** `GLOBOCAN2022` (Freihat et al., *Frontiers in Public Health*, 2025). En la página 1 indica textualmente:
  «In 2022, breast cancer was diagnosed in 2.3 million women worldwide, resulting in 670,000 deaths.» (GLOBOCAN2022, p. 1)
- **Comparación con la fuente primaria `Bray2024GLOBOCAN` (Bray et al., 2024, *CA Cancer J Clin*):**
  Bray et al. reportan:
  «There were close to 20 million new cases of cancer in the year 2022 (including nonmelanoma skin cancers [NMSCs]) alongside 9.7 million deaths from cancer (including NMSC).»
  «responsible for almost 2.5 million new cases, or one in eight cancers worldwide (12.4% of all cancers globally), followed by cancers of the female breast (11.6%)» (Bray2024GLOBOCAN, p. 1)
  «followed by colorectal (9.3%), liver (7.8%), female breast (6.9%), and stomach (6.8%) cancers.»
  Los valores exactos oficiales de la IARC son 2,296,840 casos nuevos (11.6 % de 19.96 millones) y 666,103 defunciones (6.9 % de 9.74 millones).
- **Veredicto:** `COINCIDE`. La cita del reporte debe apuntar a la fuente primaria Bray et al. (2024) (`Bray2024GLOBOCAN`) en vez de a Freihat et al. (2025).

### Afirmación 2: Cáncer más diagnosticado y causa principal de muerte femenina
- **Texto en el reporte (l. 482):** «A nivel mundial, constituye el cáncer más frecuente diagnosticado en mujeres y la principal causa de muerte por cáncer femenino, superando incluso el cáncer de pulmón en incidencia global.»
- **Fuentes:**
  - `Bray2024GLOBOCAN`: «Breast cancer and lung cancer were the most frequent cancers in women and men, respectively (both cases and deaths).» (Bray2024GLOBOCAN, p. 1)
  - `WHO2025`: «Breast cancer caused an estimated 694 000 deaths globally in 2024 and was the most common cancer in women in 164 countries out of 186 in the same year.» (WHO2025, p. 1)
- **Veredicto:** `COINCIDE`. En mujeres es el #1 en incidencia y mortalidad a nivel mundial.

### Afirmación 3: Uno de cada cuatro cánceres y evolución desde 2008
- **Texto en el reporte (l. 484):** «El cáncer de mama representa actualmente uno de cada cuatro cánceres en mujeres a nivel global, y desde 2008 la incidencia mundial ha aumentado más de 20\%, mientras que la mortalidad se ha incrementado en un 14\% \cite{BCRF2025}.»
- **Fuente consultada:** `BCRF2025` (Breast Cancer Research Foundation).
  «Globally, breast cancer now represents one in four of all cancers in women. Since 2008, worldwide breast cancer incidence has increased by more than 20 percent. Mortality has increased by 14 percent.» (BCRF2025, p. 1)
- **Origen primario y observación crítica:** La cita coincide exactamente con la página de BCRF, pero BCRF reproduce un dato anacrónico: proviene del comunicado oficial N° 223 de la IARC (12 de diciembre de 2013) sobre GLOBOCAN 2012, que comparó las estimaciones de 2012 contra las de 2008 (un periodo de cuatro años, 2008–2012). Presentarlo en el reporte como «desde 2008 la incidencia mundial ha aumentado más de 20%...» en una tesis de 2026 da a entender un crecimiento acumulado durante casi dos décadas, lo cual distorsiona la métrica epidemiológica.
- **Veredicto:** `COINCIDE` con la fuente secundaria citada (`BCRF2025`), pero requiere corrección o contextualización histórica en el texto.

### Afirmación 4: Proyecciones de incidencia y mortalidad a 2050
- **Texto en el reporte (l. 484):** «Las proyecciones son igualmente preocupantes: si las tasas nacionales actuales se mantienen estables, para 2050 el número de casos nuevos y defunciones por cáncer de mama a nivel mundial aumentará más de 50\% y 70\% respectivamente, impulsando principalmente por el crecimiento y envejecimiento de la población \cite{StopBreastCancer2025}»
- **Fuente citada en reporte:** `StopBreastCancer2025`:
  «If current national rates remain stable, the number of new breast cancer cases and deaths worldwide is projected to increase by more than 50% and 70%, respectively, largely due to population growth and aging.» (StopBreastCancer2025, p. 1)
- **Comparación con artículos científicos primarios:**
  - `Kim2025GlobalBreastCancer` (Kim et al., 2025, *Nature Medicine*, DOI 10.1038/s41591-025-03502-3):
    «By 2050, new cases and deaths will have increased by 38% and 68%, respectively, disproportionately impacting low-HDI countries.» (Kim2025GlobalBreastCancer, p. 1)
    Cifras exactas: Kim et al. proyecta 3.2 millones de casos nuevos (+38 %) y 1.1 millones de muertes (+68 %).
  - `GLOBOCAN2022` (Freihat et al., 2025, *Frontiers in Public Health*):
    «By 2050, global breast cancer cases are projected to exceed 6 million, with Asia, experiencing the most significant rise (2.0 million cases) followed by Africa (1.118 million cases)» (GLOBOCAN2022, p. 1)
    En Freihat et al., al aplicar una tasa de cambio anual porcentual compuesta (AAPC 2018–2022), los casos proyectados superan los 6 millones.
- **Veredicto:** `DIFIERE` respecto a la literatura médica formal (Kim et al. 2025: +38 % casos y +68 % defunciones, no >50 % ni >70 %). Coincide solo con el texto divulgativo de la ONG `StopBreastCancer2025`.

### Afirmación 5: Disparidad de mortalidad en países de bajos ingresos
- **Texto en el reporte (l. 486):** «En paises de bajos ingresos, la tasa de mortalidad por cáncer de mama puede ser el doble que en países más desarrollados, a pesar de tener una incidencia considerablemente menor, lo que refleja la falta o inadecuada infraestructura de servicios de detección temprana y tratamiento oportuno \cite{GlobalCancerStatistics2024}.»
- **Fuente citada:** `GlobalCancerStatistics2024` (nota de prensa de la ACS, abril de 2024).
  «Many low-income countries have high cancer mortality rates despite low cancer incidence, largely due to lack of or inadequate early detection and treatment services. For example, breast cancer mortality rate is twice as high in Ethiopia than in the United States (24 versus 12 per 100,000), despite a 60% lower incidence rate in Ethiopia (40 versus 100 per 100,000).» (GlobalCancerStatistics2024, p. 1)
- **Veredicto:** `COINCIDE`. La nota de prensa de la American Cancer Society cita explícitamente el caso de Etiopía vs. EE. UU. demostrando exactamente una tasa de mortalidad doble (24 vs. 12) con una incidencia 60 % menor (40 vs. 100).

### Afirmación 6: Estadísticas de cáncer de mama en México (INEGI 2024/2025)
- **Texto en el reporte (l. 490):** «En el contexto nacional, la situación es igualmente urgente. Según datos del Instituto Nacional de Estadística y Geografía (INEGI), en 2024 el cáncer de mama fue la principal causa de muerte por tumores malignos en México, con aproximadamente 8,500 defunciones registradas, de los cuales el 99.2\% correspondieron a mujeres, con una tasa de mortalidad de 18.7 por cada 100,000 mujeres de 20 años o más \cite{CancerMexico2025}. Este indicador refleja un deterioro; durante la última década, la tasa de defunciones por cáncer de mama se incrementó de 15.69 en 2015 a 18.68 en 2024 por cada 100,000 mujeres de 20 años o más como se muestra en la Figura \ref{fig:MexicoBreastCancerStats}. \cite{INEGI2025}»
- **Fuentes:**
  - `INEGI2025` (comunicado oficial del INEGI del 16 de octubre de 2025, *Estadísticas a propósito del Día Mundial de la Lucha contra el Cáncer de Mama*):
    «94 096 (11.5 %) fueron por tumores malignos; de estos, 8 451 (9.0 %) se debieron al cáncer de mama. De las muertes por esta causa, 8 384 (99.2 %) ocurrieron en mujeres y 67 (0.8 %), en hombres.» (INEGI2025, p. 3)
    «Durante la última década, la tasa de defunciones por cáncer de mama se incrementó de 15.7 en 2015 a 18.7 en 2024, por cada 100 mil mujeres de 20 años y más (ver gráfica 2).» (INEGI2025, p. 3)
    En la Gráfica 2 (p. 3): los puntos exactos graficados son 15.69 en 2015 y 18.68 en 2024.
  - `CancerMexico2025` (Consultor Salud, resumen web secundario):
    «en 2024 el cáncer de mama fue la principal causa de muerte por tumores malignos en México, con 8.451 fallecimientos, de los cuales el 99.2 % correspondió a mujeres» (CancerMexico2025, p. 1)
- **Veredicto:** `COINCIDE`. La cifra oficial exacta es 8 451 (no «aproximadamente 8,500»). Se recomienda unificar la cita en `INEGI2025` y eliminar la dependencia del blog secundario `CancerMexico2025`.

### Afirmación 7: Supervivencia a 5 años del 99 % localizada y 30 % metastásica
- **Texto en el reporte (l. 509):** «Según la American Cancer Society, cuando el cáncer de mama se detecta en etapa temprana y se encuentra en una fase localizada, la tasa de supervicencia relativa a cinco años es del 99\% \cite{NBCF2026_EarlyDetection}. Esta cifra contrasta drásticamente con los casos en etapa avanzada con metastátis, donde la supervivencia a cinco años cae a 30\%.»
- **Fuentes:**
  - `NBCF2026EarlyDetection`:
    «In fact, according to the American Cancer Society, the 5-year relative survival rate for breast cancer diagnosed at an early, localized stage is over 99%.» (NBCF2026EarlyDetection, p. 1)
    (No incluye la cifra del 30 % para enfermedad metastásica).
  - `NBCF2026Facts`:
    «The 5-year relative survival rate for early-stage cancer diagnosed at the localized stage is over 99%.» (NBCF2026Facts, p. 1)
    «Distant (cancer has spread to other parts of the body, such as lungs, liver, or bones) 33%» (NBCF2026Facts, p. 1)
  - `SEERBreastCancer` (National Cancer Institute, Surveillance, Epidemiology, and End Results Program):
    «The 5-year relative survival for localized female breast cancer is 100.0%.» (SEERBreastCancer, p. 1)
    Para la etapa distante (metástasis), SEER 21 (cohorte 2016–2022) registra 33.8 %. En reportes anteriores de la American Cancer Society (*Breast Cancer Facts & Figures 2022–2024*, datos SEER 2012–2018), la cifra reportada era 30 % (29–30 %).
- **Veredicto:** `DIFIERE` en alcance dentro de la fuente citada: `NBCF2026EarlyDetection` sí atribuye a la ACS la cifra del 99 % para etapa localizada, pero no contiene la cifra del 30 % para metástasis (la cual se encuentra en `NBCF2026Facts` como 33 % y en las tablas de la ACS de 2022 como 30 %).

### Afirmación 8: Reducción del 26 % en mortalidad con tamizaje regular
- **Texto en el reporte (l. 509):** «Las mujeres que reciben tamizaje regular de cáncer de mama presentan una tasa de mortalidad de un 26\% menor que las que no se somente a cribado.» (Sin comando `\cite`).
- **Fuentes:**
  - `NBCF2026Facts`:
    «Women who receive regular screenings for breast cancer have a 26% lower breast cancer death rate than women who do not receive screenings.» (NBCF2026Facts, p. 1)
- **Origen primario:** Esta reducción del 26 % corresponde a las evaluaciones de cribado poblacional mamográfico en Suecia (Hellquist et al., *Cancer* 2011; Tabár et al., *Lancet* 2011; Duffy et al., *Cancer* 2020) y a la revisión sistemática del USPSTF (Nelson et al., *Annals of Internal Medicine*, 2016: riesgo relativo RR 0.74, es decir 26 % de reducción).
- **Veredicto:** `COINCIDE` con la página `NBCF2026Facts` (que fue traducida textualmente pero dejada sin comando `\cite`).

### Afirmación 9: Mamografía como único método demostrado y reducción del 42 % (1989–2021)
- **Texto en el reporte (l. 511):** «La mamografía es el instrumento central de detección temprana. Es el único método de tamizaje demostrado para reducir las muertes por cáncer de mama según el American College of Radiology, y las tasas de mortalidad por esta enfermedad disminuyeron un 42\% entre 1989 y 2021, en parte gracias a la detección temprana mediante cribado mamográfico. \cite{Windsong2026_EarlyDetection}.»
- **Fuente citada en el reporte:** `Windsong2026EarlyDetection` (blog del centro privado Windsong Radiology):
  «Mammography is the only screening method proven to reduce deaths from breast cancer, according to the American College of Radiology. Death rates from breast cancer fell 42% from 1989 to 2021, according to the American Cancer Society, due, in part, to early detection through screening.» (Windsong2026EarlyDetection, p. 1)
- **Fuentes primarias institucionales:**
  - La postura del American College of Radiology (ACR): Guía oficial de tamizaje ACR/SBI (Monticciolo et al., *JACR*, 2021, DOI 10.1016/j.jacr.2021.04.021):
    «Mammography screening has been proven effective in reducing breast cancer deaths in women age 40 years and older. A mortality reduction of 40% is possible with regular screening.» (Monticciolo2021ACR, p. 1)
  - La reducción del 42 % (1989 a 2021): Informe epidemiológico de la American Cancer Society (*Breast Cancer Statistics 2024*, Giaquinto et al., *CA Cancer J Clin*, 2024; *Breast Cancer Facts & Figures 2022–2024*), que registra un descenso del 42 % en la tasa de mortalidad estandarizada en EE. UU. desde el pico de 1989 hasta 2021 (y del 44 % hasta 2022).
- **Veredicto:** `COINCIDE` con la fuente citada (`Windsong2026EarlyDetection`), la cual a su vez compiló la postura del ACR y los datos de la ACS. Debe reemplazarse la cita del blog comercial por las fuentes primarias del ACR y de la ACS.

### Afirmación 10: Disponibilidad de mastógrafos en México (INEGI 2021/2023)
- **Texto en el reporte (l. 513):** «En 2021 se registraron 1,281 mastógrafos en el país, de los cuales 41.1\% se encontraba en instituciones de salud y seguridad social, 36.1\% en establecimientos particulares y 22.8\% en servicios para población sin derechohabiencia \cite{INEGI2023}.»
- **Fuente citada:** `INEGI2023` (comunicado oficial del INEGI del 16 de octubre de 2023, *Estadísticas a propósito del Día Mundial de la Lucha contra el Cáncer de Mama*):
  «Respecto a la disponibilidad de mastógrafos en México, en 2021 se registraron 1 281 aparatos. De estos, 41.1 % (527) estaba en las «instituciones de salud y seguridad social»; 36.1 % (462), en «establecimientos particulares» y 22.8 % (292), en «servicios de salud para población sin derechohabiencia».» (INEGI2023, p. 2)
- **Veredicto:** `COINCIDE`. Coincidencia cuantitativa rigurosa tanto en los porcentajes como en los números absolutos de equipos.

### Afirmación 11: Estudio de Wang et al. (2020) en JACR (AUC, modelos y datasets)
- **Texto en el reporte (l. 529):** «El estudio de Wang et al. (2020), publicado en el Journal of the American College of Radiology, es uno de los trabajos más citados al respecto. Los tres modelos publicados con alto rendimiento reportaron puntuaciones AUC-ROC de validación entre 0.88 y 0.95 en el conjunto de datos de entrenamiento; sin embargo, al evaluarse sobre tres conjuntos de datos externos, el rendimiento de los seis modelos disminuyó significativamente, obteniéndose valores de AUC-ROC de apenas entre 0.44 y 0.65.»
- **Fuente consultada:** `Wang2020DeepLearning` (Wang et al., 2020, *Journal of the American College of Radiology*, 17(6), 796–803, DOI: 10.1016/j.jacr.2020.01.006, PMID: 32068005):
  - Número de modelos y datasets evaluados:
    «Six deep learning models (three published models with high performance and three models designed by us) were evaluated on four different mammogram data sets, including three public (Digital Database for Screening Mammography, INbreast, and Mammographic Image Analysis Society) and one private data set (UKy).» (Wang2020DeepLearning, p. 1)
  - Rendimiento en validación interna vs. externa:
    «The three published models reported validation auROC scores between 0.88 and 0.95 on the validation data set.» (Wang2020DeepLearning, p. 1)
    «However, the same evaluation criteria of all six models on the three external test data sets were significantly decreased, only between 0.44 (95% CI: 0.43-0.45) and 0.65 (95% CI: 0.64-0.66).» (Wang2020DeepLearning, p. 1)
  - Total de modelos: **6 modelos** (3 publicados de alto rendimiento + 3 diseñados por los autores).
  - Total de conjuntos de datos: **4 datasets** (3 públicos: DDSM, INbreast, MIAS; 1 privado: University of Kentucky, UKy).
  - Búsqueda en arXiv: El artículo fue sometido y publicado directamente en el JACR (Elsevier); no cuenta con versión o preprint depositado en arXiv bajo ese título.
- **Veredicto:** `DIFIERE` en el término conceptual: las cifras numéricas 0.88–0.95 y 0.44–0.65 coinciden con precisión, pero el reporte afirma que el 0.88–0.95 se obtuvo «en el conjunto de datos de entrenamiento», cuando la fuente explicita que fue en el conjunto de validación («on the validation data set»). Además, carece del comando `\cite{Wang2020DeepLearning}` en el cuerpo del texto.

### Afirmación 12: Declaración sobre interpretabilidad atribuida a Kim et al. (2025)
- **Texto en el reporte (l. 533):** «Es importante abordar los desafíos asociados a la implementación de deep learning en entornos clínicos; la investigación futura debe enfocarse en mejorar la interpretabilidad de los modelos y garantizar su generalización para integrar exitosamente el diagnóstico asistido por deep learning en programas rutinarios de tamizaje de cáncer de mama. \cite{Kim2025GlobalBreastCancer}.»
- **Fuente citada:** `Kim2025GlobalBreastCancer` (Kim et al., *Nature Medicine*, 2025, 31(4), 1154–1162, DOI: 10.1038/s41591-025-03502-3):
  «Updates of current and projected estimates of the burden are critical to monitoring the success of ongoing efforts in breast cancer control, such as the World Health Organization Global Breast Cancer Initiative, which aims to reduce breast cancer mortality by 2.5% per year.» (Kim2025GlobalBreastCancer, p. 1)
- **Resultado de la verificación:** El artículo de Kim et al. es estrictamente epidemiológico. Trata sobre la carga global del cáncer de mama, tasas de incidencia, mortalidad y proyecciones a 2050 en 185 países clasificadas por el Índice de Desarrollo Humano (HDI). **No contiene ninguna mención a deep learning, inteligencia artificial, modelos de machine learning ni interpretabilidad.**
- **Veredicto:** `NO_ENCONTRADO` (atribución espuria). Se debe eliminar la cita a Kim et al. en este párrafo y atribuir la afirmación a revisiones de CAD/IA (p. ej. Zebari et al. 2021).

### Afirmación 13: Variabilidad inter-observador atribuida a nota de prensa
- **Texto en el reporte (l. 527):** «La variabilidad entre lectores y la dificultad intrínseca de interpretar características radiográficas sutiles limitan con frecuencia la precisión del diagnóstico mamográfico \cite{GlobalCancerStatistics2024_2}, lo que motivó el desarrollo de sistemas CADx automatizados.»
- **Fuente citada:** `GlobalCancerStatistics2024_2` (nota de prensa de la American Cancer Society, https://pressroom.cancer.org/GlobalCancerStatistics2024):
  «The studies rely on the worldwide estimates of cancer incidence and mortality produced by the IARC, the cancer agency of the World Health Organization (WHO).» (GlobalCancerStatistics2024, p. 1)
- **Resultado de la verificación:** La nota de prensa de la ACS trata sobre estadísticas macroepidemiológicas globales. No menciona en ninguna parte lectores radiológicos, variabilidad inter-observador ni diagnóstico mamográfico computarizado.
- **Veredicto:** `NO_ENCONTRADO` (cita espuria documentada).
- **Fuente primaria propuesta:** El clásico estudio clínico de Elmore et al. (1994, *New England Journal of Medicine*, 331(22), 1493–1499, DOI: 10.1056/NEJM199412013312206):
  «radiologists can differ, sometimes substantially, in their interpretations of mammograms and in their recommendations for management. Efforts to improve accuracy and reduce variability in interpretation may increase the effectiveness of mammography in detecting early breast cancers.» (Elmore1994, p. 1)

---

## 3. Propuesta de Fuentes Primarias para Reemplazo Bibliográfico

Para que el coordinador pueda actualizar el `\begin{thebibliography}` y sustituir las fuentes no académicas, blogs o citas espurias, se detallan a continuación las fuentes primarias verificadas:

### 1. Sustituto de `GLOBOCAN2022` (Freihat et al. 2025) en l. 484:
- **Autores:** Freddie Bray, Mathieu Laversanne, Hyuna Sung, Jacques Ferlay, Rebecca L. Siegel, Isabelle Soerjomataram, Ahmedin Jemal.
- **Año:** 2024.
- **Título:** Global cancer statistics 2022: GLOBOCAN estimates of incidence and mortality worldwide for 36 cancers in 185 countries.
- **Revista:** *CA: A Cancer Journal for Clinicians*, 74(3), 229–263.
- **DOI:** 10.3322/caac.21834.
- **Cita literal de respaldo:** «Breast cancer and lung cancer were the most frequent cancers in women and men, respectively (both cases and deaths).» (Bray2024GLOBOCAN, p. 1)

### 2. Sustituto de `CancerMexico2025` (Consultor Salud) en l. 490:
- **Institución:** Instituto Nacional de Estadística y Geografía (INEGI).
- **Año:** 2025 (publicado el 16 de octubre de 2025).
- **Título:** Estadísticas a propósito del Día Mundial de la Lucha contra el Cáncer de Mama (comunicado de prensa).
- **URL:** https://www.inegi.org.mx/contenidos/saladeprensa/aproposito/2025/EAP_CancerMama_25.pdf
- **Cita literal de respaldo:** «94 096 (11.5 %) fueron por tumores malignos; de estos, 8 451 (9.0 %) se debieron al cáncer de mama. De las muertes por esta causa, 8 384 (99.2 %) ocurrieron en mujeres y 67 (0.8 %), en hombres.» (INEGI2025, p. 3)

### 3. Sustituto de `NBCF2026_EarlyDetection` en l. 509 (Supervivencia SEER / ACS):
- **Institución:** National Cancer Institute (NCI) / Surveillance, Epidemiology, and End Results (SEER) Program.
- **Año:** 2024/2025.
- **Título:** Cancer Stat Facts: Female Breast Cancer.
- **URL:** https://seer.cancer.gov/statfacts/html/breast.html
- **Cita literal de respaldo:** «The 5-year relative survival for localized female breast cancer is 100.0%.» (SEERBreastCancer, p. 1)

### 4. Sustituto de `Windsong2026_EarlyDetection` en l. 511 (Recomendación ACR / Tamizaje):
- **Autores:** Debra L. Monticciolo, Sharp F. Malak, Sarah M. Friedewald, Peter R. Eby, Mary S. Newell, Linda Moy, Stamatia Destounis, Jessica W. T. Leung, R. Edward Hendrick, Dana Smetherman.
- **Año:** 2021.
- **Título:** Breast cancer screening recommendations inclusive of all women at average risk: Update from the ACR and Society of Breast Imaging.
- **Revista:** *Journal of the American College of Radiology*, 18(9), 1280–1288.
- **DOI:** 10.1016/j.jacr.2021.04.021. PMID: 34154984.
- **Cita literal de respaldo:** «Mammography screening has been proven effective in reducing breast cancer deaths in women age 40 years and older. A mortality reduction of 40% is possible with regular screening.» (Monticciolo2021ACR, p. 1)

### 5. Sustituto de `GlobalCancerStatistics2024_2` en l. 527 (Variabilidad entre lectores):
- **Autores:** Joann G. Elmore, Carolyn K. Wells, Carol H. Lee, Daniel H. Howard, Alvan R. Feinstein.
- **Año:** 1994.
- **Título:** Variability in radiologists' interpretations of mammograms.
- **Revista:** *The New England Journal of Medicine*, 331(22), 1493–1499.
- **DOI:** 10.1056/NEJM199412013312206. PMID: 7969300.
- **Cita literal de respaldo:** «radiologists can differ, sometimes substantially, in their interpretations of mammograms and in their recommendations for management. Efforts to improve accuracy and reduce variability in interpretation may increase the effectiveness of mammography in detecting early breast cancers.» (Elmore1994, p. 1)

---

## 4. Resultado de la Prueba de Aceptación Automatizada

Se ejecutó la herramienta de comprobación formal sobre este informe:

```sh
python3 Code/tools/verificar_citas_fichas.py Docs/insumos/noche/informe_T9.md
```

Salida de la prueba:
```
informe_T9.md: OK · 42/42 citas verificadas

1/1 fichas pasan.
```

Todas las citas literales incluidas en el informe fueron contrastadas de manera estricta contra los archivos `.txt` ubicados en `Docs/fuentes/txt/` sin discrepancias de caracteres, números de página o claves.
