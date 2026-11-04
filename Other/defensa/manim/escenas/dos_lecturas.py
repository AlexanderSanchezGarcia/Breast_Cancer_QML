from pathlib import Path
import sys

import numpy as np

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
    Arrow,
    Create,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Rectangle,
    RoundedRectangle,
    Scene,
    Text,
    TransformFromCopy,
    VGroup,
    VMobject,
)

estilo.configurar()


def _tira_fases(fases, ancho=3.35, semi_alto=0.82, color=estilo.CLASICO, con_marcas=True):
    """Construye una tira horizontal de 4,096 barras finas cuyo alto es la fase en (-pi, pi],
    con eje 0 al centro y marcas -pi, 0, pi."""
    fases = np.asarray(fases, dtype=float)
    n = len(fases)
    altos = np.clip((fases / np.pi) * semi_alto, -semi_alto, semi_alto)
    xs = np.linspace(-ancho / 2, ancho / 2, n)

    # Polilínea vectorial con las 4,096 barras finas desde y=0 hasta y=alto_i
    mobj_4096 = VMobject(stroke_color=color, stroke_width=0.22, stroke_opacity=0.26)
    pts = np.zeros((4 * n, 3), dtype=float)
    p0 = np.column_stack([xs, np.zeros(n), np.zeros(n)])
    p1 = np.column_stack([xs, altos, np.zeros(n)])
    pts[0::4] = p0
    pts[1::4] = p0 + (p1 - p0) / 3.0
    pts[2::4] = p0 + 2.0 * (p1 - p0) / 3.0
    pts[3::4] = p1
    mobj_4096.points = pts

    # Peine representativo de 128 barras nítidas para distinguir las barras positivas/negativas a 1080p
    paso = 32
    peine = VGroup()
    for i in range(0, n, paso):
        x = xs[i]
        h = altos[i]
        peine.add(
            Line(
                RIGHT * x,
                RIGHT * x + UP * h,
                stroke_color=color,
                stroke_width=1.4,
                stroke_opacity=0.92,
            )
        )

    eje_cero = Line(
        LEFT * (ancho / 2 + 0.05),
        RIGHT * (ancho / 2 + 0.05),
        stroke_color=estilo.TINTA,
        stroke_width=1.8,
    )
    guia_sup = DashedLine(
        LEFT * (ancho / 2) + UP * semi_alto,
        RIGHT * (ancho / 2) + UP * semi_alto,
        stroke_color=estilo.LINEA,
        stroke_width=1.4,
    )
    guia_inf = DashedLine(
        LEFT * (ancho / 2) + DOWN * semi_alto,
        RIGHT * (ancho / 2) + DOWN * semi_alto,
        stroke_color=estilo.LINEA,
        stroke_width=1.4,
    )
    eje_y = Line(
        LEFT * (ancho / 2) + DOWN * semi_alto,
        LEFT * (ancho / 2) + UP * semi_alto,
        stroke_color=estilo.TEXTO,
        stroke_width=1.8,
    )

    grupo = VGroup(guia_sup, guia_inf, mobj_4096, peine, eje_cero, eje_y)

    if con_marcas:
        t_pi = Text("π", font=estilo.FUENTE, font_size=25, color=estilo.TEXTO)
        t_pi.next_to(eje_y.get_top(), LEFT, buff=0.10)
        t_0 = Text("0", font=estilo.FUENTE_MONO, font_size=21, color=estilo.TEXTO)
        t_0.next_to(eje_y.get_center(), LEFT, buff=0.10)
        t_mpi = Text("−π", font=estilo.FUENTE, font_size=25, color=estilo.TEXTO)
        t_mpi.next_to(eje_y.get_bottom(), LEFT, buff=0.10)
        grupo.add(t_pi, t_0, t_mpi)

    return grupo


