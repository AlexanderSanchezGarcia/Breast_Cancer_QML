"""Comprueba que cada archivo de Docs/codigo/ es copia exacta de la celda que declara su cabecera,
y que cada \\lstinputlisting de los anexos apunta a un archivo que existe.

Uso: python Code/tools/verificar_listados.py [Docs/capitulos/A_Anexos]
Sale con código 1 si algún archivo no coincide con su notebook o falta.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extraer_codigo import RAIZ, SALIDA, extraer  # noqa: E402

CABECERA = re.compile(r"^# fuente: (\S+\.ipynb) · celda de código (\d+)(?: · líneas (\d+-\d+))?$")


def main() -> int:
    fallos = 0
    archivos = sorted(SALIDA.glob("*.py"))
    for f in archivos:
        texto = f.read_text()
        m = CABECERA.match(texto.splitlines()[0]) if texto else None
        if not m:
            print(f"{f.name}: SIN CABECERA VÁLIDA")
            fallos += 1
            continue
        try:
            esperado = extraer(m.group(1), int(m.group(2)), m.group(3))
        except (IndexError, FileNotFoundError) as e:
            print(f"{f.name}: la celda declarada no existe ({e})")
            fallos += 1
            continue
        ok = texto == esperado
        print(f"{f.name}: {'OK' if ok else 'DIFIERE del notebook'}")
        fallos += not ok
    anexos = Path(sys.argv[1]) if len(sys.argv) > 1 else RAIZ / "Docs/capitulos/A_Anexos"
    for tex in sorted(anexos.glob("*.tex")) if anexos.is_dir() else []:
        for ruta in re.findall(r"\\lstinputlisting(?:\[[^\]]*\])?\{([^}]+)\}", tex.read_text()):
            destino = RAIZ / "Docs" / ruta
            if not destino.exists():
                print(f"{tex.name}: \\lstinputlisting apunta a {ruta}, que no existe")
                fallos += 1
    print(f"\n{len(archivos)} listados; {fallos} problemas.")
    return 1 if fallos else 0


if __name__ == "__main__":
    sys.exit(main())
