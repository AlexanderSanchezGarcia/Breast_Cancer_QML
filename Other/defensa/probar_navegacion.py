# Pruebas de la navegación de anexos añadida por Other/defensa/insertar_videos.py
#
# Ejecutar con:
#   /opt/anaconda3/bin/python Other/defensa/probar_navegacion.py
import html as html_mod
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import fitz

RAIZ = Path(__file__).resolve().parent
SCRIPT = RAIZ / 'insertar_videos.py'
ENTRADA = Path('~/Downloads/Defensa TT 2026-B039.html').expanduser()
REVISION = RAIZ / 'anexos' / 'revision'
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


def extraer_secciones(html):
    secs = {}
    orden = []
    for m in re.finditer(r'<section class="deck-slide".*?</section>', html, flags=re.S):
        sec = m.group(0)
        sid = re.search(r'\bid="([^"]+)"', sec).group(1)
        lab_m = re.search(r'\bdata-label="([^"]*)"', sec)
        label = lab_m.group(1) if lab_m else ''
        secs[sid] = {'html': sec, 'label': label}
        orden.append(sid)
    return secs, orden


def verificar_html_ronda7(html):
    secs, orden = extraer_secciones(html)
    ids_existentes = set(secs.keys())

    # 1. Todos los href="#N" añadidos apuntan a un id de sección existente
    hrefs = re.findall(r'<a\s+class="tt-(?:enlace|ficha[^"]*|volver)"\s+href="#([^"]+)"', html)
    assert hrefs, 'No se encontraron enlaces tt-*'
    invalidos = [h for h in hrefs if h not in ids_existentes]
    assert not invalidos, f'Enlaces a ids inexistentes: {invalidos}'
    print(f'[OK] Todos los href="#N" añadidos ({len(hrefs)} etiquetas <a>) apuntan a un id de sección existente ({len(ids_existentes)} secciones).')

    # Construir mapa anexo -> id esperado desde el pie «Anexo N / M»
    anexo_a_id = {}
    anexo_grupo = {}
    for sid in orden:
        sec = secs[sid]['html']
        label = secs[sid]['label']
        textos = [
            re.sub(r'<[^>]+>', '', t).strip()
            for t in re.findall(r'<div data-text-path="[^"]*"[^>]*>(.*?)</div>', sec, flags=re.S)
        ]
        for t in textos:
            mp = re.search(r'\bAnexo\s+(\d+)\s*/\s*(\d+)\b', t)
            if mp:
                num = int(mp.group(1))
                grp = 'figuras' if label.startswith('Figura ') else ('tablas' if label.startswith('Cuadro ') else 'respuestas')
                anexo_a_id[num] = sid
                anexo_grupo[num] = grp
                break

    assert len(anexo_a_id) == 86, f'Se esperaban 86 anexos, se hallaron {len(anexo_a_id)}'

    # 2. Índice «Anexos» (diapositiva 24): 50 entradas enlazadas, cada una al anexo de su número
    sec_resp = secs['24']['html']
    enlaces_resp = re.findall(r'<a class="tt-enlace" href="#([^"]+)">(.*?)</a>', sec_resp, flags=re.S)
    assert len(enlaces_resp) == 100, f'Se esperaban 100 bloques enlazados (50 pares) en Anexos, hay {len(enlaces_resp)}'
    pares_resp = []
    for k in range(0, len(enlaces_resp), 2):
        id_num, txt_num = enlaces_resp[k]
        id_nom, txt_nom = enlaces_resp[k + 1]
        num = int(re.sub(r'<[^>]+>', '', txt_num).strip())
        assert id_num == id_nom == anexo_a_id[num], (
            f'Anexo {num}: enlace #{id_num}/#{id_nom} != esperado #{anexo_a_id[num]}'
        )
        pares_resp.append((num, id_num, txt_nom))
    assert [n for n, _, _ in pares_resp] == list(range(1, 51)), 'Los anexos enlazados en «Anexos» no son 1..50'
    print(f'[OK] Índice «Anexos» (id=24): {len(pares_resp)} entradas enlazadas (1..50, {len(enlaces_resp)} bloques <a>), cada una al anexo de su número.')

    # 3. Índice de figuras (diapositiva 75): 36 entradas enlazadas, cada una al anexo de su número
    sec_fig = secs['75']['html']
    enlaces_fig = re.findall(r'<a class="tt-enlace" href="#([^"]+)">(.*?)</a>', sec_fig, flags=re.S)
    assert len(enlaces_fig) == 72, f'Se esperaban 72 bloques enlazados (36 pares) en Índice de figuras, hay {len(enlaces_fig)}'
    pares_fig = []
    for k in range(0, len(enlaces_fig), 2):
        id_fig, txt_fig = enlaces_fig[k]
        id_anx, txt_anx = enlaces_fig[k + 1]
        m_anx = re.match(r'^→\s*Anexo\s+(\d+)$', re.sub(r'<[^>]+>', '', txt_anx).strip())
        assert m_anx, f'Formato inesperado en par de figura: {txt_anx!r}'
        num = int(m_anx.group(1))
        assert id_fig == id_anx == anexo_a_id[num], (
            f'Figura anexo {num}: enlace #{id_fig}/#{id_anx} != esperado #{anexo_a_id[num]}'
        )
        pares_fig.append((num, id_fig, txt_fig))
    assert [n for n, _, _ in pares_fig] == list(range(51, 87)), 'Los anexos enlazados en «Índice de figuras» no son 51..86'
    print(f'[OK] Índice «Índice de figuras del reporte» (id=75): {len(pares_fig)} entradas enlazadas (51..86, {len(enlaces_fig)} bloques <a>), cada una al anexo de su número.')

    # Verificar barra de índices en 24 y 75
    for sid_ind, esperado_activo in [('24', 'Respuestas'), ('75', 'Figuras')]:
        fichas = re.findall(r'<a class="([^"]*tt-ficha[^"]*)" href="#([^"]+)">([^<]+)</a>', secs[sid_ind]['html'])
        assert len(fichas) == 2, f'En índice {sid_ind} se esperaban 2 fichas (sin Tablas), hay {fichas}'
        activas = [t for cls, _, t in fichas if 'tt-ficha-activa' in cls]
        assert activas == [esperado_activo], f'Ficha activa en {sid_ind}: {activas} != {[esperado_activo]}'
    print('[OK] Barra de índices presente en diapositivas 24 y 75 con ficha activa correcta y ficha «Tablas» omitida.')

    # 4. Cada diapositiva con pie «Anexo N / M» tiene exactamente un tt-volver que apunta al índice de su grupo
    indice_esperado = {'respuestas': '24', 'figuras': '75'}
    con_volver = 0
    for sid in orden:
        volver = re.findall(r'<a class="tt-volver" href="#([^"]+)">↩ Índice</a>', secs[sid]['html'])
        if sid in anexo_a_id.values():
            num = next(k for k, v in anexo_a_id.items() if v == sid)
            grp = anexo_grupo[num]
            assert len(volver) == 1, f'Diapositiva {sid} (Anexo {num}) tiene {len(volver)} botones tt-volver'
            assert volver[0] == indice_esperado[grp], (
                f'Diapositiva {sid} (Anexo {num}, {grp}) apunta a #{volver[0]}, esperado #{indice_esperado[grp]}'
            )
            con_volver += 1
        else:
            assert len(volver) == 0, f'Diapositiva no-anexo {sid} tiene tt-volver'
    assert con_volver == 86
    print(f'[OK] Las {con_volver} diapositivas con pie «Anexo N / M» tienen exactamente un tt-volver hacia el índice de su grupo (50 a #24, 36 a #75).')
    return anexo_a_id, anexo_grupo


