import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV
df = pd.read_csv('Encuesta.csv')

# Columnas a excluir (Marca temporal y Pregunta Abierta)
columns_to_exclude = ['Marca temporal', 'Pregunta Abierta (Opcional):\n Basándote en tu experiencia, ¿Qué sugerencias tienes para mejorar la formación académica en el área de la computación?']

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
    
    # Mostrar las primeras filas del resultado
    st.write(melted_df)

    ########################## FRONTEND #############################################################################

    st.title("Desarrollo de Frontend")
    preguntas_seleccionadas = [
        'React', 'Vue', 'Angular', 'HTML y CSS'
    ]

    # Filtrar las preguntas seleccionadas
    filtered_df = melted_df[melted_df['Pregunta'].isin(preguntas_seleccionadas)]

    # Definir los valores de respuesta de 1 a 5
    respuesta_range = [1, 2, 3, 4, 5]

    # Agrupar los datos por Respuesta y Pregunta para contar las frecuencias, garantizando la presencia de todas las respuestas (1 a 5)
    grouped_df = filtered_df.groupby(['Respuesta', 'Pregunta']).size().unstack(fill_value=0).reindex(index=respuesta_range, fill_value=0)

    # Crear el gráfico multibarra con respuestas en el eje x y preguntas como leyenda
    fig, ax = plt.subplots(figsize=(10, 6))
    grouped_df.plot(kind='bar', stacked=False, ax=ax)

    # Añadir títulos y etiquetas
    ax.set_title('Desarrollo de Frontend', fontsize=16)
    ax.set_xlabel('Respuestas')
    ax.set_ylabel('Frecuencia')
    ax.set_xticks(range(len(grouped_df.index)))
    ax.set_xticklabels(grouped_df.index, rotation=0)

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)


    ########################## FRONTEND #############################################################################

     # Separar las secciones con una línea horizontal
    st.markdown("---")

    ########################## Distintas Áreas #######################################################################
    
    st.title("Distintas Áreas - Gráfico de Araña")
    
    # Definir las preguntas para las distintas áreas (puedes cambiar las preguntas)
    preguntas_seleccionadas = [
        'Metodologías Ágiles', 'QA', 'Arquitectura de Software', 'Control de Versiones', 'Despliegue de Aplicaciones', 'Diseño de Software'
    ]

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
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Dibujar un polígono y los puntos
    ax.fill(angulos, valores, color='#1f77b4', alpha=0.25)
    ax.plot(angulos, valores, color='#1f77b4', linewidth=2)

    # Añadir las etiquetas de las categorías en los ángulos correspondientes
    ax.set_xticks(angulos[:-1])  # No añadimos el último ángulo repetido a las etiquetas
    ax.set_xticklabels(categorias)

    # Rango de las etiquetas en el eje radial (0 a 5, ya que las respuestas están en ese rango)
    ax.set_ylim(0, 5)

    # Añadir título
    ax.set_title('Promedio de Respuestas por Distintas Áreas')

    # Mostrar el gráfico en Streamlit
    st.pyplot(fig)

    ########################## FIN Distintas Áreas #######################################################################
    # Separar las secciones con una línea horizontal
    st.markdown("---")










    ########################## Información Adicional #######################################################################
    # Crear "cards" usando markdown
    st.markdown("""
    ### 🚀 Tecnologías Más Solicitadas:
    - **Python**: 85%
    - **JavaScript**: 75%
    - **SQL**: 65%
    - **Docker**: 55%
    - **AWS**: 50%
    """)

    st.markdown("""
    ### 🔧 Tecnologías DevOps:
    - **Docker**: 55%
    - **Kubernetes**: 45%
    - **Jenkins**: 40%
    """)

    ########################## FIN Información Adicional #######################################################################


# Contenido para la segunda hoja
with tab2:
    st.header("Hoja 2")
    st.write("Aquí puedes poner contenido de la Hoja 2")
    
# Contenido para la tercera hoja
with tab3:
    st.header("Hoja 3")
    st.write("Aquí puedes poner contenido de la Hoja 3")

# Contenido para la cuarta hoja
with tab4:
    st.header("Hoja 4")
    st.write("Aquí puedes poner contenido de la Hoja 4")