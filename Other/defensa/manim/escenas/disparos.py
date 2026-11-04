import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import datos
import estilo

estilo.configurar()

import numpy as np
from manim import (
    DOWN,
    RIGHT,
    UP,
    Circle,
    Dot,
    FadeIn,
    RoundedRectangle,
    Scene,
    Text,
    VGroup,
)


class Disparos(Scene):
    def construct(self):
        info_disp = datos.disparos()
        p_val = float(info_disp['mass_C4']['mediana'])
        cero_c4_pct = float(info_disp['mass_C4']['lee_cero_1024']) * 100.0
        cero_c5_pct = float(info_disp['mass_C5']['lee_cero_1024']) * 100.0

        n_lado = 32
        n_total = n_lado * n_lado  # 1,024

        # --- Cuadrícula 32x32 a la izquierda (sin título de diapositiva, regla 10) ---
        centro_grid = np.array([-3.55, 0.05, 0.0])
        paso = 0.155
        offset = (n_lado - 1) * paso / 2.0

        puntos_base = VGroup()
        coords_grid = []
        for fila in range(n_lado):
            for col in range(n_lado):
                x = centro_grid[0] - offset + col * paso
                y = centro_grid[1] + offset - fila * paso
                pos = np.array([x, y, 0.0])
                coords_grid.append(pos)
                puntos_base.add(Dot(point=pos, radius=0.044, color=estilo.LINEA))

        rotulo_grid = Text(
            f"{n_total:,} disparos",
            font=estilo.FUENTE,
            color=estilo.TINTA,
            font_size=28,
            weight="BOLD",
        ).next_to(puntos_base, UP, buff=0.26)

        # Contador dinámico debajo de la cuadrícula
        caja_contador = RoundedRectangle(
            corner_radius=0.12,
            width=4.8,
            height=0.70,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
            stroke_color=estilo.LINEA,
            stroke_width=2.0,
        ).next_to(puntos_base, DOWN, buff=0.26)

        txt_contador_inicial = Text(
            f"sí: — de {n_total:,}",
            font=estilo.FUENTE,
            color=estilo.TEXTO,
            font_size=26,
            weight="BOLD",
        ).move_to(caja_contador.get_center())

        # --- Panel derecho: las 10 rondas (semillas 0…9) ---
        subtitulo_rondas = Text(
            "10 rondas (semillas 0 a 9)",
            font=estilo.FUENTE,
            color=estilo.TEXTO,
            font_size=25,
            weight="BOLD",
        ).move_to(np.array([2.95, 2.75, 0.0]))

        # Precalculamos las 10 rondas con numpy.random.default_rng(seed) para seed = 0..9
        rondas_datos = []
        for seed in range(10):
            rng = np.random.default_rng(seed)
            exitos = rng.random(n_total) < p_val
            indices_si = np.flatnonzero(exitos)
            rondas_datos.append((seed, int(indices_si.size), indices_si))

        # Posiciones de las 10 tarjetas de ronda (2 filas de 5 columnas a la derecha)
        tarjetas_ronda = []
        x_inicio = 0.05
        dx = 1.44
        y_filas = [1.72, 0.28]

        for idx, (seed, conteo, _) in enumerate(rondas_datos):
            col_idx = idx % 5
            fila_idx = idx // 5
            pos_card = np.array([x_inicio + col_idx * dx, y_filas[fila_idx], 0.0])

            es_cero = conteo == 0
            borde_col = estilo.DESTACADO if es_cero else estilo.LINEA
            fondo_col = estilo.TARJETA

            rect = RoundedRectangle(
                corner_radius=0.10,
                width=1.32,
                height=1.20,
                fill_color=fondo_col,
                fill_opacity=1.0,
                stroke_color=borde_col,
                stroke_width=2.8 if es_cero else 1.8,
            ).move_to(pos_card)

            lbl_semilla = Text(
                f"Ronda {seed + 1}",
                font=estilo.FUENTE,
                color=estilo.TEXTO,
                font_size=18,
            ).move_to(pos_card + np.array([0.0, 0.37, 0.0]))

            lbl_num = Text(
                str(conteo),
                font=estilo.FUENTE,
                color=estilo.DESTACADO if es_cero else estilo.C4,
                font_size=32,
                weight="BOLD",
            ).move_to(pos_card + np.array([0.0, -0.02, 0.0]))

            if es_cero:
                lbl_pie = Text(
                    "se lee 0",
                    font=estilo.FUENTE,
                    color=estilo.DESTACADO,
                    font_size=19,
                    weight="BOLD",
                ).move_to(pos_card + np.array([0.0, -0.39, 0.0]))
            else:
                lbl_pie = Text(
                    f"de {n_total:,}",
                    font=estilo.FUENTE,
                    color=estilo.TEXTO,
                    font_size=17,
                ).move_to(pos_card + np.array([0.0, -0.39, 0.0]))

            tarjetas_ronda.append(VGroup(rect, lbl_semilla, lbl_num, lbl_pie))

        # --- Paso 1: Mostrar cuadrícula de 1,024 puntos grises y rótulo ---
        self.play(
            FadeIn(puntos_base),
            FadeIn(rotulo_grid),
            FadeIn(caja_contador),
            FadeIn(txt_contador_inicial),
            FadeIn(subtitulo_rondas),
            run_time=1.2,
        )
        self.wait(0.8)

        # --- Paso 2 y 3: Simular las 10 rondas ---
        capa_encendidos = VGroup()
        self.add(capa_encendidos)
        txt_contador_actual = txt_contador_inicial

        for idx, (seed, conteo, indices_si) in enumerate(rondas_datos):
            es_lenta = idx < 3
            t_anim = 0.45 if es_lenta else 0.15
            t_pausa = 1.55 if es_lenta else 0.35

            nuevos_encendidos = VGroup()
            for pos_i in indices_si:
                c_pos = coords_grid[int(pos_i)]
                aro = Circle(radius=0.11, color=estilo.C4, stroke_width=2.5).move_to(c_pos)
                pto = Dot(point=c_pos, radius=0.075, color=estilo.C4)
                nuevos_encendidos.add(VGroup(aro, pto))

            es_cero = conteo == 0
            col_cnt = estilo.DESTACADO if es_cero else estilo.C4
            nuevo_txt_contador = Text(
                f"sí: {conteo} de {n_total:,}",
                font=estilo.FUENTE,
                color=col_cnt,
                font_size=27,
                weight="BOLD",
            ).move_to(caja_contador.get_center())

            self.remove(capa_encendidos)
            self.remove(txt_contador_actual)
            capa_encendidos = nuevos_encendidos
            txt_contador_actual = nuevo_txt_contador
            self.add(capa_encendidos, txt_contador_actual)

            self.play(
                FadeIn(tarjetas_ronda[idx]),
                run_time=t_anim,
            )
            self.wait(t_pausa)

        # --- Paso 4: Resumen final con valor real y porcentajes de lectura 0 ---
        caja_resumen = RoundedRectangle(
            corner_radius=0.14,
            width=6.95,
            height=2.15,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
            stroke_color=estilo.TINTA,
            stroke_width=2.4,
        ).move_to(np.array([2.95, -1.85, 0.0]))

        linea_real = Text(
            f"valor real ≈ {p_val:.4f}",
            font=estilo.FUENTE,
            color=estilo.TINTA,
            font_size=30,
            weight="BOLD",
        )

        t_pref = Text("se leen exactamente 0: ", font=estilo.FUENTE, color=estilo.TINTA, font_size=24)
        t_c4 = Text(f"C4 {cero_c4_pct:.0f}%", font=estilo.FUENTE, color=estilo.C4, font_size=26, weight="BOLD")
        t_sep = Text(" · ", font=estilo.FUENTE, color=estilo.TEXTO, font_size=24)
        t_c5 = Text(f"C5 {cero_c5_pct:.0f}%", font=estilo.FUENTE, color=estilo.C5, font_size=26, weight="BOLD")
        linea_ceros = VGroup(t_pref, t_c4, t_sep, t_c5).arrange(RIGHT, buff=0.10)

        linea_sub = Text(
            "de los pares, masas",
            font=estilo.FUENTE,
            color=estilo.TEXTO,
            font_size=23,
        )

        bloque_texto_resumen = VGroup(linea_real, linea_ceros, linea_sub).arrange(DOWN, buff=0.20)
        bloque_texto_resumen.move_to(caja_resumen.get_center())
        grupo_resumen = VGroup(caja_resumen, bloque_texto_resumen)

        self.play(FadeIn(grupo_resumen), run_time=0.9)
        self.wait(2.2)
