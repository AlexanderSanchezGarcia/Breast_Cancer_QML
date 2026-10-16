"""Verifica las cifras de los capítulos de Docs/capitulos/ contra las fuentes que declara cada párrafo.

Cada párrafo, ítem o pie con cifras debe ir precedido de un comentario `% fuente: H-042, D-036; 7_test.csv`.
Para cada número con decimales del párrafo se busca:
  1. en el texto de las entradas de la bitácora citadas (tal como está escrito, admitiendo coma de miles y signo −);
  2. en los CSV citados y en los CSV que nombran esas entradas (con la tolerancia de redondeo de trazabilidad_cifras.py).
Lo que no aparece en ninguna fuente se reporta como NO_ENCONTRADO: puede ser derivado, venir de otra entrada o ser una
invención. Los párrafos con cifras y sin comentario de fuente se reportan como SIN_FUENTE.

Uso: python Code/tools/verificar_cifras_capitulos.py Docs/capitulos/6_Resultados [Docs/capitulos/4_EDA ...]
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from trazabilidad_cifras import CSV_NAME, ROOT, load_pool, match  # noqa: E402

# Como NUM de trazabilidad_cifras, pero acepta un punto final de oración tras el número.
NUM = re.compile(r'(?<![\w.§/])[-−]?\d+\.\d+(?!\d)(?!\.\d)(?!\s*\\times\s*10)')

ENTRY = re.compile(r'\b([DHQ])-(\d{3})\b')
FUENTE = re.compile(r'%\s*fuente:\s*(.*)', re.I)


def bitacora_entries():
    bit = (ROOT / 'Other/bitacora_decisiones.md').read_text(encoding='utf-8')
    out = {}
    for part in re.split(r'\n(?=### [DHQ]-\d{3} · )', bit):
        m = re.match(r'### ([DHQ])-(\d{3}) · ', part)
        if m:
            out[f'{m.group(1)}-{m.group(2)}'] = part
    return out


def blocks(tex):
    """Párrafos separados por línea en blanco. La fuente de un párrafo es el comentario `% fuente:` que contiene,
    o el del bloque inmediatamente anterior si ese bloque solo tiene comentarios."""
    out, pending = [], None
    for block in re.split(r'\n\s*\n', tex):
        lines = block.split('\n')
        found = [FUENTE.search(l).group(1) for l in lines if FUENTE.search(l)]
        only_comments = all(l.lstrip().startswith('%') or not l.strip() for l in lines)
        if only_comments:
            pending = found[-1] if found else pending
            continue
        source = found[-1] if found else pending
        pending = None
        body = '\n'.join('' if l.lstrip().startswith('%') else re.split(r'(?<!\\)%', l)[0] for l in lines)
        body = re.sub(r'\\(label|ref|eqref|cite|input|includegraphics)(\[[^\]]*\])?\{[^}]*\}', ' ', body)
        if NUM.search(body):
            out.append((source, body))
    return out


def in_text(tok, text):
    t = tok.replace('-', '−') if tok.startswith('-') else tok
    variants = {tok, t, tok.lstrip('-−'), tok.replace('.', ',')}
    return any(re.search(r'(?<![\d.])' + re.escape(v) + r'(?![\d])', text) for v in variants)


def main(folders):
    entries, pool = bitacora_entries(), load_pool()
    rows = []
    for folder in folders:
        for f in sorted(Path(folder).glob('*.tex')):
            for source, body in blocks(f.read_text(encoding='utf-8')):
                cited_e = ENTRY.findall(source or '')
                texts = [entries.get(f'{a}-{b}', '') for a, b in cited_e]
                csvs = set(CSV_NAME.findall(source or ''))
                for t in texts:
                    csvs |= set(CSV_NAME.findall(t))
                arrays = [pool[c] for c in csvs if c in pool]
                for m in NUM.finditer(body):
                    tok = m.group(0).replace('−', '-')
                    if source is None:
                        status = 'SIN_FUENTE'
                    elif any(in_text(tok, t) for t in texts):
                        status = 'EN_BITACORA'
                    elif any(match(float(tok), len(tok.split('.')[1]), a) for a in arrays):
                        status = 'EN_CSV'
                    else:
                        status = 'NO_ENCONTRADO'
                    ctx = re.sub(r'\s+', ' ', body[max(0, m.start() - 60):m.end() + 40])
                    rows.append((f.name, tok, status, source or '', ctx))
    bad = [r for r in rows if r[2] in ('NO_ENCONTRADO', 'SIN_FUENTE')]
    counts = {s: sum(r[2] == s for r in rows) for s in ('EN_BITACORA', 'EN_CSV', 'NO_ENCONTRADO', 'SIN_FUENTE')}
    print(f'{len(rows)} cifras: ' + ', '.join(f'{k} {v}' for k, v in counts.items()))
    for r in bad + [r for r in rows if r[2] == 'EN_CSV']:
        tag = r[2] if r[2] != 'EN_CSV' else 'EN_CSV(revisar)'
        print(f'{tag:15s} {r[0]:32s} {r[1]:>9s}  [{r[3][:40]}]  …{r[4]}…')
    return bad


if __name__ == '__main__':
    main(sys.argv[1:] or [str(ROOT / 'Docs/capitulos/6_Resultados')])
