# Reinserta los clips de Manim en el HTML que exporta Claude Design, que los sustituye por su imagen fija.
#
# Uso:
#   python3 Other/defensa/insertar_videos.py "<exportado>.html" "<salida>.html"
#
# Qué hace:
# - Busca las imágenes cuyo texto alternativo empieza con «Video» y, según ese texto, les superpone
#   el clip correspondiente de Other/defensa/manim/clips/, incrustado en base64: el HTML sigue siendo
#   un solo archivo que funciona sin internet.
# - La imagen fija se conserva debajo, así que al imprimir a PDF sale como hasta ahora.
# - Control: en la diapositiva con video, la primera flecha → (o espacio, o Av Pág, que es lo que
#   envían los controles remotos) reproduce el video en lugar de avanzar; la siguiente avanza.
#   Un clic sobre el video lo pausa o reanuda. Al salir de la diapositiva, el video vuelve al inicio.
# - Coloca las figuras del reporte en los anexos de figura: en cada diapositiva cuyo data-label empieza con
#   «Figura X.Y.Z ·», llena el marco vacío (div con data-img-path) con Other/defensa/figuras_anexos/Fig_X.Y.Z_*.png,
#   en base64, con texto alternativo «Figura del reporte X.Y.Z». Claude Design deja esos marcos vacíos.
# - Incrusta las fuentes del deck (Other/defensa/fuentes/fuentes_incrustadas.css) y quita los enlaces a
#   Google Fonts, para que el diseño no cambie si el día de la defensa no hay internet.
# - Cambia los caracteres «❶ ❷» del hilo de la pregunta (que la fuente del deck no trae y se ven con una
#   fuente del sistema) por un círculo dibujado con CSS, del alto de la minúscula, solo en el texto visible.
# - Ajustes puntuales de composición (AJUSTES): cada uno localiza un bloque por su texto y solo se aplica si
#   el estilo sigue siendo el esperado; si Claude Design cambió esa diapositiva, avisa y no toca nada.
import base64
import html
import json
import re
import sys
from pathlib import Path

CLIPS = Path(__file__).resolve().parent / 'manim' / 'clips'
FUENTES = Path(__file__).resolve().parent / 'fuentes' / 'fuentes_incrustadas.css'
FIGURAS = Path(__file__).resolve().parent / 'figuras_anexos'
CUADROS = Path(__file__).resolve().parent / 'tablas_anexos' / 'deck'
# Palabra clave del texto alternativo → clip
MAPA = [
    ('proceso', 'mapa_trabajo.mp4'),
    ('esfera de Bloch', 'qubit_bloch.mp4'),
    ('dos lecturas', 'dos_lecturas.mp4'),
    ('mapas de calor', 'concentracion.mp4'),
    ('AUC-ROC', 'x11_curva.mp4'),
    ('disparos', 'disparos.mp4'),
    ('curva ROC', 'roc_umbral.mp4'),
]

CSS = """<style id="tt-videos-css">
.tt-video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:transparent;cursor:pointer}
@media print{.tt-video{display:none!important}}
.tt-num{display:inline-flex;align-items:center;justify-content:center;box-sizing:border-box;width:1.08em;height:1.08em;
border-radius:50%;background:#00002E;color:#fff!important;-webkit-text-fill-color:#fff!important;font-family:Inter,sans-serif;
font-size:.8em;font-weight:700;line-height:1;font-style:normal;vertical-align:.1em;letter-spacing:0;padding-top:.04em;
-webkit-print-color-adjust:exact;print-color-adjust:exact}
.tt-enlace{color:inherit;font:inherit;text-decoration:none;cursor:pointer}
.tt-enlace:hover{text-decoration:underline}
.tt-indices{position:absolute;right:120px;top:44px;z-index:2;display:inline-flex;align-items:center;gap:8px}
.tt-ficha{display:inline-flex;align-items:center;padding:6px 14px;border-radius:999px;background:#F3F4FB;
border:1px solid #DCDFEE;color:#505468!important;-webkit-text-fill-color:#505468;font-family:Inter,sans-serif;
font-size:15px;font-weight:500;line-height:1.2;text-decoration:none;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.tt-ficha:hover{color:#00002E!important;-webkit-text-fill-color:#00002E;border-color:#2D4DF2}
.tt-ficha-activa{background:#00002E;border-color:#00002E;color:#fff!important;-webkit-text-fill-color:#fff!important;font-weight:600}
.tt-volver{position:absolute;left:50%;transform:translateX(-50%);bottom:40px;z-index:2;display:inline-flex;
align-items:center;gap:6px;padding:6px 16px;border-radius:999px;background:#F3F4FB;border:1px solid #DCDFEE;
color:#505468!important;-webkit-text-fill-color:#505468;font-family:Inter,sans-serif;font-size:15px;font-weight:500;
line-height:1.2;text-decoration:none;-webkit-print-color-adjust:exact;print-color-adjust:exact}
.tt-volver:hover{color:#00002E!important;-webkit-text-fill-color:#00002E;border-color:#2D4DF2}
.tt-indicador{position:fixed;right:24px;bottom:24px;z-index:9999;padding:8px 16px;border-radius:999px;
background:#00002E;color:#fff;font-family:Inter,sans-serif;font-size:15px;font-weight:600;line-height:1.3;
box-shadow:0 4px 14px rgba(0,0,46,.22);pointer-events:none;opacity:0;transition:opacity .15s}
.tt-indicador[data-on]{opacity:1}
@media print{.tt-indicador{display:none!important}}
</style>"""

