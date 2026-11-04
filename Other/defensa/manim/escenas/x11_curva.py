from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from manim import (
     DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    Arrow,
    BraceBetweenPoints,
    Create,
    DashedLine,
    Dot,
    FadeIn,
    Line,
    Rectangle,
    RoundedRectangle,
    Scene,
    Text,
    VGroup,
    VMobject,
)

import datos
import estilo

estilo.configurar()


class X11Curva(Scene):
    def construct(self):
        df = datos.x11()
        umbrales = datos.x11_umbral()

        alphas = df["alpha"].to_numpy(dtype=float)
        q_auc = df["quantum_auc"].to_numpy(dtype=float)
        c_auc = df["classical_auc"].to_numpy(dtype=float)
        wins = df["quantum_wins"].to_numpy(dtype=bool)

        # Primer alpha donde quantum_wins == True (coincide con x11_umbral()['mass|Projected (ZZ full)'])
        idx_star = int(np.argmax(wins))
        alpha_star = float(alphas[idx_star])
        _ = umbrales.get("mass|Projected (ZZ full)", alpha_star)

        a_min, a_max = float(alphas[0]), float(alphas[-1])
        y_min, y_max = 0.5, 1.0

        # Geometría de los ejes en el lienzo con margen amplio a la derecha para «tarea diseñada»
        x_izq, x_der = -4.85, 3.75
        y_inf, y_sup = -1.55, 2.95

        def a_coord(a: float, y: float) -> np.ndarray:
            xp = x_izq + (a - a_min) / (a_max - a_min) * (x_der - x_izq)
            yp = y_inf + (y - y_min) / (y_max - y_min) * (y_sup - y_inf)
            return np.array([xp, yp, 0.0])

        # Construcción de ejes y rejilla suave
        eje_x = Line(
            a_coord(a_min, y_min), a_coord(a_max, y_min), stroke_color=estilo.TEXTO, stroke_width=2.4
        ).set_z_index(2)
        eje_y = Line(
            a_coord(a_min, y_min), a_coord(a_min, y_max), stroke_color=estilo.TEXTO, stroke_width=2.4
        ).set_z_index(2)

        marcas_x = VGroup()
        rejilla = VGroup()
        for a_val in alphas[::2]:
            p = a_coord(float(a_val), y_min)
            tick = Line(p + UP * 0.08, p + DOWN * 0.08, stroke_color=estilo.TEXTO, stroke_width=2.0)
            lbl = Text(f"{a_val:.1f}", font=estilo.FUENTE, font_size=24, color=estilo.TEXTO).next_to(
                tick, DOWN, buff=0.12
            )
            marcas_x.add(VGroup(tick, lbl))

        marcas_y = VGroup()
        n_pasos_y = int(round((y_max - y_min) * 10)) + 1
        for k in range(n_pasos_y):
            yv = y_min + k * (y_max - y_min) / (n_pasos_y - 1)
            p = a_coord(a_min, yv)
            tick = Line(p + LEFT * 0.08, p + RIGHT * 0.08, stroke_color=estilo.TEXTO, stroke_width=2.0)
            lbl = Text(f"{yv:.1f}", font=estilo.FUENTE, font_size=24, color=estilo.TEXTO).next_to(
                tick, LEFT, buff=0.14
            )
            marcas_y.add(VGroup(tick, lbl))
            if k > 0:
                linea_g = Line(
                    a_coord(a_min, yv),
                    a_coord(a_max, yv),
                    stroke_color=estilo.LINEA,
                    stroke_width=1.2,
                ).set_z_index(-8)
                rejilla.add(linea_g)

        titulo_x = Text(
            "α: fracción de etiquetas que siguen la geometría cuántica",
            font=estilo.FUENTE,
            font_size=27,
            color=estilo.TINTA,
        ).move_to([(x_izq + x_der) / 2, -3.48, 0.0])

        titulo_y = (
            Text("AUC-ROC", font=estilo.FUENTE, font_size=28, color=estilo.TINTA, weight="BOLD")
            .rotate(PI / 2)
            .move_to([x_izq - 1.15, (y_inf + y_sup) / 2, 0.0])
        )

        grupo_ejes = VGroup(rejilla, eje_x, eje_y, marcas_x, marcas_y, titulo_x, titulo_y)

        # Puntos de las dos curvas
        pts_q = [a_coord(float(a), float(y)) for a, y in zip(alphas, q_auc)]
        pts_c = [a_coord(float(a), float(y)) for a, y in zip(alphas, c_auc)]

        # 1. Puntos en alpha = 0 y rótulo «diagnóstico real»
        dot_q0 = Dot(pts_q[0], radius=0.09, color=estilo.C4).set_z_index(5)
        dot_c0 = Dot(pts_c[0], radius=0.09, color=estilo.CLASICO).set_z_index(5)

        etq_diag = (
            Text("diagnóstico real", font=estilo.FUENTE, font_size=26, color=estilo.TINTA, weight="BOLD")
            .move_to([x_izq + 1.35, pts_c[0][1] + 0.78, 0.0])
            .set_z_index(5)
        )
        flecha_diag = Arrow(
            etq_diag.get_bottom() + LEFT * 0.35,
            pts_c[0] + RIGHT * 0.08 + UP * 0.06,
            buff=0.08,
            stroke_width=2.2,
            color=estilo.TINTA,
            max_tip_length_to_length_ratio=0.22,
        ).set_z_index(5)

        # Momento 1: ejes y alpha = 0
        self.play(FadeIn(grupo_ejes), run_time=1.2)
        self.play(
            FadeIn(dot_q0),
            FadeIn(dot_c0),
            FadeIn(etq_diag),
            Create(flecha_diag),
            run_time=1.0,
        )
        self.wait(0.8)

        # 2. Trazado de las dos curvas de izquierda a derecha hasta alpha*
        curva_q_1 = (
            VMobject(stroke_color=estilo.C4, stroke_width=4.5)
            .set_points_as_corners(pts_q[: idx_star + 1])
            .set_z_index(4)
        )
        curva_c_1 = (
            VMobject(stroke_color=estilo.CLASICO, stroke_width=4.5)
            .set_points_as_corners(pts_c[: idx_star + 1])
            .set_z_index(4)
        )
        dots_q_1 = VGroup(
            *[Dot(p, radius=0.065, color=estilo.C4).set_z_index(5) for p in pts_q[1 : idx_star + 1]]
        )
        dots_c_1 = VGroup(
            *[Dot(p, radius=0.065, color=estilo.CLASICO).set_z_index(5) for p in pts_c[1 : idx_star + 1]]
        )

        x_star = a_coord(alpha_star, y_min)[0]

        # Rótulos de las curvas colocados arriba/izquierda de la curva naranja y debajo de la azul sin tocarlas
        etq_curva_q = (
            VGroup(
                Text("kernel cuántico", font=estilo.FUENTE, font_size=25, color=estilo.C4, weight="BOLD"),
                Text("proyectado", font=estilo.FUENTE, font_size=25, color=estilo.C4, weight="BOLD"),
            )
            .arrange(DOWN, buff=0.08, aligned_edge=LEFT)
            .move_to(a_coord(0.56, 0.92))
            .set_z_index(6)
        )

        etq_curva_c = (
            Text(
                "mejor clásico",
                font=estilo.FUENTE,
                font_size=25,
                color=estilo.CLASICO,
                weight="BOLD",
            )
            .move_to(a_coord(0.80, 0.68))
            .set_z_index(6)
        )

        self.play(
            Create(curva_q_1),
            Create(curva_c_1),
            FadeIn(dots_q_1),
            FadeIn(dots_c_1),
            FadeIn(etq_curva_q),
            FadeIn(etq_curva_c),
            run_time=1.8,
        )

        # 3. Al llegar a alpha*: línea vertical punteada y zona sombreada a su derecha
        linea_star = DashedLine(
            [x_star, y_inf, 0.0],
            [x_star, y_sup, 0.0],
            dash_length=0.14,
            stroke_color=estilo.C4,
            stroke_width=3.0,
        ).set_z_index(3)
        etq_star = (
            Text(
                f"α* = {alpha_star:g}",
                font=estilo.FUENTE,
                font_size=28,
                color=estilo.C4,
                weight="BOLD",
            )
            .next_to(linea_star, UP, buff=0.14)
            .set_z_index(6)
        )

        zona_ventaja = (
            Rectangle(
                width=x_der - x_star,
                height=y_sup - y_inf,
                fill_color=estilo.C4,
                fill_opacity=0.10,
                stroke_width=0.0,
            )
            .move_to([(x_star + x_der) / 2, (y_inf + y_sup) / 2, 0.0])
            .set_z_index(-5)
        )

        txt_ventaja = Text(
            "ventaja cuántica",
            font=estilo.FUENTE,
            font_size=27,
            color=estilo.C4,
            weight="BOLD",
        )
        caja_ventaja = RoundedRectangle(
            corner_radius=0.12,
            width=txt_ventaja.width + 0.45,
            height=txt_ventaja.height + 0.26,
            fill_color=estilo.FONDO,
            fill_opacity=0.95,
            stroke_color=estilo.C4,
            stroke_width=1.8,
        )
        insignia_ventaja = (
            VGroup(caja_ventaja, txt_ventaja)
            .move_to([(x_star + x_der) / 2 + 0.25, y_inf + 0.62, 0.0])
            .set_z_index(6)
        )

        self.play(
            Create(linea_star),
            FadeIn(etq_star),
            FadeIn(zona_ventaja),
            FadeIn(insignia_ventaja),
            run_time=1.4,
        )
        self.wait(0.6)

        # Continuación del trazado de las dos curvas hasta alpha = 1
        curva_q_2 = (
            VMobject(stroke_color=estilo.C4, stroke_width=4.5)
            .set_points_as_corners(pts_q[idx_star:])
            .set_z_index(4)
        )
        curva_c_2 = (
            VMobject(stroke_color=estilo.CLASICO, stroke_width=4.5)
            .set_points_as_corners(pts_c[idx_star:])
            .set_z_index(4)
        )
        dots_q_2 = VGroup(
            *[Dot(p, radius=0.065, color=estilo.C4).set_z_index(5) for p in pts_q[idx_star + 1 :]]
        )
        dots_c_2 = VGroup(
            *[Dot(p, radius=0.065, color=estilo.CLASICO).set_z_index(5) for p in pts_c[idx_star + 1 :]]
        )

        self.play(
            Create(curva_q_2),
            Create(curva_c_2),
            FadeIn(dots_q_2),
            FadeIn(dots_c_2),
            run_time=2.2,
        )

        # 4. Rótulo «tarea diseñada» en alpha = 1
        dot_q_fin = Dot(pts_q[-1], radius=0.09, color=estilo.C4).set_z_index(5)
        dot_c_fin = Dot(pts_c[-1], radius=0.09, color=estilo.CLASICO).set_z_index(5)
        etq_disenada = (
            Text(
                "tarea diseñada",
                font=estilo.FUENTE,
                font_size=26,
                color=estilo.TINTA,
                weight="BOLD",
            )
            .move_to([x_der + 1.65, (pts_q[-1][1] + pts_c[-1][1]) / 2, 0.0])
            .set_z_index(6)
        )
        flecha_dis_q = Arrow(
            etq_disenada.get_left() + UP * 0.08,
            pts_q[-1] + RIGHT * 0.08,
            buff=0.08,
            stroke_width=2.0,
            color=estilo.TINTA,
            max_tip_length_to_length_ratio=0.22,
        ).set_z_index(6)
        flecha_dis_c = Arrow(
            etq_disenada.get_left() + DOWN * 0.08,
            pts_c[-1] + RIGHT * 0.08,
            buff=0.08,
            stroke_width=2.0,
            color=estilo.TINTA,
            max_tip_length_to_length_ratio=0.22,
        ).set_z_index(6)

        self.play(
            FadeIn(dot_q_fin),
            FadeIn(dot_c_fin),
            FadeIn(etq_disenada),
            Create(flecha_dis_q),
            Create(flecha_dis_c),
            run_time=1.2,
        )
        self.wait(0.7)

        # 5. Final: llave entre alpha = 0 y alpha*: «distancia del diagnóstico a la ventaja»
        llave = BraceBetweenPoints(
            [x_izq, y_inf - 0.52, 0.0],
            [x_star, y_inf - 0.52, 0.0],
            direction=DOWN,
            color=estilo.DESTACADO,
            buff=0.06,
        ).set_z_index(6)
        etq_llave = (
            Text(
                "distancia del diagnóstico a la ventaja",
                font=estilo.FUENTE,
                font_size=25,
                color=estilo.DESTACADO,
                weight="BOLD",
            )
            .next_to(llave, DOWN, buff=0.10)
            .set_z_index(6)
        )
        if etq_llave.get_left()[0] < -6.5:
            etq_llave.shift(RIGHT * (-6.5 - etq_llave.get_left()[0]))

        self.play(
            FadeIn(llave),
            FadeIn(etq_llave),
            run_time=1.2,
        )
        self.wait(2.3)
