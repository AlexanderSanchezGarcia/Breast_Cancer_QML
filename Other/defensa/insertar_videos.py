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
import base64
import re
import sys
from pathlib import Path

CLIPS = Path(__file__).resolve().parent / 'manim' / 'clips'
FUENTES = Path(__file__).resolve().parent / 'fuentes' / 'fuentes_incrustadas.css'
FIGURAS = Path(__file__).resolve().parent / 'figuras_anexos'
# Palabra clave del texto alternativo → clip
MAPA = [
    ('proceso', 'mapa_trabajo.mp4'),
    ('esfera de Bloch', 'qubit_bloch.mp4'),
    ('dos lecturas', 'dos_lecturas.mp4'),
    ('mapas de calor', 'concentracion.mp4'),
    ('AUC-ROC', 'x11_curva.mp4'),
    ('disparos', 'disparos.mp4'),
]

CSS = """<style id="tt-videos-css">
.tt-video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;background:transparent;cursor:pointer}
@media print{.tt-video{display:none!important}}
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


def main(entrada, salida):
    s = Path(entrada).read_text(encoding='utf-8')
    if 'id="tt-videos-js"' in s or 'id="tt-fuentes"' in s:
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
    s = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/[^"]*">\s*', '', s)
    fuentes = '<style id="tt-fuentes">' + FUENTES.read_text(encoding='utf-8') + '</style>'
    s = s.replace('</head>', fuentes + CSS + '</head>', 1)
    s = s.replace('</body>', JS + '</body>', 1) if '</body>' in s else s + JS
    Path(salida).write_text(s, encoding='utf-8')
    print(f'{len(usados)} videos insertados: {usados}')
    print(f'{len(figuras)} figuras del reporte insertadas')
    print(f'{salida}: {Path(salida).stat().st_size / 1e6:.1f} MB')



def insertar_figuras(s):
    archivos = {f.name.split('_')[1]: f for f in FIGURAS.glob('Fig_*.png')}
    usadas = []

    def seccion(m):
        sec = m.group(0)
        lab = re.search(r'data-label="Figura ([0-9A-Z.]+) ·', sec)
        if not lab:
            return sec
        num = lab.group(1)
        if num not in archivos:
            print('Aviso: no hay PNG para la figura', num)
            return sec
        marco = re.search(r'(<div data-img-path="[^"]*"[^>]*>)(</div>)', sec)
        if not marco:
            print('Aviso: la diapositiva de la figura', num, 'no tiene marco vacío')
            return sec
        datos = base64.b64encode(archivos[num].read_bytes()).decode()
        img = (f'<img alt="Figura del reporte {num}" src="data:image/png;base64,{datos}" '
               f'style="display:block;width:100%;height:100%;object-fit:contain">')
        usadas.append(num)
        return sec[:marco.end(1)] + img + sec[marco.end(1):]

    s = re.sub(r'<section class="deck-slide".*?</section>', seccion, s, flags=re.S)
    faltan = sorted(set(archivos) - set(usadas))
    if faltan:
        print('Aviso: figuras sin diapositiva:', faltan)
    return s, usadas


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
