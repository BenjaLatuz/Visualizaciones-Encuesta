import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go

# Configurar el tema de Streamlit
st.set_page_config(
    page_title="Dashboard de Encuesta",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded")


# CSS para ajustar el color de fondo, el estilo de las tarjetas y el color de texto
st.markdown("""
<style>
html, body, [class*="ViewContainer"] {
    color: #ddd;
    background-color: #1c1f26;
}
.metric {
    margin: 10px;
    padding: 15px;
    text-align: center;
    color: #ddd;
    background-color: #2a2d35;
    border-radius: 10px;
    box-shadow: 2px 2px 10px grey;
}
.metric-name {
    font-size: 16px;
    color: #4caf50;
    font-weight: bold;
}
.metric-value {
    font-size: 26px;
    color: #fff;
    margin-top: 5px;
    margin-bottom: 5px;
}
.metric-freq {
    font-size: 16px;
    color: #ccc;
}
.box {
    border: 1px solid #555;
    padding: 10px;
    margin: 10px 0;
    border-radius: 10px;
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.1);
    background-color: #333;
}
            
.card-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
}
.card {
    flex: 1 0 30%;
    margin: 10px;
    padding: 15px;
    text-align: center;
    color: #ddd;
    background-color: #2a2d35;
    border-radius: 10px;
    box-shadow: 2px 2px 10px grey;
    min-width: 250px;
}
.card-title {
    font-size: 20px;
    color: #4caf50;
    font-weight: bold;
    margin-bottom: 10px;
}
.card-text {
    font-size: 16px;
    color: #ccc;
    line-height: 1.6;
}
            
/* Ajustes para pantallas pequeñas */
@media (max-width: 768px) {
    .card {
        flex: 1 0 45%; /* Ocupa 45% de la pantalla para 2 columnas en móviles */
        min-width: 150px; /* Tamaño mínimo más pequeño en móviles */
    }
    .metric-value {
        font-size: 20px;
    }
}

@media (max-width: 480px) {
    .card {
        flex: 1 0 100%; /* Ocupa el 100% del ancho de la pantalla en móviles */
        margin: 10px 0;
    }
    .metric-value {
        font-size: 18px;
    }
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

st.title("Dashboard de Visualizaciones")
st.write("A continuación se muestran las visualizaciones asociadas a las respuestas de la encuesta, y con las tecnologías más demandadas en el mercado laboral.")


# Crear las pestañas
tab1, tab2 = st.tabs(["Ofertas Laborales", "Perfil de Egreso"])

# Contenido para la primera hoja
with tab1:
    st.header("Demandas del Mercado Laboral")
    st.write("Aquí se muestra la demanda de tecnologías, habilidades, herramientas y conocimientos categorizadas por distintas áreas de la ingeniería en computación. Se puede navegar entre las categorías, y algunas contienen más de una página, por lo que se puede avanzar y retroceder entre ellas.")
    
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
            
        ],
        "Herramientas y Tecnologías de Análisis, Procesamiento y Visualización de Datos": [
            {"name": "PowerBI", "percentage": "35%", "frequency": "79 veces mencionado en 229 ofertas de Ingeniería de Datos"},
            {"name": "Tableau", "percentage": "14%", "frequency": "33 veces mencionado en 229 ofertas de Ingeniería de Datos"},
            {"name": "Apache Spark", "percentage": "14%", "frequency": "33 veces mencionado en 229 ofertas de Ingeniería de Datos"},
            {"name": "Apache Hadoop", "percentage": "9%", "frequency": "20 veces mencionado en 229 ofertas de Ingeniería de Datos"},
            {"name": "Looker", "percentage": "7%", "frequency": "15 veces mencionado en 229 ofertas de Ingeniería de Datos"},
        ],
        "Conceptos y Áreas de la Ingeniería de Datos": [
            {"name": "Procesos ETL", "percentage": "30%", "frequency": "68 veces mencionado en 229 ofertas de Ingeniería de Datos"},
            {"name": "Machine Learning", "percentage": "26%", "frequency": "59 veces mencionado en 229 ofertas de Ingeniería de Datos"},
            {"name": "Big Data", "percentage": "20%", "frequency": "46 veces mencionado en 229 ofertas de Ingeniería de Datos"},
            {"name": "Inteligencia Artificial", "percentage": "15%", "frequency": "34 veces mencionado en 229 ofertas de Ingeniería de Datos"}
        ]
        #"Habilidades Profesionales": [
        #    {"name": "Trabajo en Equipo", "percentage": "10%", "frequency": "64 veces mencionado en 640 ofertas totales"},
        #    {"name": "Habilidades de Comunicación", "percentage": "7%", "frequency": "46 veces mencionado en 640 ofertas totales"},
        #    {"name": "Resolución de Problemas", "percentage": "6%", "frequency": "39 veces mencionado en 640 ofertas totales"},
        #    {"name": "Gestión de Proyectos", "percentage": "5%", "frequency": "33 veces mencionado en 640 ofertas totales"},
        #    {"name": "Toma de Decisiones", "percentage": "5%", "frequency": "31 veces mencionado en 640 ofertas totales"}
        #]
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
        st.button("Anterior", disabled=st.session_state.current_page == 0, on_click=lambda: st.session_state.update(current_page=st.session_state.current_page - 1))

    with col3:
        st.button("Siguiente", disabled=st.session_state.current_page >= num_pages - 1, on_click=lambda: st.session_state.update(current_page=st.session_state.current_page + 1))

    # Calcular el índice de inicio y final para mostrar las tecnologías de la página actual
    start_idx = st.session_state.current_page * num_items_per_page
    end_idx = min(start_idx + num_items_per_page, total_items)

    # Mostrar solo las tecnologías de la página actual
    cols = st.columns(num_items_per_page)
    for idx, col in enumerate(cols):
        if start_idx + idx < len(technologies):
            tech = technologies[start_idx + idx]
            col.markdown(f"""
            <div class="metric">
                <div class="metric-name">{tech['name']}</div>
                <div class="metric-value">{tech['percentage']}</div>
                <div class="metric-freq">{tech['frequency']}</div>
            </div>
            """, unsafe_allow_html=True)
    # Mostrar el número de página actual
    st.write(f"Página {st.session_state.current_page + 1} de {num_pages}")

    #Separador
    st.markdown("<hr>", unsafe_allow_html=True)

    st.header("Visualización de Respuestas Encuesta: Sección Ofertas Laborales")
    st.write("Aquí se muestran las visualizaciones interactivas de las respuestas de la encuesta sobre las ofertas laborales, categorizadas por distintas áreas y aspectos de la ingeniería en computación. Algunas categorías contienen más de un gráfico, y puedes seleccionar cuál deseas ver utilizando los botones disponibles. Recordar que las respuestas de la encuesta están en una escala de 1 a 5, donde 1 es 'Muy poco competente' y 5 es 'Muy competente'.")
    #Separador
    st.markdown("<hr>", unsafe_allow_html=True)

    ########################## Títulos para cada columna ##########################
    col1, col2 = st.columns(2)

    ########################## Distribución de los gráficos ##########################
    #col3, col4 = st.columns(2)  # Crear dos columnas para alinear los gráficos
    
    with col1:
        st.header("Frecuencia de Competencia en Tecnologías Backend y Frontend")
        # Usar st.radio para seleccionar entre Frontend y Backend
        selected_tech_category = st.radio(
            "Seleccione una categoría", 
            options=["Frontend", "Backend"], 
            index=0, 
            horizontal=True
        )

    # Gráfico de barras (Frontend/Backend)
    #with col3:
        ########################## FRONTEND y BACKEND ##########################
        category_switch = {
            "Frontend": ['React', 'Vue', 'Angular', 'HTML y CSS'],
            "Backend": ['Spring Boot', 'Django', 'Rails', 'Nodejs (Frameworks)']
        }

        selected_technologies = category_switch[selected_tech_category]

        # Filtrar el DataFrame según las tecnologías seleccionadas
        filtered_df = melted_df[melted_df['Pregunta'].isin(selected_technologies)]

        # Agrupar los datos por Respuesta y Pregunta para contar las frecuencias
        grouped_df = filtered_df.groupby(['Respuesta', 'Pregunta']).size().unstack(fill_value=0)


        fig = go.Figure()

        # Añadir cada tecnología como un conjunto de barras
        for tecnologia in grouped_df.columns:
            fig.add_trace(go.Bar(
                x=grouped_df.index,  # Eje X serán las respuestas
                y=grouped_df[tecnologia],  # Eje Y serán las frecuencias
                name=tecnologia
            ))

        # Ajustar el layout del gráfico
        fig.update_layout(
            title=dict(text=f'Desarrollo de {selected_tech_category}', font=dict(size=18)),
            xaxis_title=dict(text='Respuestas', font=dict(size=18)),
            yaxis_title=dict(text='Frecuencia', font=dict(size=18)),
            legend=dict(font=dict(size=14)),  # Aumenta el tamaño de la leyenda
            barmode='group',  # Estilo multibarra
            yaxis=dict(tickmode='linear', tickfont=dict(size=18)),  # Solo enteros en el eje Y, ajustar tamaño de los ticks
            xaxis=dict(tickfont=dict(size=18)),  # Ajustar tamaño de las etiquetas del eje X
            plot_bgcolor='#1c1f26',  # Fondo oscuro como tu estilo de Streamlit
            paper_bgcolor='#1c1f26',
            font=dict(color='#ddd'),
            height=600,
            width=600  # Ajustar tamaño para asegurar que se vea bien en pantallas grandes y pequeñas
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.header("Competencia Promedio en distintos aspectos de la Ingeniería en Computación")
        
        # Definir las categorías
        categorias_disponibles = {
            "Ingeniería de Software": ['Metodologías Ágiles', 'Arquitectura de Software', 'QA', 'Control de Versiones', 'Despliegue de Aplicaciones', 'Diseño de Software'],
            "Ingeniería de Datos": ['BD Relacionales', 'BD No Relacionales', 'Machine Learning', 'Procesos ETL', 'IA (LLM NLP RN)', 'Big Data', 'Análisis de Datos'],
            "Ingeniería de Sistemas (+ Cloud y Habilidades Profesionales)": ['Redes','Ciberseguridad','Virtualización', 'Windows', 'Linux','Cloud','Habilidades Profesionales']
        }

        # Crear un control radio en col2 para seleccionar la categoría
        categoria_seleccionada = st.radio(
            "Seleccione una categoría:", 
            list(categorias_disponibles.keys()), 
            horizontal=True
        )

    #with col4:
        # Obtener las preguntas basadas en la categoría seleccionada
        preguntas_seleccionadas = categorias_disponibles[categoria_seleccionada]

        # Filtrar el DataFrame para incluir las preguntas seleccionadas
        filtered_df = melted_df[melted_df['Pregunta'].isin(preguntas_seleccionadas)]
        mean_responses = filtered_df.groupby('Pregunta')['Respuesta'].mean()

        categorias = mean_responses.index.tolist()
        valores = mean_responses.values
        valores = np.append(valores, valores[0])
        num_vars = len(categorias)
        angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
        angulos += angulos[:1]

        # Crear un gráfico de radar con Plotly
        fig_radar = go.Figure()

        fig_radar.add_trace(go.Scatterpolar(
            r=valores,
            theta=categorias + [categorias[0]],  # Cerrar el círculo
            fill='toself',
            fillcolor='rgba(31, 119, 180, 0.3)',  # Color azul con transparencia
            line=dict(color='rgba(31, 119, 180, 1)'),  # Color de la línea azul
            name='Promedio'
        ))

        # Ajustar el layout del gráfico de radar
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 6],
                    tickvals=[0, 1, 2, 3, 4, 5],  # Asegurar que se muestren todas las divisiones
                    ticktext=['0', '1', '2', '3', '4', '5'],  # Mostrar los valores de 0 a 5
                    showline=False,  # Ocultar líneas radiales
                    gridcolor='#555',  # Color de las líneas del grid
                    tickfont=dict(size=14),  # Ajustar el tamaño de letra del eje radial
                ),
                angularaxis=dict(
                    showline=False,
                    gridcolor='#555',  # Color de las líneas del grid angular
                    tickfont=dict(size=14)  # Ajustar el tamaño de letra en los ejes angulares (categorías)
                ),
                bgcolor='#1c1f26',  # Fondo del radar para que coincida con el estilo oscuro
            ),
            title=dict(text=f"Promedio de Respuestas por {categoria_seleccionada}", font=dict(size=18)),  # Título ajustado
            plot_bgcolor='#1c1f26',
            paper_bgcolor='#1c1f26',
            font=dict(color='#ddd'),
            margin=dict(l=115, r=115, t=115, b=115),  # Aumentar márgenes laterales
            height=600,
            width=800  # Ajustar el tamaño como desees
        )

        # Mostrar el gráfico de radar en Streamlit
        st.plotly_chart(fig_radar, use_container_width=True)



    #Separador
    #st.markdown("<hr>", unsafe_allow_html=True)

    ########################## Títulos para cada columna ##########################
    col1, col2 = st.columns(2)
    ########################## Distribución de los gráficos ##########################
    #col3, col4 = st.columns(2)  # Crear dos columnas para alinear los gráficos

    with col1:
        st.header("Competencia Promedio en Lenguajes de Programación (+SQL) y Herramientas de Visualización de Datos")

    ########################## Lenguajes de Programación + SQL ##########################    
    #with col3:
        # Seleccionar las preguntas para el mapa de calor
        preguntas_seleccionadas_1 = ['Python (Software)', 'R', 'Java', 'JavaScript', 'TypeScript', 'Python (Datos)', 'Ruby Go C', 'SQL', 'PowerBI', 'Tableau']
        filtered_df_1 = melted_df[melted_df['Pregunta'].isin(preguntas_seleccionadas_1)]

        # Calcular el promedio de respuestas para cada lenguaje de programación
        mean_responses_1 = filtered_df_1.groupby('Pregunta')['Respuesta'].mean()

        # Crear una matriz pivot para el mapa de calor y ordenar de mayor a menor por el promedio
        heatmap_data = mean_responses_1.reset_index().sort_values(by='Respuesta', ascending=False)  # Ordenar por el valor promedio
        heatmap_data = heatmap_data.pivot_table(index='Pregunta', values='Respuesta')

        # Convertir la matriz a una lista de valores para el heatmap en Plotly
        z_data = heatmap_data.values
        y_labels = heatmap_data.index.tolist()  # Esto ahora está ordenado por los valores promedio

        # Eje X artificial para mostrar la competencia promedio
        x_labels = ['Promedio']

        # Crear el gráfico de heatmap con Plotly
        fig = go.Figure()

        # Agregar heatmap
        fig.add_trace(go.Heatmap(
            z=z_data,
            x=x_labels,  # Eje X artificial
            y=y_labels,  # Lenguajes de programación en el eje Y (ordenado por promedio)
            colorscale='balance',  # Escala de colores
            showscale=True,  # Mostrar la barra de colores
            hoverongaps=False,  # No mostrar espacios en blanco
            zmin=1.3,  # Ajuste de mínimo para el rango de colores
            zmax=5   # Ajuste de máximo para el rango de colores
        ))

        # Añadir anotaciones de texto dentro de las celdas del heatmap
        for i in range(len(y_labels)):
            fig.add_trace(go.Scatter(
                x=[x_labels[0]],  # Un solo punto en el eje X
                y=[y_labels[i]],  # Puntos en el eje Y para cada etiqueta
                mode='text',
                text=[f'{z_data[i][0]:.2f}'],  # Mostrar el valor formateado
                textfont=dict(color='black' if z_data[i][0] > 2.5 and z_data[i][0] < 4  else 'white'),  # Color del texto (dependiendo del fondo)
                textposition="middle center",
                showlegend=False  # Deshabilitar leyenda para este scatter
            ))

        # Ajustar el layout del gráfico
        fig.update_layout(
            xaxis_title="Competencia",  # Etiqueta para el eje X
            yaxis_title="Lenguajes y Herramientas",  # Etiqueta para el eje Y
            xaxis=dict(tickfont=dict(size=18)),
            yaxis=dict(tickfont=dict(size=18)),
            height=600,  # Ajustar el tamaño del gráfico
            width=800,
            plot_bgcolor='#1c1f26',
            paper_bgcolor='#1c1f26',
            font=dict(color='#ddd'),  # Asegurarse de que el texto sea visible
            showlegend=False  # Deshabilitar todas las leyendas
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.header("Promedio de Competencia por Área")
        st.write("""
        A continuación se muestra el promedio de competencia por área de la ingeniería en computación. Las áreas consideradas son Ingeniería de Software, Ingeniería de Datos y Sistemas. 

        Este análisis incluye todas las preguntas relacionadas con ofertas laborales de la encuesta. Además, se ha considerado que las competencias en **Habilidades Profesionales**, **SQL**, y **Herramientas Cloud** son transversales y aplican a las tres áreas mencionadas, ya que son altamente demandadas en el ámbito laboral en todas las disciplinas de la Ingeniería en Computación.
        """)
    
    #with col4:
        # Definir las áreas y sus preguntas asociadas
        areas = {
            "Ingeniería de Software": ['Python (Software)', 'Java', 'JavaScript', 'TypeScript', 'Ruby Go C', 'Arquitectura de Software','QA','Control de Versiones','Despliegue de Aplicaciones','Diseño de Software','Metodologías Ágiles','SQL','Habilidades Profesionales','Cloud','React','Vue','Angular','HTML y CSS','Spring Boot','Django','Rails','Nodejs (Frameworks)' ],
            "Ingeniería de Datos": ['Python (Datos)', 'R', 'SQL', 'PowerBI', 'Tableau','Machine Learning','Procesos ETL','IA (LLM NLP RN)','Big Data','Análisis de Datos','BD Relacionales','BD No Relacionales','Cloud','Habilidades Profesionales'],
            "Ingeniería en Sistemas": ['Cloud','Redes','Ciberseguridad','Habilidades Profesionales','Virtualización','Windows','Linux'] 
        }

         # Mostrar las tarjetas una debajo de la otra
        for area, preguntas in areas.items():
            # Filtrar el DataFrame por las preguntas del área
            filtered_df = melted_df[melted_df['Pregunta'].isin(preguntas)]
            
            # Calcular el promedio de las respuestas para el área
            promedio_area = filtered_df['Respuesta'].mean()

            # Mostrar tarjeta
            st.markdown(f"""
            <div class="card">
                <div class="card-title">{area}</div>
                <div class="card-text">Promedio de Competencia: {promedio_area:.2f}</div>
            </div>
            """, unsafe_allow_html=True)


    st.markdown("<hr>", unsafe_allow_html=True)
    ############################################################


with tab2:
    st.header("Visualización de Respuestas Encuesta: Sección Perfil de Egreso")
    st.write("En esta sección se presentan las visualizaciones de las respuestas de la encuesta sobre el perfil de egreso. Las competencias están categorizadas por Fundamentos de la Computación, Ingeniería de Datos, Ingeniería de Software y Sistemas, evaluando el nivel de preparación de los egresados en cada área. Recuerda que las respuestas están en una escala de 1 a 5, donde 1 significa 'Muy poco competente' y 5 representa 'Muy competente'.")    #Separador
    #st.markdown("<hr>", unsafe_allow_html=True)
    # Diccionario de preguntas completas por categoría
    areas_preguntas = {
        'Fundamentos de la Computación': ['Fundamentos de la Computación 1', 'Fundamentos de la Computación 2'],
        'Ingeniería de Datos': ['Ingeniería de Datos 1', 'Ingeniería de Datos 2'],
        'Ingeniería de Software': ['Ingeniería de Software 1', 'Ingeniería de Software 2', 'Ingeniería de Software 3'],
        'Sistemas': ['Sistemas']
    }

    # Diccionario de preguntas con el texto completo
    preguntas_completas = {
        'Fundamentos de la Computación 1': '¿Qué tan competente te sientes para analizar problemas computacionales, construir modelos y expresarlos en representaciones y lenguajes formales adecuados?',
        'Fundamentos de la Computación 2': '¿Qué tan competente te sientes para analizar, diseñar y/o adaptar algoritmos y estructuras de datos que cumplan con las garantías requeridas de correctitud y eficiencia?',
        'Ingeniería de Datos 1': '¿Qué tan competente te sientes para gestionar, extraer, obtener, generar, almacenar y recuperar información valiosa de datos diversos, complejos y masivos, utilizando modelos, lenguajes de consulta y técnicas de acceso a datos eficientes y seguras?',
        'Ingeniería de Datos 2': '¿Qué tan competente te sientes para extraer información relevante mediante el proceso de descubrimiento de conocimiento en datos, que incluye observar, modelar, procesar y analizar los datos?',
        'Ingeniería de Software 1': '¿Qué tan competente te sientes para concebir, diseñar y construir soluciones de software siguiendo un proceso sistemático y cuantificable, eligiendo el paradigma y las técnicas más adecuadas?',
        'Ingeniería de Software 2': '¿Qué tan competente te sientes para desarrollar software en una amplia variedad de plataformas y lenguajes de programación?',
        'Ingeniería de Software 3': '¿Qué tan competente te sientes para gestionar proyectos de diseño, desarrollo, implementación y evolución de soluciones de software, considerando tanto los procesos involucrados como el producto final, su calidad y la respuesta efectiva al problema que aborda?',
        'Sistemas': '¿Qué tan competente te sientes para implementar programas eficientes que optimicen el uso de recursos computacionales, explotando las características del sistema operativo y su interacción con la arquitectura de hardware y la red de datos, previniendo, diagnosticando y resolviendo errores de programación y/o problemas de desempeño?'
    }

    def generar_grafico_barras(pregunta):
        # Filtrar los datos para la pregunta correspondiente
        filtered_df = melted_df[melted_df['Pregunta'] == pregunta]

        # Agrupar las respuestas para la pregunta, asegurando que haya todas las opciones de 1 a 5
        grouped_df = filtered_df.groupby('Respuesta').size().reindex([1, 2, 3, 4, 5], fill_value=0).reset_index(name='Frecuencia')

        # Calcular el porcentaje para cada respuesta
        total_respuestas = grouped_df['Frecuencia'].sum()
        grouped_df['Porcentaje'] = (grouped_df['Frecuencia'] / total_respuestas * 100).round(2)  # Calcular el porcentaje con 2 decimales

        # Crear el texto que mostrará tanto la frecuencia como el porcentaje
        grouped_df['Texto'] = grouped_df.apply(lambda row: f"{int(row['Frecuencia'])} ({row['Porcentaje']}%)", axis=1)

        # Crear gráfico de barras con Plotly
        fig = go.Figure(go.Bar(
            x=grouped_df['Respuesta'],
            y=grouped_df['Frecuencia'],
            text=grouped_df['Texto'],  # Mostrar el texto con la frecuencia y el porcentaje
            textposition='auto'
        ))

        # Ajustar el layout del gráfico
        fig.update_layout(
            xaxis_title="Respuestas",
            yaxis_title="Frecuencia",
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4, 5],  # Asegurar que solo se muestren los valores 1-5
            ),
            plot_bgcolor='#1c1f26',
            paper_bgcolor='#1c1f26',
            font=dict(color='#ddd'),
            height=600,  # Ajustar el tamaño del gráfico
            width=600  # Ajustar el tamaño del gráfico
        )

        return fig

    # Mostrar las preguntas y gráficos por categoría
    for area, preguntas in areas_preguntas.items():
        st.markdown("<hr>", unsafe_allow_html=True)  # Separador horizontal
        st.subheader(f"{area}")  # Título de la categoría (e.g., Fundamentos de la Computación)
        
        # Iterar sobre las preguntas, creando 2 columnas siempre
        for i in range(0, len(preguntas), 2):  # Avanzar de 2 en 2
            cols = st.columns(2)  # Siempre crear 2 columnas

            # Primera columna
            with cols[0]:
                if i < len(preguntas):  # Verificar que hay una pregunta para esta columna
                    texto_pregunta = preguntas_completas.get(preguntas[i], preguntas[i])
                    st.write(f"**{texto_pregunta}**")  # Mostrar la pregunta en negrita
                    fig = generar_grafico_barras(preguntas[i])
                    st.plotly_chart(fig, use_container_width=True)

            # Segunda columna (si hay una segunda pregunta)
            with cols[1]:
                if i + 1 < len(preguntas):  # Verificar que hay una segunda pregunta
                    texto_pregunta = preguntas_completas.get(preguntas[i + 1], preguntas[i + 1])
                    st.write(f"**{texto_pregunta}**")  # Mostrar la pregunta en negrita
                    fig = generar_grafico_barras(preguntas[i + 1])
                    st.plotly_chart(fig, use_container_width=True)





    st.markdown("<hr>", unsafe_allow_html=True)

    ###############################################################
    st.header("Sugerencias para Mejorar la Formación Académica")
    st.write("A continuación se muestran algunas de las sugerencias que fueron mencionadas por los encuestados para mejorar la formación académica en la carrera de Ingeniería en Computación.")
    # Lista de sugerencias con títulos y texto
    sugerencias = [
    {"title": "Enfoque en Tecnologías y Lenguajes del Mundo Laboral", "text": "Talleres prácticos con lenguajes de programación y tecnologías relevantes en el mundo laboral, actualizando cursos con nuevas tecnologías y evitando centrarse solo en Python o C/C++."},
    {"title": "Malla Curricular con Especializaciones","text": "Materializar las distintas líneas de especialización en la malla curricular, garantizando que los estudiantes adquieran conocimientos especializados en alguna área clave de la computación, sin dejar a la suerte del estudiante la elección de ramos optativos para completar la malla."},
    {"title": "Conexión Teoría-Práctica a través de Proyectos Reales", "text": "Desafiar a los estudiantes a aplicar conocimientos en más proyectos reales durante la carrera, conectando la teoría con la práctica y permitiendo que desarrollen soluciones que los preparen directamente para su futuro profesional."}
    ]   
    # Mostrar sugerencias en tarjetas con títulos
    st.markdown('<div class="card-container">', unsafe_allow_html=True)
    # Crear columnas para las tarjetas
    num_cols = 3  # Número de columnas por fila

    # Dividir las sugerencias en grupos de 3 para cada fila de columnas
    for i in range(0, len(sugerencias), num_cols):
        cols = st.columns(num_cols)  # Crear las columnas

        # Iterar sobre las sugerencias y asignar a las columnas
        for j, sugerencia in enumerate(sugerencias[i:i+num_cols]):
            with cols[j]:
                st.markdown(f"""
                <div class="card">
                    <div class="card-title">{sugerencia['title']}</div>
                    <div class="card-text">{sugerencia['text']}</div>
                </div>
                """, unsafe_allow_html=True)