#Pasar un archivo excel a un archivo csv
#Sin streamlit
import pandas as pd

# Leer el archivo excel
df = pd.read_excel("Encuesta.xlsx")

# Guardar el archivo en formato csv
df.to_csv("Encuesta.csv", index=False)
