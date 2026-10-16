# Lee2017CBISDDSM · A curated mammography data set for use in computer-aided detection and diagnosis research

- Autores y año: Lee, R. S., Gimenez, F., Hoogi, A., Miyake, K. K., Gorovoy, M., & Rubin, D. L. (2017).
- Versión leída: Docs/fuentes/pdf/Lee2017CBISDDSM.pdf · versión publicada en Scientific Data, 4, 170177 · 9 páginas
- Tipo: conjunto de datos (Data Descriptor)

## Qué concluye
- Publica el conjunto CBIS-DDSM (*Curated Breast Imaging Subset of DDSM*) estandarizando imágenes descomprimidas, segmentaciones refinadas de masas y diagnósticos patológicos: «Our data set, the CBIS-DDSM (Curated Breast Imaging Subset of DDSM), includes decompressed images, data selection and curation by trained mammographers, updated mass segmentation and bounding boxes, and pathologic diagnosis for training data, formatted similarly to modern computer vision data sets.» (p. 1)
- Proporciona un volumen representativo de 753 casos de calcificaciones y 891 casos de masas para investigación reproducible en CADe y CADx: «The data set contains 753 calciﬁcation cases and 891 mass cases, providing a data-set size capable of analyzing decision support systems in mammography.» (p. 1)
- Resuelve la obsolescencia técnica del DDSM original (2\,620 estudios escaneados en formato comprimido LJPEG no mantenido) convirtiendo los datos a formato estándar DICOM sin pérdida de información: «The DDSM is a database of 2,620 scanned ﬁlm mammography studies. It contains normal, benign, and malignant cases with veriﬁed pathology information.» (p. 2)
- Establece una partición oficial de entrenamiento y prueba (*train/test*) estratificada por categoría BI-RADS: «The data were split into a training set and a testing set based on the BI-RADS category. This allows for an appropriate stratiﬁcation for researchers working on CADe as well as CADx.» (p. 5)
- Define la proporción de la partición en 80\,\% entrenamiento y 20\,\% prueba de forma independiente para masas y calcificaciones: «The split was obtained using 20% of the cases for testing and the rest for training. The data were split for all mass cases and all calciﬁcation cases separately.» (p. 5)

## Qué deja como trabajo futuro o limitación declarada
- Señala como limitación intrínseca que las imágenes provienen de películas radiográficas digitalizadas (*scanned film*) y no de mamografía digital directa de campo completo (FFDM): «The scale of the database along with ground truth validation makes the DDSM a useful tool in the development and testing of decision support systems despite the fact that the images are scanned ﬁlm instead of full ﬁeld digital mammograms.» (p. 2)
- La re-segmentación automatizada mediante *level sets* se aplicó exclusivamente a masas, no a calcificaciones: «This segmentation was done only for masses and not calciﬁcations.» (p. 4)
- Excluyó 339 imágenes donde la masa no era claramente visible según revisión de un mamografista experto: «In this process, we found 339 images in which a mass was not clearly seen. These images were removed from the ﬁnal data set.» (p. 4)
- Advierte que las asignaciones BI-RADS registradas probablemente reflejan información diagnóstica posterior a la mamografía de tamizaje, dado el alto predominio de categorías BI-RADS 4 y 5: «Note that many of the BI-RADS assessments likely were updated after additional information was gathered by the physician, as it is unconventional to subscribe BI-RADS 4 and 5 to screening images.» (p. 5)

## Diseño experimental (solo obras experimentales)
No aplica: artículo descriptor de conjunto de datos (*Data Descriptor*). La evaluación cuantitativa interna consistió en comparar las segmentaciones automatizadas de contornos de masas frente a 118 trazos manuales de un radiólogo experto (coeficiente de Dice medio $0.792 \pm 0.108$ frente a $0.398 \pm 0.195$ de los contornos originales del DDSM, $p = 5.54 \times 10^{-19}$).

## Las cuatro preguntas de H-046 (solo obras que reportan una ventaja o un resultado cuántico frente a clásico)
No aplica: obra que describe y publica un conjunto de datos médicos clásicos; no propone ni evalúa modelos cuánticos.

## Preguntas específicas
- **Número de casos/estudios/pacientes que reporta:**
  - El DDSM original contenía «2,620 scanned ﬁlm mammography studies» (p. 2).
  - El subconjunto CBIS-DDSM curado contiene «753 calciﬁcation cases and 891 mass cases» (p. 1), sumando un total de 1\,644 casos de lesiones (Tabla 3, p. 7).
  - A nivel de anormalidades, contiene 1\,045 anormalidades en calcificaciones y 970 en masas (total 2\,015 anormalidades, Tabla 3, p. 7).
  - El término *case* en el artículo se define como «a particular abnormality, seen on the craniocaudal (CC) and/or mediolateral oblique (MLO) views» (p. 5).
  - El número de **1\,566 participantes** mencionado en el reporte técnico del TT no aparece explícitamente en el texto del artículo de Lee et al.; corresponde al conteo de identificadores únicos de paciente (`PatientID`, primeros 7 caracteres) alojados en el repositorio de The Cancer Imaging Archive (TCIA), corroborado empíricamente en la bitácora del TT (`Other/bitacora_decisiones.md:957`).
