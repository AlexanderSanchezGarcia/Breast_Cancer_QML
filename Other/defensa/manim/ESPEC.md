# Especificación de las escenas de Manim · Defensa TT 2026-B039

Clips cortos que se insertan en las diapositivas de la presentación de una tesis sobre codificación cuántica de características de mamografías. El jurado no es especialista en computación cuántica: cada clip debe entenderse sin leer mucho texto.

## Reglas comunes (obligatorias)

1. **Manim Community Edition**, entorno ya instalado: `/opt/anaconda3/envs/manim/bin/manim` y `/opt/anaconda3/envs/manim/bin/python`. No instales nada ni crees otros entornos.
2. **Trabaja solo dentro de `Other/defensa/manim/`.** Escribe tus escenas en `escenas/<nombre>.py`. **No modifiques** `datos.py`, `estilo.py`, `preparar_datos.py`, `datos/` ni ningún archivo fuera de esta carpeta. No hagas `git add`, `git commit` ni ninguna otra operación de git.
3. **Ninguna cifra del trabajo se escribe a mano.** Toda cifra (conteos, AUC, medianas, umbrales, fracciones) sale de las funciones de `datos.py`. Importa con `sys.path.insert(0, str(Path(__file__).resolve().parents[1]))` y luego `import datos, estilo`. Si necesitas una cifra que `datos.py` no da, **no la inventes**: déjala fuera y dilo en tu reporte final.
4. **Estilo:** llama a `estilo.configurar()` al inicio del archivo y usa solo los colores y fuentes de `estilo.py` (fondo crema, tinta azul marino, azul = clásico, naranja = C4, verde = C5, magenta solo para una cifra destacada). Texto con `Text(..., font=estilo.FUENTE)`; fórmulas con `MathTex` (LaTeX está instalado). Trazos finos y limpios, estilo plano, sin sombras ni degradados decorativos.
5. **Todo el texto visible en español**, poco y grande: etiquetas cortas, nunca párrafos. Tamaño mínimo legible en un proyector (no menos de unos 28 px de alto a 1080p).
6. **Ritmo:** el clip se reproduce de principio a fin con un clic mientras el expositor habla. Cada «momento» dura 2 a 4 s, con pausas (`self.wait`) entre momentos. Duración total entre 10 y 22 s.
7. **El último fotograma debe resumir el clip por sí solo** (se usa como imagen fija en el PDF): termina con todo lo importante visible y un `self.wait(2)`.
8. **Render:** desde `Other/defensa/manim/`:
   `/opt/anaconda3/envs/manim/bin/manim render --resolution 1920,1080 --frame_rate 30 --format mp4 --media_dir media escenas/<nombre>.py <Clase>`
   El MP4 debe ser H.264 y pesar menos de 20 MB.
9. **Evidencia para revisión**, en `revision/`:
   - `<nombre>_final.png`: el último fotograma (`ffmpeg -sseof -0.1 -i <mp4> -frames:v 1 revision/<nombre>_final.png -y`).
   - `<nombre>_t1.png` … `<nombre>_t4.png`: fotogramas al 20, 45, 70 y 90 % de la duración.
   - Copia el MP4 final a `clips/<nombre>.mp4`.
   - En tu reporte: duración (`ffprobe`), códec, tamaño en MB y la lista de funciones de `datos.py` que usaste para cada cifra visible.
10. **Sin título en el clip.** La diapositiva ya tiene su título; el clip solo lleva etiquetas.
11. **Nada se encima ni se sale de su caja.** Revisa cada fotograma de revision/ al 100 % de tamaño: si dos textos se tocan o un texto toca el borde de su recuadro, sepáralos, abrevia o reduce un poco la fuente (sin bajar de unos 26 px).
12. Si algo no se puede hacer como se pide, haz la versión más cercana y explícalo en el reporte. No te detengas a preguntar por detalles de diseño menores.

## Clips

