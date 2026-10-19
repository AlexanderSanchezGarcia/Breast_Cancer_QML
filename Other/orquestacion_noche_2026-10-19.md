# Orquestación nocturna · 2026-10-18/19

Archivo de estado para retomar si se corta la sesión coordinadora (recordatorio a la 01:27). **Quien retome: lee todo esto antes de actuar.** La última línea de «Bitácora» es el punto exacto donde quedó.

## Acordado con el autor (22:50–23:00)

1. Integrar sobre el mismo `Docs/Technical_Report.tex` (tag `reporte-tt1` = respaldo de TT1).
2. Portada: nombre seguido del apellido; directores por apellido (Montiel, luego Winfield).
3. Fecha de TT2: desconocida; macro `\fechaTTII` = «Noviembre de 2026» marcada PENDIENTE.
4. Manuales: el protocolo (`Other/ESCOM/Protocolo.pdf`, no versionado) no promete ninguno → carpeta `MANUALES NINGUNO`.
5. Limpieza en `Other/` (hecha). 6. Push solo de lo pendiente y la limpieza; **lo demás, commits locales sin push**. Sin atribución a IA en commits.

## Hecho por el coordinador

| Paso | Commit | Push |
|---|---|---|
| Pendiente: §7, §8, X9 | 2060cc4 | sí |
| Limpieza de Other/ | 9ca063b | sí |
| Integración con formato CATT | 52af6c1 | **no** |

Remoto actualizado a `https://github.com/AlexanderSanchezGarcia/Breast_Cancer_QML.git` (el repo se renombró; es PÚBLICO).

## Ola 1 · auditoría (Orca run `run_14455a05dede`, agente antigravity)

Especificaciones: `Docs/insumos/auditoria/` (reglas.md + A1…A6, G1). Informes: `Docs/insumos/auditoria/informe_<ID>.md`.

| ID | Tarea | Modelo | task | dispatch | Estado |
|---|---|---|---|---|---|
| A1 | Referencias, etiquetas, bibitems | gemini-3.8-flash-high | task_5f7d9ed99c1d | ctx_b94ca676535c | lanzada |
| A2 | Cifras entre secciones | gemini-4-argon-high | task_99057d2d788c | ctx_97d7e27b5e23 | lanzada |
| A3 | Terminología y estilo | gemini-3.8-flash-high | task_decea60d6b98 | ctx_305106b9ecf9 | lanzada |
| A4 | Fidelidad de citas, bibliografía | gemini-4-argon-high | task_04b9d44cedf8 | ctx_49c7acc58853 | lanzada |
| A5 | Coherencia lógica | gemini-4-argon-high | task_6cd84bed88ee | ctx_b7c0eed6e377 | lanzada |
| A6 | Formato CATT | gemini-3.8-flash-high | task_908d80912d72 | ctx_f122fd38056a | lanzada |
| G1 | Borrador del glosario | gemini-3.8-flash-high | task_3f1cf8ec520e | ctx_72e16cd026ea | lanzada |

## Fase C (coordinador, al volver la cuota)

1. `orca orchestration run-use --run run_14455a05dede`; `worker-list`/`check`; release de los terminados.
2. `git status --short`: revertir cualquier archivo fuera de `Docs/insumos/auditoria/`.
3. Verificar **cada** hallazgo ALTA/MEDIA contra el archivo, el CSV o la fuente (Gemini ha inventado datos antes). Re-correr `a1_refs.py`.
4. Aplicar correcciones mecánicas verificadas (refs, rótulos, cifras con fuente clara, estilo) en commits locales pequeños; compilar tras cada grupo (`pdflatex` ×3 en /tmp/ttbuild y copiar el PDF a Docs/). Lo que requiere criterio del autor → lista en el informe.
5. Glosario: revisar `glosario_borrador.tex` término a término, copiar a `Docs/capitulos/G_Glosario/glosario.tex`.
6. Informe de la mañana: `Docs/insumos/informe_noche_2026-10-19.md`.

## Ola 2 (si hay tiempo y cuota)

- Artículo técnico IEEE ≤ 6 cuartillas (`Docs/articulo/`), formato del ejemplo (`Other/ESCOM/Ejemplo Articulo Tecnico.pdf`): Resumen, Palabras clave, I Introducción, II Metodología, III Resultados, IV Conclusiones, Referencias IEEE; autores alumno + directores, ESCOM, Tel. 57-29-6000 ext. 52000 y 52021.
- Script de la estructura del DVD `2026-B039/` con las siete carpetas.

## Pendientes del autor detectados

- Título: el protocolo registra «Modelo de transformación cuántica variacional de características de cáncer de mama para un sistema híbrido de prediagnóstico»; la 2.ª portada de TT1 y CLAUDE.md usan «…para un Sistema Híbrido de Prediagnóstico de Cáncer de Mama». El reporte integrado usa el del protocolo.
- Resumen y abstract nuevos son BORRADOR (`Docs/capitulos/0_Preliminares/`); los de TT1 hablaban de TorchConnector.
- Secretaria Ejecutiva: el PDF del formato dice M. en A.N. María Magdalena Saldívar Almorejo; la carta 2026, Lic. Mildred Sandoval García (usar la 2026).
- Agradecimientos: opcionales, comentados en el `.tex`.
- Fecha de TT2; escaneos de carta responsiva y carta de difusión (`Docs/preliminares/`); presentación de TT2 en PDF; video y capturas.
- La bibliografía de TT1 está en APA; el artículo exige IEEE.

## Bitácora

- 23:12 Ola 1 lanzada (7 trabajadores). Recordatorio CronCreate a la 01:27 (one-shot, solo de esta sesión). caffeinate activo 10 h.
