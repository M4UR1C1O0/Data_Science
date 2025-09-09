# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacion del DataFrame
df_alumnos = pd.DataFrame(datos)
# Calcular el promedio individual de cada estudiante
df_alumnos['Promedio'] = round(df_alumnos[['Nota1', 'Nota2', 'Nota3']].mean(axis=1),1)

# Calcular el promedio total del curso, OJO redondeado a 1 decimal y es promedio 3.95 se aproxima a 4 
promedio_total_curso = round(df_alumnos['Promedio'].mean(), 1)
print("El promedio total del curso es:", promedio_total_curso,"%")