from Limpieza import df
#2. Filtrado y selección
#-----------------------
#- Filtra todos los Pokémon de tipo "Fuego".
#- Selecciona solo las columnas Nombre, Tipo 1, Ataque y Velocidad.

#creo un nuevo dataframe con los pokemones de tipo fuego
tipo_fuego = df[(df["Tipo 1"] == "Fuego") | (df["Tipo 2"] == "Fuego")]
#selecciono sola las columnas que quiero mostrar
fuego = tipo_fuego[["Nombre","Tipo 1","Ataque","Velocidad"]]
#muestro el resultado
print(fuego)