from Limpieza import df

tipo_fuego = df[(df["Tipo 1"] == "Fuego") | (df["Tipo 2"] == "Fuego")]
fuego = tipo_fuego[["Nombre","Tipo 1","Ataque","Velocidad"]]
print(fuego)