def verificar_formato_ronda8():
    """Prueba unitaria del formato de ronda 8 (entradas de un solo bloque y 3 índices incluido Tablas)."""
    from insertar_videos import insertar_navegacion

    html_r8 = (
        '<section class="deck-slide" id="1" data-label="Índice de respuestas"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">57 · ¿Por qué no una CNN?</div></div></div></div></section>'
        '<section class="deck-slide" id="2" data-label="Índice de figuras"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">63 · Figura 6.2.3 · Diferencia geométrica</div></div></div></div></section>'
        '<section class="deck-slide" id="3" data-label="Índice de tablas"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">90 · Cuadro 12 · Separabilidad de los kernels</div></div></div></div></section>'
        '<section class="deck-slide" id="4" data-label="¿Por qué no una CNN?"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">Anexo 57 / 122</div></div></div></div></section>'
        '<section class="deck-slide" id="5" data-label="Figura 6.2.3 · Diferencia geométrica"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">Reporte técnico, p. 123 · Anexo 63 / 122</div></div></div></div></section>'
        '<section class="deck-slide" id="6" data-label="Cuadro 12 · Separabilidad de los kernels"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">Reporte técnico, p. 121 · Anexo 90 / 122</div></div></div></div></section>'
    )
    procesado, info = insertar_navegacion(html_r8)
    assert info['enlazadas'] == {'respuestas': 1, 'figuras': 1, 'tablas': 1}
    assert info['con_boton'] == 3
    assert info['sin_indice'] == []
    assert '<a class="tt-enlace" href="#4">57 · ¿Por qué no una CNN?</a>' in procesado
    assert '<a class="tt-enlace" href="#5">63 · Figura 6.2.3 · Diferencia geométrica</a>' in procesado
    assert '<a class="tt-enlace" href="#6">90 · Cuadro 12 · Separabilidad de los kernels</a>' in procesado
    assert '<a class="tt-volver" href="#1">↩ Índice</a>' in procesado
    assert '<a class="tt-volver" href="#2">↩ Índice</a>' in procesado
    assert '<a class="tt-volver" href="#3">↩ Índice</a>' in procesado
    print('[OK] Convenciones de Ronda 8 (3 índices + entradas de 1 bloque «N · texto» + grupo Cuadro) verificadas.')


