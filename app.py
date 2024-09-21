import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configurar la página para usar el ancho completo
st.set_page_config(layout="wide")

# CSS personalizado para las tarjetas de métricas
st.markdown("""
<style>
.card {
    margin: 10px;
    padding: 15px;
    text-align: center;
    color: black;
    background-color: white;
    border-radius: 10px;
    box-shadow: 2px 2px 10px grey;
}
.metric-name {
    font-size: 16px;
    color: #008080;  # Adjusted to a teal color for visibility
    font-weight: bold;
}
.metric-value {
    font-size: 26px;
    color: black;
    margin-top: 5px;
    margin-bottom: 5px;
}
.metric-freq {
    font-size: 16px;
    color: grey;
}
</style>
""", unsafe_allow_html=True)

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
    st.header("Área de Software")
    st.write("A continuación se muestran las visualizaciones asociadas a las respuestas de la encuesta en el área de Software")
    st.title("Lenguajes de Programación más solicitados")

    
    # Datos de ejemplo para las métricas
    technologies = [
        {"name": "Python", "percentage": "85%", "frequency": "1200 times"},
        {"name": "JavaScript", "percentage": "75%", "frequency": "1100 times"},
        {"name": "SQL", "percentage": "65%", "frequency": "900 times"},
        {"name": "Docker", "percentage": "55%", "frequency": "800 times"},
        {"name": "AWS", "percentage": "50%", "frequency": "700 times"}
    ]

    # Crear métricas personalizadas en columnas
    cols = st.columns(len(technologies))
    
    for col, tech in zip(cols, technologies):
        col.markdown(f"""
        <div class="card">
            <div class="metric-name">{tech['name']}</div>
            <div class="metric-value">{tech['percentage']}</div>
            <div class="metric-freq">{tech['frequency']}</div>
        </div>
        """, unsafe_allow_html=True)

    ########################## FRONTEND #############################################################################

   
    preguntas_seleccionadas = ['React', 'Vue', 'Angular', 'HTML y CSS']

    # Filtrar las preguntas seleccionadas
    filtered_df = melted_df[melted_df['Pregunta'].isin(preguntas_seleccionadas)]

    # Definir los valores de respuesta de 1 a 5
    respuesta_range = [1, 2, 3, 4, 5]

    # Agrupar los datos por Respuesta y Pregunta para contar las frecuencias, garantizando la presencia de todas las respuestas (1 a 5)
    grouped_df = filtered_df.groupby(['Respuesta', 'Pregunta']).size().unstack(fill_value=0).reindex(index=respuesta_range, fill_value=0)

    # Crear el gráfico multibarra con respuestas en el eje x y preguntas como leyenda
    fig, ax = plt.subplots(figsize=(6, 4))
    grouped_df.plot(kind='bar', stacked=False, ax=ax)
    ax.set_title('Desarrollo de Frontend', fontsize=10)
    ax.set_xlabel('Respuestas', fontsize=8)
    ax.set_ylabel('Frecuencia', fontsize=8)
    ax.set_xticks(range(len(grouped_df.index)))
    ax.set_xticklabels(grouped_df.index, rotation=0)
    ax.legend(fontsize=7)

    # Organizar gráficos en dos columnas
    col1, col2 = st.columns(2)
    with col1:
        st.title("Desarrollo de Frontend")
        st.pyplot(fig)

    ########################## Distintas Áreas #######################################################################

    

    # Definir las preguntas para las distintas áreas
    preguntas_seleccionadas = ['Metodologías Ágiles', 'QA', 'Arquitectura de Software', 'Control de Versiones', 'Despliegue de Aplicaciones', 'Diseño de Software']

    # Filtrar las preguntas seleccionadas
    filtered_df = melted_df[melted_df['Pregunta'].isin(preguntas_seleccionadas)]

    # Calcular el promedio de las respuestas para cada pregunta
    mean_responses = filtered_df.groupby('Pregunta')['Respuesta'].mean()

    # Crear el gráfico de radar
    categorias = mean_responses.index.tolist()  # Lista de categorías
    valores = mean_responses.values

    # Añadir el primer valor al final para cerrar el gráfico
    valores = np.append(valores, valores[0])

    # Número de variables
    num_vars = len(categorias)

    # Ángulos para cada eje (una para cada categoría)
    angulos = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Añadir el primer ángulo para cerrar el gráfico
    angulos += angulos[:1]

    # Crear el gráfico de radar
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



    ########################## FIN DISTINAS ÁREAS #######################################################################



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