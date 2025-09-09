# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacion del DataFrame
df_alumnos = pd.DataFrame(datos)

# Calcular la moda de las notas de los estudiantes
Notas = ['Nota1', 'Nota2', 'Nota3']

# Unimos todas las notas a una fila
Notas_totales = pd.concat([df_alumnos[nota] for nota in Notas])

# Sacamos la moda de donde tenemos todas las notas
df_alumnos = Notas_totales.mode()[0]

print('La moda de las notas de los estudiantes es:',df_alumnos)