### 1 · `mapa_trabajo` · El proceso general del trabajo
Un camino de izquierda a derecha con 7 estaciones. Un punto (una «lesión») recorre el camino y cada estación aparece cuando el punto llega:
1. **CBIS-DDSM:** `pipeline()['lesiones']` lesiones · `pipeline()['pacientes']` pacientes. Ícono: un rectángulo tipo mamografía.
2. **Recorte:** «región de interés a resolución original». Ícono: un rectángulo con un recuadro dentro.
3. **Características:** `pipeline()['caracteristicas']` «radiómicas» (forma, intensidad, textura). Ícono: tres barras pequeñas.
4. **Ángulos:** `pipeline()['seleccionadas']` «ángulos en [0, π]». Ícono: un arco con un ángulo marcado.
5. **5 representaciones:** cinco puntos etiquetados C1, C2, C3 (azules: `CLASICO`, `CLASICO_2`, `CLASICO_3`) y C4, C5 (`C4` naranja, `C5` verde).
6. Aquí el camino **se bifurca** en dos estaciones paralelas: **Separabilidad** (arriba) y **Clasificación** (abajo).
7. Los dos caminos se reúnen en **Comparación**.

Al final, una franja discreta bajo el camino: «masas y calcificaciones, por separado». Duración de unos 18 a 22 s.

**Además**, renderiza **7 imágenes fijas** del mismo camino en versión miniatura (recortadas al camino: el PNG final debe medir 1600×220 px, sin márgenes vacíos), para usarlas como «usted está aquí» al inicio de cada sección: `revision/mapa_mini_1.png` … `mapa_mini_7.png`, de 1600×220 px, **con fondo transparente** (`-t` y `--format png` con `-s`, o un `config.transparent = True`). En la imagen k, la estación k va resaltada en `TINTA` y las demás atenuadas en `LINEA`. Solo los nombres de las estaciones, sin cifras.

### 2 · `dos_lecturas` · Las dos formas de leer el estado (REVISADO)
Dato clave verificado: tras Hadamard y las fases ZZ, **las 4,096 probabilidades valen exactamente 1/4096**. Una tira de probabilidades sale plana y no enseña nada. **La información de la lesión está en las fases.** Usa `estado_lesion()['fase_a']` y `['fase_b']`, en (−π, π].
1. Una tira horizontal de 4,096 barras finas cuyo alto es la fase (eje de −π a π, con 0 al centro), con el rótulo «el estado de una lesión: 4,096 fases» y, debajo y pequeño, «todas con la misma probabilidad: la información está en las fases».
2. **Rama (a), «comparar los estados completos → kernel»:**
   - aparece una segunda tira (`fase_b`, «otra lesión»);
   - luego se convierten en **flechas**: cada componente es una flecha unitaria con ángulo `fase_a − fase_b`, y las 4,096 flechas se ponen una tras otra (punta con cola), como una caminata;
   - la caminata da vueltas y termina cerca de donde empezó;
   - se dibuja la flecha resultante, de la salida a la llegada, y aparece «parecido = |resultante|² / 4,096² = » con `lesion()['kernel_c4_con_otra']` redondeado a 4 decimales;
   - rótulo pequeño: «las fases apuntan a todos lados y se cancelan».
   Escala la caminata para que quepa en su recuadro; si 4,096 flechas son pesadas, dibuja la caminata como una sola polilínea de 4,097 vértices.
3. **Rama (b), «resumir en 12 números ⟨Zᵢ⟩ → MLP»:** la tira pasa por una caja «ansatz (θ fijo)» y se convierte en 12 barras verticales con `lesion()['z_c4']`. Usa una escala de −0.25 a 0.25, con esas marcas en el eje, para que las barras se vean.
4. Final: las dos ramas visibles a la vez, la (a) con su rótulo en `CLASICO` y la (b) en `C4`.

Duración de unos 18 a 22 s.

