# Importación de las librerias
import numpy as np
import pandas as pd

# Importación de los datos
datos = pd.read_csv('Datos_estudiantes.csv')

# Creacion del DataFrame
df_alumnos = pd.DataFrame(datos)

solo_notas = ['Nota1','Nota2','Nota3']

notas= df_alumnos[solo_notas].values

nota_baja_4 = np.any(notas < 4.0, axis=1)

porcentaje = round(np.mean(nota_baja_4)*100,1)

print("Porcentaje total de alumnos con al menos una nota bajo 4.0:",porcentaje,"%")