def verificar_pdf_y_capturas(html_path, pdf_path, anexo_a_id):
    cmd = [
        CHROME,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        '--virtual-time-budget=20000',
        f'--print-to-pdf={pdf_path}',
        html_path.as_uri(),
    ]
    subprocess.run(cmd, check=True, capture_output=True)
    doc = fitz.open(pdf_path)
    assert len(doc) == 111, f'El PDF tiene {len(doc)} páginas, se esperaban 111'

    # En PyMuPDF 1.25+, Chrome --print-to-pdf exporta <a href="#N"> como destinos con nombre
    # que get_links() devuelve con kind == fitz.LINK_NAMED (4) o fitz.LINK_GOTO (1) y el campo 'page' (0-based)
    TIPOS_INTERNOS = (fitz.LINK_GOTO, fitz.LINK_NAMED)

    # Página del índice «Anexos» (diapositiva 24 -> página índice 23)
    links_p24 = doc[23].get_links()
    internos_p24 = [l for l in links_p24 if l['kind'] in TIPOS_INTERNOS]
    paginas_destino_p24 = {l['page'] for l in internos_p24}
    esperadas_p24 = {int(anexo_a_id[n]) - 1 for n in range(1, 51)} | {23, 74}
    assert paginas_destino_p24 == esperadas_p24, (
        f'Páginas destino en índice Anexos no coinciden: faltan {esperadas_p24 - paginas_destino_p24}'
    )

    # Página del índice de figuras (diapositiva 75 -> página índice 74)
    links_p75 = doc[74].get_links()
    internos_p75 = [l for l in links_p75 if l['kind'] in TIPOS_INTERNOS]
    paginas_destino_p75 = {l['page'] for l in internos_p75}
    esperadas_p75 = {int(anexo_a_id[n]) - 1 for n in range(51, 87)} | {23, 74}
    assert paginas_destino_p75 == esperadas_p75, (
        f'Páginas destino en índice Figuras no coinciden: faltan {esperadas_p75 - paginas_destino_p75}'
    )

    # Comprobar enlace de regreso en todas las páginas de anexo
    anexos_con_link_pdf = 0
    for num, sid in anexo_a_id.items():
        p_idx = int(sid) - 1
        links_anx = [l for l in doc[p_idx].get_links() if l['kind'] in TIPOS_INTERNOS]
        esperada_idx_page = 23 if num <= 50 else 74
        assert any(l['page'] == esperada_idx_page for l in links_anx), (
            f'Página PDF {p_idx + 1} (Anexo {num}) no tiene enlace interno de regreso a página {esperada_idx_page + 1}'
        )
        anexos_con_link_pdf += 1

    # Comprobar que ni la barra de índices ni el botón tt-volver tapan palabras ni imágenes en las 88 páginas
    solapes = []
    for pno in range(23, 111):
        page = doc[pno]
        links = page.get_links()
        words = page.get_text('words')
        imgs = [fitz.Rect(im['bbox']) for im in page.get_image_info()]
        if pno in (23, 74):
            nav_rects = [l['from'] for l in links if l['from'].y0 < 100]
            propios = {'Respuestas', 'Figuras', 'Tablas'}
        else:
            nav_rects = [l['from'] for l in links]
            propios = {'↩', 'Índice'}
        for nr in nav_rects:
            for w in words:
                wr = fitz.Rect(w[:4])
                wt = w[4]
                if wt in propios and not (nr & wr).is_empty:
                    continue
                inter = nr & wr
                if not inter.is_empty and inter.width > 1 and inter.height > 1:
                    solapes.append((pno + 1, 'word', wt, nr, wr))
            for im in imgs:
                inter = nr & im
                if not inter.is_empty and inter.width > 1 and inter.height > 1:
                    solapes.append((pno + 1, 'img', nr, im))
    assert not solapes, f'Se detectaron solapes de barra/botón con contenido: {solapes}'

    kinds_vistos = sorted({l['kind'] for l in internos_p24 + internos_p75})
    print(f'[OK] PDF generado ({len(doc)} páginas):')
    print(f'     - Página 24 («Anexos»): {len(internos_p24)} enlaces internos (50 pares de entradas + 2 fichas de barra), '
          f'apuntando a las 50 páginas de anexos (25..74) y a los índices (24, 75). kinds={kinds_vistos} (fitz.LINK_NAMED/GOTO)')
    print(f'     - Página 75 («Índice de figuras»): {len(internos_p75)} enlaces internos (36 pares de entradas + 2 fichas de barra), '
          f'apuntando a las 36 páginas de figuras (76..111) y a los índices (24, 75).')
    print(f'     - Páginas de anexo con enlace interno de regreso verificado en PDF: {anexos_con_link_pdf}/86.')
    print('     - Solapes geométricos de barra de índices y botón «↩ Índice» con texto/imágenes en las 88 páginas: 0.')

    # Renderizar a PNG las 4 páginas pedidas en Other/defensa/anexos/revision/
    REVISION.mkdir(parents=True, exist_ok=True)
    capturas = [
        (23, REVISION / 'indice_respuestas.png', 'Índice de respuestas (diapositiva 24)'),
        (74, REVISION / 'indice_figuras.png', 'Índice de figuras (diapositiva 75)'),
        (24, REVISION / 'anexo_texto.png', 'Anexo 1 de texto (diapositiva 25)'),
        (75, REVISION / 'anexo_figura.png', 'Anexo 51 de figura (diapositiva 76)'),
    ]
    for p_idx, ruta_png, desc in capturas:
        pix = doc[p_idx].get_pixmap(dpi=144)
        pix.save(str(ruta_png))
        print(f'[OK] Captura guardada: {ruta_png} ({pix.width}x{pix.height} px) — {desc}')


