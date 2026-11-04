import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import datos
import estilo

estilo.configurar()

import numpy as np
from manim import (
    DEGREES,
    PI,
    TAU,
    Create,
    DashedLine,
    Dot3D,
    FadeIn,
    FadeOut,
    Line,
    MathTex,
    ParametricFunction,
    RoundedRectangle,
    Text,
    ThreeDScene,
    UpdateFromAlphaFunc,
    VGroup,
)


class QubitBloch(ThreeDScene):
    def construct(self):
        # Ángulo real de la primera característica de la lesión (datos.py)
        info_lesion = datos.lesion()
        x_val = float(info_lesion['x'][0])
        giro_total = 2.0 * x_val

        # Configuración de cámara fija que deja ver bien el ecuador
        phi_cam = 65 * DEGREES
        theta_cam = -45 * DEGREES
        self.set_camera_orientation(phi=phi_cam, theta=theta_cam)
        self.camera.reset_rotation_matrix()

        # Vectores unitarios del plano de pantalla en coordenadas 3D del mundo
        u_right = np.array([-np.sin(theta_cam), np.cos(theta_cam), 0.0])
        u_up = np.array([
            -np.cos(phi_cam) * np.cos(theta_cam),
            -np.cos(phi_cam) * np.sin(theta_cam),
            np.sin(phi_cam),
        ])

        # Esfera grande que ocupa más de la mitad izquierda del cuadro
        centro = -2.65 * u_right + 0.02 * u_up
        R = 2.95

        def pt(vx, vy, vz):
            return centro + R * np.array([vx, vy, vz], dtype=float)

        def proyeccion_2d(punto_3d):
            p = self.camera.project_point(np.array(punto_3d, dtype=float))
            return np.array([float(p[0]), float(p[1]), 0.0])

        # --- Esfera de Bloch en trazo fino ---
        ecuador = ParametricFunction(
            lambda t: pt(np.cos(t), np.sin(t), 0.0),
            t_range=[0, TAU, 0.04],
            color=estilo.TEXTO,
            stroke_width=2.6,
            stroke_opacity=0.68,
        )
        meridiano_xz = ParametricFunction(
            lambda t: pt(np.cos(t), 0.0, np.sin(t)),
            t_range=[0, TAU, 0.04],
            color=estilo.LINEA,
            stroke_width=2.0,
            stroke_opacity=0.88,
        )
        meridiano_yz = ParametricFunction(
            lambda t: pt(0.0, np.cos(t), np.sin(t)),
            t_range=[0, TAU, 0.04],
            color=estilo.LINEA,
            stroke_width=2.0,
            stroke_opacity=0.88,
        )

        # Ejes internos Z, Y y el eje X principal
        eje_z = Line(pt(0, 0, -1.10), pt(0, 0, 1.10), color=estilo.TEXTO, stroke_width=2.0, stroke_opacity=0.6)
        eje_x = Line(pt(-1.10, 0, 0), pt(1.12, 0, 0), color=estilo.TINTA, stroke_width=2.8, stroke_opacity=0.85)
        eje_y = Line(pt(0, -1.08, 0), pt(0, 1.08, 0), color=estilo.TEXTO, stroke_width=1.8, stroke_opacity=0.55)

        punto_centro = Dot3D(point=centro, radius=0.05, color=estilo.TEXTO)
        punto_polo_n = Dot3D(point=pt(0, 0, 1), radius=0.065, color=estilo.TINTA)
        punto_polo_s = Dot3D(point=pt(0, 0, -1), radius=0.065, color=estilo.TEXTO)
        punto_mas = Dot3D(point=pt(1, 0, 0), radius=0.07, color=estilo.TINTA)

        esfera_grupo = VGroup(
            meridiano_xz,
            meridiano_yz,
            ecuador,
            eje_z,
            eje_y,
            eje_x,
            punto_centro,
            punto_polo_n,
            punto_polo_s,
            punto_mas,
        )

        # --- Rótulos 2D fijos en pantalla para los polos y |+⟩ (sin letra 'X' que se encime) ---
        lbl_0 = MathTex(r"|0\rangle", color=estilo.TINTA, font_size=40)
        lbl_0.move_to(proyeccion_2d(pt(0, 0, 1.16)) + np.array([0.0, 0.14, 0.0]))

        lbl_1 = MathTex(r"|1\rangle", color=estilo.TINTA, font_size=40)
        lbl_1.move_to(proyeccion_2d(pt(0, 0, -1.16)) + np.array([0.0, -0.14, 0.0]))

        lbl_mas = MathTex(r"|+\rangle", color=estilo.TINTA, font_size=38)
        lbl_mas.move_to(proyeccion_2d(pt(1.18, 0, 0)) + np.array([0.16, -0.10, 0.0]))

        # --- Flecha 3D del estado del qubit ---
        vec_actual = np.array([0.0, 0.0, 1.0])

        def construir_flecha(v_unit, col):
            destino = pt(v_unit[0], v_unit[1], v_unit[2])
            cuerpo = Line(centro, destino, color=col, stroke_width=6.5)
            punta = Dot3D(point=destino, radius=0.105, color=col)
            return VGroup(cuerpo, punta)

        flecha = construir_flecha(vec_actual, estilo.TINTA)

        # --- Tarjetas de rótulos en el lado derecho (2D fijas, una sola línea por tarjeta) ---
        panel_x = 3.80
        ancho_panel = 5.85
        alto_panel = 1.08

        # Rótulo Hadamard
        caja_h = RoundedRectangle(
            corner_radius=0.14,
            width=ancho_panel,
            height=alto_panel,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
            stroke_color=estilo.LINEA,
            stroke_width=2.2,
        ).move_to(np.array([panel_x, 1.65, 0.0]))
        txt_h = Text(
            "Hadamard",
            font=estilo.FUENTE,
            color=estilo.TINTA,
            font_size=26,
            weight="BOLD",
        ).move_to(caja_h.get_center())
        tarjeta_h = VGroup(caja_h, txt_h)

        # Rótulo C4
        caja_c4 = RoundedRectangle(
            corner_radius=0.14,
            width=ancho_panel,
            height=alto_panel,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
            stroke_color=estilo.C4,
            stroke_width=3.0,
        ).move_to(np.array([panel_x, 0.0, 0.0]))
        txt_c4 = Text(
            "C4: giro en Z, se queda en el ecuador",
            font=estilo.FUENTE,
            color=estilo.C4,
            font_size=21,
            weight="BOLD",
        ).move_to(caja_c4.get_center())
        tarjeta_c4 = VGroup(caja_c4, txt_c4)

        # Rótulo C5
        caja_c5 = RoundedRectangle(
            corner_radius=0.14,
            width=ancho_panel,
            height=alto_panel,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
            stroke_color=estilo.C5,
            stroke_width=3.0,
        ).move_to(np.array([panel_x, -1.65, 0.0]))
        txt_c5 = Text(
            "C5: giro en Y, sale del ecuador",
            font=estilo.FUENTE,
            color=estilo.C5,
            font_size=21,
            weight="BOLD",
        ).move_to(caja_c5.get_center())
        tarjeta_c5 = VGroup(caja_c5, txt_c5)

        # --- Paso 1: Esfera y flecha apuntando a |0⟩ ---
        self.add_fixed_in_frame_mobjects(lbl_0, lbl_1)
        self.add(esfera_grupo, flecha)
        self.play(
            FadeIn(lbl_0),
            FadeIn(lbl_1),
            run_time=1.0,
        )
        self.wait(1.0)

        # --- Paso 2: Hadamard (giro continuo de π alrededor de (X+Z)/√2 hasta |+⟩) ---
        eje_h_dir = np.array([1.0 / np.sqrt(2.0), 0.0, 1.0 / np.sqrt(2.0)])
        eje_h_linea = DashedLine(
            pt(-0.85 * eje_h_dir[0], 0.0, -0.85 * eje_h_dir[2]),
            pt(1.15 * eje_h_dir[0], 0.0, 1.15 * eje_h_dir[2]),
            color=estilo.CLASICO,
            stroke_width=2.5,
            dash_length=0.12,
        )

        def vec_hadamard(alpha):
            t = alpha * PI
            return np.array([
                0.5 * (1.0 - np.cos(t)),
                -np.sin(t) / np.sqrt(2.0),
                0.5 * (1.0 + np.cos(t)),
            ])

        estela_h = ParametricFunction(
            lambda t: pt(
                0.5 * (1.0 - np.cos(t)),
                -np.sin(t) / np.sqrt(2.0),
                0.5 * (1.0 + np.cos(t)),
            ),
            t_range=[0, PI, 0.04],
            color=estilo.CLASICO,
            stroke_width=3.2,
            stroke_opacity=0.45,
        )

        self.add_fixed_in_frame_mobjects(tarjeta_h)
        self.play(FadeIn(tarjeta_h), Create(eje_h_linea), run_time=0.6)

        def actualizar_h(mob, alpha):
            v = vec_hadamard(alpha)
            mob.become(construir_flecha(v, estilo.TINTA))

        self.play(
            UpdateFromAlphaFunc(flecha, actualizar_h),
            Create(estela_h),
            run_time=2.2,
        )
        self.add_fixed_in_frame_mobjects(lbl_mas)
        self.play(FadeIn(lbl_mas), FadeOut(eje_h_linea), FadeOut(estela_h), run_time=0.5)
        self.wait(1.0)

        # --- Paso 3: C4, giro en Z de ángulo 2·x dejando estela naranja en el ecuador ---
        self.add_fixed_in_frame_mobjects(tarjeta_c4)
        self.play(FadeIn(tarjeta_c4), run_time=0.6)

        def vec_c4(alpha):
            ang = alpha * giro_total
            return np.array([np.cos(ang), np.sin(ang), 0.0])

        estela_c4 = ParametricFunction(
            lambda t: pt(np.cos(t), np.sin(t), 0.0),
            t_range=[0, giro_total, 0.03],
            color=estilo.C4,
            stroke_width=8.0,
        )

        def actualizar_c4(mob, alpha):
            v = vec_c4(alpha)
            mob.become(construir_flecha(v, estilo.C4))

        self.play(
            UpdateFromAlphaFunc(flecha, actualizar_c4),
            Create(estela_c4),
            run_time=2.5,
        )
        v_fin_c4 = vec_c4(1.0)
        flecha_testigo_c4 = construir_flecha(v_fin_c4, estilo.C4)
        flecha_testigo_c4[0].set_stroke(opacity=0.55, width=4.2)
        self.add(flecha_testigo_c4)
        self.wait(1.2)

        # --- Paso 4: Vuelve a |+⟩ ---
        def actualizar_regreso(mob, alpha):
            v = vec_c4(1.0 - alpha)
            mob.become(construir_flecha(v, estilo.TINTA))

        self.play(
            UpdateFromAlphaFunc(flecha, actualizar_regreso),
            run_time=1.2,
        )
        self.wait(0.6)

        # --- Paso 5: C5, giro en Y el mismo ángulo 2·x dejando estela verde que sale del ecuador ---
        self.add_fixed_in_frame_mobjects(tarjeta_c5)
        self.play(FadeIn(tarjeta_c5), run_time=0.6)

        def vec_c5(alpha):
            ang = alpha * giro_total
            return np.array([np.cos(ang), 0.0, -np.sin(ang)])

        estela_c5 = ParametricFunction(
            lambda t: pt(np.cos(t), 0.0, -np.sin(t)),
            t_range=[0, giro_total, 0.03],
            color=estilo.C5,
            stroke_width=8.0,
        )

        def actualizar_c5(mob, alpha):
            v = vec_c5(alpha)
            mob.become(construir_flecha(v, estilo.C5))

        self.play(
            UpdateFromAlphaFunc(flecha, actualizar_c5),
            Create(estela_c5),
            run_time=2.5,
        )

        # --- Paso 6: Final con las dos estelas visibles a la vez ---
        self.wait(2.2)
