#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Auditoría A1: Referencias cruzadas, etiquetas y bibliografía (mecánica)
Trabajo Terminal 2026-B039.
"""

import os
import sys
import re
import glob
import difflib
from collections import defaultdict, Counter

REPO_ROOT = "/Users/alexander_san/TT"
DOCS_DIR = os.path.join(REPO_ROOT, "Docs")
TMP_BUILD = "/tmp/aud_A1"

def get_included_files(main_file):
    included = []
    def rec_input(fpath):
        if not os.path.isabs(fpath):
            fpath = os.path.join(DOCS_DIR, fpath)
        if not fpath.endswith(".tex") and not os.path.exists(fpath):
            fpath = fpath + ".tex"
        if not os.path.exists(fpath):
            return
        # Exclude borrador_*.tex and comun/
        rel = os.path.relpath(fpath, DOCS_DIR)
        parts = rel.split(os.sep)
        if any(p.startswith("borrador_") for p in parts):
            return
        if "comun" in parts:
            return
        if fpath in included:
            return
        included.append(fpath)
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        for line in lines:
            clean_line = re.sub(r"(?<!\\)%.*", "", line)
            for m in re.finditer(r"\\input\{([^}]+)\}", clean_line):
                sub = m.group(1).strip()
                rec_input(sub)
    rec_input(main_file)
    return included

def verify_casing_and_exists(base_dir, rel_path, default_exts=None):
    candidates = [rel_path]
    if default_exts:
        for ext in default_exts:
            if not rel_path.endswith(ext):
                candidates.append(rel_path + ext)
    
    found_cand = None
    for cand in candidates:
        full_p = os.path.join(base_dir, cand)
        if os.path.exists(full_p):
            found_cand = cand
            break
            
    if not found_cand:
        return False, "FILE_NOT_FOUND", None
        
    parts = os.path.normpath(found_cand).split(os.sep)
    curr = base_dir
    mismatches = []
    for part in parts:
        if part == ".":
            continue
        try:
            actual_entries = os.listdir(curr)
        except Exception as e:
            return False, f"CANNOT_LIST_DIR: {e}", None
        if part not in actual_entries:
            match = None
            for e in actual_entries:
                if e.lower() == part.lower():
                    match = e
                    break
            if match:
                mismatches.append((part, match))
                curr = os.path.join(curr, match)
            else:
                return False, f"ENTRY_NOT_FOUND: {part}", None
        else:
            curr = os.path.join(curr, part)
            
    if mismatches:
        return False, f"CASE_MISMATCH: {mismatches}", found_cand
    return True, "OK", found_cand

def parse_toc(toc_path):
    toc_sections = {}
    if not os.path.exists(toc_path):
        return toc_sections
    with open(toc_path, "r", encoding="utf-8", errors="ignore") as f:
        toc_text = f.read()
    for m in re.finditer(r"\\contentsline\s*\{([^}]+)\}\{\\numberline\s*\{([^}]+)\}(.*?)\}\{([^}]+)\}", toc_text):
        level, num, title, page = m.groups()
        clean_title = re.sub(r"\\[a-zA-Z]+", "", title).replace("{", "").replace("}", "").strip()
        toc_sections[num] = (level, clean_title, page)
    return toc_sections

def main():
    print("=" * 70)
    print("AUDITORÍA A1: REFERENCIAS, ETIQUETAS, BIBLIOGRAFÍA Y COMPILACIÓN")
    print("=" * 70)

    # 1. Archivos incluidos
    files = get_included_files("Technical_Report.tex")
    print(f"\n[+] Archivos .tex en alcance analizados: {len(files)}")

    # 2. Extracción de etiquetas, referencias, citas y bibitems
    labels = defaultdict(list)
    refs = []
    cites = []
    bibitems = defaultdict(list)
    raw_lines = {}

    for fpath in files:
        rel = os.path.relpath(fpath, DOCS_DIR)
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
        raw_lines[rel] = lines
        for lno, line in enumerate(lines, 1):
            clean_line = re.sub(r"(?<!\\)%.*", "", line)
            # labels
            for m in re.finditer(r"\\label\{([^}]+)\}", clean_line):
                lbl = m.group(1).strip()
                labels[lbl].append((rel, lno))
            # bibitems
            for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", clean_line):
                bkey = m.group(1).strip()
                bibitems[bkey].append((rel, lno, line.strip()))
            # refs
            for m in re.finditer(r"\\([a-zA-Z]*ref)\{([^}]+)\}", clean_line):
                cmd = m.group(1)
                for t in m.group(2).split(","):
                    refs.append((cmd, t.strip(), rel, lno, line.strip()))
            # cites
            for m in re.finditer(r"\\cite[a-zA-Z*]*(?:\[[^\]]*\])*\{([^}]+)\}", clean_line):
                target = m.group(1).strip()
                for k in target.split(","):
                    cites.append((k.strip(), rel, lno, line.strip()))

    print(f"    - Etiquetas definidas: {len(labels)}")
    print(f"    - Referencias en texto: {len(refs)}")
    print(f"    - Claves bibliográficas (bibitem): {len(bibitems)}")
    print(f"    - Citas en texto (cite): {len(cites)}")

    # ----------------------------------------------------
    # ÍTEM 1 & 2: Etiquetas duplicadas, no referenciadas, inexistentes
    # ----------------------------------------------------
    print("\n" + "=" * 50)
    print("1. ETIQUETAS Y REFERENCIAS CRUZADAS")
    print("=" * 50)

    # Duplicadas
    dup_labels = {k: v for k, v in labels.items() if len(v) > 1}
    print(f"\n[1.1] Etiquetas duplicadas: {len(dup_labels)}")
    for k, v in dup_labels.items():
        print(f"  - {k}: {v}")

    # Referencias a etiquetas inexistentes
    defined_label_names = set(labels.keys())
    unresolved_refs = [r for r in refs if r[1] not in defined_label_names]
    print(f"\n[1.2] Referencias a etiquetas inexistentes: {len(unresolved_refs)}")
    for r in unresolved_refs:
        print(f"  - {r[0]}{{{r[1]}}} en {r[2]}:{r[3]}")

    # Etiquetas nunca referenciadas
    used_label_names = {r[1] for r in refs}
    unused_labels = {k: v for k, v in labels.items() if k not in used_label_names}
    unused_fig_tab = {k: v for k, v in unused_labels.items() if k.startswith("fig:") or k.startswith("tab:")}
    unused_others = {k: v for k, v in unused_labels.items() if not (k.startswith("fig:") or k.startswith("tab:"))}

    print(f"\n[1.3] Etiquetas de figuras y tablas NUNCA referenciadas en el texto: {len(unused_fig_tab)}")
    for k, v in sorted(unused_fig_tab.items()):
        locs = ", ".join(f"{rel}:{lno}" for rel, lno in v)
        print(f"  - {k} ({locs})")

    print(f"\n[1.4] Otras etiquetas nunca referenciadas (ecuaciones, secciones, anexos): {len(unused_others)}")
    counts_by_prefix = Counter(k.split(":")[0] if ":" in k else "otros" for k in unused_others.keys())
    for pref, cnt in counts_by_prefix.most_common():
        print(f"  - Prefijo '{pref}:': {cnt} etiquetas")

    # ----------------------------------------------------
    # ÍTEM 3 & 4: Bibliografía
    # ----------------------------------------------------
    print("\n" + "=" * 50)
    print("2. BIBLIOGRAFÍA (CITAS Y BIBITEMS)")
    print("=" * 50)

    defined_bib_keys = set(bibitems.keys())
    unresolved_cites = [c for c in cites if c[0] not in defined_bib_keys]
    print(f"\n[2.1] Citas a claves sin bibitem: {len(unresolved_cites)}")
    for c in unresolved_cites:
        print(f"  - \\cite{{{c[0]}}} en {c[1]}:{c[2]}")

    used_bib_keys = {c[0] for c in cites}
    unused_bibitems = {k: v for k, v in bibitems.items() if k not in used_bib_keys}
    print(f"\n[2.2] Bibitems que NADIE cita: {len(unused_bibitems)}")
    for k, v in sorted(unused_bibitems.items()):
        locs = ", ".join(f"{rel}:{lno}" for rel, lno, _ in v)
        print(f"  - {k} ({locs})")

    # Duplicados / casi duplicados en bibliografía
    bib_file = os.path.join(DOCS_DIR, "bibliografia.tex")
    with open(bib_file, "r", encoding="utf-8", errors="ignore") as f:
        bib_text = f.read()
    bib_entries = re.split(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", bib_text)
    bib_parsed = {}
    for i in range(1, len(bib_entries), 2):
        k = bib_entries[i].strip()
        c = bib_entries[i+1]
        bib_parsed[k] = c

    # DOIs
    dois = defaultdict(list)
    for k, c in bib_parsed.items():
        m_doi = re.search(r"(?:doi\.org/|doi:\s*)(10\.\d{4,9}/[-._;()/:A-Za-z0-9]+)", c, re.IGNORECASE)
        if m_doi:
            doi = m_doi.group(1).rstrip(".").lower()
            dois[doi].append(k)

    print(f"\n[2.3] Bibitems con el mismo DOI: {sum(1 for keys in dois.values() if len(keys) > 1)}")
    for doi, keys in dois.items():
        if len(keys) > 1:
            print(f"  - DOI {doi}: {keys}")

    # URLs
    urls = defaultdict(list)
    for k, c in bib_parsed.items():
        for m in re.finditer(r"\\url\{([^}]+)\}", c):
            u = m.group(1).strip().rstrip("/")
            urls[u].append(k)

    print(f"\n[2.4] Bibitems con la misma URL: {sum(1 for keys in urls.values() if len(keys) > 1)}")
    for u, keys in urls.items():
        if len(keys) > 1:
            print(f"  - URL {u}: {keys}")

    # ----------------------------------------------------
    # ÍTEM 5: Prefijos incorrectos y ecuación~\ref
    # ----------------------------------------------------
    print("\n" + "=" * 50)
    print("3. PREFIJOS DE REFERENCIAS Y FORMULACIÓN")
    print("=" * 50)

    prefix_issues = []
    for fpath in files:
        rel = os.path.relpath(fpath, DOCS_DIR)
        lines = raw_lines[rel]
        for lno, line in enumerate(lines, 1):
            clean = re.sub(r"(?<!\\)%.*", "", line)
            # Buscar ??
            if "??" in clean:
                prefix_issues.append((rel, lno, "REFERENCIA_INCOMPLETA_??", clean.strip()))
            # Figura con tab:
            for m in re.finditer(r"\b(?:[Ff]igura|[Ff]ig\.)(?:\\[, ]|[~\s])*\\(?:[a-zA-Z]*ref)\{([^}]+)\}", clean):
                for t in m.group(1).split(","):
                    if t.strip().startswith("tab:"):
                        prefix_issues.append((rel, lno, f"FIGURA_APUNTA_A_TABLA: {t.strip()}", clean.strip()))
            # Tabla con fig:
            for m in re.finditer(r"\b(?:[Tt]abla)(?:\\[, ]|[~\s])*\\(?:[a-zA-Z]*ref)\{([^}]+)\}", clean):
                for t in m.group(1).split(","):
                    if t.strip().startswith("fig:"):
                        prefix_issues.append((rel, lno, f"TABLA_APUNTA_A_FIGURA: {t.strip()}", clean.strip()))
            # Ecuación con \ref en lugar de \eqref
            for m in re.finditer(r"\b(?:[Ee]cuaci[oó]n|[Ee]c\.)(?:\\[, ]|[~\s])*\\ref\{([^}]+)\}", clean):
                target = m.group(1).strip()
                prefix_issues.append((rel, lno, f"ECUACION_CON_REF_EN_VEZ_DE_EQREF: {target}", clean.strip()))
            # \ref directo apuntando a eq:
            for m in re.finditer(r"(?<![a-zA-Z])\\ref\{([^}]+)\}", clean):
                target = m.group(1).strip()
                if target.startswith("eq:"):
                    prefix_issues.append((rel, lno, f"REF_A_ECUACION_SIN_EQREF: {target}", clean.strip()))

    print(f"\n[3.1] Problemas de prefijo detectados: {len(prefix_issues)}")
    for rel, lno, kind, text in prefix_issues:
        print(f"  - [{kind}] en {rel}:{lno}")
        print(f"    «{text}»")

    # ----------------------------------------------------
    # ÍTEM 6: Menciones a secciones escritas a mano frente a TOC
    # ----------------------------------------------------
    print("\n" + "=" * 50)
    print("4. MENCIONES A SECCIONES ESCRITAS A MANO Y TABLA DE CONTENIDOS")
    print("=" * 50)

    toc_sections = parse_toc(os.path.join(TMP_BUILD, "Technical_Report.toc"))
    print(f"Entradas numeradas cargadas del .toc: {len(toc_sections)}")

    pat_s = re.compile(r"(?:§|\\S(?![a-zA-Z]))(?:\\[, ]|[~\s])*([0-9A-Za-z]+(?:\.[0-9A-Za-z]+)*)")
    pat_word = re.compile(r"\b(secci[oó]n|secciones|subsecci[oó]n|subsecciones|cap[ií]tulo|cap[ií]tulos|anexo|anexos|ap[eé]ndice|ap[eé]ndices)(?:\\[, ]|[~\s])+([0-9A-Za-z]+(?:\.[0-9A-Za-z]+)*)", re.IGNORECASE)

    handwritten = []
    for fpath in files:
        rel = os.path.relpath(fpath, DOCS_DIR)
        lines = raw_lines[rel]
        for lno, line in enumerate(lines, 1):
            clean = re.sub(r"(?<!\\)%.*", "", line)
            # Find \S or §
            for m in pat_s.finditer(clean):
                full = m.group(0)
                num = m.group(1)
                handwritten.append((rel, lno, "§", full, num, clean.strip()))
            # Find words
            for m in pat_word.finditer(clean):
                wtype = m.group(1)
                full = m.group(0)
                num = m.group(2)
                if num.lower() in ("ref", "eqref", "autoref", "cref", "pageref", "siguiente", "siguientes", "anterior", "anteriores", "del", "de", "correspondiente"):
                    continue
                handwritten.append((rel, lno, wtype, full, num, clean.strip()))

    print(f"\n[4.1] Menciones a mano encontradas: {len(handwritten)}")
    discordant = []
    valid = []
    for rel, lno, ptype, full, num, line in handwritten:
        if num in toc_sections:
            valid.append((rel, lno, ptype, full, num, toc_sections[num][1], line))
        else:
            discordant.append((rel, lno, ptype, full, num, line))

    print(f"\n[4.2] Menciones DISCORDANTES o fuera de TOC: {len(discordant)}")
    for rel, lno, ptype, full, num, line in discordant:
        print(f"  - {rel}:{lno} -> «{full}» (número '{num}' NO EXISTE en TOC)")
        print(f"    Línea: {line[:100]}")

    print(f"\n[4.3] Menciones existentes en TOC (pero escritas a mano sin \\ref): {len(valid)}")
    for rel, lno, ptype, full, num, title, line in valid:
        print(f"  - {rel}:{lno} -> «{full}» (apunta a {num} '{title}')")

    # ----------------------------------------------------
    # ÍTEM 7: Rutas de imágenes, inputs y listings (case-sensitivity)
    # ----------------------------------------------------
    print("\n" + "=" * 50)
    print("5. VERIFICACIÓN DE RUTAS Y SENSIBILIDAD A MAYÚSCULAS")
    print("=" * 50)

    path_issues = []
    for fpath in files:
        rel = os.path.relpath(fpath, DOCS_DIR)
        lines = raw_lines[rel]
        for lno, line in enumerate(lines, 1):
            clean = re.sub(r"(?<!\\)%.*", "", line)
            # \includegraphics
            for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", clean):
                target = m.group(1).strip()
                ok, status, cand = verify_casing_and_exists(DOCS_DIR, target, [".png", ".pdf", ".jpg"])
                if not ok:
                    path_issues.append((rel, lno, "includegraphics", target, status))
            # \input
            for m in re.finditer(r"\\input\{([^}]+)\}", clean):
                target = m.group(1).strip()
                ok, status, cand = verify_casing_and_exists(DOCS_DIR, target, [".tex"])
                if not ok:
                    path_issues.append((rel, lno, "input", target, status))
            # \lstinputlisting
            for m in re.finditer(r"\\lstinputlisting(?:\[[^\]]*\])?\{([^}]+)\}", clean):
                target = m.group(1).strip()
                ok, status, cand = verify_casing_and_exists(DOCS_DIR, target)
                if not ok:
                    path_issues.append((rel, lno, "lstinputlisting", target, status))

    print(f"\n[5.1] Problemas en rutas o diferencias de mayúsculas: {len(path_issues)}")
    for rel, lno, cmd, target, status in path_issues:
        print(f"  - {rel}:{lno} \\{cmd}{{{target}}} -> {status}")

    # ----------------------------------------------------
    # COMPILACIÓN Y LOG: Overfull \hbox > 10pt, Float too large
    # ----------------------------------------------------
    print("\n" + "=" * 50)
    print("6. EXTRACCIÓN DEL LOG DE COMPILACIÓN (/tmp/aud_A1/Technical_Report.log)")
    print("=" * 50)

    log_path = os.path.join(TMP_BUILD, "Technical_Report.log")
    if not os.path.exists(log_path):
        print("[-] No se encontró el log en", log_path)
        return

    with open(log_path, "r", encoding="utf-8", errors="ignore") as f:
        log_text = f.read()

    # Float too large
    floats = re.findall(r"LaTeX Warning: Float too large for page by ([0-9.]+)pt on input line (\d+)", log_text)
    print(f"\n[6.1] Float too large: {len(floats)}")
    for fl in floats:
        print(f"  - Float too large by {fl[0]}pt on input line {fl[1]}")

    # Overfull \hbox > 10pt
    log_lines = log_text.splitlines()
    overfull_hboxes = []
    for i, line in enumerate(log_lines):
        m = re.search(r"Overfull \\hbox \(([0-9.]+)pt too wide\)(?: in paragraph)? at lines? (\d+)(?:--(\d+))?", line)
        if m:
            pts = float(m.group(1))
            if pts >= 10.0:
                start_l = int(m.group(2))
                end_l = int(m.group(3)) if m.group(3) else start_l
                snippet = []
                for j in range(i+1, min(i+10, len(log_lines))):
                    l_str = log_lines[j].strip()
                    if l_str.startswith("Overfull") or l_str.startswith("Underfull") or re.match(r"^\[\d+\]", l_str) or l_str.startswith("(") or l_str.startswith(")"):
                        break
                    snippet.append(l_str)
                snip_text = " ".join(snippet)
                
                # Attribute source file
                source_loc = "Desconocido"
                if "Depuracin y se-lec-cin de com-po-nen-te" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:36 (caption Listado 2 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Recorte de re-gin de in-te-rs con mar-gen" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:44 (caption Listado 3 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Configuracin del ex-trac-tor Py-Ra-dio-mics" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:56 (caption Listado 4 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Seleccin vo-raz por" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:67 (caption Listado 5 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Transformacin an-gu-lar por cuan-ti-les" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:75 (caption Listado 6 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Generacin y ba-lan-ceo de folds" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:83 (caption Listado 7 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Construccin de ma-pas cun-ti-cos, an-satz con" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:94 (caption Listado 8 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Evaluacin de ma-tri-ces de ker-nel cl-si-co" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:102 (caption Listado 9 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Centrado ma-tri-cial y ali-nea-mien-to kernel-objeti" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:113 (caption Listado 10 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Clculo de la di-fe-ren-cia geo-m-tri-ca re-gu-la-r" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:121 (caption Listado 11 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Definicin del per-cep-trn mul-ti-ca-pa" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:132 (caption Listado 12 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Bucle de en-tre-na-mien-to con pa-ra-da" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:140 (caption Listado 13 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Clculo del co-efi-cien-te de Spear-man" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:151 (caption Listado 14 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Muestreo mul-ti-no-mial de me-di-cio-nes" in snip_text:
                    source_loc = "capitulos/A_Anexos/A.1_codigo.tex:159 (caption Listado 15 vía \\lstlistoflistings en Technical_Report.tex:402)"
                elif "Nat. Com-mun." in snip_text:
                    source_loc = "capitulos/3_Marco_Teorico/3.4.2_geometric_difference.tex:87"
                elif "pauli_feature_map(paulis=['Y'" in snip_text:
                    source_loc = "capitulos/3_Marco_Teorico/3.2.4_paulifeaturemap.tex:28-29"
                elif "an-satz \\T1/cmtt/m/n/12 real_amplitudes" in snip_text or "zz_feature_map \\T1/ptm/m/n/12 en C4" in snip_text:
                    source_loc = "capitulos/3_Marco_Teorico/3.3.3_integracion.tex:19-21"
                elif "fea-tu-re map" in snip_text or "zz_feature_map(12" in snip_text:
                    source_loc = "capitulos/3_Marco_Teorico/3.3.4_implementacion_qiskit.tex:10"
                elif "mar-ca-das co-mo ob-so-le-tas" in snip_text:
                    source_loc = "capitulos/3_Marco_Teorico/3.3.4_implementacion_qiskit.tex:19"
                elif "real_amplitudes()" in snip_text and "BlueprintCircuit" in snip_text:
                    source_loc = "capitulos/3_Marco_Teorico/3.3.4_implementacion_qiskit.tex:19"
                elif "SecondaryCapture" in snip_text or "SOPClassUID" in snip_text:
                    source_loc = "capitulos/4_EDA/4.4_imagenes_dicom.tex:36-39"
                elif "IRRE-GU-LA-R/SPICULATED" in snip_text:
                    source_loc = "capitulos/4_EDA/4.5_hallazgos.tex:28"
                elif "Obsolescencia" in snip_text or "PauliFeatureMap" in snip_text:
                    source_loc = "capitulos/6_Resultados/6.7_lecciones_implementacion.tex:88"

                overfull_hboxes.append((pts, start_l, end_l, source_loc, snip_text))

    print(f"\n[6.2] Overfull \\hbox >= 10pt: {len(overfull_hboxes)}")
    for pts, s_l, e_l, loc, snip in overfull_hboxes:
        print(f"  - {pts}pt en {loc}: {snip[:80]}")

if __name__ == "__main__":
    main()