def _polilinea_caminata(fase_a, fase_b, ancho_caja=2.10, alto_caja=1.50, centro=ORIGIN):
    """Construye la caminata de 4,096 flechas unitarias exp(i*(fase_a - fase_b)) como una sola polilínea
    de 4,097 vértices escalada al recuadro, junto con su punto de salida, llegada y flecha resultante."""
    df = np.asarray(fase_a, dtype=float) - np.asarray(fase_b, dtype=float)
    pasos = np.exp(1j * df)
    z = np.r_[0j, np.cumsum(pasos)]
    xs, ys = z.real, z.imag

    min_x, max_x = xs.min(), xs.max()
    min_y, max_y = ys.min(), ys.max()
    escala = min(ancho_caja / max(max_x - min_x, 1e-6), alto_caja / max(max_y - min_y, 1e-6))

    cx = 0.5 * (min_x + max_x)
    cy = 0.5 * (min_y + max_y)
    xs_esc = (xs - cx) * escala + centro[0]
    ys_esc = (ys - cy) * escala + centro[1]

    v = np.column_stack([xs_esc, ys_esc, np.zeros_like(xs_esc)])
    n_seg = len(v) - 1
    pts = np.zeros((4 * n_seg, 3), dtype=float)
    p0 = v[:-1]
    p1 = v[1:]
    pts[0::4] = p0
    pts[1::4] = p0 + (p1 - p0) / 3.0
    pts[2::4] = p0 + 2.0 * (p1 - p0) / 3.0
    pts[3::4] = p1

    camino = VMobject(stroke_color=estilo.CLASICO_2, stroke_width=1.35, stroke_opacity=0.85)
    camino.points = pts

    p_inicio = v[0]
    p_fin = v[-1]
    pto_inicio = Dot(point=p_inicio, radius=0.065, color=estilo.TINTA)
    pto_fin = Dot(point=p_fin, radius=0.065, color=estilo.DESTACADO)
    flecha_res = Arrow(
        p_inicio,
        p_fin,
        buff=0.0,
        stroke_color=estilo.DESTACADO,
        stroke_width=3.6,
        max_tip_length_to_length_ratio=0.22,
    )
    return camino, pto_inicio, pto_fin, flecha_res


