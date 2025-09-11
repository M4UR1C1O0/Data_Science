import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Limpieza import df

df_prueba = df.copy()#creo una copia por mientras

df_prueba["Poder Total"] = df_prueba["Ataque"] + df_prueba["Defensa"] + df_prueba["Velocidad"] + df_prueba["PS"]#agrego la nueva columna que esa la sumatoria

#print(df_prueba[["Nombre", "Poder Total"]])

#ordenar

df_prueba = df_prueba.sort_values(by="Poder Total", ascending=False)#ordeno mayor a menor    

print(df_prueba[["Nombre","Tipo 1", "Tipo 2", "Poder Total"]]) #no puse lo demas porque no alcanza xd

