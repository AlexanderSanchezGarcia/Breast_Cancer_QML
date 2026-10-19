# Informe de la noche del 18 al 19 de octubre de 2026

Integración del reporte con el formato de la CATT, auditoría completa (siete trabajadores de Gemini más la verificación en sesión) y primer borrador del artículo.

## Qué pasó durante la noche

- 22:50–23:45: commit y push de lo pendiente, limpieza de `Other/`, integración, lanzamiento de los ocho trabajadores y primeras correcciones (A1, A6).
- Hacia las 23:45 se agotó la cuota de la sesión coordinadora y la sesión se reinició. **El recordatorio de la 01:27 no se disparó**, porque `CronCreate` solo vive dentro de la sesión.
- Los ocho trabajadores terminaron solos durante la noche y no tocaron nada fuera de `Docs/insumos/auditoria/` y `Docs/articulo/`.
- 07:35–09:00: verificación de cada hallazgo y correcciones, en sesión.

## Commits

En GitHub (repositorio renombrado a `Breast_Cancer_QML`, público):

| Commit | Contenido |
|---|---|
| `2060cc4` | §7, §8, X9 |
| `9ca063b` | Limpieza de `Other/` (`ESCOM/`, `verificacion/`, `archivo/`), sin borrar nada |

**Solo locales, para que los revises antes del push:**

| Commit | Contenido |
|---|---|
| `52af6c1` | Integración en `Technical_Report.tex` con el formato de la CATT |
| `c247c9e` | Especificaciones de la auditoría |
| `cabc38e` | A1/A6: índice duplicado, marcadores, márgenes de listados, galería D4, Schuld duplicado |
| `b0c452f` | A2: cifras y anexos |
| `08e640b` | A5: coherencia entre capítulos |
| `3e00ee4` | A4: bibliografía y atribuciones |
| `45b4cc1` | A3: notación |
| `08aa764` | Glosario |
| `61e23ef` | Citas a las 25 figuras de los capítulos 1–6 |
| `dae81b9` | Borrador del artículo IEEE |

Para revisar un cambio: `git show <commit>`. Para descartarlo: `git revert <commit>`.

## Estado del reporte

- `Docs/Technical_Report.pdf`: 201 páginas, 0 referencias sin resolver, 0 etiquetas duplicadas, marcadores en todas las secciones. Quedan 11 cajas desbordadas de más de 10 pt, cosméticas (rutas en `\texttt`).
- Orden del formato: portada, hoja de Resumen, carta responsiva, advertencia, carta de difusión, índices, capítulos 1–8, referencias, glosario y anexos.
- Las cartas escaneadas se ponen en `Docs/preliminares/carta_responsiva.pdf` y `carta_difusion.pdf`, que no se versionan; el `.tex` las incluye solas.
- **Datos para la carta de difusión**, con el PDF actual:
  - desde la hoja de Resumen, que es la página 2: **200 páginas**;
  - desde la carta de difusión, página 5: **197 páginas**.

  Cambiarán al integrar los escaneos si alguno ocupa más de una hoja.

## Correcciones de contenido verificadas (las más importantes)

1. **§4.2, *subtlety*.** Las medias de TT1 (3.1, 2.8, 3.4 y 3.2) no salen de los datos. Recalculadas de `cbis_ddsm_unified.csv`:
   - masas: 3.98 en malignas frente a 3.88 en benignas; el sentido era el **inverso** al que decía el texto;
   - calcificaciones: 3.23 frente a 3.49.
2. **§6.2.** La dispersión de C4 en masas sobre el entrenamiento es 0.058. El 0.056 de `5a_resumen.csv` es sobre todas las lesiones.
3. **§6.6 y §7.4.** La misma oración decía «205 h a k = 12» y «deja de caber en un día a partir de 15 qubits». Ahora distingue los dos regímenes:
   - las 205 h se miden con `EstimatorQNN`;
   - los 14–15 qubits son una cota inferior calculada con el tiempo de `AerSimulator`.
4. **Azevedo et al. (regla 2).**
   - La fuente propone cinco líneas de trabajo futuro (pp. 12–13).
   - §1.2, §1.3 y §2.1.5 decían que proponen «dos»; ahora dicen que el trabajo retoma dos de ellas como ejes, coherente con las cuatro de §7.5.
5. **§3.2.2.** Quitado «correlaciones de orden superior que los métodos clásicos no capturan». Contradecía §2.1.3 y §3.2.4, y las fuentes citadas no lo afirman.
6. **§4.3.** Quitado que la codificación cuántica «puede revelar estructura no accesible para los métodos clásicos».
7. **Anexo E.** El generador ahora:
   - deriva la sección del módulo con `\ref`, convirtiendo la numeración anterior a D-030;
   - incluye D-041 y D-042, con D-041 marcada como *Provisional*.
