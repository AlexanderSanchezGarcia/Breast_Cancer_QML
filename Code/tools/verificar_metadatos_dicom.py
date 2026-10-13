"""Verifica sobre todas las mamografías del CBIS-DDSM las etiquetas DICOM que condicionan el diseño (H-002).

H-002 se midió sobre una muestra de 25 mamografías. Este script lee la cabecera (sin píxeles) de cada
mamografía completa distinta del índice unificado y cuenta en cuántas está presente cada etiqueta.

Uso (entorno radiomics o qml_cancer, con pydicom): python Code/tools/verificar_metadatos_dicom.py
Salida: Code/results/1_metadatos_dicom.csv
"""
from pathlib import Path

import pandas as pd
import pydicom

ROOT = Path(__file__).resolve().parents[2]
TAGS = ['PixelSpacing', 'ImagerPixelSpacing', 'Manufacturer', 'Modality', 'BitsStored', 'PhotometricInterpretation']

index = pd.read_csv(ROOT / 'Data/cbis_ddsm_unified.csv')
paths = index['path_full_mammo'].dropna().unique()
rows = []
for p in paths:
    ds = pydicom.dcmread(p, stop_before_pixels=True)
    rows.append({t: (str(ds.get(t)) if t in ds and ds.get(t) not in (None, '') else None) for t in TAGS})
meta = pd.DataFrame(rows)

out = pd.DataFrame({
    'etiqueta': TAGS,
    'presente': [meta[t].notna().sum() for t in TAGS],
    'ausente': [meta[t].isna().sum() for t in TAGS],
    'valores': [', '.join(f'{v} ({n})' for v, n in meta[t].value_counts().items()) for t in TAGS],
})
out.to_csv(ROOT / 'Code/results/1_metadatos_dicom.csv', index=False)
print(f'{len(index)} registros, {len(paths)} mamografías distintas')
print(out.to_string(index=False))
