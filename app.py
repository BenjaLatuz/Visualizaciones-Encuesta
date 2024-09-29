import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Configurar la página para usar el ancho completo
st.set_page_config(layout="wide")

# CSS para ajustar el color de fondo, el estilo de las tarjetas y el color de texto
st.markdown("""
<style>
html, body, [class*="ViewContainer"] {
    color: #ddd; /* Color de texto claro */
    background-color: #1c1f26; /* Ajusta el fondo oscuro */
}
.card {
    margin: 10px;
    padding: 15px;
    text-align: center;
    color: #ddd; /* Color de texto dentro de las tarjetas para contraste con el fondo claro */
    background-color: #2a2d35; /* Fondo oscuro para las tarjetas */
    border-radius: 10px;
    box-shadow: 2px 2px 10px grey;
}
.metric-name {
    font-size: 16px;
    color: #4caf50; /* Color verde claro para los nombres métricos */
    font-weight: bold;
}
.metric-value {
    font-size: 26px;
    color: #fff; /* Texto blanco para valores métricos */
    margin-top: 5px;
    margin-bottom: 5px;
}
.metric-freq {
    font-size: 16px;
    color: #ccc; /* Gris claro para la frecuencia */
}
.box {
    border: 1px solid #555; /* Borde más oscuro para las cajas */
    padding: 10px;
    margin: 10px 0;
    border-radius: 10px;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
    background-color: #333; /* Fondo más oscuro para las cajas */
}
</style>
""", unsafe_allow_html=True)

# Define el color de fondo y el color del texto para que coincida con el estilo de tu página
background_color = '#1c1f26'  # Color de fondo de la página
text_color = '#ddd'  # Color del texto en la página
edge_color = '#555'  # Color para los bordes del gráfico, que podría coincidir con tu estilo

# Configuración de Matplotlib para que coincida con los estilos de Streamlit
plt.rcParams['figure.facecolor'] = background_color
plt.rcParams['axes.facecolor'] = background_color
plt.rcParams['text.color'] = text_color
plt.rcParams['axes.labelcolor'] = text_color
plt.rcParams['xtick.color'] = text_color
plt.rcParams['ytick.color'] = text_color
plt.rcParams['axes.edgecolor'] = edge_color


# Cargar el archivo CSV
df = pd.read_csv('Encuesta.csv')

# Columnas a excluir (Marca temporal y Pregunta Abierta)
columns_to_exclude = ['Marca temporal', 'Pregunta Abierta']

# Seleccionar solo las columnas que no están excluidas (es decir, las numéricas)
columns_to_melt = [col for col in df.columns if col not in columns_to_exclude]

# Hacer el unpivot (melt) de las columnas con respuestas numéricas, excluyendo Marca temporal y Pregunta Abierta
melted_df = pd.melt(df.drop(columns=columns_to_exclude), var_name='Pregunta', value_name='Respuesta')

# Crear las pestañas
tab1, tab2, tab3, tab4 = st.tabs(["Área de Software", "Área de Datos", "Área de Sistemas", "Hoja 4"])

