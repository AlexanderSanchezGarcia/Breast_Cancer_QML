# Ronda 10 · «Defensa TT 2026-B039»: la diapositiva de viabilidad se divide en dos (costo computacional y medición en hardware)

La diapositiva 20, «Simular cabe; medir en hardware sería el problema», mezcla dos mensajes y no muestra ningún costo real. Se divide en dos diapositivas, cada una con un solo mensaje:
- **20 · NUEVA · «Simular 12 qubits fue barato; entrenar θ, no»**: una gráfica de barras con los tiempos reales del trabajo.
- **21 · «Medir en hardware sería el problema»**: el video de los disparos, que ya existe, con una línea de costo.

La gráfica actual de «qubits que caben en 24 h» sale de la parte principal; esa información ya está en los Anexos 82 (Fig. 6.6.1) y 114 (Cuadro 31). **No se crea ningún anexo nuevo: los números de anexo 1 a 122 no cambian.**

Las reglas de las rondas anteriores siguen vigentes. **No inventes ni redondees cifras:** todas salen de este documento.

**Importante sobre los videos:** no cambies el texto alternativo de las imágenes de los siete videos; en particular, el del video de los disparos debe seguir empezando con «Video: 10 rondas reales de 1,024 disparos…». Ninguna imagen nueva puede empezar con «Video».

---

## Nuevo orden y tiempos (solo cambia del 20 en adelante)

| # | Diapositiva | Cambio | Tiempo (acumulado) |
|---|---|---|---|
| 1–19 | Sin cambios | — | (16:15 al terminar la 19) |
| 20 | **NUEVA · Simular 12 qubits fue barato; entrenar θ, no** | nueva | 0:50 (17:05) |
| 21 | **Medir en hardware sería el problema** (antes 20) | solo el video y el costo | 0:45 (17:50) |
| 22 | Objetivos cumplidos (antes 21) | — | 0:55 (18:45) |
| 23 | Trabajo futuro (antes 22) | — | 0:35 (19:20) |
| 24 | Gracias (antes 23) | — | 0:10 (19:30) |
| 25–27 | Índices (antes 24–26) | — | — |
| 28–170 | Anexos 1–122, mismos números | — | — |

- La parte principal pasa a **24 diapositivas**: actualiza los contadores a «n / 24». El deck queda en **170 diapositivas**.
- Actualiza el «Tiempo objetivo» y el «acumulado» de las notas de la 20 a la 24 según la tabla.

---

## 20 · NUEVA · «Simular 12 qubits fue barato; entrenar θ, no»

- Etiqueta de sección: «04 · Viabilidad». Sin insignia ① ②.
- **Visual: una «escalera de tiempos».** Gráfica de barras horizontales, una debajo de otra, con el **eje horizontal en escala logarítmica de tiempo**. Las marcas del eje van rotuladas en unidades humanas, no en potencias de 10: «1 s», «1 min», «1 h», «1 día», «1 semana» (en segundos: 1, 60, 3,600, 86,400 y 604,800). El eje empieza en 0.1 s.
- Cinco barras, de arriba abajo. La etiqueta va a la izquierda de cada barra, y el valor, al final de la barra, en grande:

| # | Etiqueta (izquierda) | Aclaración (debajo de la etiqueta, pequeña y gris) | Valor para dibujar (s) | Rótulo del valor | Estilo |
|---|---|---|---|---|---|
| 1 | Transformación clásica (C3) | todas las lesiones de un subconjunto | 0.2 | **0.2 s** | barra llena, `CLASICO` |
| 2 | Kernel entre 200 lesiones · atajo de simulación | vector de estado; solo existe en simulación | 1.5 | **1.5 s** | barra llena, `C4` |
| 3 | Embedding cuántico (C4 o C5) | los 12 ⟨Zᵢ⟩ de todas las lesiones de un subconjunto | 14 | **14 s** | barra llena, `C4` |
| 4 | Kernel entre 200 lesiones · como en hardware | 19,900 circuitos *compute-uncompute* | 2,784 | **46 min** | barra rayada o con borde y relleno tenue, `C4` |
| 5 | Entrenar θ por *parameter-shift* | 50 épocas, un mapa, masas y calcificaciones | 687,600 | **191 h ≈ 8 días** | barra rayada o con borde y relleno tenue, `DESTACADO` |

