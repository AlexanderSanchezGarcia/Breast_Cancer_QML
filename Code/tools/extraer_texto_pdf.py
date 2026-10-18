"""Extrae el texto de un PDF de Docs/fuentes/pdf/ a Docs/fuentes/txt/<Clave>/pNNN.txt, una página por archivo.

NNN es la página del archivo PDF, desde 001, que es la convención que usa verificar_citas_fichas.py.
Imprime el número de páginas y las primeras líneas de la página 1, para comprobar que el PDF es la obra
que se buscaba (título y DOI).

Uso: python3 Code/tools/extraer_texto_pdf.py <Clave> [<Clave> ...]
"""
import sys
from pathlib import Path

import fitz  # PyMuPDF

RAIZ = Path(__file__).resolve().parents[2]
PDF = RAIZ / "Docs" / "fuentes" / "pdf"
TXT = RAIZ / "Docs" / "fuentes" / "txt"


def extraer(clave: str) -> None:
    origen = PDF / f"{clave}.pdf"
    if not origen.is_file():
        print(f"{clave}: FALTA {origen}")
        return
    destino = TXT / clave
    destino.mkdir(parents=True, exist_ok=True)
    with fitz.open(origen) as doc:
        for i, pagina in enumerate(doc, start=1):
            (destino / f"p{i:03d}.txt").write_text(pagina.get_text(), encoding="utf-8")
        primera = doc[0].get_text().strip().splitlines()[:6]
        print(f"{clave}: {len(doc)} páginas")
    for linea in primera:
        print(f"    {linea}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for clave in sys.argv[1:]:
        extraer(clave)
