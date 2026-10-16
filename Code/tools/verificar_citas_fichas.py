"""Comprueba que cada cita literal de las fichas de lectura aparece en el PDF, en la página declarada.

Las fichas están en Docs/insumos/fichas/<clave>.md y el texto de cada PDF, página por página,
en Docs/fuentes/txt/<clave>/pNNN.txt (lo genera el coordinador con PyMuPDF).

Formato de cita que se verifica, en cualquier línea de la ficha:
    «texto literal en el idioma original» (p. 7)
    «texto que cruza de página» (pp. 7–8)

La comparación ignora espacios, saltos de línea, guiones de corte de línea, ligaduras tipográficas
y la diferencia entre comillas rectas y curvas. Nada más: si una palabra cambia, la cita falla.

Fuera de las fichas (auditorías, comentarios de respaldo en los .tex) la cita lleva la clave:
    «texto literal» (Clave, p. 7)        % respaldo: «texto literal» (Clave, pp. 7–8)

Uso: python Code/tools/verificar_citas_fichas.py [archivo.md|archivo.tex|carpeta ...]
Sin argumentos revisa todas las fichas. Una carpeta se recorre buscando .md y .tex. Sale con código 1 si alguna cita no se encuentra.
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
FICHAS = RAIZ / "Docs/insumos/fichas"
TXT = RAIZ / "Docs/fuentes/txt"

CITA = re.compile(r"«([^»]+)»\s*\((?:([A-Za-z][A-Za-z0-9]*),\s*)?pp?\.\s*(\d+)(?:\s*[–-]\s*(\d+))?\)")
LIGADURAS = {"ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl", "ﬅ": "st", "ﬆ": "st"}
COMILLAS = {"“": '"', "”": '"', "„": '"', "‘": "'", "’": "'", "´": "'", "`": "'", "−": "-", "–": "-", "—": "-"}


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKC", texto)
    for a, b in {**LIGADURAS, **COMILLAS}.items():
        texto = texto.replace(a, b)
    texto = re.sub(r"(\w)-\s*\n\s*(\w)", r"\1\2", texto)  # guion de corte de línea
    texto = re.sub(r"\s+", "", texto)                      # sin espacios: robusto a la maquetación
    return texto.lower()


def paginas(clave: str, ini: int, fin: int) -> str | None:
    d = TXT / clave
    if not d.is_dir():
        return None
    partes = []
    for n in range(ini, fin + 1):
        f = d / f"p{n:03d}.txt"
        if not f.exists():
            return None
        partes.append(f.read_text())
    return "\n".join(partes)


def revisar(ficha: Path) -> tuple[int, list[str]]:
    texto = ficha.read_text()
    errores, total = [], 0
    for m in CITA.finditer(texto):
        total += 1
        clave = m.group(2) or ficha.stem
        cita, ini = m.group(1), int(m.group(3))
        fin = int(m.group(4) or ini)
        fuente = paginas(clave, ini, fin)
        if fuente is None:
            errores.append(f"  página {ini}–{fin} inexistente para {clave}: «{cita[:70]}»")
            continue
        if normalizar(cita) not in normalizar(fuente):
            # ¿Está en otra página? Ayuda a corregir, pero sigue siendo error.
            if not (TXT / clave).is_dir():
                errores.append(f"  clave sin texto fuente: {clave}")
                continue
            otras = [p.stem for p in sorted((TXT / clave).glob("p*.txt")) if normalizar(cita) in normalizar(p.read_text())]
            pista = f" (sí aparece en {', '.join(otras)})" if otras else " (no aparece en ninguna página)"
            errores.append(f"  NO ENCONTRADA en {clave} p. {ini}–{fin}{pista}: «{cita[:90]}»")
    return total, errores


def main() -> int:
    fichas = []
    for a in sys.argv[1:]:
        p = Path(a)
        fichas += sorted(list(p.rglob("*.md")) + list(p.rglob("*.tex"))) if p.is_dir() else [p]
    fichas = fichas or sorted(FICHAS.glob("*.md"))
    fallos = 0
    for f in fichas:
        if f.parent.resolve() == FICHAS.resolve() and not (TXT / f.stem).is_dir():
            print(f"{f.name}: SIN TEXTO FUENTE (el nombre de la ficha debe ser la clave del PDF)")
            fallos += 1
            continue
        total, errores = revisar(f)
        estado = "OK" if total and not errores else ("SIN CITAS" if not total else "FALLA")
        print(f"{f.name}: {estado} · {total - len(errores)}/{total} citas verificadas")
        for e in errores:
            print(e)
        fallos += (estado != "OK")
    print(f"\n{len(fichas) - fallos}/{len(fichas)} fichas pasan.")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
