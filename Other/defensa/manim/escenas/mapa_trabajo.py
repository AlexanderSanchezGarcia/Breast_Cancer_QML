from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import datos
import estilo
from manim import (
    ORIGIN,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    PI,
    Arc,
    Circle,
    Create,
    CubicBezier,
    Dot,
    FadeIn,
    Line,
    MoveAlongPath,
    Rectangle,
    RoundedRectangle,
    Scene,
    Text,
    VGroup,
    config,
    rate_functions,
)

if any("MapaMini" in arg for arg in sys.argv):
    estilo.configurar(ancho=1600, alto=220, fps=30)
    config.transparent = True
    config.frame_width = 14.222222222222221
    config.frame_height = 14.222222222222221 * 220 / 1600
else:
    estilo.configurar()


def _icono_mamografia():
    marco = RoundedRectangle(
        width=0.68, height=0.82, corner_radius=0.08,
        stroke_color=estilo.TINTA, stroke_width=2.5, fill_color=estilo.TARJETA, fill_opacity=1.0
    )
    perfil = Arc(
        radius=0.24, start_angle=-PI / 2, angle=PI,
        stroke_color=estilo.CLASICO, stroke_width=2.5
    ).move_to(marco.get_left() + RIGHT * 0.21)
    punto = Dot(point=marco.get_center() + RIGHT * 0.04 + UP * 0.07, radius=0.05, color=estilo.C4)
    return VGroup(marco, perfil, punto)


def _icono_recorte():
    marco = RoundedRectangle(
        width=0.74, height=0.80, corner_radius=0.08,
        stroke_color=estilo.TEXTO, stroke_width=2.2, fill_color=estilo.TARJETA, fill_opacity=1.0
    )
    roi = Rectangle(
        width=0.36, height=0.36,
        stroke_color=estilo.C4, stroke_width=2.6, fill_color=estilo.FONDO, fill_opacity=0.9
    ).move_to(marco.get_center() + RIGHT * 0.05 + UP * 0.04)
    return VGroup(marco, roi)


def _icono_caracteristicas():
    fondo = RoundedRectangle(
        width=0.78, height=0.80, corner_radius=0.08,
        stroke_color=estilo.LINEA, stroke_width=2.0, fill_color=estilo.TARJETA, fill_opacity=1.0
    )
    alturas = [0.26, 0.50, 0.38]
    colores = [estilo.CLASICO, estilo.C4, estilo.C5]
    barras = VGroup()
    for i, (h, col) in enumerate(zip(alturas, colores)):
        b = Rectangle(
            width=0.13, height=h,
            stroke_width=0, fill_color=col, fill_opacity=1.0
        )
        b.move_to(fondo.get_bottom() + UP * (0.13 + h / 2) + RIGHT * ((i - 1) * 0.19))
        barras.add(b)
    return VGroup(fondo, barras)


def _icono_angulos():
    fondo = RoundedRectangle(
        width=0.78, height=0.80, corner_radius=0.08,
        stroke_color=estilo.LINEA, stroke_width=2.0, fill_color=estilo.TARJETA, fill_opacity=1.0
    )
    origen = fondo.get_center() + DOWN * 0.18 + LEFT * 0.20
    r1 = Line(origen, origen + RIGHT * 0.44, stroke_color=estilo.TINTA, stroke_width=2.5)
    r2 = Line(origen, origen + RIGHT * 0.31 + UP * 0.36, stroke_color=estilo.C4, stroke_width=2.5)
    arco = Arc(
        radius=0.24, start_angle=0, angle=0.87,
        arc_center=origen, stroke_color=estilo.CLASICO, stroke_width=2.3
    )
    return VGroup(fondo, r1, r2, arco)


def _icono_cinco_rep():
    """Cinco puntos C1..C5 alineados limpiamente en fila horizontal para quedar bien arriba del rótulo."""
    espec = [
        ("C1", estilo.CLASICO),
        ("C2", estilo.CLASICO_2),
        ("C3", estilo.CLASICO_3),
        ("C4", estilo.C4),
        ("C5", estilo.C5),
    ]
    grupo = VGroup()
    for i, (etq, col) in enumerate(espec):
        x_off = (i - 2) * 0.40
        pto = Dot(point=RIGHT * x_off, radius=0.085, color=col)
        txt = Text(etq, font=estilo.FUENTE, font_size=20, weight="BOLD", color=col)
        txt.next_to(pto, UP, buff=0.08)
        grupo.add(VGroup(pto, txt))
    return grupo