8. **Anexo D.** La re-ejecución bit a bit cubrió M2–M8, X1–X6, B2 y B3, salvo los tiempos y el muestreo de B3. X7–X9 se ejecutaron después.
9. **§5.7** define «Arquitectura A/B», un término que se usaba sin definir.
10. **§6.0.** El test no interviene en decisiones de diseño; las variantes de sensibilidad se evaluaron después de fijarlo.
11. **§6.7.** B3 usa `SamplerV2`; el OE-6 usa muestreo multinomial.
12. **Bibliografía.**
    - Zebari et al. (2021) era una plantilla sin rellenar («Author(s). [Article title]»).
    - Toufah, Kadim y El Hafidi (2025) tenía los autores en otro orden; en el texto ahora se cita como «Toufah et al.».
    - Mashekova et al. (2025) tenía la lista de autores incompleta.
    - 13 entradas quedan comentadas, no borradas: 3 duplicadas y 10 que nadie cita. Se imprimen 67 referencias.
13. **Glosario.** 65 términos, revisados contra las definiciones del reporte. Corregidos los de dimensión efectiva, heurística de la mediana y *ansatz*; quitados tres términos que el reporte no usa.
14. **Figuras.** Las 25 figuras de los capítulos 1–6 que no se citaban ahora se citan en el párrafo que las comenta.

## Hallazgos de Gemini que resultaron falsos (descartados)

- **A5-5, en parte.** Decía que Azevedo et al. usaron el CBIS-DDSM; usaron BCDR, y el reporte ya lo dice bien. La parte de «dos líneas» sí era real y se corrigió.
- **A4-5 y A4-9.** Auditaron una versión vieja de §1.1. El texto actual ya dice 33 % y ya no cita Sung et al. (2021).
- **A4-7.** Decía que la tabla 2.1 tiene una fila «Solo calcs.» y que Baccouche et al. dice «only mass cases». Ninguna de las dos cosas existe.

## Decisiones que te tocan

1. **Título.** El protocolo registra «Modelo de transformación cuántica variacional de características de cáncer de mama para un sistema híbrido de prediagnóstico». La segunda portada de TT1 y CLAUDE.md usaban otro. El reporte y el artículo usan el del protocolo, que es el que irá en la carta de difusión.
2. **Resumen y abstract** (`Docs/capitulos/0_Preliminares/`). Son borradores míos: los de TT1 describían el diseño anterior, con `TorchConnector`.
3. **Fecha de TT2.** Está en la macro `\fechaTTII` de `Technical_Report.tex`.
4. **Objetivos y conclusiones** con `ZZFeatureMap`/`PauliFeatureMap` (§1.4, §6.8, §7.1). Los dejé así porque D-041 está pendiente con los directores. CLAUDE.md pide los nombres de función.
5. **«Introducción».** El formato pide INTRODUCCIÓN como primera sección del índice, y el capítulo 1 se llama «Panorama General» con la introducción en 1.1. Opciones:
   - dejarlo así;
   - renombrar el capítulo a «Introducción».
6. **«Anexos» o «Apéndices».** El formato dice «Apéndice».
7. **Estilo de la bibliografía.** El reporte está en APA, uniforme; el artículo ya está en IEEE. ¿Pasar también el reporte a IEEE? A las fuentes web les falta la fecha de consulta.
8. **Propuestas de A5 que añaden contenido.**
   - A5-4: estadística de agrupamiento por paciente dentro de §4, que ahora solo aparece en §5 y §6.
   - A5-14: los objetivos nombran cuatro métricas; se evalúan seis.
9. **Notación.**
   - A3-11: $n$ se usa para muestras, disparos y condiciones según la sección.
   - A3-10: $\theta$ sin negrita en las tablas.
   - A3-12: X1/B3 en el texto sin `\ref`.
10. **Tabla 2.1, Wang et al. (2020).** La columna CBIS-DDSM dice «Parcial», pero usaron el DDSM original.
11. **Agradecimientos.** Opcionales; están comentados en el `.tex`.
12. **Artículo.** Faltan los correos de los directores (`% [VERIFICAR]` en `Docs/articulo/articulo.tex`).
13. **Push.** Diez commits locales esperan tu revisión.

## DVD: estado de cada carpeta

| Carpeta | Estado |
|---|---|
| PROTOCOLO FINAL | Escanear el protocolo firmado (`Other/ESCOM/Protocolo.pdf` es la versión sin firmas) |
| REPORTE TÉCNICO FINAL | Listo salvo cartas, fecha y tus decisiones |
| ARTÍCULO TÉCNICO | Borrador en `Docs/articulo/` |
| PRESENTACIONES | Falta la de TT2; la de TT1 está en `Documents/ESCOM/TT` en `.pptx`, hay que exportarla a PDF |
| MANUALES NINGUNO | El protocolo no promete manuales |
| ARCHIVOS EJECUTABLES | `Code/` |
| FOTOS Y VIDEO | Pendiente: capturas JPG y video narrado de los notebooks |

No preparé el script de la estructura del DVD; queda para otro día.
