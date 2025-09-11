from Limpieza import df

#2. Filtrado y selección
#-----------------------
#- Filtra todos los Pokémon de tipo "Fuego".
#- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.

#1. Creo un nuevo DataFrame con los pokemones de tipo fuego
tipo_fuego = df[(df["Tipo 1"] == "Fuego") | (df["Tipo 2"] == "Fuego")]

#2. Selecciono sola las columnas que quiero mostrar
fuego = tipo_fuego[["Nombre","Tipo 1","Ataque","Velocidad"]]

#Muestro el resultado
print(fuego)