def _curva_bifurcacion(p_ini, p_fin):
    dx = (p_fin[0] - p_ini[0]) * 0.48
    return CubicBezier(
        p_ini,
        p_ini + RIGHT * dx,
        p_fin + LEFT * dx,
        p_fin,
        stroke_color=estilo.TINTA,
        stroke_width=3.2,
    )


class MapaTrabajo(Scene):
    def construct(self):
        estilo.configurar()
        p = datos.pipeline()

        # Regla 10: sin título en el clip. Centramos el camino en vertical y usamos todo el ancho.
        xs = [-6.10, -4.45, -2.80, -1.15, 0.80, 3.45, 4.65]
        x_bif = 2.20
        y_camino = 0.25
        dy_bif = 1.35

        pts_base = [RIGHT * x + UP * y_camino for x in xs[:5]]
        pt_bif = RIGHT * x_bif + UP * y_camino
        pt_sep = RIGHT * xs[5] + UP * (y_camino + dy_bif)
        pt_cla = RIGHT * xs[5] + UP * (y_camino - dy_bif)
        pt_cmp = RIGHT * xs[6] + UP * y_camino

        tramos_guia = VGroup(
            *[
                Line(pts_base[i], pts_base[i + 1], stroke_color=estilo.LINEA, stroke_width=3.0)
                for i in range(4)
            ],
            Line(pts_base[4], pt_bif, stroke_color=estilo.LINEA, stroke_width=3.0),
            _curva_bifurcacion(pt_bif, pt_sep).set_color(estilo.LINEA),
            _curva_bifurcacion(pt_bif, pt_cla).set_color(estilo.LINEA),
            _curva_bifurcacion(pt_sep, pt_cmp).set_color(estilo.LINEA),
            _curva_bifurcacion(pt_cla, pt_cmp).set_color(estilo.LINEA),
        )
        self.add(tramos_guia)

        def _bloque_estacion(x, icono, nombre, lineas_detalle, offset_detalle=0.42):
            """Nombres e íconos arriba del camino (sin tocarse) y detalles cortos debajo."""
            pos = RIGHT * x + UP * y_camino
            nodo = Circle(
                radius=0.12,
                stroke_color=estilo.TINTA,
                stroke_width=3.0,
                fill_color=estilo.FONDO,
                fill_opacity=1.0,
            ).move_to(pos)

            lbl_nombre = Text(
                nombre, font=estilo.FUENTE, font_size=20, weight="BOLD", color=estilo.TINTA
            ).next_to(nodo, UP, buff=0.22)

            icono.next_to(lbl_nombre, UP, buff=0.26)

            detalles = VGroup(
                *[
                    Text(linea, font=estilo.FUENTE, font_size=19, color=estilo.TEXTO)
                    for linea in lineas_detalle
                ]
            ).arrange(DOWN, buff=0.07)
            detalles.move_to(pos + DOWN * (offset_detalle + detalles.height / 2))
            guia_det = Line(
                nodo.get_bottom() + DOWN * 0.04,
                detalles.get_top() + UP * 0.06,
                stroke_color=estilo.LINEA,
                stroke_width=1.8,
            )

            return nodo, VGroup(icono, lbl_nombre, guia_det, detalles)

        est1_nodo, est1_info = _bloque_estacion(
            xs[0],
            _icono_mamografia(),
            "CBIS-DDSM",
            [f"{p['lesiones']:,} lesiones", f"{p['pacientes']:,} pacientes"],
            offset_detalle=0.42,
        )
        est2_nodo, est2_info = _bloque_estacion(
            xs[1],
            _icono_recorte(),
            "Recorte",
            ["resolución original"],
            offset_detalle=1.05,
        )
        est3_nodo, est3_info = _bloque_estacion(
            xs[2],
            _icono_caracteristicas(),
            "Características",
            [f"{p['caracteristicas']} radiómicas"],
            offset_detalle=0.42,
        )
        est4_nodo, est4_info = _bloque_estacion(
            xs[3],
            _icono_angulos(),
            "Ángulos",
            [f"{p['seleccionadas']} ángulos en [0, π]"],
            offset_detalle=1.05,
        )
        est5_nodo, est5_info = _bloque_estacion(
            xs[4],
            _icono_cinco_rep(),
            "5 representaciones",
            ["C1–C3 clásicas", "C4, C5 cuánticas"],
            offset_detalle=0.42,
        )

        # Estación 6: Separabilidad (arriba) y Clasificación (abajo) — texto en negritas sin cajas
        nodo_sep = Circle(
            radius=0.12, stroke_color=estilo.TINTA, stroke_width=3.0,
            fill_color=estilo.FONDO, fill_opacity=1.0
        ).move_to(pt_sep)
        txt_sep = Text(
            "Separabilidad", font=estilo.FUENTE, font_size=22, weight="BOLD", color=estilo.TINTA
        ).next_to(nodo_sep, UP, buff=0.24)

        nodo_cla = Circle(
            radius=0.12, stroke_color=estilo.TINTA, stroke_width=3.0,
            fill_color=estilo.FONDO, fill_opacity=1.0
        ).move_to(pt_cla)
        txt_cla = Text(
            "Clasificación", font=estilo.FUENTE, font_size=22, weight="BOLD", color=estilo.TINTA
        ).next_to(nodo_cla, DOWN, buff=0.24)

        # Estación 7: Comparación a la derecha del nodo final para no tocar la curva
        nodo_cmp = Circle(
            radius=0.13, stroke_color=estilo.TINTA, stroke_width=3.2,
            fill_color=estilo.FONDO, fill_opacity=1.0
        ).move_to(pt_cmp)
        txt_cmp = Text(
            "Comparación", font=estilo.FUENTE, font_size=22, weight="BOLD", color=estilo.TINTA
        ).next_to(nodo_cmp, RIGHT, buff=0.22)

        # Punto viajero ("una lesión")
        lesion_dot = Dot(point=pts_base[0], radius=0.13, color=estilo.C4)
        lesion_halo = Circle(
            radius=0.22, stroke_color=estilo.C4, stroke_width=2.0, stroke_opacity=0.55
        ).move_to(pts_base[0])
        viajero = VGroup(lesion_halo, lesion_dot)

        # 1. CBIS-DDSM
        self.play(
            FadeIn(est1_nodo),
            FadeIn(est1_info, shift=UP * 0.12),
            FadeIn(viajero, scale=0.7),
            run_time=1.4,
        )
        self.wait(0.6)

        # 2..5
        estaciones = [
            (pts_base[0], pts_base[1], est2_nodo, est2_info),
            (pts_base[1], pts_base[2], est3_nodo, est3_info),
            (pts_base[2], pts_base[3], est4_nodo, est4_info),
            (pts_base[3], pts_base[4], est5_nodo, est5_info),
        ]
        for p_a, p_b, nodo, info in estaciones:
            tramo = Line(p_a, p_b, stroke_color=estilo.TINTA, stroke_width=3.4)
            self.play(
                Create(tramo),
                viajero.animate.move_to(p_b),
                run_time=0.95,
                rate_func=rate_functions.ease_in_out_sine,
            )
            self.play(
                FadeIn(nodo),
                FadeIn(info, shift=UP * 0.10),
                run_time=0.95,
            )
            self.wait(0.45)

        # 6. Avance hasta el inicio de la bifurcación (a la derecha de '5 representaciones') y división
        tramo_pre_bif = Line(pts_base[4], pt_bif, stroke_color=estilo.TINTA, stroke_width=3.4)
        self.play(
            Create(tramo_pre_bif),
            viajero.animate.move_to(pt_bif),
            run_time=0.45,
            rate_func=rate_functions.ease_in_out_sine,
        )

        curva_a_sep = _curva_bifurcacion(pt_bif, pt_sep)
        curva_a_cla = _curva_bifurcacion(pt_bif, pt_cla)
        viajero_inf = viajero.copy()
        self.add(viajero_inf)

        self.play(
            Create(curva_a_sep),
            Create(curva_a_cla),
            MoveAlongPath(viajero, curva_a_sep),
            MoveAlongPath(viajero_inf, curva_a_cla),
            run_time=1.05,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.play(
            FadeIn(nodo_sep),
            FadeIn(txt_sep),
            FadeIn(nodo_cla),
            FadeIn(txt_cla),
            run_time=0.95,
        )
        self.wait(0.4)

        # 7. Reunión en Comparación
        curva_de_sep = _curva_bifurcacion(pt_sep, pt_cmp)
        curva_de_cla = _curva_bifurcacion(pt_cla, pt_cmp)
        self.play(
            Create(curva_de_sep),
            Create(curva_de_cla),
            MoveAlongPath(viajero, curva_de_sep),
            MoveAlongPath(viajero_inf, curva_de_cla),
            run_time=1.1,
            rate_func=rate_functions.ease_in_out_sine,
        )
        self.remove(viajero_inf)
        self.play(
            FadeIn(nodo_cmp),
            FadeIn(txt_cmp),
            run_time=0.9,
        )
        self.wait(0.35)

        # Franja discreta bajo el camino
        franja_fondo = RoundedRectangle(
            width=7.8, height=0.58, corner_radius=0.12,
            stroke_color=estilo.LINEA, stroke_width=2.0,
            fill_color=estilo.TARJETA, fill_opacity=1.0
        ).to_edge(DOWN, buff=0.42)
        franja_txt = Text(
            "masas y calcificaciones, por separado",
            font=estilo.FUENTE,
            font_size=22,
            color=estilo.TINTA,
        ).move_to(franja_fondo)
        self.play(FadeIn(franja_fondo), FadeIn(franja_txt), run_time=1.0)
        self.wait(2.0)


def _construir_mini(scene, estacion_activa):
    """Miniatura 1600x220 recortada al camino, con fondo transparente y sin textos encimados."""
    config.pixel_width = 1600
    config.pixel_height = 220
    config.transparent = True
    config.frame_width = 14.222222222222221
    config.frame_height = 14.222222222222221 * 220 / 1600

    xs = [-6.05, -4.20, -2.30, -0.45, 1.80, 4.15, 6.05]
    y_base = -0.04
    dy = 0.36

    pts = [RIGHT * x + UP * y_base for x in xs[:5]]
    pt_sep = RIGHT * xs[5] + UP * (y_base + dy)
    pt_cla = RIGHT * xs[5] + UP * (y_base - dy)
    pt_cmp = RIGHT * xs[6] + UP * y_base

    lineas = VGroup(
        *[
            Line(pts[i], pts[i + 1], stroke_color=estilo.LINEA, stroke_width=3.2)
            for i in range(4)
        ],
        _curva_bifurcacion(pts[4], pt_sep).set_color(estilo.LINEA),
        _curva_bifurcacion(pts[4], pt_cla).set_color(estilo.LINEA),
        _curva_bifurcacion(pt_sep, pt_cmp).set_color(estilo.LINEA),
        _curva_bifurcacion(pt_cla, pt_cmp).set_color(estilo.LINEA),
    )
    scene.add(lineas)

    nombres = [
        "CBIS-DDSM",
        "Recorte",
        "Características",
        "Ángulos",
        "5 representaciones",
    ]
    for i, nombre in enumerate(nombres, start=1):
        activo = i == estacion_activa
        col = estilo.TINTA if activo else estilo.LINEA
        r = 0.13 if activo else 0.095
        pto = Dot(point=pts[i - 1], radius=r, color=col)
        etq = Text(
            nombre,
            font=estilo.FUENTE,
            font_size=20,
            weight="BOLD" if activo else "NORMAL",
            color=col,
        ).next_to(pto, UP, buff=0.14)
        scene.add(pto, etq)

    # Estación 6
    act6 = estacion_activa == 6
    col6 = estilo.TINTA if act6 else estilo.LINEA
    r6 = 0.13 if act6 else 0.095
    pto_sep = Dot(point=pt_sep, radius=r6, color=col6)
    pto_cla = Dot(point=pt_cla, radius=r6, color=col6)
    etq_sep = Text(
        "Separabilidad",
        font=estilo.FUENTE,
        font_size=20,
        weight="BOLD" if act6 else "NORMAL",
        color=col6,
    ).next_to(pto_sep, UP, buff=0.09)
    etq_cla = Text(
        "Clasificación",
        font=estilo.FUENTE,
        font_size=20,
        weight="BOLD" if act6 else "NORMAL",
        color=col6,
    ).next_to(pto_cla, DOWN, buff=0.09)
    scene.add(pto_sep, pto_cla, etq_sep, etq_cla)

    # Estación 7
    act7 = estacion_activa == 7
    col7 = estilo.TINTA if act7 else estilo.LINEA
    r7 = 0.13 if act7 else 0.095
    pto_cmp = Dot(point=pt_cmp, radius=r7, color=col7)
    etq_cmp = Text(
        "Comparación",
        font=estilo.FUENTE,
        font_size=20,
        weight="BOLD" if act7 else "NORMAL",
        color=col7,
    ).next_to(pto_cmp, UP, buff=0.14)
    scene.add(pto_cmp, etq_cmp)


class MapaMini1(Scene):
    def construct(self):
        _construir_mini(self, 1)


class MapaMini2(Scene):
    def construct(self):
        _construir_mini(self, 2)


class MapaMini3(Scene):
    def construct(self):
        _construir_mini(self, 3)


class MapaMini4(Scene):
    def construct(self):
        _construir_mini(self, 4)


class MapaMini5(Scene):
    def construct(self):
        _construir_mini(self, 5)


class MapaMini6(Scene):
    def construct(self):
        _construir_mini(self, 6)


class MapaMini7(Scene):
    def construct(self):
        _construir_mini(self, 7)
