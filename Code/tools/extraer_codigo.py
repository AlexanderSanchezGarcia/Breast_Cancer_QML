"""Copia literalmente una celda de código de un notebook a Docs/codigo/<nombre>.py, para el Anexo A.

La primera línea del archivo generado es una cabecera que dice de dónde sale el código:
    # fuente: Code/4_Selection_and_Scaling.ipynb · celda de código 12 · líneas 3-28
El resto es la celda tal cual (o el rango de líneas pedido). No se edita a mano:
`verificar_listados.py` vuelve a extraer cada archivo y falla si no coincide.

La «celda de código k» cuenta solo las celdas de código, empezando en 1, en el orden del notebook.

Uso:
    python Code/tools/extraer_codigo.py --listar Code/4_Selection_and_Scaling.ipynb
    python Code/tools/extraer_codigo.py Code/4_Selection_and_Scaling.ipynb 12 m4_seleccion [--lineas 3-28]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
SALIDA = RAIZ / "Docs/codigo"


def celdas_codigo(nb: Path) -> list[str]:
    datos = json.loads((RAIZ / nb).read_text())
    return ["".join(c["source"]) for c in datos["cells"] if c["cell_type"] == "code"]


def extraer(nb: str, k: int, lineas: str | None) -> str:
    fuente = celdas_codigo(Path(nb))[k - 1].splitlines()
    if lineas:
        a, b = (int(x) for x in lineas.split("-"))
        fuente = fuente[a - 1:b]
        rango = f" · líneas {a}-{b}"
    else:
        rango = ""
    return f"# fuente: {nb} · celda de código {k}{rango}\n" + "\n".join(fuente) + "\n"


def main() -> int:
    args = sys.argv[1:]
    if args and args[0] == "--listar":
        for k, c in enumerate(celdas_codigo(Path(args[1])), 1):
            primera = next((l for l in c.splitlines() if l.strip()), "")
            print(f"{k:3d} · {len(c.splitlines()):3d} líneas · {primera[:90]}")
        return 0
    if len(args) < 3:
        print(__doc__)
        return 2
    nb, k, nombre = args[0], int(args[1]), args[2]
    lineas = args[args.index("--lineas") + 1] if "--lineas" in args else None
    SALIDA.mkdir(parents=True, exist_ok=True)
    destino = SALIDA / f"{nombre}.py"
    destino.write_text(extraer(nb, k, lineas))
    print(f"Escrito {destino.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
