from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from manim import (
    BackgroundRectangle,
     Create,
    DashedLine,
    Dot,
    FadeIn,
    FadeOut,
    Line,
    Polygon,
    RegularPolygon,
    RoundedRectangle,
    Scene,
    Text,
    Transform,
    ValueTracker,
    VGroup,
    VMobject,
     always_redraw,
    linear,
    smooth,
)
import numpy as np
import datos
import estilo

estilo.configurar()


def calcular_trazo_roc(prob, label, umbral_actual):
    """Calcula los vértices (fpr, tpr) desde datos reales hasta umbral_actual.

    En cada umbral u >= umbral_actual, fpr = fracción de benignas con prob >= u
    y tpr = fracción de malignas con prob >= u.
    """
    ben = prob[label == 0]
    mal = prob[label == 1]
    umbrales_cruzados = np.unique(prob[prob >= umbral_actual])[::-1]
    vertices = [(0.0, 0.0)]
    for u in umbrales_cruzados:
        fpr_u = float(np.mean(ben >= u))
        tpr_u = float(np.mean(mal >= u))
        if (fpr_u, tpr_u) != vertices[-1]:
            vertices.append((fpr_u, tpr_u))
    fpr_t = float(np.mean(ben >= umbral_actual))
    tpr_t = float(np.mean(mal >= umbral_actual))
    if (fpr_t, tpr_t) != vertices[-1]:
        vertices.append((fpr_t, tpr_t))
    return np.array(vertices, dtype=float), fpr_t, tpr_t


