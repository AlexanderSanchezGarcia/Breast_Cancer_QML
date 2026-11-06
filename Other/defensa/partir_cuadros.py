# Parte los recortes de cuadros demasiado altos para una diapositiva de 16:9 y deja en
# Other/defensa/tablas_anexos/deck/ una imagen por diapositiva, en el orden del deck.
#
# Uso: /opt/anaconda3/bin/python Other/defensa/partir_cuadros.py
#
# - Entrada: tablas_anexos/manifiesto.json y sus PNG (los genera extraer_tablas.py).
# - El área de contenido de un anexo mide ~1680 × 760 px. Una imagen se muestra a escala
#   min(1680/ancho, 760/alto); por debajo de ESCALA_MIN la letra queda demasiado pequeña.
# - Esas imágenes se cortan en k trozos, lo más cerca posible de alturas iguales, solo entre FILAS de la
#   tabla, no entre renglones de una misma celda. Como en la imagen los dos espacios miden casi lo mismo,
#   se usa el texto del PDF dentro del mismo rectángulo que recortó extraer_tablas.py: un corte es válido
#   si el renglón de abajo tiene texto en la primera columna, ninguna de sus columnas empieza con
#   minúscula (sería la continuación de una celda) y ningún fragmento del renglón de arriba acaba en guion.
# - Salida: tablas_anexos/deck/Cuadro_N_k.png (k = 1..n por cuadro) y, en el manifiesto, los campos
#   'diapositivas' (lista de archivos) y 'n_diapositivas'.
import json
import math
from pathlib import Path

import fitz
import numpy as np

import extraer_tablas as ET

DIR = Path(__file__).resolve().parent / 'tablas_anexos'
SALIDA = DIR / 'deck'
ANCHO, ALTO, ESCALA_MIN = 1680, 760, 0.70
MARGEN = 14   # px blancos que se dejan arriba y abajo de cada trozo


def escala(w, h):
    return min(ANCHO / w, ALTO / h)


def filas_blancas(img):
    return (img.min(axis=(1, 2)) >= 245)


def renglones(page, rect, alto_img):
    """Renglones de texto del recorte, en px de la imagen: lista de (y0, y1, grupos), donde cada grupo
    es la lista de palabras de un mismo fragmento de columna (separadas por más de 8 pt de las otras)."""
    f = alto_img / rect.height
    palabras = sorted(page.get_text('words', clip=rect), key=lambda w: ((w[1] + w[3]) / 2, w[0]))
    filas = []
    for w in palabras:
        yc = (w[1] + w[3]) / 2
        if filas and abs(filas[-1]['yc'] - yc) < 2.5:
            filas[-1]['w'].append(w)
        else:
            filas.append({'yc': yc, 'w': [w]})
    lineas = []
    for fl in filas:
        ws = sorted(fl['w'], key=lambda w: w[0])
        grupos = [[ws[0]]]
        for w in ws[1:]:
            (grupos[-1].append(w) if w[0] - grupos[-1][-1][2] < 8 else grupos.append([w]))
        lineas.append((ws, grupos))
    # borde izquierdo de la tabla: el de los renglones con varias columnas (el pie y la nota pueden ser más anchos)
    x_tabla = min(ws[0][0] for ws, g in lineas if len(g) >= 2)
    out = []
    for ws, grupos in lineas:
        y0 = (min(w[1] for w in ws) - rect.y0) * f
        y1 = (max(w[3] for w in ws) - rect.y0) * f
        out.append((y0, y1, grupos, ws[0][0] <= x_tabla + 30))   # primera columna, con sangría de subgrupo
    return out


def corte_valido(arriba, abajo):
    _, _, g_arr, _ = arriba
    _, _, g_ab, col1 = abajo
    if not col1:
        return False
    if any(g[0][4][:1].isalpha() and g[0][4][:1].islower() for g in g_ab):
        return False
    if any(g[-1][4].endswith('-') for g in g_arr):
        return False
    return True


def cortar(img, page, rect_de):
    h, w = img.shape[:2]
    if escala(w, h) >= ESCALA_MIN:
        return [img]
    alto_max = int(ALTO / ESCALA_MIN)                  # alto máximo de un trozo para que se vea a ESCALA_MIN
    k = math.ceil(h / alto_max)
    rect = rect_de()   # solo se calcula si hay que partir (el Cuadro 1, apaisado, no se parte)
    lin = renglones(page, rect, h)
    # cortes posibles: a media altura del hueco entre dos renglones consecutivos que cumplen corte_valido
    validos = [int((a[1] + b[0]) / 2) for a, b in zip(lin, lin[1:]) if corte_valido(a, b)]
    cortes, inicio = [], 0
    for j in range(1, k):
        objetivo = inicio + (h - inicio) // (k - j + 1)
        candidatos = [y for y in validos if inicio + 200 <= y <= min(h - 200, inicio + alto_max)]
        if not candidatos:
            raise SystemExit(f'No hay un corte entre filas cerca de y = {objetivo}')
        y = min(candidatos, key=lambda c: abs(c - objetivo))
        cortes.append(y)
        inicio = y
    trozos, ini = [], 0
    for y in cortes + [h]:
        t = img[ini:y]
        # recorta el blanco sobrante y deja un margen uniforme
        nb = ~filas_blancas(t)
        a, b = np.argmax(nb), len(nb) - np.argmax(nb[::-1])
        t = t[max(0, a - MARGEN):min(len(t), b + MARGEN)]
        trozos.append(t)
        ini = y
    return trozos


def main():
    man = json.load(open(DIR / 'manifiesto.json', encoding='utf-8'))
    doc = fitz.open(str(Path(__file__).resolve().parents[2] / 'Docs' / 'Technical_Report.pdf'))
    SALIDA.mkdir(exist_ok=True)
    for f in SALIDA.glob('*.png'):
        f.unlink()
    for e in sorted(man, key=lambda e: e['orden_deck']):
        trozos = []
        for parte, (archivo, pag) in enumerate(zip(e['archivos'], e['paginas_pdf'])):
            px = fitz.Pixmap(str(DIR / archivo))
            img = np.frombuffer(px.samples, dtype=np.uint8).reshape(px.height, px.width, px.n)[:, :, :3]
            page = doc[pag - 1]
            trozos += cortar(img, page, lambda: ET.compute_crop_rect(page, e['numero'], parte > 0))
        e['diapositivas'] = []
        for k, t in enumerate(trozos, 1):
            nombre = f"Cuadro_{e['numero']}_{k}.png"
            t = np.ascontiguousarray(t)
            fitz.Pixmap(fitz.csRGB, t.shape[1], t.shape[0], t.tobytes(), False).save(str(SALIDA / nombre))
            e['diapositivas'].append(nombre)
        e['n_diapositivas'] = len(trozos)
        escalas = [round(escala(t.shape[1], t.shape[0]), 2) for t in trozos]
        print(f"Cuadro {e['numero']:>2}: {len(trozos)} diapositiva(s), escalas {escalas}")
    json.dump(man, open(DIR / 'manifiesto.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('Total de diapositivas de cuadros:', sum(e['n_diapositivas'] for e in man))


if __name__ == '__main__':
    main()
