# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacion del DataFrame
df_alumnos = pd.DataFrame(datos)
# Calcular el promedio individual de cada estudiante usando axis para utilizar filas
df_alumnos['Promedio'] = round(df_alumnos[['Nota1', 'Nota2', 'Nota3']].mean(axis=1),1)
# Ordenar por la columna promedio de forma descendente utlizando sort_values y ademas reset_index para reiniciar los indices
df_ordenado_descendente = df_alumnos.sort_values(by= 'Promedio',ascending=False).reset_index(drop=True)

print("Listado Ordenado de forma Descendente de los promedios del curso",df_ordenado_descendente)