JS = r"""<script id="tt-videos-js">
(function(){
  function slides(){return Array.prototype.slice.call(document.querySelectorAll('.deck-slide'));}
  function actual(){
    var s=slides(), on=s.filter(function(x){return !x.hasAttribute('data-off');});
    if(on.length===1) return on[0];
    var best=null, area=0, h=window.innerHeight;
    s.forEach(function(x){var r=x.getBoundingClientRect(); var v=Math.max(0,Math.min(r.bottom,h)-Math.max(r.top,0)); if(v>area){area=v;best=x;}});
    return best;
  }
  window.addEventListener('keydown',function(e){
    if(e.metaKey||e.ctrlKey||e.altKey) return;
    var k=e.key;
    if(!(k==='ArrowRight'||k==='PageDown'||(k===' '&&!e.shiftKey))) return;
    var sl=actual(); if(!sl) return;
    var v=sl.querySelector('video.tt-video'); if(!v) return;
    if(v.paused && !v.ended && v.dataset.ttVisto!=='1'){
      e.preventDefault(); e.stopImmediatePropagation();
      v.dataset.ttVisto='1'; v.play();
    }
  },true);
  document.addEventListener('click',function(e){
    var v=e.target.closest&&e.target.closest('video.tt-video'); if(!v) return;
    e.stopPropagation(); e.preventDefault();
    v.dataset.ttVisto='1'; if(v.paused){v.play();}else{v.pause();}
  },true);
  // Al salir de una diapositiva (recibe data-off), su video vuelve al inicio
  new MutationObserver(function(ms){ms.forEach(function(m){
    var sl=m.target; if(m.attributeName==='data-off' && sl.hasAttribute('data-off')){
      sl.querySelectorAll('video.tt-video').forEach(function(v){v.pause(); v.currentTime=0; v.dataset.ttVisto='';});
    }
  });}).observe(document.body,{subtree:true,attributes:true,attributeFilter:['data-off']});
})();
</script>"""

