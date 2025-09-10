from Limpieza import df

#Promedios
promedio_ataque = round (df["Ataque"].mean(),1)
mediana_ataque = df["Ataque"].median()
moda_ataque = df["Ataque"].mode()[0]
print("Promedios: ",promedio_ataque, mediana_ataque, moda_ataque )

#Mayor def y menos vel
mayor_def = df["Defensa"].max()
menos_vel = df["Velocidad"].min()
print("Mayor defensa: ", mayor_def)
print("Menor velocidad: ", menos_vel)

#Doble tipo
doble_tipo = df[df["Tipo 2"] != "No tiene"]
print("Pokemones de doble tipo: ", len(doble_tipo))

#devisacion y rango
