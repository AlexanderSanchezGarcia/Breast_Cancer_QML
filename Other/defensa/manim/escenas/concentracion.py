from pathlib import Path
import math
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import numpy as np
from manim import (
    DOWN,
    LEFT,
    PI,
    RIGHT,
    UP,
    Create,
    FadeIn,
    FadeOut,
    Line,
    ManimColor,
    RoundedRectangle,
    Scene,
    Square,
    Succession,
    SurroundingRectangle,
    Text,
    UpdateFromAlphaFunc,
    VGroup,
    Wait,
    interpolate_color,
)

import datos
import estilo

estilo.configurar()


def fmt_2sig(val: float) -> str:
    """Formatea un flotante positivo con 2 cifras significativas en notación decimal."""
    if val == 0:
        return "0"
    exp = math.floor(math.log10(abs(val)))
    decimals = max(0, 1 - exp)
    return f"{val:.{decimals}f}"


def construir_mapa_calor(matriz: np.ndarray, lado: float, centro: np.ndarray):
    """Construye una cuadrícula 40x40 con escala lineal de 0 (FONDO) a 1 (TINTA)."""
    n = matriz.shape[0]
    paso = lado / n
    c_fondo = ManimColor(estilo.FONDO)
    c_tinta = ManimColor(estilo.TINTA)

    celdas = VGroup()
    x0 = centro[0] - lado / 2 + paso / 2
    y0 = centro[1] + lado / 2 - paso / 2

    for i in range(n):
        for j in range(n):
            v = float(np.clip(matriz[i, j], 0.0, 1.0))
            col = interpolate_color(c_fondo, c_tinta, v)
            sq = Square(
                side_length=paso,
                fill_color=col,
                fill_opacity=1.0,
                stroke_color=col,
                stroke_width=0.6,
            )
            sq.move_to([x0 + j * paso, y0 - i * paso, 0.0])
            celdas.add(sq)

    borde = Square(
        side_length=lado,
        fill_opacity=0.0,
        stroke_color=estilo.TEXTO,
        stroke_width=2.0,
    ).move_to(centro)

    # Línea fina que divide los bloques 0-19 (benignas) y 20-39 (malignas)
    div_h = Line(
        centro + LEFT * (lado / 2) + UP * 0,
        centro + RIGHT * (lado / 2) + UP * 0,
        stroke_color=estilo.TEXTO,
        stroke_width=1.4,
        stroke_opacity=0.75,
    )
    div_v = Line(
        centro + DOWN * (lado / 2) + RIGHT * 0,
        centro + UP * (lado / 2) + RIGHT * 0,
        stroke_color=estilo.TEXTO,
        stroke_width=1.4,
        stroke_opacity=0.75,
    )

    # Etiquetas de ejes: benignas (0-19) y malignas (20-39)
    cuarto = lado / 4
    etq_col_ben = Text("benignas", font=estilo.FUENTE, font_size=24, color=estilo.TEXTO)
    etq_col_ben.move_to(centro + LEFT * cuarto + DOWN * (lado / 2 + 0.30))

    etq_col_mal = Text("malignas", font=estilo.FUENTE, font_size=24, color=estilo.TEXTO)
    etq_col_mal.move_to(centro + RIGHT * cuarto + DOWN * (lado / 2 + 0.30))

    etq_fil_ben = Text("benignas", font=estilo.FUENTE, font_size=24, color=estilo.TEXTO)
    etq_fil_ben.rotate(PI / 2)
    etq_fil_ben.move_to(centro + UP * cuarto + LEFT * (lado / 2 + 0.32))

    etq_fil_mal = Text("malignas", font=estilo.FUENTE, font_size=24, color=estilo.TEXTO)
    etq_fil_mal.rotate(PI / 2)
    etq_fil_mal.move_to(centro + DOWN * cuarto + LEFT * (lado / 2 + 0.32))

    decoracion = VGroup(borde, div_h, div_v, etq_col_ben, etq_col_mal, etq_fil_ben, etq_fil_mal)
    decoracion.set_z_index(5)
    return celdas, decoracion


def construir_barra_color(centro: np.ndarray, ancho: float = 0.30, alto: float = 3.6, pasos: int = 60):
    """Barra de color lineal de 0 (FONDO) a 1 (TINTA)."""
    c_fondo = ManimColor(estilo.FONDO)
    c_tinta = ManimColor(estilo.TINTA)
    franjas = VGroup()
    dy = alto / pasos
    y_base = centro[1] - alto / 2 + dy / 2

    for k in range(pasos):
        v = k / (pasos - 1)
        col = interpolate_color(c_fondo, c_tinta, v)
        rect = Square(side_length=1.0).stretch_to_fit_width(ancho).stretch_to_fit_height(dy)
        rect.set_fill(col, opacity=1.0)
        rect.set_stroke(col, width=0.6)
        rect.move_to([centro[0], y_base + k * dy, 0.0])
        franjas.add(rect)

    borde = (
        Square(side_length=1.0)
        .stretch_to_fit_width(ancho)
        .stretch_to_fit_height(alto)
        .set_fill(opacity=0.0)
        .set_stroke(estilo.TEXTO, width=1.8)
        .move_to(centro)
    )

    t_max = Text("1", font=estilo.FUENTE, font_size=24, color=estilo.TEXTO).next_to(borde, UP, buff=0.14)
    t_min = Text("0", font=estilo.FUENTE, font_size=24, color=estilo.TEXTO).next_to(borde, DOWN, buff=0.14)
    t_mid = Text("0.5", font=estilo.FUENTE, font_size=22, color=estilo.TEXTO).next_to(borde, RIGHT, buff=0.14)

    return VGroup(franjas, borde, t_max, t_min, t_mid)