JS_NAV_PLANTILLA = r"""<script id="tt-nav-js">
(function(){
  var ANEXOS = __MAPA_ANEXOS__;
  var INDICES = __ORDEN_INDICES__;
  var ID_RESPUESTAS = __ID_RESPUESTAS__;
  var buf = '';
  var timer = null;
  var ind = document.createElement('div');
  ind.id = 'tt-indicador';
  ind.className = 'tt-indicador';
  ind.setAttribute('aria-live', 'polite');
  document.body.appendChild(ind);

  function mostrar(txt){
    ind.textContent = txt;
    ind.setAttribute('data-on', '');
  }
  function ocultar(){
    ind.removeAttribute('data-on');
    ind.textContent = '';
  }
  function cancelar(){
    if(timer){ clearTimeout(timer); timer = null; }
    buf = '';
    ocultar();
  }
  function actualId(){
    var s = Array.prototype.slice.call(document.querySelectorAll('.deck-slide'));
    var on = s.filter(function(x){ return !x.hasAttribute('data-off'); });
    if(on.length === 1) return on[0].id;
    var m = /^#(\d+)$/.exec(window.location.hash);
    if(m) return m[1];
    var best = null, area = 0, h = window.innerHeight;
    s.forEach(function(x){
      var r = x.getBoundingClientRect();
      var v = Math.max(0, Math.min(r.bottom, h) - Math.max(r.top, 0));
      if(v > area){ area = v; best = x; }
    });
    return best ? best.id : (s[0] ? s[0].id : '');
  }
  function irA(id){
    if(!id) return;
    var h = '#' + id;
    if(window.location.hash === h){
      window.dispatchEvent(new HashChangeEvent('hashchange'));
    } else {
      window.location.hash = h;
    }
  }
  window.addEventListener('keydown', function(e){
    if(e.metaKey || e.ctrlKey || e.altKey) return;
    var t = e.target;
    if(t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.isContentEditable)) return;
    var k = e.key;
    if(/^[0-9]$/.test(k)){
      e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
      buf += k;
      mostrar('Anexo ' + buf + ' \u23ce');
      if(timer) clearTimeout(timer);
      timer = setTimeout(cancelar, 4000);
      return;
    }
    if(k === 'Backspace' && buf.length > 0){
      e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
      buf = buf.slice(0, -1);
      if(timer) clearTimeout(timer);
      if(buf.length === 0){
        timer = null;
        ocultar();
      } else {
        mostrar('Anexo ' + buf + ' \u23ce');
        timer = setTimeout(cancelar, 4000);
      }
      return;
    }
    if(k === 'Escape' && buf.length > 0){
      e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
      cancelar();
      return;
    }
    if(k === 'Enter' && buf.length > 0){
      e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
      if(timer){ clearTimeout(timer); timer = null; }
      var nStr = String(parseInt(buf, 10));
      var raw = buf;
      buf = '';
      var dest = ANEXOS[nStr] || ANEXOS[raw];
      if(dest){
        ocultar();
        irA(dest);
      } else {
        mostrar('No existe el anexo ' + raw);
        timer = setTimeout(ocultar, 2000);
      }
      return;
    }
    if(k === 'i' || k === 'I'){
      if(!INDICES.length) return;
      e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
      cancelar();
      var cur = actualId();
      var pos = INDICES.indexOf(cur);
      if(pos === -1){
        irA(ID_RESPUESTAS || INDICES[0]);
      } else {
        irA(INDICES[(pos + 1) % INDICES.length]);
      }
      return;
    }
  }, true);
})();
</script>"""

NOMBRES_INDICES = [
    ('respuestas', 'Anexos'),
    ('figuras', 'Figuras'),
    ('tablas', 'Tablas'),
]

ETIQUETAS_INDICE = {
    'Índice de anexos': 'respuestas',       # desde la ronda 9 (entradas por título, agrupadas por tema)
    'Índice de respuestas': 'respuestas',   # rondas 8 y anteriores
    'Anexos': 'respuestas',
    'Índice de figuras': 'figuras',
    'Índice de figuras del reporte': 'figuras',
    'Índice de tablas': 'tablas',
}