- **Construcción de las ROI:**
  - Para masas: Se utilizó un algoritmo de contornos activos deformables (*level sets* locales modificado a partir de Chan-Vese) inicializado con las anotaciones gruesas del DDSM original: «Due to the dependence of these methods on accurate ROI segmentation and the imprecise nature of many of the DDSM-provided annotations, as seen in Fig. 2, we applied a lesion segmentation algorithm (described below) that is initialized by the general original DDSM contours but is able to supply much more accurate ROIs.» (p. 4).
  - Para calcificaciones: No se realizó segmentación con *level sets*; se conservaron los contornos curados originales: «This segmentation was done only for masses and not calciﬁcations.» (p. 4).
  - Recortes (*bounding boxes*): Se generaron calculando el rectángulo delimitador envolvente de la anormalidad respecto a su ROI: «Abnormalities were cropped by determining the bounding rectangle of the abnormality with respect to its ROI.» (p. 4).
- **Partición train/test:**
  - Sí está estratificada por categoría BI-RADS: «The data were split into a training set and a testing set based on the BI-RADS category. This allows for an appropriate stratiﬁcation for researchers working on CADe as well as CADx.» (p. 5).
  - Se dividió en proporción 80\,\% entrenamiento y 20\,\% prueba separadamente para masas y calcificaciones: «The split was obtained using 20% of the cases for testing and the rest for training. The data were split for all mass cases and all calciﬁcation cases separately.» (p. 5).
- **Licencia:**
  - El artículo en *Scientific Data* está publicado bajo licencia Creative Commons Attribution 4.0 International (CC BY 4.0): «Open Access This article is licensed under a Creative Commons Attribution 4.0 International License» (p. 9).
  - Los datos en The Cancer Imaging Archive (TCIA) se distribuyen bajo la licencia Creative Commons Attribution 3.0 Unported (CC BY 3.0).

## Relevancia para el TT
- Se conecta directamente con la especificación de datos del proyecto: §1.2, §2.1.5, §5.3 (M1), D-008 y H-020.
- Justifica metodológicamente el tratamiento de masas y calcificaciones como problemas independientes debido a sus diferencias de adquisición, contorno y distribución BI-RADS.
- Fundamenta el uso de la partición preestablecida de 80/20 estratificada por BI-RADS para evitar sesgos de fuga de datos en la evaluación de separabilidad.
- **Qué NO se puede afirmar con esta fuente:** No se puede afirmar que CBIS-DDSM consista en mamografías digitales directas (FFDM); son películas escaneadas con densitómetro óptico sin calibración física de espaciado ni dosis. Tampoco se puede afirmar que el artículo reporte 1\,566 pacientes como cifra textual del texto publicado, pues reporta 1\,644 casos de patología (753 calcificaciones y 891 masas).

## Contraste con lo que el proyecto ya le atribuye
- `Docs/Technical_Report.tex:622`: Afirma que el dataset CBIS-DDSM tiene «1,566 participantes, partición train/test por categoría BI-RADS, y metadatos clínicos estructurados en archivos CSV». Sostiene: Parcial. La estratificación por BI-RADS («split into a training set and a testing set based on the BI-RADS category», p. 5) y los CSV de metadatos («compiled into a single comma-separated values (CSV) ﬁle», p. 4; «individual ﬁles for mass and calciﬁcation training and test sets», p. 7) están plenamente respaldados. Sin embargo, la cifra de «1,566 participantes» no aparece en el texto del artículo (reporta 753 casos de calcificaciones y 891 de masas, p. 1); 1\,566 es el número de sujetos únicos en el repositorio TCIA.
- `Docs/Technical_Report.tex:817`: Afirma que el dataset destaca «precisamente por su partición train-test previamente definida, sus máscaras ROI validadas patológicamente y su licencia pública CC BY 3.0». Sostiene: Sí («Standardized train/test splits», p. 4; «veriﬁed pathology information», p. 2; licencia en TCIA CC BY 3.0).
- `Docs/Technical_Report.tex:2498`: Afirma partición «(80\,\%/20\,\%, estratificada por BI-RADS)». Sostiene: Sí («The split was obtained using 20% of the cases for testing and the rest for training. The data were split for all mass cases and all calciﬁcation cases separately.» p. 5; «based on the BI-RADS category», p. 5).
- `Other/bitacora_decisiones.md:957`: Registra «3,568 registros sobre 1,566 pacientes: media de 2.28 ROIs por paciente». Sostiene: Compatible con la estructura de TCIA; Lee et al. aclaran que «some cases contain more than one abnormality» (p. 7) y «some cases contain both calciﬁcations and masses» (p. 6).
