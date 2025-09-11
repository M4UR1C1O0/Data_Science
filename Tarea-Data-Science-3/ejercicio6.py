from Limpieza import df 
import pandas as pd
import numpy as np

#6. Agrupamiento y análisis por grupo
#-------------------------------------
#- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1). 
#- ¿Qué tipo tiene el mayor promedio de velocidad? 
#- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?# 

#1. Calculo de promedio, mediana y desviacion estandar de ataque por tipo 1

#Agrupamos los Tipos 1 y a ataque y usamos agg para hacer las 3 operaciones de una
Tabla_resumen = df.groupby("Tipo 1")['Ataque'].agg(
    Promedio='mean',
    Mediana='median',
    Desviacion_estandar='std'
).round(1)

#2. ¿Qué tipo tiene el mayor promedio de velocidad?
Promedio_velocidad = df.groupby("Tipo 1")['Velocidad'].mean().round(1)
Mayor_promedio = df.groupby("Tipo 1")['Velocidad'].mean().idxmax()

#3. Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
Mayor_ps = df.loc[df.groupby("Tipo 1")['PS'].idxmax()][['Tipo 1', 'Nombre', 'PS']]
Menor_ps = df.loc[df.groupby("Tipo 1")['PS'].idxmin()][['Tipo 1', 'Nombre', 'PS']]

#Creamos otro DataFrame con los resultados obtenidos
Tabla_datos_ps = pd.DataFrame({
    'Pokemon con mayor PS': Mayor_ps.set_index('Tipo 1')['Nombre'],
    'Mayor PS': Mayor_ps.set_index('Tipo 1')['PS'],
    'Pokemon con menor PS': Menor_ps.set_index('Tipo 1')['Nombre'],
    'Menor PS': Menor_ps.set_index('Tipo 1')['PS']
})

print(Tabla_resumen[['Promedio', 'Mediana', 'Desviacion_estandar']])
print(
    f"\nEl tipo de Pokemon con mayor promedio de velocidad es: {Mayor_promedio} "
    f"con un promedio de {Promedio_velocidad[Mayor_promedio]} \n"
)
print(Tabla_datos_ps[['Pokemon con mayor PS', 'Mayor PS', 'Pokemon con menor PS', 'Menor PS']])
