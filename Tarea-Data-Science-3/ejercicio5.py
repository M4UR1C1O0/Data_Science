from Limpieza import df
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#5. Manipulación de datos
#------------------------
#- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
#- Ordena el DataFrame por "Poder Total" de mayor a menor.

#1. Creo una copia del dataframe original para no modificarlo
df_prueba = df.copy()

#2. Creo la nueva columna y le ingreso los valores del poder total
df_prueba["Poder Total"] = df_prueba["Ataque"] + df_prueba["Defensa"] + df_prueba["Velocidad"] + df_prueba["PS"]#agrego la nueva columna que esa la sumatoria

#3. Ordeno el dataframe utilizando un sort_values usando como parametro el poder total
df_prueba = df_prueba.sort_values(by="Poder Total", ascending=False) 

#4. Muestro el resultado del dataframe de prueba
print(df_prueba[["Nombre","Tipo 1", "Tipo 2", "Poder Total"]]) #para mejor visibilidad omiti los datos de ataque, defensa, velocidad y ps 

