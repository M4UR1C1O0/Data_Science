# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacion del DataFrame
df_alumnos = pd.DataFrame(datos)

# Cuantos aprobaron con mayor a 4.0
Notas = ['Nota1', 'Nota2', 'Nota3']

# Revisamos si el estudiante aprobó con todas las notas mayores a 4.0
df_alumnos = df_alumnos[df_alumnos[Notas].gt(4.0).all(axis=1)]

print('El numero de alumnos que aprobaron todos sus ramos fueron:',len(df_alumnos),'\n',df_alumnos)