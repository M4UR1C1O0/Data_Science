from Limpieza import df

#3. Estadística descriptiva básica
#---------------------------------
#- Calcula el promedio, la mediana y la moda del ataque de todos los Pokémon.
#- ¿Cuál es el Pokémon con mayor defensa? ¿Y el de menor velocidad?
#- ¿Cuántos Pokémon tienen dos tipos?
#- Calcula el rango y la desviación estándar de los PS (Puntos de Salud).


#1. Promedio, mediana y moda
promedio_ataque = round(df["Ataque"].mean(),1)#uso de mean para el promedio
mediana_ataque = df["Ataque"].median()#uso de median para la mediana
moda_ataque = df["Ataque"].mode()[0]#uso de mode para la moda y el 0 para que solo haya una

#2. Mayor def y menos vel
mayor_def = df["Defensa"].max()#uso de max para encontrar el valor mas grande

#prueba 
#mayor_def_pokemon = df.loc[df["Defensa"].idxmax()]["Nombre"] #encuentra el nombre del pokemon con mayor defensa
Mayor_def_pokemon = df.loc[df["Defensa"].idxmax(), "Nombre"]
Menor_vel_pokemon = df.loc[df["Velocidad"].idxmin(), "Nombre"]

menos_vel = df["Velocidad"].min()#uso de min para encontrar el valor mas pequeño

#3. Doble tipo
doble_tipo = df[df["Tipo 2"] != "No tiene"]#buscamos todos aquellos que no tenga en segundo tipo "No tiene"

#4. Desviacion y rango
rango = df["PS"].max() - df["PS"].min() #(ps maximo - ps minimo) o  (chansey - digglet)
desviacion = round(df["PS"].std(),1) #desviacion estandar std

#Muestro los resultados
print(f"Promedio ataque: {promedio_ataque}\nMediana ataque: {mediana_ataque}\nModa ataque: {moda_ataque}"
      f"\nMayor defensa: {Mayor_def_pokemon} con {mayor_def}\nMenor velocidad: {Menor_vel_pokemon} con {menos_vel}" #Cambios de Mayor_def_pokemon y Menor_vel_pokemon
      f"\nPokemones de doble tipo: {len(doble_tipo)}\nRango PS: {rango}\nDesviacion Estandar PS: {desviacion}")
