from Limpieza import df 
#5. Manipulación de datos
#------------------------
#- Crea una nueva columna llamada "Poder Total" que sea la suma de ataque, defensa, velocidad y PS.
#- Ordena el DataFrame por "Poder Total" de mayor a menor.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Limpieza import df
#creo una copia del dataframe original para no modificarlo
df_prueba = df.copy()
#creo la nueva columna y le ingreso los valores del poder total
df_prueba["Poder Total"] = df_prueba["Ataque"] + df_prueba["Defensa"] + df_prueba["Velocidad"] + df_prueba["PS"]#agrego la nueva columna que esa la sumatoria
#ordeno el dataframe utilizando un sort_values usando como parametro el poder total
df_prueba = df_prueba.sort_values(by="Poder Total", ascending=False) 
#muestro el resultado del dataframe de prueba
print(df_prueba[["Nombre","Tipo 1", "Tipo 2", "Poder Total"]]) #para mejor visibilidad omiti los datos de ataque, defensa, velocidad y ps 