class Concentracion(Scene):
    def construct(self):
        lado = 4.1
        centro_izq = np.array([-3.25, -0.15, 0.0])
        centro_der = np.array([2.15, -0.15, 0.0])
        centro_barra = np.array([5.45, -0.15, 0.0])

        # Datos reales desde datos.py
        mat_rbf = datos.kernel("RBF")
        med_rbf = datos.mediana_kernel("RBF")
        c_vals_inv = list(reversed(datos.c_valores()))  # [0.02, 0.05, 0.1, 0.2, 0.5, 1.0]

        # Mapa izquierdo (RBF fijo)
        celdas_rbf, deco_rbf = construir_mapa_calor(mat_rbf, lado, centro_izq)
        titulo_rbf = Text(
            "RBF clásico", font=estilo.FUENTE, font_size=34, color=estilo.CLASICO, weight="BOLD"
        ).move_to([centro_izq[0], 2.95, 0.0])
        sub_rbf = Text(
            f"mediana = {med_rbf:.2f}", font=estilo.FUENTE, font_size=28, color=estilo.TINTA
        ).move_to([centro_izq[0], 2.38, 0.0])

        # Mapa derecho (C4 inicial en c = 0.02)
        c_ini = c_vals_inv[0]
        nombre_ini = f"C4_c{c_ini}"
        mat_c4_actual = datos.kernel(nombre_ini).astype(float)
        med_ini = datos.mediana_kernel(nombre_ini)

        celdas_c4, deco_c4 = construir_mapa_calor(mat_c4_actual, lado, centro_der)
        titulo_c4 = Text(
            "Kernel cuántico C4", font=estilo.FUENTE, font_size=34, color=estilo.C4, weight="BOLD"
        ).move_to([centro_der[0], 2.95, 0.0])

        def crear_rotulo_c4(c_val: float, med_val: float) -> VGroup:
            t_c = Text(f"c = {c_val:g}", font=estilo.FUENTE, font_size=28, color=estilo.C4, weight="BOLD")
            t_sep = Text("  ·  ", font=estilo.FUENTE, font_size=28, color=estilo.TEXTO)
            t_m = Text(
                f"mediana = {fmt_2sig(med_val)}", font=estilo.FUENTE, font_size=28, color=estilo.TINTA
            )
            grp = VGroup(t_c, t_sep, t_m).arrange(RIGHT, buff=0.12)
            grp.move_to([centro_der[0], 2.38, 0.0])
            return grp

        sub_c4 = crear_rotulo_c4(c_ini, med_ini)

        # Barra de color
        barra = construir_barra_color(centro_barra)

        # Momento 1: aparición de ambos mapas y barra de color
        self.play(
            FadeIn(titulo_rbf),
            FadeIn(sub_rbf),
            FadeIn(celdas_rbf),
            FadeIn(deco_rbf),
            FadeIn(titulo_c4),
            FadeIn(sub_c4),
            FadeIn(celdas_c4),
            FadeIn(deco_c4),
            FadeIn(barra),
            run_time=1.4,
        )
        self.wait(0.8)

        # Momento 2: barrido de c en orden inverso hasta c = 1
        c_fondo = ManimColor(estilo.FONDO)
        c_tinta = ManimColor(estilo.TINTA)

        for c_sig in c_vals_inv[1:]:
            nombre_sig = f"C4_c{c_sig}"
            mat_sig = datos.kernel(nombre_sig).astype(float)
            med_sig = datos.mediana_kernel(nombre_sig)
            nuevo_sub_c4 = crear_rotulo_c4(c_sig, med_sig)

            mat_origen = mat_c4_actual.copy()
            mat_destino = mat_sig.copy()

            def actualizar_matriz(grupo, alpha, m0=mat_origen, m1=mat_destino):
                m_interp = (1.0 - alpha) * m0 + alpha * m1
                plano = np.clip(m_interp.ravel(), 0.0, 1.0)
                for idx, sq in enumerate(grupo):
                    col = interpolate_color(c_fondo, c_tinta, float(plano[idx]))
                    sq.set_fill(col, opacity=1.0)
                    sq.set_stroke(col, width=0.6)

            self.play(
                UpdateFromAlphaFunc(celdas_c4, actualizar_matriz, run_time=1.5),
                Succession(
                    FadeOut(sub_c4, run_time=0.25),
                    FadeIn(nuevo_sub_c4, run_time=0.25),
                    Wait(1.0),
                ),
            )
            sub_c4 = nuevo_sub_c4
            mat_c4_actual = mat_sig
            self.wait(0.35)

        # Momento 3: mensaje final con c = 1
        texto_final = Text(
            "c = 1: casi todos los pares se ven ortogonales",
            font=estilo.FUENTE,
            font_size=30,
            color=estilo.TINTA,
            weight="BOLD",
        )
        caja_final = RoundedRectangle(
            corner_radius=0.15,
            width=texto_final.width + 0.7,
            height=texto_final.height + 0.36,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
            stroke_color=estilo.C4,
            stroke_width=2.2,
        )
        banner_final = VGroup(caja_final, texto_final).move_to([0.0, -3.32, 0.0])

        self.play(FadeIn(banner_final), run_time=1.0)
        self.wait(2.2)
