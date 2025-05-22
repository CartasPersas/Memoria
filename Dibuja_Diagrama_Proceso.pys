from graphviz import Digraph

dot = Digraph(format='png')
dot.attr(
    rankdir='TB',        
    splines='polyline',
    bgcolor='white',
    fontname='Arial',
    nodesep="0.5",
    ranksep="1.5"
)

def create_node(dot, node_id, title, entrada, accion, salida, border_color): 
    # Esta función genera un nodo con estilo de tabla, borde grueso y color personalizado.
    label = f'''<
        <TABLE BORDER="0" CELLBORDER="0" CELLSPACING="4">
            <TR><TD ALIGN="LEFT"><B>{title}</B></TD></TR>
            <TR><TD ALIGN="LEFT"><I>Entrada:</I> {entrada}</TD></TR>
            <TR><TD ALIGN="LEFT"><I>Acción:</I> {accion}</TD></TR>
            <TR><TD ALIGN="LEFT"><I>Salida:</I> {salida}</TD></TR>
        </TABLE>>'''
    dot.node(
        node_id,
        label=label,
        shape='box',
        style='filled',
        fillcolor='white',
        color=border_color,
        fontname="Arial",
        fontcolor="black",
        penwidth="5"
    )

# Definimos los nodos
create_node(dot, 'A', '1️⃣ Recepción de Peticiones y Priorización',
            'Solicitudes de desarrollo/mejoras...', 
            'Evaluación del impacto...', 
            'Definición de prioridades.', '#003366')
create_node(dot, 'B', '2️⃣ Planificación del Proyecto',
            'Demandas priorizadas.', 
            'Asignación de metodología...', 
            'Plan de trabajo definido.', '#003366')
create_node(dot, 'C', '3️⃣ Análisis y Diseño',
            'Proyecto planificado.', 
            'Validación de requisitos...', 
            'Documento de especificaciones...', '#0099cc')
create_node(dot, 'D', '4️⃣ Desarrollo e Integración',
            'Diseño aprobado.', 
            'Codificación, revisión...', 
            'Versión lista para pruebas.', '#0099cc')
create_node(dot, 'E', '5️⃣ Pruebas y Aseguramiento de Calidad',
            'Aplicación desarrollada.', 
            'Pruebas unitarias...', 
            'Aplicación lista para producción.', '#666666')
create_node(dot, 'F', '6️⃣ Despliegue en Producción y Gestión del Cambio',
            'Aplicación validada en QA.', 
            'Coordinación del despliegue...', 
            'Nueva versión en producción.', '#666666')
create_node(dot, 'G', '7️⃣ Gestión de Incidencias y Soporte',
            'Aplicación en producción.', 
            'Monitorización, resolución...', 
            'Mantenimiento continuo y mejoras.', '#cc0066')

# Definimos Subgrafos para alinear nodos en filas 
with dot.subgraph() as s1:
    s1.attr(rank='same')
    s1.node('A')
    s1.node('B')
with dot.subgraph() as s2:
    s2.attr(rank='same')
    s2.node('C')
    s2.node('D')
with dot.subgraph() as s3:
    s3.attr(rank='same')
    s3.node('E')
    s3.node('F')
with dot.subgraph() as s4:
    s4.attr(rank='same')
    s4.node('G')

# Nodos con patrón zig-zag:
dot.edge('A:e', 'B:w')
dot.edge('B:s', 'C:n')
dot.edge('C:e', 'D:w')
dot.edge('D:s', 'E:n')
dot.edge('E:e', 'F:w')
dot.edge('F:s', 'G:n')

# Generar y abrir la imagen 
dot.render('diagrama_zigzag_puertos', view=True)
