"""Trazabilidad de cifras: busca cada número decimal de la bitácora (H-020 en adelante, D-020 en adelante)
y del borrador del §4 en los CSV de Code/results.

Solo busca en los archivos que la propia entrada cita (en su línea «Datos.» o en el texto). Buscar en todos los
CSV no sirve: con más de 100,000 valores, un número cualquiera de 2 o 3 decimales coincide con alguno por azar.
Un número citado con d decimales coincide con un valor x si x, o 100·x para porcentajes, redondea a él.

Como también los archivos citados pueden tener muchos valores, cada coincidencia se califica con su «cobertura»:
la fracción de los 40 números vecinos (v ± k·10⁻ᵈ, k = 1…20) que también coincidirían. Con cobertura baja la
coincidencia es informativa (OK); con cobertura alta pudo ser azar (DEBIL).

Los archivos citados con más de 2,000 valores (por ejemplo, `2_preprocesamiento_qa.csv` o
`6_diferencia_geometrica.csv`) cubren casi todos los números posibles, así que una coincidencia solo con ellos no
prueba nada: se marca SOLO_ARCHIVO_GRANDE y hay que revisarla. Así se encontró que H-039 dice 0.152 donde el CSV
da 0.151.

Estados: OK, DEBIL, SOLO_ARCHIVO_GRANDE, REDONDEO (difiere en una unidad del último decimal), NO_ENCONTRADO (la entrada cita CSV
y la cifra no está en ellos: puede ser derivada, venir de otra entrada, o ser un error) y SIN_CSV_CITADO
(la entrada no cita ningún CSV: no se puede verificar automáticamente).

Uso: python Code/tools/trazabilidad_cifras.py
Salidas: Other/trazabilidad_cifras.csv y Other/trazabilidad_cifras.md
"""
import re
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RESULTS = ROOT / 'Code/results'
NUM = re.compile(r'(?<![\w.§/])[-−]?\d+\.\d+(?![\d.]|\s*×\s*10)')
CSV_NAME = re.compile(r'([A-Za-z0-9_\-]+\.csv)')
LARGE = 2000


def numbers_in_text(text):
    return [(m.group(0).replace('−', '-'), m.start()) for m in NUM.finditer(text)]


def load_pool():
    pool = {}
    for f in sorted(RESULTS.glob('*.csv')):
        df = pd.read_csv(f, low_memory=False)
        vals = [df.select_dtypes('number').to_numpy(float).ravel()]
        for c in df.select_dtypes(exclude='number').columns:          # números escritos dentro de texto
            found = df[c].astype(str).str.findall(r'-?\d+\.?\d*').explode().dropna()
            vals.append(pd.to_numeric(found, errors='coerce').to_numpy(float))
        v = np.concatenate(vals)
        pool[f.name] = v[np.isfinite(v)]
    return pool


def match(value, decimals, arr):
    if arr.size == 0:
        return None
    half, unit = 0.5 * 10 ** -decimals + 1e-12, 10 ** -decimals + 1e-12
    for scale in (1.0, 100.0):
        if np.any(np.abs(arr * scale - value) <= half):
            return 'exacto'
    for scale in (1.0, 100.0):
        if np.any(np.abs(arr * scale - value) <= unit):
            return 'redondeo'
    return None


def coverage(value, decimals, arrays):
    step = 10 ** -decimals
    neighbors = [value + k * step for k in range(-20, 21) if k != 0]
    return np.mean([any(match(n, decimals, a) == 'exacto' for a in arrays) for n in neighbors])


def entries():
    bit = (ROOT / 'Other/bitacora_decisiones.md').read_text(encoding='utf-8')
    body = bit[bit.index('\n## Decisiones'):bit.index('\n## Preguntas abiertas')]
    parts = re.split(r'\n(?=### [DH]-\d{3} · )', body)
    for p in parts:
        m = re.match(r'### ([DH])-(\d{3}) · ', p)
        if m and int(m.group(2)) >= 20:
            yield f'{m.group(1)}-{m.group(2)}', p
    yield 'borrador §4', (ROOT / 'Docs/borrador_secciones_4.md').read_text(encoding='utf-8')


def main():
    pool = load_pool()
    rows = []
    for entry, text in entries():
        cited = [n for n in dict.fromkeys(CSV_NAME.findall(text)) if n in pool]
        for tok, pos in numbers_in_text(text):
            value, decimals = float(tok), len(tok.split('.')[1])
            small = [n for n in cited if pool[n].size <= LARGE]
            hits = [n for n in small if match(value, decimals, pool[n]) == 'exacto']
            big_hits = [n for n in cited if n not in small and match(value, decimals, pool[n]) == 'exacto']
            near = [n for n in small if match(value, decimals, pool[n]) == 'redondeo']
            cov = np.nan
            if not cited:
                status = 'SIN_CSV_CITADO'
            elif big_hits and not hits:
                status, hits = 'SOLO_ARCHIVO_GRANDE', big_hits
            elif hits:
                cov = coverage(value, decimals, [pool[n] for n in hits])
                status = 'OK' if cov <= 0.25 and decimals >= 2 else 'DEBIL'
            elif near:
                status = 'REDONDEO'
            else:
                status = 'NO_ENCONTRADO'
            context = re.sub(r'\s+', ' ', text[max(0, pos - 70):pos + len(tok) + 50])
            rows.append({'entrada': entry, 'cifra': tok, 'decimales': decimals, 'estado': status, 'cobertura_azar': cov,
                         'archivos': ', '.join(hits or near), 'citados_en_entrada': ', '.join(cited), 'contexto': context})
    df = pd.DataFrame(rows)
    df.to_csv(ROOT / 'Other/trazabilidad_cifras.csv', index=False)
    return df


if __name__ == '__main__':
    df = main()
    print(df.estado.value_counts().to_string())
