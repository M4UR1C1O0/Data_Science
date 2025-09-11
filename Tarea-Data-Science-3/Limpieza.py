import pandas as pd 
import numpy as np 
from unidecode import unidecode

#Definimos donde se ubica el archivo "pokemon_primera_gen.csv" para leer lo bien
patharchivo = "/workspaces/Data_Science/Tarea-Data-Science-3/pokemon_primera_gen.csv"

#Mostrar todos los datos en la terminal
pd.set_option("display.max_rows", None)   
pd.set_option("display.max_columns", None)  

#Lectura del archivo .csv
df = pd.read_csv(patharchivo)

#Definimos los tipos de pokemon y guardamos en una variable "tipos_gen1"
tipos_gen1 = ["Normal", "Fuego", "Agua", "Planta", "Eléctrico", "Hielo",
    "Lucha", "Veneno", "Tierra", "Volador", "Psíquico",
    "Bicho", "Roca", "Fantasma", "Dragón","No tiene"]

datos_numericos = ["Ataque", "Defensa", "Velocidad", "PS"]

#Rellena los vacios
df ["Tipo 2"] = df["Tipo 2"].fillna("No tiene")

#Eliminar Tipo 2 de pokemon de tipos que aun no existian 
df["Tipo 2"] = df["Tipo 2"].apply(lambda x: x if x in tipos_gen1 else "No tiene")

#Correccion de nombre de nidoran
df["Nombre"] = df["Nombre"].replace({"Nidoran♂": "NidoranM","Nidoran♀": "NidoranF"})

#Eliminar acentos o normalizar
df["Nombre"] = df["Nombre"].apply(unidecode)
df["Tipo 1"] = df["Tipo 1"].apply(unidecode)
df["Tipo 2"] = df["Tipo 2"].apply(unidecode)

#Comprobor tipos de datos aunque pandas lo hace solo
#df["Ataque"] = df["Ataque"].astype(int)
#df["Defensa"] = df["Defensa"].astype(int)
#df["Velocidad"] = df["Velocidad"].astype(int)
#df["PS"] = df["PS"].astype(int)
#print(df[["Ataque", "Defensa", "Velocidad", "PS"]].dtypes)
#print(df["Ataque","Defensa","Velocidad","PS"].dtypes())

for col in datos_numericos:
    if (df[col] < 0).any():
        print(f"La columna '{col}' tiene numeros negativos, corregir")
        error = True
    if not (df[col] % 1 == 0).all():
        print(f"La columna '{col}' tiene decimales,corregir")
        error = True
    if df[col].isna().any():
        print(f"La columna '{col}' tiene valores nulos, corregir")
        error = True

#print(df)