def probar_atajos_html_minimo(td):
    """Ejecuta el script tt-nav-js en un HTML mínimo dentro de Chrome headless (--dump-dom)
    simulando eventos keydown para comprobar el acumulador de dígitos, Retroceso, Escape,
    Enter (anexo existente e inexistente), tecla i/I y no-intercepción de f o Enter vacío."""
    from insertar_videos import insertar_navegacion

    html_base = (
        '<section class="deck-slide" id="24" data-label="Índice de respuestas"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">1 · Estado del arte</div></div></div></div></section>'
        '<section class="deck-slide" id="25" data-label="Índice de figuras"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">51 · Figura 3.4.1 · Geometría</div></div></div></div></section>'
        '<section class="deck-slide" id="26" data-label="Índice de tablas"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">87 · Cuadro 1 · Estado del arte</div></div></div></div></section>'
        '<section class="deck-slide" id="27" data-label="Estado del arte"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">Anexo 1 / 122</div></div></div></div></section>'
        '<section class="deck-slide" id="50" data-label="Figura 3.4.1 · Geometría"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">Anexo 51 / 122</div></div></div></div></section>'
        '<section class="deck-slide" id="70" data-label="¿Por qué no una CNN?" data-off=""><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">Anexo 57 / 122</div></div></div></div></section>'
        '<section class="deck-slide" id="90" data-label="Cuadro 1 · Estado del arte"><div class="deck-fit"><div class="deck-scaler">'
        '<div class="slide"><div data-text-path="0">Anexo 87 / 122</div></div></div></div></section>'
    )
    procesado, info = insertar_navegacion(html_base)
    prueba_js = """
    <pre id="resultado"></pre>
    <script>
    (function(){
      var log = [];
      function key(k, opts){
        var ev = new KeyboardEvent('keydown', Object.assign({key: k, bubbles: true, cancelable: true}, opts || {}));
        var noCancelado = window.dispatchEvent(ev);
        return {defaultPrevented: ev.defaultPrevented, noCancelado: noCancelado};
      }
      var ind = document.getElementById('tt-indicador');
      // 1) Teclear 5, 8, Backspace, 7 -> 'Anexo 57 ⏎', y Enter -> salta a #70
      key('5');
      log.push('tras 5: ' + ind.textContent);
      key('8');
      log.push('tras 58: ' + ind.textContent);
      key('Backspace');
      log.push('tras Backspace: ' + ind.textContent);
      key('7');
      log.push('tras 57: ' + ind.textContent);
      key('Enter');
      log.push('tras Enter(57): hash=' + location.hash + ' ind=' + JSON.stringify(ind.textContent));

      // 2) Teclear 9, 9, 9 + Enter -> no existe
      key('9'); key('9'); key('9');
      key('Enter');
      log.push('tras Enter(999): ' + ind.textContent);

      // 3) Teclear 4 + Escape -> cancela
      key('4');
      key('Escape');
      log.push('tras Escape: ind=' + JSON.stringify(ind.textContent));

      // 4) Tecla i: ir a índice de respuestas (#24), luego #25, #26, #24
      document.querySelectorAll('.deck-slide').forEach(function(s){ s.setAttribute('data-off', ''); });
      document.getElementById('70').removeAttribute('data-off');
      key('i');
      log.push('i desde anexo 57 -> ' + location.hash);
      document.getElementById('70').setAttribute('data-off', '');
      document.getElementById('24').removeAttribute('data-off');
      key('I');
      log.push('I desde #24 -> ' + location.hash);
      document.getElementById('24').setAttribute('data-off', '');
      document.getElementById('25').removeAttribute('data-off');
      key('i');
      log.push('i desde #25 -> ' + location.hash);
      document.getElementById('25').setAttribute('data-off', '');
      document.getElementById('26').removeAttribute('data-off');
      key('i');
      log.push('i desde #26 -> ' + location.hash);

      // 5) f y Enter sin número en curso no se interceptan
      var rf = key('f');
      var re = key('Enter');
      log.push('f interceptada=' + rf.defaultPrevented + ', Enter vacío interceptado=' + re.defaultPrevented);

      document.getElementById('resultado').textContent = log.join('\\n');
    })();
    </script>
    """
    doc_html = f'<!doctype html><html><head><meta charset="utf-8"></head><body>{procesado}{ info["js"] }{prueba_js}</body></html>'
    p = Path(td) / 'prueba_teclado.html'
    p.write_text(doc_html, encoding='utf-8')
    res = subprocess.run(
        [CHROME, '--headless=new', '--disable-gpu', '--dump-dom', p.as_uri()],
        check=True, capture_output=True, text=True,
    )
    m = re.search(r'<pre id="resultado">(.*?)</pre>', res.stdout, flags=re.S)
    assert m, 'No se encontró salida de prueba de teclado'
    lineas = html_mod.unescape(m.group(1)).strip().splitlines()
    esperado = [
        'tras 5: Anexo 5 ⏎',
        'tras 58: Anexo 58 ⏎',
        'tras Backspace: Anexo 5 ⏎',
        'tras 57: Anexo 57 ⏎',
        'tras Enter(57): hash=#70 ind=""',
        'tras Enter(999): No existe el anexo 999',
        'tras Escape: ind=""',
        'i desde anexo 57 -> #24',
        'I desde #24 -> #25',
        'i desde #25 -> #26',
        'i desde #26 -> #24',
        'f interceptada=false, Enter vacío interceptado=false',
    ]
    assert lineas == esperado, f'Fallo en prueba de teclado:\nObtenido: {lineas}\nEsperado: {esperado}'
    print('[OK] Atajos de teclado verificados en HTML mínimo con eventos sintéticos (Chrome --dump-dom):')
    for ln in lineas:
        print('     ', ln)