class RocUmbral(Scene):
    def construct(self):
        c1 = datos.roc_prueba('C1')
        c4 = datos.roc_prueba('C4')

        labels = np.asarray(c1['label'])
        prob_c1 = np.asarray(c1['prob'], dtype=float)
        prob_c4 = np.asarray(c4['prob'], dtype=float)

        n_ben = int(c1['n_benignas'])
        n_mal = int(c1['n_malignas'])
        auc_c1 = float(c1['auc'])
        auc_c4 = float(c4['auc'])

        v_min = float(c1['fpr'][0])
        v_max = float(c1['fpr'][-1])
        v_med = (v_min + v_max) / 2.0

        # Geometría del panel izquierdo (~55 % del ancho)
        x_izq = -6.35
        x_der = 0.35
        ancho_franja = x_der - x_izq

        y_ben_c = 1.45
        y_mal_c = -1.10
        alto_franja = 1.24
        y_eje_prob = -2.15

        def x_de_prob(p):
            return x_izq + float(p) * ancho_franja

        # Geometría del panel derecho (~40 % del ancho, ejes cuadrados ROC)
        roc_x0 = 2.15
        roc_y0 = -1.75
        roc_lado = 4.25

        def punto_roc(fpr_val, tpr_val):
            return np.array([
                roc_x0 + float(fpr_val) * roc_lado,
                roc_y0 + float(tpr_val) * roc_lado,
                0.0,
            ])

        # --- Panel izquierdo: franjas y eje común ---
        caja_ben = RoundedRectangle(
            width=ancho_franja,
            height=alto_franja,
            corner_radius=0.08,
            stroke_color=estilo.LINEA,
            stroke_width=1.6,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
        ).move_to([(x_izq + x_der) / 2.0, y_ben_c, 0.0])

        caja_mal = RoundedRectangle(
            width=ancho_franja,
            height=alto_franja,
            corner_radius=0.08,
            stroke_color=estilo.LINEA,
            stroke_width=1.6,
            fill_color=estilo.TARJETA,
            fill_opacity=1.0,
        ).move_to([(x_izq + x_der) / 2.0, y_mal_c, 0.0])

        icono_ben = RegularPolygon(
            n=3,
            radius=0.09,
            stroke_color=estilo.BENIGNA,
            stroke_width=1.5,
            fill_color=estilo.BENIGNA,
            fill_opacity=0.9,
        )
        txt_ben = Text(
            f'benignas · {n_ben}',
            font=estilo.FUENTE,
            font_size=25,
            color=estilo.BENIGNA,
        )
        rotulo_ben = VGroup(icono_ben, txt_ben).arrange( buff=0.14)
        rotulo_ben.move_to([
            x_izq + rotulo_ben.width / 2.0,
            y_ben_c + alto_franja / 2.0 + 0.24,
            0.0,
        ])

        icono_mal = Dot(
            radius=0.075,
            color=estilo.MALIGNA,
            fill_opacity=0.9,
        )
        txt_mal = Text(
            f'malignas · {n_mal}',
            font=estilo.FUENTE,
            font_size=25,
            color=estilo.MALIGNA,
        )
        rotulo_mal = VGroup(icono_mal, txt_mal).arrange(buff=0.14)
        rotulo_mal.move_to([
            x_izq + rotulo_mal.width / 2.0,
            y_mal_c + alto_franja / 2.0 + 0.24,
            0.0,
        ])

        # Fondo opaco y z_index alto: la línea del umbral pasa por detrás de los rótulos de clase
        for _r in (rotulo_ben, rotulo_mal):
            _r.add_to_back(BackgroundRectangle(_r, color=estilo.FONDO, fill_opacity=1.0, buff=0.08))
            _r.set_z_index(5)

        # Eje de probabilidad de 0 a 1
        linea_eje_prob = Line(
            [x_izq, y_eje_prob, 0.0],
            [x_der, y_eje_prob, 0.0],
            stroke_color=estilo.TEXTO,
            stroke_width=2.0,
        )
        marcas_prob = VGroup()
        for val, texto_val in [(v_min, f'{v_min:.0f}'), (v_med, f'{v_med:.1f}'), (v_max, f'{v_max:.0f}')]:
            xp = x_de_prob(val)
            tick = Line(
                [xp, y_eje_prob - 0.08, 0.0],
                [xp, y_eje_prob + 0.08, 0.0],
                stroke_color=estilo.TEXTO,
                stroke_width=2.0,
            )
            lbl = Text(
                texto_val,
                font=estilo.FUENTE,
                font_size=23,
                color=estilo.TEXTO,
            ).move_to([xp, y_eje_prob - 0.30, 0.0])
            marcas_prob.add(tick, lbl)

        titulo_eje_prob = Text(
            'probabilidad de maligno que da el MLP',
            font=estilo.FUENTE,
            font_size=25,
            color=estilo.TINTA,
        ).move_to([(x_izq + x_der) / 2.0, y_eje_prob - 0.72, 0.0])

        # Rótulo de condición (C1 -> C4)
        rotulo_cond = Text(
            'C1',
            font=estilo.FUENTE,
            font_size=36,
            weight='BOLD',
            color=estilo.CLASICO,
        )
        rotulo_cond.move_to([x_izq + rotulo_cond.width / 2.0, 3.42, 0.0])

        # Puntos de lesiones con jitter vertical reproducible (default_rng(0))
        rng = np.random.default_rng(0)
        desplazamiento_y = rng.uniform(-0.44, 0.44, size=len(labels))

        puntos_lesiones = VGroup()
        coords_y = np.zeros(len(labels), dtype=float)
        for i, (lbl_i, p_i, dy_i) in enumerate(zip(labels, prob_c1, desplazamiento_y)):
            xp = x_de_prob(p_i)
            if lbl_i == 0:
                yp = y_ben_c + float(dy_i)
                m = RegularPolygon(
                    n=3,
                    radius=0.048,
                    stroke_color=estilo.BENIGNA,
                    stroke_width=1.0,
                    fill_color=estilo.BENIGNA,
                    fill_opacity=0.85,
                ).move_to([xp, yp, 0.0])
            else:
                yp = y_mal_c + float(dy_i)
                m = Dot(
                    point=[xp, yp, 0.0],
                    radius=0.042,
                    stroke_color=estilo.MALIGNA,
                    stroke_width=0.8,
                    fill_color=estilo.MALIGNA,
                    fill_opacity=0.85,
                )
            coords_y[i] = yp
            puntos_lesiones.add(m)

        # --- Panel derecho: ejes cuadrados ROC ---
        marco_roc = RoundedRectangle(
            width=roc_lado,
            height=roc_lado,
            corner_radius=0.02,
            stroke_color=estilo.LINEA,
            stroke_width=1.5,
            fill_color=estilo.TARJETA,
            fill_opacity=0.45,
        ).move_to([roc_x0 + roc_lado / 2.0, roc_y0 + roc_lado / 2.0, 0.0])

        eje_roc_x = Line(
            punto_roc(v_min, v_min),
            punto_roc(v_max, v_min),
            stroke_color=estilo.TEXTO,
            stroke_width=2.2,
        )
        eje_roc_y = Line(
            punto_roc(v_min, v_min),
            punto_roc(v_min, v_max),
            stroke_color=estilo.TEXTO,
            stroke_width=2.2,
        )
        borde_sup_roc = Line(
            punto_roc(v_min, v_max),
            punto_roc(v_max, v_max),
            stroke_color=estilo.LINEA,
            stroke_width=1.4,
        )
        borde_der_roc = Line(
            punto_roc(v_max, v_min),
            punto_roc(v_max, v_max),
            stroke_color=estilo.LINEA,
            stroke_width=1.4,
        )

        marcas_roc = VGroup()
        for val, texto_val in [(v_min, f'{v_min:.0f}'), (v_med, f'{v_med:.1f}'), (v_max, f'{v_max:.0f}')]:
            px = punto_roc(val, v_min)
            tx = Line(
                px + np.array([0.0, -0.07, 0.0]),
                px + np.array([0.0, 0.07, 0.0]),
                stroke_color=estilo.TEXTO,
                stroke_width=1.8,
            )
            lx = Text(
                texto_val,
                font=estilo.FUENTE,
                font_size=22,
                color=estilo.TEXTO,
            ).move_to(px + np.array([0.0, -0.28, 0.0]))

            py = punto_roc(v_min, val)
            ty = Line(
                py + np.array([-0.07, 0.0, 0.0]),
                py + np.array([0.07, 0.0, 0.0]),
                stroke_color=estilo.TEXTO,
                stroke_width=1.8,
            )
            ly = Text(
                texto_val,
                font=estilo.FUENTE,
                font_size=22,
                color=estilo.TEXTO,
            ).move_to(py + np.array([-0.32, 0.0, 0.0]))
            marcas_roc.add(tx, lx, ty, ly)

        lbl_roc_x = Text(
            '1 − especificidad',
            font=estilo.FUENTE,
            font_size=25,
            color=estilo.TINTA,
        ).move_to([roc_x0 + roc_lado / 2.0, y_eje_prob - 0.72, 0.0])

        lbl_roc_y = Text(
            'sensibilidad',
            font=estilo.FUENTE,
            font_size=25,
            color=estilo.TINTA,
        ).rotate(np.pi / 2.0).move_to([roc_x0 - 0.76, roc_y0 + roc_lado / 2.0, 0.0])

        diagonal_azar = DashedLine(
            punto_roc(v_min, v_min),
            punto_roc(v_max, v_max),
            dash_length=0.12,
            dashed_ratio=0.55,
            stroke_color=estilo.TEXTO,
            stroke_width=2.0,
        )
        lbl_azar = Text(
            'azar',
            font=estilo.FUENTE,
            font_size=24,
            color=estilo.TEXTO,
        ).move_to(punto_roc(0.76, 0.60))

        grupo_izq = VGroup(
            caja_ben,
            caja_mal,
            rotulo_ben,
            rotulo_mal,
            linea_eje_prob,
            marcas_prob,
            titulo_eje_prob,
            rotulo_cond,
        )
        grupo_roc_base = VGroup(
            marco_roc,
            borde_sup_roc,
            borde_der_roc,
            eje_roc_x,
            eje_roc_y,
            marcas_roc,
            lbl_roc_x,
            lbl_roc_y,
            diagonal_azar,
            lbl_azar,
        )

        # --- Momento 1: Franjas de C1 y ejes ROC con diagonal ---
        self.play(
            FadeIn(grupo_izq),
            FadeIn(puntos_lesiones),
            FadeIn(grupo_roc_base),
            run_time=1.2,
        )
        self.wait(0.8)

        # --- Momento 2: Línea vertical «umbral» en el extremo derecho ---
        tracker_t = ValueTracker(v_max)
        y_umbral_inf = y_eje_prob
        y_umbral_sup = 2.66

        def construir_linea_umbral():
            xt = x_de_prob(tracker_t.get_value())
            linea = Line(
                [xt, y_umbral_inf, 0.0],
                [xt, y_umbral_sup, 0.0],
                stroke_color=estilo.TINTA,
                stroke_width=2.8,
            )
            etiqueta = Text(
                'umbral',
                font=estilo.FUENTE,
                font_size=24,
                weight='BOLD',
                color=estilo.TINTA,
            )
            x_lbl = float(np.clip(xt, x_izq + etiqueta.width / 2.0, x_der - etiqueta.width / 2.0))
            etiqueta.move_to([x_lbl, y_umbral_sup + 0.24, 0.0])
            return VGroup(linea, etiqueta)

        umbral_mob = always_redraw(construir_linea_umbral)

        rotulo_pred_maligno = Text(
            'a la derecha: se predice maligno →',
            font=estilo.FUENTE,
            font_size=24,
            color=estilo.TEXTO,
        )
        rotulo_pred_maligno.move_to([
            x_der - rotulo_pred_maligno.width / 2.0,
            3.42,
            0.0,
        ])

        self.play(
            FadeIn(umbral_mob),
            FadeIn(rotulo_pred_maligno),
            run_time=0.9,
        )
        self.wait(0.8)

        # --- Momento 3: Barrido de derecha a izquierda (1 -> 0) en ~5 s para C1 ---
        prob_activa = {'valores': prob_c1}
        color_activo = {'color': estilo.CLASICO}

        def actualizar_opacidad_puntos(mob):
            t_val = tracker_t.get_value()
            probs = prob_activa['valores']
            for m, p_i in zip(mob, probs):
                if p_i >= t_val:
                    m.set_fill(opacity=0.90)
                    m.set_stroke(opacity=1.0)
                else:
                    m.set_fill(opacity=0.16)
                    m.set_stroke(opacity=0.22)

        puntos_lesiones.add_updater(actualizar_opacidad_puntos)

        def construir_curva_activa():
            verts, _, _ = calcular_trazo_roc(
                prob_activa['valores'], labels, tracker_t.get_value()
            )
            pts_manim = [punto_roc(vx, vy) for vx, vy in verts]
            trazo = VMobject(
                stroke_color=color_activo['color'],
                stroke_width=3.8,
            )
            if len(pts_manim) >= 2:
                trazo.set_points_as_corners(pts_manim)
            else:
                trazo.set_points_as_corners([pts_manim[0], pts_manim[0]])
            return trazo

        def construir_punto_activo():
            _, fpr_t, tpr_t = calcular_trazo_roc(
                prob_activa['valores'], labels, tracker_t.get_value()
            )
            return Dot(
                point=punto_roc(fpr_t, tpr_t),
                radius=0.075,
                color=color_activo['color'],
            )

        def construir_contadores():
            _, fpr_t, tpr_t = calcular_trazo_roc(
                prob_activa['valores'], labels, tracker_t.get_value()
            )
            t1 = Text(
                f'sensibilidad = {tpr_t:.2f}',
                font=estilo.FUENTE,
                font_size=25,
                color=estilo.TINTA,
            )
            t2 = Text(
                f'1 − especificidad = {fpr_t:.2f}',
                font=estilo.FUENTE,
                font_size=25,
                color=estilo.TINTA,
            )
            grupo = VGroup(t1, t2).arrange(direction=[0.0, -1.0, 0.0], aligned_edge=[-1.0, 0.0, 0.0], buff=0.12)
            grupo.move_to([
                roc_x0 + grupo.width / 2.0,
                roc_y0 + roc_lado + 0.56,
                0.0,
            ])
            return grupo

        curva_c1_dinamica = always_redraw(construir_curva_activa)
        punto_roc_dinamico = always_redraw(construir_punto_activo)
        contadores_dinamicos = always_redraw(construir_contadores)

        self.add(curva_c1_dinamica, punto_roc_dinamico, contadores_dinamicos)
        self.play(
            tracker_t.animate.set_value(v_min),
            run_time=5.0,
            rate_func=linear,
        )
        self.wait(0.4)

        # Fijar la curva C1 completa al terminar el barrido
        verts_c1_final, _, _ = calcular_trazo_roc(prob_c1, labels, v_min)
        curva_c1_fija = VMobject(
            stroke_color=estilo.CLASICO,
            stroke_width=3.8,
        ).set_points_as_corners([punto_roc(vx, vy) for vx, vy in verts_c1_final])
        self.remove(curva_c1_dinamica)
        self.add(curva_c1_fija)

        # --- Momento 4: Sombreado bajo C1 y AUC de C1 ---
        pts_poligono_c1 = (
            [punto_roc(v_min, v_min)]
            + [punto_roc(vx, vy) for vx, vy in verts_c1_final]
            + [punto_roc(v_max, v_min)]
        )
        area_c1 = Polygon(
            *pts_poligono_c1,
            stroke_width=0.0,
            fill_color=estilo.CLASICO,
            fill_opacity=0.15,
        )

        lbl_auc_c1 = Text(
            f'C1 · AUC = {auc_c1:.3f}',
            font=estilo.FUENTE,
            font_size=25,
            weight='BOLD',
            color=estilo.CLASICO,
        )
        # Bajo el eje, para que no cruce las curvas
        lbl_auc_c1.move_to([roc_x0 + roc_lado / 2.0, y_eje_prob - 1.16, 0.0])

        self.play(
            FadeIn(area_c1),
            FadeIn(lbl_auc_c1),
            run_time=1.0,
        )
        self.wait(0.8)

        # --- Momento 5: Cambio a C4 (punto a punto ~1.5 s) y barrido ~3 s ---
        puntos_lesiones.remove_updater(actualizar_opacidad_puntos)
        self.remove(punto_roc_dinamico)

        rotulo_cond_c4 = Text(
            'C4',
            font=estilo.FUENTE,
            font_size=36,
            weight='BOLD',
            color=estilo.C4,
        ).move_to([x_izq + rotulo_cond.width / 2.0, 3.42, 0.0])

        animaciones_puntos = []
        for i, (m, p4) in enumerate(zip(puntos_lesiones, prob_c4)):
            xp4 = x_de_prob(p4)
            yp4 = coords_y[i]
            animaciones_puntos.append(
                m.animate.move_to([xp4, yp4, 0.0]).set_fill(opacity=0.88).set_stroke(opacity=1.0)
            )

        prob_activa['valores'] = prob_c4
        color_activo['color'] = estilo.C4

        self.play(
            *animaciones_puntos,
            Transform(rotulo_cond, rotulo_cond_c4),
            tracker_t.animate.set_value(v_max),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(0.3)

        puntos_lesiones.add_updater(actualizar_opacidad_puntos)
        curva_c4_dinamica = always_redraw(construir_curva_activa)
        punto_roc_c4_dinamico = always_redraw(construir_punto_activo)
        self.add(curva_c4_dinamica, punto_roc_c4_dinamico)

        self.play(
            tracker_t.animate.set_value(v_min),
            run_time=3.0,
            rate_func=linear,
        )

        verts_c4_final, _, _ = calcular_trazo_roc(prob_c4, labels, v_min)
        curva_c4_fija = VMobject(
            stroke_color=estilo.C4,
            stroke_width=3.8,
        ).set_points_as_corners([punto_roc(vx, vy) for vx, vy in verts_c4_final])
        self.remove(curva_c4_dinamica)
        self.add(curva_c4_fija)

        lbl_auc_c4 = Text(
            f'C4 · AUC = {auc_c4:.3f}',
            font=estilo.FUENTE,
            font_size=25,
            weight='BOLD',
            color=estilo.C4,
        )
        lbl_auc_c4.move_to([roc_x0 + roc_lado / 2.0, y_eje_prob - 1.54, 0.0])

        self.play(
            FadeIn(lbl_auc_c4),
            run_time=0.8,
        )
        self.wait(0.4)

        # --- Momento 6: Final con ambas curvas, ambos AUC y «más cerca del azar» ---
        puntos_lesiones.remove_updater(actualizar_opacidad_puntos)
        for m in puntos_lesiones:
            m.set_fill(opacity=0.88)
            m.set_stroke(opacity=1.0)

        lbl_cerca_azar = Text(
            'más cerca del azar',
            font=estilo.FUENTE,
            font_size=24,
            weight='BOLD',
            color=estilo.C4,
        ).move_to(punto_roc(0.63, 0.22))

        guia_cerca_azar = Line(
            lbl_cerca_azar.get_top() + np.array([-0.25, 0.04, 0.0]),
            punto_roc(0.42, 0.38),
            stroke_color=estilo.C4,
            stroke_width=2.0,
        )

        self.play(
            FadeOut(contadores_dinamicos),
            FadeOut(punto_roc_c4_dinamico),
            FadeIn(lbl_cerca_azar),
            Create(guia_cerca_azar),
            run_time=0.9,
        )
        self.wait(2.0)