### 3 · `qubit_bloch` · El qubit como flecha en una esfera, y C4 frente a C5
Escena 3D (`ThreeDScene`) con la esfera de Bloch en trazo fino (ecuador y meridiano principales), los polos rotulados `|0⟩` arriba y `|1⟩` abajo, y el eje X.
1. La flecha apunta a `|0⟩`.
2. **Hadamard:** la flecha gira de forma **continua** con la rotación verdadera de H, un giro de π alrededor del eje (X+Z)/√2, hasta `|+⟩` en el ecuador. Rótulo: «Hadamard».
3. **C4, giro en Z:** la flecha gira alrededor de Z un ángulo 2·x, con x = `lesion()['x'][0]`, dejando una estela naranja (`C4`) sobre el ecuador. Rótulo: «C4: giro 2xᵢ en Z, se queda en el ecuador».
4. Vuelve a `|+⟩`.
5. **C5, giro en Y:** desde `|+⟩` la flecha gira alrededor de Y el mismo ángulo 2·x, dejando una estela verde (`C5`) que sale del ecuador. Rótulo: «C5: giro 2xᵢ en Y, sale del ecuador».
6. Final: las dos estelas visibles a la vez.

Cámara fija en un ángulo que deje ver bien el ecuador (por ejemplo `phi=65°`, `theta=-45°`). Los rótulos en 2D (`add_fixed_in_frame_mobjects`). Duración de unos 16 a 20 s.

### 4 · `concentracion` · La concentración del kernel, con datos reales
Dos mapas de calor de 40×40 lado a lado, con escala de color **lineal** de 0 (`FONDO`) a 1 (`TINTA`), la misma para los dos, y una barra de color pequeña.
- Izquierda, fijo: `kernel('RBF')`, rótulo «RBF clásico», mediana `mediana_kernel('RBF')` con 2 decimales.
- Derecha: el kernel C4, que **cambia** recorriendo `c_valores()` **en orden inverso**, de c = 0.02 a c = 1 (`kernel(f'C4_c{c}')`), con transiciones suaves entre matrices de unos 1.5 s cada una. Rótulos que se actualizan: «c = …» y «mediana = …» con `mediana_kernel(f'C4_c{c}')`, con 2 cifras significativas.
- Las filas y columnas 0–19 son benignas y 20–39 malignas: una línea fina divide los bloques y los ejes llevan «benignas» y «malignas».
- Final con c = 1: solo queda la diagonal. Texto: «c = 1: casi todos los pares se ven ortogonales».

Duración de unos 14 a 18 s.

### 5 · `x11_curva` · ¿Cuándo aparece la ventaja?
Ejes: X «α: fracción de etiquetas que siguen la geometría cuántica», de 0 a 1; Y «AUC-ROC», de 0.5 a 1.0. Datos: `x11()`.
1. Ejes y los dos puntos de α = 0, con el rótulo «diagnóstico real».
2. Las dos curvas se **trazan de izquierda a derecha a la vez** (`Create`): naranja (`C4`) «kernel cuántico proyectado», azul (`CLASICO`) «mejor clásico».
3. Al llegar al primer α con `quantum_wins == True`, aparece una línea vertical punteada «α* = …» (ese valor de la tabla) y se sombrea suavemente la zona a su derecha, con el rótulo «ventaja cuántica».
4. Rótulo «tarea diseñada» en α = 1.
5. Final: las curvas completas, la zona sombreada y una llave entre α = 0 y α*: «distancia del diagnóstico a la ventaja».

Duración de unos 14 a 18 s.

### 6 · `disparos` · Medir el kernel con 1,024 disparos
1. Una cuadrícula de 32×32 = 1,024 puntos grises (`LINEA`), rótulo «1,024 disparos».
2. Usa p = `disparos()['mass_C4']['mediana']`. Simula **10 rondas** de 1,024 disparos con `numpy.random.default_rng(seed)` para seed = 0…9 (Bernoulli con probabilidad p). En cada ronda se encienden en naranja los puntos que salieron «sí» (posiciones aleatorias con la misma semilla) y un contador muestra «sí: n de 1,024». Las primeras 3 rondas a ritmo lento (unos 2 s) y las demás rápido (unos 0.5 s).
3. A la derecha se va armando una fila con el conteo de cada ronda; las rondas con 0 se marcan «se lee 0».
4. Final: «valor real ≈ » p con 4 decimales y, debajo, «se leen exactamente 0: C4 » `disparos()['mass_C4']['lee_cero_1024']` en % sin decimales « · C5 » `disparos()['mass_C5']['lee_cero_1024']` en %, con el rótulo «de los pares, masas».

No elijas semillas para que salga un 0: usa exactamente 0…9 y muestra lo que salga. Duración de unos 14 a 18 s.