def main():
    assert ENTRADA.exists(), f'No existe {ENTRADA}'
    with tempfile.TemporaryDirectory() as td:
        html_temp = Path(td) / 'Defensa_nav_temp.html'
        pdf_temp = Path(td) / 'Defensa_nav_temp.pdf'

        # 1. Procesar el HTML exportado actual a un archivo temporal
        r1 = subprocess.run(
            [sys.executable, str(SCRIPT), str(ENTRADA), str(html_temp)],
            check=True, capture_output=True, text=True,
        )
        print('=== Salida de insertar_videos.py ===')
        print(r1.stdout.strip())

        # 2. Comprobar idempotencia
        r2 = subprocess.run(
            [sys.executable, str(SCRIPT), str(html_temp), str(html_temp)],
            capture_output=True, text=True,
        )
        assert r2.returncode != 0 and 'El archivo ya tiene los videos insertados.' in (r2.stderr + r2.stdout), (
            f'Fallo de idempotencia: rc={r2.returncode}, out={r2.stdout!r}, err={r2.stderr!r}'
        )
        print('[OK] Idempotencia verificada («El archivo ya tiene los videos insertados.»).')

        # 3. Verificaciones sobre el HTML procesado (Ronda 7) y prueba de formato Ronda 8
        html = html_temp.read_text(encoding='utf-8')
        anexo_a_id, _ = verificar_html_ronda7(html)
        verificar_formato_ronda8()

        # 4. Impresión a PDF con Chrome headless, verificación de enlaces con PyMuPDF y capturas PNG
        verificar_pdf_y_capturas(html_temp, pdf_temp, anexo_a_id)

        # 5. Prueba de lógica de atajos de teclado en HTML mínimo
        probar_atajos_html_minimo(td)

    print('=== TODAS LAS PRUEBAS PASARON ===')


if __name__ == '__main__':
    main()