class DosLecturas(Scene):
    def construct(self):
        estilo.configurar()
        est = datos.estado_lesion()
        les = datos.lesion()
        fase_a = est["fase_a"]
        fase_b = est["fase_b"]
        z_vals = les["z_c4"]
        k_val = les["kernel_c4_con_otra"]
        n_qubits = len(les["x"])
        n_comp = len(fase_a)

        # Regla 10: sin título en el clip.
        # --- 1. Panel izquierdo: el estado de una lesión (4,096 fases) ---
        panel_izq = RoundedRectangle(
            width=4.45,
            height=5.20,
            corner_radius=0.14,
            stroke_color=estilo.LINEA,
            stroke_width=2.2,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
        ).move_to(LEFT * 4.55)

        lbl_est_1 = Text(
            "el estado de una lesión:",
            font=estilo.FUENTE,
            font_size=22,
            weight="BOLD",
            color=estilo.TINTA,
        )
        lbl_est_2 = Text(
            f"{n_comp:,} fases",
            font=estilo.FUENTE,
            font_size=24,
            weight="BOLD",
            color=estilo.CLASICO,
        )
        lbl_estado_sup = VGroup(lbl_est_1, lbl_est_2).arrange(DOWN, buff=0.08)
        lbl_estado_sup.move_to(panel_izq.get_top() + DOWN * 0.68)

        tira_principal = _tira_fases(
            fase_a, ancho=3.20, semi_alto=0.88, color=estilo.CLASICO, con_marcas=True
        )
        tira_principal.move_to(panel_izq.get_center() + UP * 0.12 + RIGHT * 0.18)

        lbl_sub_1 = Text(
            "todas con la misma probabilidad:",
            font=estilo.FUENTE,
            font_size=19,
            color=estilo.TEXTO,
        )
        lbl_sub_2 = Text(
            "la información está en las fases",
            font=estilo.FUENTE,
            font_size=19,
            weight="BOLD",
            color=estilo.TINTA,
        )
        lbl_estado_inf = VGroup(lbl_sub_1, lbl_sub_2).arrange(DOWN, buff=0.07)
        lbl_estado_inf.move_to(panel_izq.get_bottom() + UP * 0.68)

        self.play(
            FadeIn(panel_izq),
            FadeIn(lbl_estado_sup),
            FadeIn(tira_principal, shift=UP * 0.12),
            FadeIn(lbl_estado_inf),
            run_time=2.0,
        )
        self.wait(1.0)

        # --- 2. Rama (a), arriba a la derecha: comparar los estados completos -> kernel ---
        panel_a = RoundedRectangle(
            width=8.45,
            height=3.45,
            corner_radius=0.14,
            stroke_color=estilo.LINEA,
            stroke_width=2.2,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
        ).move_to(RIGHT * 2.40 + UP * 1.85)

        rotulo_a = Text(
            "(a) comparar los estados completos → kernel",
            font=estilo.FUENTE,
            font_size=23,
            weight="BOLD",
            color=estilo.TEXTO,
        ).move_to(panel_a.get_top() + DOWN * 0.36).align_to(panel_a.get_left() + RIGHT * 0.32, LEFT)

        flecha_a = Arrow(
            panel_izq.get_right() + UP * 0.95,
            panel_a.get_left() + DOWN * 0.10,
            buff=0.10,
            stroke_color=estilo.CLASICO,
            stroke_width=3.0,
            max_tip_length_to_length_ratio=0.18,
        )

        # Dos tiras iniciales dentro de panel_a (fase_a y fase_b), bien centradas dentro de la caja
        pos_tira_a1 = panel_a.get_left() + RIGHT * 3.45 + UP * 0.30
        pos_tira_a2 = panel_a.get_left() + RIGHT * 3.45 + DOWN * 0.72

        tira_a1 = _tira_fases(fase_a, ancho=2.60, semi_alto=0.34, color=estilo.CLASICO, con_marcas=False)
        tira_a1.move_to(pos_tira_a1)
        lbl_a1 = Text("lesión", font=estilo.FUENTE, font_size=20, color=estilo.CLASICO)
        lbl_a1.next_to(tira_a1, LEFT, buff=0.20)

        tira_a2 = _tira_fases(fase_b, ancho=2.60, semi_alto=0.34, color=estilo.C4, con_marcas=False)
        tira_a2.move_to(pos_tira_a2)
        lbl_a2 = Text("otra lesión", font=estilo.FUENTE, font_size=20, color=estilo.C4)
        lbl_a2.next_to(tira_a2, LEFT, buff=0.20)

        self.play(
            FadeIn(panel_a),
            FadeIn(rotulo_a),
            Create(flecha_a),
            TransformFromCopy(tira_principal, tira_a1),
            FadeIn(lbl_a1),
            run_time=1.4,
        )
        self.play(
            FadeIn(tira_a2, shift=UP * 0.12),
            FadeIn(lbl_a2),
            run_time=1.2,
        )
        self.wait(0.6)

        # Conversión de las dos tiras en la caminata 2D de 4,096 flechas con ángulo (fase_a - fase_b)
        centro_caminata = panel_a.get_left() + RIGHT * 1.72 + DOWN * 0.08
        marco_cam = RoundedRectangle(
            width=2.65,
            height=1.75,
            corner_radius=0.10,
            stroke_color=estilo.LINEA,
            stroke_width=1.8,
            fill_color=estilo.FONDO,
            fill_opacity=1.0,
        ).move_to(centro_caminata)

        camino, pto_ini, pto_fin, flecha_res = _polilinea_caminata(
            fase_a, fase_b, ancho_caja=2.20, alto_caja=1.35, centro=centro_caminata
        )

        rotulo_cancelan = Text(
            "las fases apuntan a todos lados y se cancelan",
            font=estilo.FUENTE,
            font_size=19,
            color=estilo.TEXTO,
        ).move_to(panel_a.get_bottom() + UP * 0.30).align_to(panel_a.get_left() + RIGHT * 0.32, LEFT)

        caja_parecido = RoundedRectangle(
            width=4.40,
            height=1.55,
            corner_radius=0.12,
            stroke_color=estilo.CLASICO,
            stroke_width=2.4,
            fill_color=estilo.FONDO,
            fill_opacity=1.0,
        ).move_to(panel_a.get_right() + LEFT * 2.48 + DOWN * 0.08)

        txt_par_1 = Text(
            f"parecido = |resultante|² / {n_comp:,}²",
            font=estilo.FUENTE,
            font_size=20,
            color=estilo.TEXTO,
        )
        txt_par_2 = Text(
            f"= {k_val:.4f}",
            font=estilo.FUENTE,
            font_size=26,
            weight="BOLD",
            color=estilo.TINTA,
        )
        txt_parecido = VGroup(txt_par_1, txt_par_2).arrange(DOWN, buff=0.12).move_to(caja_parecido)

        flecha_int_a = Arrow(
            marco_cam.get_right(),
            caja_parecido.get_left(),
            buff=0.10,
            stroke_color=estilo.TEXTO,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22,
        )

        self.play(
            FadeOut(tira_a1),
            FadeOut(tira_a2),
            FadeOut(lbl_a1),
            FadeOut(lbl_a2),
            FadeIn(marco_cam),
            FadeIn(pto_ini),
            run_time=0.9,
        )
        self.play(
            Create(camino),
            run_time=1.8,
        )
        self.play(
            FadeIn(pto_fin),
            Create(flecha_res),
            FadeIn(rotulo_cancelan),
            Create(flecha_int_a),
            FadeIn(caja_parecido),
            FadeIn(txt_parecido),
            run_time=1.4,
        )
        self.wait(0.8)

        # --- 3. Rama (b), abajo a la derecha: resumir en 12 números <Z_i> -> MLP ---
        panel_b = RoundedRectangle(
            width=8.45,
            height=3.45,
            corner_radius=0.14,
            stroke_color=estilo.LINEA,
            stroke_width=2.2,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
        ).move_to(RIGHT * 2.40 + DOWN * 1.85)

        rotulo_b = Text(
            f"(b) resumir en {n_qubits} números ⟨Zᵢ⟩ → MLP",
            font=estilo.FUENTE,
            font_size=23,
            weight="BOLD",
            color=estilo.TEXTO,
        ).move_to(panel_b.get_top() + DOWN * 0.36).align_to(panel_b.get_left() + RIGHT * 0.32, LEFT)

        flecha_b = Arrow(
            panel_izq.get_right() + DOWN * 0.95,
            panel_b.get_left() + UP * 0.10,
            buff=0.10,
            stroke_color=estilo.C4,
            stroke_width=3.0,
            max_tip_length_to_length_ratio=0.18,
        )

        caja_ansatz = RoundedRectangle(
            width=2.15,
            height=1.18,
            corner_radius=0.12,
            stroke_color=estilo.TINTA,
            stroke_width=2.4,
            fill_color=estilo.FONDO,
            fill_opacity=1.0,
        ).move_to(panel_b.get_left() + RIGHT * 1.38 + DOWN * 0.22)
        txt_ansatz = Text(
            "ansatz\n(θ fijo)",
            font=estilo.FUENTE,
            font_size=21,
            weight="BOLD",
            color=estilo.TINTA,
        ).move_to(caja_ansatz)

        self.play(
            FadeIn(panel_b),
            FadeIn(rotulo_b),
            Create(flecha_b),
            FadeIn(caja_ansatz),
            FadeIn(txt_ansatz),
            run_time=1.4,
        )

        # Gráfico de 12 barras verticales con escala de -0.25 a 0.25 y eje en 0
        escala_z = 0.25
        centro_graf = panel_b.get_right() + LEFT * 2.38 + DOWN * 0.18
        ancho_graf = 3.90
        semi_alto = 0.88

        eje_y = Line(
            centro_graf + LEFT * (ancho_graf / 2) + DOWN * semi_alto,
            centro_graf + LEFT * (ancho_graf / 2) + UP * semi_alto,
            stroke_color=estilo.TEXTO,
            stroke_width=2.0,
        )
        eje_cero = Line(
            centro_graf + LEFT * (ancho_graf / 2),
            centro_graf + RIGHT * (ancho_graf / 2),
            stroke_color=estilo.TINTA,
            stroke_width=2.0,
        )
        guia_sup = DashedLine(
            centro_graf + LEFT * (ancho_graf / 2) + UP * semi_alto,
            centro_graf + RIGHT * (ancho_graf / 2) + UP * semi_alto,
            stroke_color=estilo.LINEA,
            stroke_width=1.6,
        )
        guia_inf = DashedLine(
            centro_graf + LEFT * (ancho_graf / 2) + DOWN * semi_alto,
            centro_graf + RIGHT * (ancho_graf / 2) + DOWN * semi_alto,
            stroke_color=estilo.LINEA,
            stroke_width=1.6,
        )

        t_pos = Text("0.25", font=estilo.FUENTE_MONO, font_size=19, color=estilo.TEXTO)
        t_pos.next_to(eje_y.get_top(), LEFT, buff=0.10)
        t_cero = Text("0", font=estilo.FUENTE_MONO, font_size=19, color=estilo.TEXTO)
        t_cero.next_to(eje_y.get_center(), LEFT, buff=0.10)
        t_neg = Text("−0.25", font=estilo.FUENTE_MONO, font_size=19, color=estilo.TEXTO)
        t_neg.next_to(eje_y.get_bottom(), LEFT, buff=0.10)

        flecha_int_b = Arrow(
            caja_ansatz.get_right() + RIGHT * 0.05,
            t_neg.get_left() + LEFT * 0.08 + UP * semi_alto,
            buff=0.06,
            stroke_color=estilo.C4,
            stroke_width=2.5,
            max_tip_length_to_length_ratio=0.22,
        )

        barras_z = VGroup()
        xs_z = np.linspace(
            -ancho_graf / 2 + 0.24,
            ancho_graf / 2 - 0.20,
            len(z_vals),
        )
        for x_rel, val in zip(xs_z, z_vals):
            frac = np.clip(abs(val) / escala_z, 0.0, 1.0)
            h_vis = max(frac * semi_alto, 0.03)
            barra = Rectangle(
                width=0.20,
                height=h_vis,
                stroke_color=estilo.C4,
                stroke_width=1.2,
                fill_color=estilo.C4,
                fill_opacity=0.95,
            )
            if val >= 0:
                barra.move_to(centro_graf + RIGHT * x_rel + UP * (h_vis / 2))
            else:
                barra.move_to(centro_graf + RIGHT * x_rel + DOWN * (h_vis / 2))
            barras_z.add(barra)

        etq_12 = Text(
            f"1 … {n_qubits}",
            font=estilo.FUENTE_MONO,
            font_size=19,
            color=estilo.TEXTO,
        ).next_to(guia_inf, DOWN, buff=0.10)

        self.play(
            Create(flecha_int_b),
            Create(eje_y),
            Create(eje_cero),
            Create(guia_sup),
            Create(guia_inf),
            FadeIn(t_pos),
            FadeIn(t_cero),
            FadeIn(t_neg),
            run_time=1.2,
        )
        self.play(
            FadeIn(barras_z, lag_ratio=0.06),
            FadeIn(etq_12),
            run_time=1.4,
        )
        self.wait(0.8)

        # --- 4. Final: las dos ramas visibles a la vez, (a) en CLASICO y (b) en C4 ---
        self.play(
            rotulo_a.animate.set_color(estilo.CLASICO),
            panel_a.animate.set_stroke(estilo.CLASICO, width=3.0),
            rotulo_b.animate.set_color(estilo.C4),
            panel_b.animate.set_stroke(estilo.C4, width=3.0),
            run_time=1.3,
        )
        self.wait(2.0)