- Leyenda pequeña bajo la gráfica: «barra llena = medido · barra rayada = estimado con el tiempo medido por par o por lesión».
- **Pasos:**
  1. Entran las barras 1, 2 y 3, con el rótulo de grupo «lo que se ejecutó: segundos».
  2. Entra la barra 4.
  3. Entra la barra 5 y, a su derecha o encima, un recuadro con borde `DESTACADO`: «Por eso θ quedó fijo: la Arquitectura B es ~1,900 veces más barata».
  4. Entra, abajo y a todo el ancho, la frase: «Cada qubit extra casi duplica el costo: simular un estado tarda **2.9 ms** con 12 qubits y **75 s** con 28».
- Pie: «Apple M3, 16 GiB · simulación exacta con Qiskit · k = 12 · tiempos de los módulos 5 y 8 y de los estudios B1 y X9».
- **Notas:** *Tiempo objetivo: 0:50 (acumulado 17:05).* ¿Cuánto costó simular? Con 12 qubits, poco. Todo se ejecutó en esta laptop: la transformación clásica tarda 0.2 segundos; el kernel de 200 lesiones, 1.5 segundos con el atajo de la simulación, y el embedding cuántico de todas las lesiones, unos 14 segundos. El eje es logarítmico: cada marca es mucho más grande que la anterior. Si el kernel se calculara como en un procesador real, un circuito por par, serían 46 minutos. Y entrenar θ por parameter-shift, que pide dos evaluaciones del circuito por cada parámetro, costaría unas 191 horas por mapa, ocho días. Por eso θ quedó fijo: la Arquitectura B es unas 1,900 veces más barata. Además, cada qubit extra casi duplica el costo: un estado tarda 2.9 milisegundos con 12 qubits y 75 segundos con 28. [Si preguntan hasta cuántos qubits caben: Anexo 82, Fig. 6.6.1, y Anexo 114, Cuadro 31. Embedding hasta ~25, kernel hasta ~22 y entrenar θ hasta ~14–15 en 24 h. Los 191 h son con EstimatorQNN de Qiskit; con el simulador más rápido serían al menos 5.7 h.]

## 21 · «Medir en hardware sería el problema» (antes 20)

- Mismo título y etiqueta «04 · Viabilidad».
- **Quita la gráfica de barras de qubits** («Embedding exacto… hasta ~25 qubits», «Kernel entre 200 lesiones…», «Entrenar θ…», el eje de 0 a 30 y «Qubits que caben en 24 h»). Esa información ya está en los Anexos 82 y 114.
- El **video de los disparos** pasa a ocupar el área principal, más grande que hoy, con su mismo texto alternativo.
- **Arriba del video**, una línea en grande: «Una matriz de 200 lesiones = **19,900 circuitos × 1,024 disparos ≈ 20 millones de ejecuciones**».
- **Paso (igual que hoy):** «Los ⟨Zᵢ⟩ sí toleran 1,024 disparos: el MLP queda a menos de 0.02 del AUC exacto».
- **Notas:** *Tiempo objetivo: 0:45 (acumulado 17:50).* En simulación todo cupo; el problema estaría en el hardware. Una matriz de 200 lesiones son 19,900 circuitos, y cada valor se estima como una encuesta: se repite el circuito 1,024 veces y se cuenta cuántas veces salen todos los qubits en cero. Son unos 20 millones de ejecuciones por matriz. Si el valor real es 0.002, se esperan unas dos respuestas «sí» de 1,024, y muchas veces no sale ninguna. Con C4, uno de cada cinco o seis pares se leería exactamente como cero; con C5, tres de cada cuatro. El kernel sería inmedible. En cambio, los valores esperados sí toleran 1,024 disparos. [El video arranca con un clic sobre él. Cifras medidas: C4 21 % (masas) y 16 % (calcificaciones); C5 74 % y 72 %.]

## 22, 23 y 24 (antes 21, 22 y 23)
- Sin cambios de contenido; solo el número, el contador «n / 24» y el tiempo de la tabla.

## Referencias cruzadas en los anexos
- **Anexo 7** («Todo se hizo en simulación exacta, a propósito»), notas: «(diapositiva 20)» pasa a **«(diapositiva 21)»**.
- Revisa si alguna otra nota o texto menciona la diapositiva 20, 21, 22 o 23 y súmale uno.

## Comprobación final antes de exportar
- [ ] 24 diapositivas principales con «n / 24», 170 en total; los anexos conservan sus números 1–122.
- [ ] La 20 nueva tiene el eje logarítmico rotulado en «1 s · 1 min · 1 h · 1 día · 1 semana», y las cinco barras con exactamente 0.2 s, 1.5 s, 14 s, 46 min y 191 h ≈ 8 días; las dos últimas, rayadas («estimado»).
- [ ] La 21 ya no tiene la gráfica de qubits; el video de los disparos conserva su texto alternativo.
- [ ] La referencia del Anexo 7 apunta a la diapositiva 21.
