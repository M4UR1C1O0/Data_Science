# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacion del DataFrame
df_alumnos = pd.DataFrame(datos)

# Cálculo del promedio de las notas
Notas = ['Nota1', 'Nota2', 'Nota3']

# Creación de la nueva columna 'promedio' con el promedio de las notas
df_alumnos['Promedio'] = df_alumnos[Notas].mean(axis=1).round(1) # axis=1 es para calcular el promedio por fila

#print(df_alumnos)

# Sacamos los estudiantes con mayor y menor promedio
df_alumnos_max = df_alumnos.loc[df_alumnos['Promedio'].idxmax()]
df_alumnos_min = df_alumnos.loc[df_alumnos['Promedio'].idxmin()]

print('El alumno con mayor promedio es:','\n',df_alumnos_max)
print('El alumno con menor promedio es:','\n',df_alumnos_min)
print('Los promedios de los estudiantes son:','\n',df_alumnos)