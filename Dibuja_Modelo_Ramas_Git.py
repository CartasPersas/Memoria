import matplotlib.pyplot as plt
import numpy as np

# --- Configuración de Colores Corporativos ---
colores_corporativos = {
    "main_azul": "#003366",
    "hotfix_rosa": "#cc0066",
    "develop_azul_claro": "#3366cc",
    "release_amarillo": "#ffcc00",
    "feature_cyan": "#00cccc",
}

# --- Estilos y Posiciones de las Ramas ---
estilos_rama = {
    "main": {"color": colores_corporativos["main_azul"], "y": 4, "etiqueta": "main"},
    "hotfix/*": {"color": colores_corporativos["hotfix_rosa"], "y": 5, "etiqueta": "hotfix/*"},
    "release/x.y.z": {"color": colores_corporativos["release_amarillo"], "y": 3, "etiqueta": "release/x.y.z"},
    "develop": {"color": colores_corporativos["develop_azul_claro"], "y": 2, "etiqueta": "develop"},
    "feature/*": {"color": colores_corporativos["feature_cyan"], "y": 1, "etiqueta": "feature/*"},
}

# --- Coordenadas X para los Eventos del Diagrama ---
coordenadas_x = {
    "inicio_lineas": 0.5,
    "fin_lineas": 9.5,
    "x_ramificar_feature_desde_develop": 1.5,
    "x_fin_trabajo_feature": 3.0,
    "x_ramificar_release_desde_develop": 4.0,
    "x_fin_trabajo_release": 5.5,
    "x_ramificar_hotfix_desde_main": 2.5,
    "x_fin_trabajo_hotfix": 4.5,
    "x_objetivo_comun_merge": 7.5,
}

# --- Configuración de Grosores de Línea ---
GROSOR_ESPECIAL_RAMA_MAIN = 12.0
GROSOR_OTRAS_RAMAS_PRINCIPALES = 8.0
GROSOR_FLECHA = 5.0

# --- Parámetros para la punta de la flecha ---
ANCHO_PUNTA_FLECHA = 0.4
LARGO_PUNTA_FLECHA = 0.4


# --- Creación de la Figura y Ejes ---
figura, ejes = plt.subplots(figsize=(16, 8))

# --- Dibujar Líneas Horizontales para las Ramas ---
for nombre_clave_rama, estilo in estilos_rama.items():
    grosor_a_usar = GROSOR_ESPECIAL_RAMA_MAIN if nombre_clave_rama == "main" else GROSOR_OTRAS_RAMAS_PRINCIPALES
    ejes.plot([coordenadas_x["inicio_lineas"], coordenadas_x["fin_lineas"]], [estilo["y"], estilo["y"]],
              color=estilo["color"], linewidth=grosor_a_usar, label=estilo["etiqueta"])
    ejes.text(coordenadas_x["inicio_lineas"] - 0.2, estilo["y"], estilo["etiqueta"],
              ha='right', va='center', color=estilo["color"], fontsize=26, fontweight='bold')

# --- Función Auxiliar para Dibujar Flechas ---
def dibujar_flecha(clave_rama_origen, clave_rama_destino, clave_x_inicio_flecha, es_accion_merge, color_flecha, radio_curvatura=0.3):
    y_desde = estilos_rama[clave_rama_origen]["y"]
    y_hacia = estilos_rama[clave_rama_destino]["y"]
    x_inicio_absoluto = coordenadas_x[clave_x_inicio_flecha]

    if es_accion_merge:
        x_fin_absoluto = coordenadas_x["x_objetivo_comun_merge"]
    else:
        x_fin_absoluto = coordenadas_x[clave_x_inicio_flecha]

    estilo_punta_flecha = f'-|>,head_width={ANCHO_PUNTA_FLECHA},head_length={LARGO_PUNTA_FLECHA}'

    if x_inicio_absoluto == x_fin_absoluto and y_desde != y_hacia: # Flecha vertical
        connection_style_str = "arc3,rad=0"
        ejes.annotate(
            "",
            xy=(x_fin_absoluto, y_hacia),
            xytext=(x_inicio_absoluto, y_desde),
            arrowprops=dict(arrowstyle=estilo_punta_flecha, color=color_flecha, linewidth=GROSOR_FLECHA,
                            connectionstyle=connection_style_str),
        )
    else: # Flecha curvada u horizontal
        valor_curvatura_real = radio_curvatura if y_hacia > y_desde else -radio_curvatura if y_hacia < y_desde else 0
        if y_desde == y_hacia and not es_accion_merge :
             valor_curvatura_real = 0

        connection_style_str = f"arc3,rad={valor_curvatura_real}"
        ejes.annotate(
            "",
            xy=(x_fin_absoluto, y_hacia),
            xytext=(x_inicio_absoluto, y_desde),
            arrowprops=dict(arrowstyle=estilo_punta_flecha, color=color_flecha, linewidth=GROSOR_FLECHA,
                            connectionstyle=connection_style_str),
        )


# --- Dibujar Flujos Específicos (Ramificaciones y Fusiones) ---
# 1. Rama Feature (Característica)
dibujar_flecha("develop", "feature/*", "x_ramificar_feature_desde_develop", False, estilos_rama["develop"]["color"]) # Color de develop
dibujar_flecha("feature/*", "develop", "x_fin_trabajo_feature", True, estilos_rama["feature/*"]["color"])      # Color de feature

# 2. Rama Release (Lanzamiento)
dibujar_flecha("develop", "release/x.y.z", "x_ramificar_release_desde_develop", False, estilos_rama["develop"]["color"]) # Color de develop
dibujar_flecha("release/x.y.z", "main", "x_fin_trabajo_release", True, estilos_rama["release/x.y.z"]["color"])   # Color de release
dibujar_flecha("release/x.y.z", "develop", "x_fin_trabajo_release", True, estilos_rama["release/x.y.z"]["color"]) # Color de release

# 3. Rama Hotfix (Corrección Urgente)
dibujar_flecha("main", "hotfix/*", "x_ramificar_hotfix_desde_main", False, estilos_rama["main"]["color"]) # Color de main
dibujar_flecha("hotfix/*", "main", "x_fin_trabajo_hotfix", True, estilos_rama["hotfix/*"]["color"], radio_curvatura=0.5) # Color de hotfix
dibujar_flecha("hotfix/*", "develop", "x_fin_trabajo_hotfix", True, estilos_rama["hotfix/*"]["color"], radio_curvatura=0.4) # Color de hotfix


# --- Estética Final del Gráfico ---
ejes.set_yticks([])
ejes.set_xticks([])
ejes.spines['top'].set_visible(False)
ejes.spines['right'].set_visible(False)
ejes.spines['bottom'].set_visible(False)
ejes.spines['left'].set_visible(False)

#plt.title("Modelo de Ramas Git", fontsize=32)
plt.xlim(coordenadas_x["inicio_lineas"] - 0.7, coordenadas_x["fin_lineas"] + 0.5)
plt.ylim(min(estilo["y"] for estilo in estilos_rama.values()) - 0.5, max(estilo["y"] for estilo in estilos_rama.values()) + 0.5)
plt.tight_layout()
plt.show()