def main(entrada, salida):
    s = Path(entrada).read_text(encoding='utf-8')
    if 'id="tt-videos-js"' in s or 'id="tt-fuentes"' in s or 'id="tt-nav-js"' in s:
        sys.exit('El archivo ya tiene los videos insertados.')
    usados = []

    def reemplazo(m):
        img = m.group(0)
        alt = re.search(r'alt="([^"]*)"', img).group(1)
        clip = next((c for clave, c in MAPA if clave in alt), None)
        if clip is None:
            return img
        datos = base64.b64encode((CLIPS / clip).read_bytes()).decode()
        usados.append(clip)
        video = (f'<video class="tt-video" muted playsinline preload="auto" '
                 f'src="data:video/mp4;base64,{datos}"></video>')
        return img + video

    s = re.sub(r'<img[^>]*alt="Video[^"]*"[^>]*>', reemplazo, s)
    faltan = [c for _, c in MAPA if c not in usados]
    if faltan:
        print('Aviso: no se encontró imagen para', faltan)
    s, figuras = insertar_figuras(s)
    s, circulos = insertar_circulos(s)
    s, ajustes = aplicar_ajustes(s)
    s, nav = insertar_navegacion(s)
    s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/[^"]*">\s*', '', s)
    fuentes = '<style id="tt-fuentes">' + FUENTES.read_text(encoding='utf-8') + '</style>'
    s = s.replace('</head>', fuentes + CSS + '</head>', 1)
    scripts = JS + nav['js']
    s = s.replace('</body>', scripts + '</body>', 1) if '</body>' in s else s + scripts
    Path(salida).write_text(s, encoding='utf-8')
    print(f'{len(usados)} videos insertados: {usados}')
    print(f"{sum(1 for f in figuras if not f.startswith('C') or '-' not in f)} figuras y {sum(1 for f in figuras if f.startswith('C') and '-' in f)} diapositivas de cuadros insertadas")
    print(f'{circulos} círculos ❶ ❷ redibujados')
    print(f'{len(ajustes)} de {len(AJUSTES) + len(SUSTITUCIONES)} ajustes de composición aplicados')
    print(f'Navegación: entradas enlazadas por índice={nav["enlazadas"]}, '
          f'anexos con botón={nav["con_boton"]}, '
          f'anexos sin índice de su grupo={len(nav["sin_indice"])}')
    print(f'{salida}: {Path(salida).stat().st_size / 1e6:.1f} MB')


def grupo_de_anexo(label):
    if label.startswith('Figura '):
        return 'figuras'
    if label.startswith('Cuadro '):
        return 'tablas'
    return 'respuestas'


def insertar_navegacion(s):
    secciones = list(re.finditer(r'<section class="deck-slide".*?</section>', s, flags=re.S))
    indices = {}
    anexo_a_id = {}
    anexo_grupo = {}
    diap_anexo = {}

    for m in secciones:
        sec = m.group(0)
        sid = re.search(r'\bid="([^"]+)"', sec).group(1)
        lab_m = re.search(r'\bdata-label="([^"]*)"', sec)
        label = lab_m.group(1) if lab_m else ''
        if label in ETIQUETAS_INDICE:
            indices[ETIQUETAS_INDICE[label]] = sid
        textos = [
            re.sub(r'<[^>]+>', '', t).strip()
            for t in re.findall(r'<div data-text-path="[^"]*"[^>]*>(.*?)</div>', sec, flags=re.S)
        ]
        for t in textos:
            mp = re.search(r'\bAnexo\s+(\d+)\s*/\s*(\d+)\b', t)
            if mp:
                num = int(mp.group(1))
                grp = grupo_de_anexo(label)
                anexo_a_id.setdefault(num, sid)
                anexo_grupo[num] = grp
                diap_anexo[sid] = (num, grp)
                break

    for clave, _ in NOMBRES_INDICES:
        if clave not in indices:
            print(f'Aviso: no se encontró el índice de {clave}')

    id_a_indice = {sid: g for g, sid in indices.items()}
    enlazadas = {g: 0 for g in indices}
    con_boton = 0
    sin_indice = []

    def procesar_seccion(m):
        nonlocal con_boton
        sec = m.group(0)
        sid = re.search(r'\bid="([^"]+)"', sec).group(1)
        if sid in id_a_indice:
            g = id_a_indice[sid]
            bloques = list(re.finditer(r'(<div data-text-path="[^"]*"[^>]*>)(.*?)(</div>)', sec, flags=re.S))
            textos = [re.sub(r'<[^>]+>', '', b.group(2)).strip() for b in bloques]
            a_enlazar = []
            i = 0
            while i < len(bloques):
                t = textos[i]
                m_r8 = re.match(r'^(\d+)\s*·\s*\S', t)
                if m_r8:
                    num = int(m_r8.group(1))
                    if num in anexo_a_id:
                        a_enlazar.append((i, anexo_a_id[num]))
                        enlazadas[g] += 1
                    else:
                        print(f'Aviso: anexo {num} en índice de {g} no tiene diapositiva')
                    i += 1
                    continue
                m_num = re.match(r'^(\d+)$', t)
                if m_num and i + 1 < len(bloques):
                    num = int(m_num.group(1))
                    if num in anexo_a_id:
                        a_enlazar.append((i, anexo_a_id[num]))
                        a_enlazar.append((i + 1, anexo_a_id[num]))
                        enlazadas[g] += 1
                    else:
                        print(f'Aviso: anexo {num} en índice de {g} no tiene diapositiva')
                    i += 2
                    continue
                if i + 1 < len(bloques):
                    m_fig = re.match(r'^→\s*Anexo\s+(\d+)$', textos[i + 1])
                    if m_fig:
                        num = int(m_fig.group(1))
                        if num in anexo_a_id:
                            a_enlazar.append((i, anexo_a_id[num]))
                            a_enlazar.append((i + 1, anexo_a_id[num]))
                            enlazadas[g] += 1
                        else:
                            print(f'Aviso: anexo {num} en índice de {g} no tiene diapositiva')
                        i += 2
                        continue
                i += 1

            for idx, dest_id in reversed(a_enlazar):
                b = bloques[idx]
                enlace = f'<a class="tt-enlace" href="#{dest_id}">{b.group(2)}</a>'
                sec = sec[:b.start(2)] + enlace + sec[b.end(2):]

            fichas = []
            for clave, titulo in NOMBRES_INDICES:
                if clave not in indices:
                    continue
                cls = 'tt-ficha tt-ficha-activa' if clave == g else 'tt-ficha'
                fichas.append(f'<a class="{cls}" href="#{indices[clave]}">{titulo}</a>')
            barra = f'<nav class="tt-indices" aria-label="Índices de anexos">{"".join(fichas)}</nav>'
            cierre = '</div></div></div></section>'
            assert sec.endswith(cierre)
            sec = sec[:-len(cierre)] + barra + cierre
            return sec

        if sid in diap_anexo:
            num, grp = diap_anexo[sid]
            if grp in indices:
                boton = f'<a class="tt-volver" href="#{indices[grp]}">\u21a9 Índice</a>'
                cierre = '</div></div></div></section>'
                assert sec.endswith(cierre)
                sec = sec[:-len(cierre)] + boton + cierre
                con_boton += 1
            else:
                sin_indice.append(num)
        return sec

    s = re.sub(r'<section class="deck-slide".*?</section>', procesar_seccion, s, flags=re.S)
    orden_indices = [indices[g] for g, _ in NOMBRES_INDICES if g in indices]
    id_resp = indices.get('respuestas') or (orden_indices[0] if orden_indices else None)
    js_nav = (
        JS_NAV_PLANTILLA
        .replace('__MAPA_ANEXOS__', json.dumps({str(k): v for k, v in sorted(anexo_a_id.items())}))
        .replace('__ORDEN_INDICES__', json.dumps(orden_indices))
        .replace('__ID_RESPUESTAS__', json.dumps(id_resp))
    )
    return s, {
        'indices': indices,
        'anexo_a_id': anexo_a_id,
        'anexo_grupo': anexo_grupo,
        'enlazadas': enlazadas,
        'con_boton': con_boton,
        'sin_indice': sin_indice,
        'js': js_nav,
    }


# (texto que identifica el bloque, [(estilo del marco esperado, nuevo)], [(estilo del texto esperado, nuevo)])
AJUSTES = [
    # Diapositiva 17: el rótulo del QSVM, a 17 px entre dos filas, pasa debajo del recuadro, a 22 px y a todo el ancho
    ('el QSVM empata con el SVM clásico',
     [('left: 536px; width: 958px; top: 690px;', 'left: 112px; width: 1696px; top: 786px;')],
     [('font-size: 17px;', 'font-size: 22px;'), ('background-color: rgb(251, 250, 247); padding: 6px 8px;', 'padding: 0px;')]),
    # ... y la nota gris de debajo baja para dejarle sitio
    ('Exceso de KTA de C3 = kernel RBF',
     [('top: 798px;', 'top: 842px;')], []),
]


# Sustituciones literales: (texto que debe aparecer exactamente una vez, sustituto)
SUSTITUCIONES = [
    # Portada: el bloque de texto ocupa todo el lienzo (inset: 0) sin margen interior y queda pegado al borde
    ('justify-content: center; gap: 32px; width: 100%; height: 100%;"><div data-text-path="0" data-node-path="0" '
     'style="font-family: Inter, Arial, ui-sans-serif, system-ui, sans-serif; font-size: 18px; font-weight: 600; '
     'line-height: 1.4; color: rgb(45, 77, 242); margin: 0px; white-space: pre-wrap; overflow-wrap: break-word; '
     'text-wrap-style: pretty; min-width: 0px; min-height: 0px; letter-spacing: 4px; text-transform: uppercase; '
     'overflow-y: visible;">Instituto Politécnico Nacional',
     'justify-content: center; gap: 32px; width: 100%; height: 100%; padding: 270px 120px 120px; box-sizing: border-box;">'
     '<div data-text-path="0" data-node-path="0" '
     'style="font-family: Inter, Arial, ui-sans-serif, system-ui, sans-serif; font-size: 18px; font-weight: 600; '
     'line-height: 1.4; color: rgb(45, 77, 242); margin: 0px; white-space: pre-wrap; overflow-wrap: break-word; '
     'text-wrap-style: pretty; min-width: 0px; min-height: 0px; letter-spacing: 4px; text-transform: uppercase; '
     'overflow-y: visible;">Instituto Politécnico Nacional'),
]


def aplicar_ajustes(s):
    hechos = []
    for viejo, nuevo in SUSTITUCIONES:
        if s.count(viejo) != 1:
            print(f'Aviso: sustitución no aplicada (aparece {s.count(viejo)} veces): «{viejo[-60:]}»')
            continue
        s = s.replace(viejo, nuevo)
        hechos.append(viejo[-40:])
    for clave, marco, texto in AJUSTES:
        patron = re.compile(r'(<div data-frame-id="[^"]*" style=")([^"]*)(">\s*<div[^>]*?style=")([^"]*)("[^>]*>)(?=' + re.escape(clave) + ')')
        m = patron.search(s)
        if not m or not all(a in m.group(2) for a, _ in marco) or not all(a in m.group(4) for a, _ in texto):
            print(f'Aviso: ajuste no aplicado (la diapositiva cambió): «{clave}»')
            continue
        st_marco, st_texto = m.group(2), m.group(4)
        for a, b in marco:
            st_marco = st_marco.replace(a, b)
        for a, b in texto:
            st_texto = st_texto.replace(a, b)
        s = s[:m.start()] + m.group(1) + st_marco + m.group(3) + st_texto + m.group(5) + s[m.end():]
        hechos.append(clave)
    return s, hechos


def insertar_circulos(s):
    """Sustituye ❶ y ❷ por <span class="tt-num">, solo en el texto entre etiquetas (no en atributos ni notas)."""
    n = 0
    def texto(m):
        nonlocal n
        t = m.group(0)
        for car, num in (('❶', '1'), ('❷', '2')):
            n += t.count(car)
            t = t.replace(car, f'<span class="tt-num">{num}</span>')
        return t
    return re.sub(r'>[^<]*<', texto, s), n


def insertar_figuras(s):
    archivos = {f.name.split('_')[1]: f for f in FIGURAS.glob('Fig_*.png')}
    # Cuadros del reporte (anexos 87-122): tablas_anexos/deck/Cuadro_C_k.png, de partir_cuadros.py.
    # Clave «C» o «C-k»; la diapositiva dice «Cuadro C · título» o «Cuadro C · título (parte k de n)».
    for f in CUADROS.glob('Cuadro_*.png'):
        _, c, k = f.stem.split('_')
        archivos[f'C{c}-{k}'] = f
    usadas = []

    def seccion(m):
        sec = m.group(0)
        lab = re.search(r'data-label="Figura ([0-9A-Z.]+) ·', sec)
        cua = re.search(r'data-label="Cuadro (\d+) ·([^"]*)"', sec)
        if not lab and not cua:
            return sec
        parte = None
        if cua:
            parte = re.search(r'\(parte (\d+) de \d+\)', html.unescape(cua.group(2)))
            num = f'C{cua.group(1)}-{parte.group(1) if parte else 1}'
        else:
            num = lab.group(1)
        if num not in archivos:
            print('Aviso: no hay PNG para la figura', num)
            return sec
        marco = re.search(r'(<div data-img-path="[^"]*"[^>]*>)(</div>)', sec)
        if not marco:
            print('Aviso: la diapositiva de la figura', num, 'no tiene marco vacío')
            return sec
        datos = base64.b64encode(archivos[num].read_bytes()).decode()
        if num.startswith('C') and '-' in num:
            c, k = num[1:].split('-')
            alt = f'Cuadro del reporte {c}' + (f', parte {k}' if parte else '')
        else:
            alt = f'Figura del reporte {num}'
        img = (f'<img alt="{alt}" src="data:image/png;base64,{datos}" '
               f'style="display:block;width:100%;height:100%;object-fit:contain">')
        usadas.append(num)
        return sec[:marco.end(1)] + img + sec[marco.end(1):]

    s = re.sub(r'<section class="deck-slide".*?</section>', seccion, s, flags=re.S)
    faltan = sorted(set(archivos) - set(usadas))
    if faltan:
        print('Aviso: figuras o cuadros sin diapositiva:', faltan)
    return s, usadas


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
