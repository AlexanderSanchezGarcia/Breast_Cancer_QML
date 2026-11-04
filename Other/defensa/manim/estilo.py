# Estilo común de las escenas de Manim de la defensa: la paleta y la tipografía del deck
# «Defensa TT 2026-B039». Todas las escenas importan de aquí; no definen colores propios.
from manim import config

# Paleta extraída del HTML del deck
FONDO = '#FBFAF7'        # fondo crema de todas las diapositivas
TINTA = '#00002E'        # títulos y texto principal
TEXTO = '#505468'        # texto secundario, ejes y etiquetas
LINEA = '#DCDFEE'        # líneas suaves, rejillas y bordes
TARJETA = '#F3F4FB'      # fondo de tarjetas
CLASICO = '#2D4DF2'      # C1 y clásico (RBF, mejor clásico)
CLASICO_2 = '#6F86F6'    # C2
CLASICO_3 = '#A9B7FA'    # C3
C4 = '#E8622C'           # C4 (naranja) y kernels derivados del mapa ZZ
C5 = '#1A9E77'           # C5 (verde)
DESTACADO = '#DA33BF'    # cifras destacadas, con moderación

# El deck usa Inter, que no está instalada en esta Mac; Helvetica Neue es la más parecida de las del sistema.
FUENTE = 'Helvetica Neue'
FUENTE_MONO = 'Menlo'


def configurar(ancho=1920, alto=1080, fps=30):
    """Lienzo 16:9 con el fondo del deck. Llamar al inicio de cada archivo de escena."""
    config.background_color = FONDO
    config.pixel_width = ancho
    config.pixel_height = alto
    config.frame_rate = fps
