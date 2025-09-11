from Limpieza import df
#3. Estadística descriptiva básica
#---------------------------------
#- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
#- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
#- ¿Cuántos Pokémon tienen dos tipos?
#- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).


#Promedio, mediana y moda
promedio_ataque = round (df["Ataque"].mean(),1)#uso de mean para el promedio
mediana_ataque = df["Ataque"].median()#uso de median para la mediana
moda_ataque = df["Ataque"].mode()[0]#uso de mode para la moda y el 0 para que solo haya una
print("Promedios: ",promedio_ataque, "Mediana:",mediana_ataque,"Moda:",moda_ataque )

#Mayor def y menos vel
mayor_def = df["Defensa"].max()#uso de max para encontrar el valor mas grande
menos_vel = df["Velocidad"].min()#uso de min para encontrar el valor mas pequeño
print("Mayor defensa: ", mayor_def)
print("Menor velocidad: ", menos_vel)

#Doble tipo
doble_tipo = df[df["Tipo 2"] != "No tiene"]#buscamos todos aquellos que no tenga en segundo tipo "No tiene"
print("Pokemones de doble tipo: ", len(doble_tipo))

#desviacion y rango
rango = df["PS"].max() - df["PS"].min() #(ps maximo - ps minimo) o  (chansey - digglet)
desviacion = round(df["PS"].std(),1) #desviacion estandar std

print("Rango:", rango,"\nDesviacion Estandar:", desviacion)