# Contenido para la primera hoja
with tab1:
    st.header("Dashboard de Visualizaciones")
    st.write("A continuación se muestran las visualizaciones asociadas a las respuestas de la encuesta en el área de Software")
    
    # Selector de categoría
    # Se buscará que si hay muchas tecnologías asociadas, haya un scroll horizontal
    # y proximamente, se ligará a un csv y así se actualizará automáticamente (no hardcodeado, si es que alcanza el tiempo)
    # Datos de categorías de tecnologías
    category_options = {
        "Lenguajes de Programación": [
            {"name": "Python (Ingeniería de Datos)", "percentage": "64%", "frequency": "147 veces mencionado en 229 ofertas de Ingeniería de Datos"},
            {"name": "SQL", "percentage": "43%", "frequency": "275 veces mencionado en 640 ofertas totales"},
            {"name": "JavaScript", "percentage": "38%", "frequency": "131 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Java", "percentage": "36%", "frequency": "125 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Python (Ingeniería de Software)", "percentage": "28%", "frequency": "97 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "R", "percentage": "21%", "frequency": "49 veces mencionado en 229 ofertas de Ingeniería de Datos"},
            {"name": "TypeScript", "percentage": "17%", "frequency": "58 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "C", "percentage": "12%", "frequency": "40 veces mencionado en 345 ofertas de Ingeniería de Software"}
        ],
        "Tecnologías Frontend": [
            {"name": "React", "percentage": "34%", "frequency": "118 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Angular", "percentage": "28%", "frequency": "97 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "HTML", "percentage": "24%", "frequency": "82 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "CSS", "percentage": "22%", "frequency": "77 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Vue", "percentage": "9%", "frequency": "32 veces mencionado en 345 ofertas de Ingeniería de Software"}
        ],
        "Tecnologías Backend": [
            {"name": "Spring Boot", "percentage": "17%", "frequency": "118 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Rails", "percentage": "4%", "frequency": "15 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Express.js", "percentage": "4%", "frequency": "15 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "NestJS", "percentage": "4%", "frequency": "15 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Next.js", "percentage": "4%", "frequency": "14 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Django", "percentage": "4%", "frequency": "12 veces mencionado en 345 ofertas de Ingeniería de Software"}
        ],
        "Otras Herramientas, Tecnologías, Metodologías y/o Prácticas de Desarrollo de Software": [
            {"name": "Git", "percentage": "39%", "frequency": "134 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Arquitectura Rest", "percentage": "19%", "frequency": "65 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Docker", "percentage": "16%", "frequency": "54 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Arquitectura Microservicios", "percentage": "14%", "frequency": "50 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Metodología Scrum", "percentage": "14%", "frequency": "48 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Kubernetes", "percentage": "11%", "frequency": "39 veces mencionado en 345 ofertas de Ingeniería de Software"},
            {"name": "Pruebas Unitarias", "percentage": "10%", "frequency": "33 veces mencionado en 345 ofertas de Ingeniería de Software"}
        ],
        "Herramientas y Servicios en la Nube": [
            {"name": "AWS", "percentage": "26%", "frequency": "169 veces mencionado en 640 ofertas totales"},
            {"name": "Azure", "percentage": "17%", "frequency": "111 veces mencionado en 640 ofertas totales"},
            {"name": "Google Cloud Platform", "percentage": "13%", "frequency": "84 veces mencionado en 640 ofertas totales"}
            
        ]
    }
    # Crear un estado para la página actual y la categoría seleccionada
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 0

    if 'previous_category' not in st.session_state:
        st.session_state.previous_category = None

    # Seleccionar la categoría principal
    selected_category = st.selectbox("Seleccione una categoría para ver los detalles:", list(category_options.keys()))

    # Restablecer la página a 1 si cambia la categoría
    if st.session_state.previous_category != selected_category:
        st.session_state.current_page = 0  # Restablece a la primera página cuando cambia de categoría
        st.session_state.previous_category = selected_category  # Actualiza la categoría previa

    # Obtener las tecnologías de la categoría seleccionada
    technologies = category_options[selected_category]

    # Definir cuántas tecnologías mostrar por página
    num_items_per_page = 4
    total_items = len(technologies)
    num_pages = (total_items + num_items_per_page - 1) // num_items_per_page  # Número total de páginas

    # Botones para avanzar y retroceder páginas
    col1, col2, col3 = st.columns([1, 8, 1])

    with col1:
        if st.button("Anterior") and st.session_state.current_page > 0:
            st.session_state.current_page -= 1

    with col3:
        if st.button("Siguiente") and st.session_state.current_page < num_pages - 1:
            st.session_state.current_page += 1

    # Calcular el índice de inicio y final para mostrar las tecnologías de la página actual
    start_idx = st.session_state.current_page * num_items_per_page
    end_idx = min(start_idx + num_items_per_page, total_items)

    # Mostrar solo las tecnologías de la página actual
    cols = st.columns(num_items_per_page)
    for idx, col in enumerate(cols):
        if start_idx + idx < len(technologies):
            tech = technologies[start_idx + idx]
            col.markdown(f"""
            <div class="card">
                <div class="metric-name">{tech['name']}</div>
                <div class="metric-value">{tech['percentage']}</div>
                <div class="metric-freq">{tech['frequency']}</div>
            </div>
            """, unsafe_allow_html=True)

    # Mostrar el número de página actual
    st.write(f"Página {st.session_state.current_page + 1} de {num_pages}")
        ########################## FRONTEND ##################################################

    preguntas_seleccionadas = ['React', 'Vue', 'Angular', 'HTML y CSS']

    filtered_df = melted_df[melted_df['Pregunta'].isin(preguntas_seleccionadas)]
    respuesta_range = [1, 2, 3, 4, 5]
    grouped_df = filtered_df.groupby(['Respuesta', 'Pregunta']).size().unstack(fill_value=0).reindex(index=respuesta_range, fill_value=0)

    fig, ax = plt.subplots(figsize=(6, 4))
    grouped_df.plot(kind='bar', stacked=False, ax=ax)
    ax.set_title('Desarrollo de Frontend', fontsize=10)
    ax.set_xlabel('Respuestas', fontsize=8)
    ax.set_ylabel('Frecuencia', fontsize=8)
    ax.set_xticks(range(len(grouped_df.index)))
    ax.set_xticklabels(grouped_df.index, rotation=0)
    ax.legend(fontsize=7)

    col1, col2 = st.columns(2)
    with col1:
        st.title("Desarrollo de Frontend")
        st.pyplot(fig)

    ########################## Distintas Áreas ##################################################

    preguntas_seleccionadas = ['Metodologías Ágiles', 'QA', 'Arquitectura de Software', 'Control de Versiones', 'Despliegue de Aplicaciones', 'Diseño de Software']
    filtered_df = melted_df[melted_df['Pregunta'].isin(preguntas_seleccionadas)]
    mean_responses = filtered_df.groupby('Pregunta')['Respuesta'].mean()

    categorias = mean_responses.index.tolist()
    valores = mean_responses.values
    valores = np.append(valores, valores[0])
    num_vars = len(categorias)
    angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angulos += angulos[:1]

    fig, ax = plt.subplots(figsize=(4, 4), subplot_kw=dict(polar=True))
    ax.fill(angulos, valores, color='#1f77b4', alpha=0.25)
    ax.plot(angulos, valores, color='#1f77b4', linewidth=2)
    ax.set_xticks(angulos[:-1])
    ax.set_xticklabels(categorias, fontsize=7)
    ax.set_ylim(0, 5)
    ax.set_title('Promedio de Respuestas por Distintas Áreas', fontsize=9)

    with col2:
        st.title("Distintas Áreas - Gráfico de Araña")
        st.pyplot(fig)

    ########################## Lenguajes de Programación + SQL ##########################

    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.title("Mapa de Calor - Competencia en Lenguajes de Programación")
        
        preguntas_seleccionadas_1 = ['Python (Software)', 'R', 'Java', 'JavaScript', 'TypeScript', 'Python (Datos)', 'Ruby Go C', 'SQL']
        filtered_df_1 = melted_df[melted_df['Pregunta'].isin(preguntas_seleccionadas_1)]
        mean_responses_1 = filtered_df_1.groupby('Pregunta')['Respuesta'].mean()

        heatmap_data = mean_responses_1.reset_index()
        heatmap_data = heatmap_data.pivot_table(index='Pregunta', values='Respuesta')

        plt.figure(figsize=(6, 4))
        sns.heatmap(heatmap_data, annot=True, cmap="YlGnBu", linewidths=.5)
        plt.title('Mapa de Calor de Competencia en Lenguajes de Programación', fontsize=12)
        plt.xlabel('Competencias', fontsize=10)
        plt.ylabel('Lenguajes de Programación', fontsize=10)

        st.pyplot(plt)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="box">', unsafe_allow_html=True)
        st.title("Otra Visualización")
        fig, ax = plt.subplots()
        ax.bar(['A', 'B', 'C'], [10, 20, 30])
        st.pyplot(fig)
        st.markdown('</div>', unsafe_allow_html=True)
    # Contenido para la segunda hoja











with tab2:
    st.header("Hoja 2")
    st.write("Aquí puedes poner contenido de la Hoja 2")
 
    # Dividir en columnas
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.metric(label="Documents", value="10.5K", delta="125")
    with col2:
        st.metric(label="Annotations", value="510", delta="-2")
    with col3:
        st.metric(label="Accuracy", value="87.9%", delta="0.1%")
    with col4:
        st.metric(label="Training Time", value="1.5 hours", delta="10 mins")
    with col5:
        st.metric(label="Processing Time", value="3 seconds", delta="-0.1 seconds")

















    
# Contenido para la tercera hoja
with tab3:
    st.header("Hoja 3")
    st.write("Aquí puedes poner contenido de la Hoja 3")

# Contenido para la cuarta hoja
with tab4:
    st.header("Hoja 4")
    st.write("Aquí puedes poner contenido de la Hoja 4")