from Limpieza import df 
import pandas as pd 
#6. Agrupamiento y análisis por grupo
#-------------------------------------
#- Calcula el promedio, la mediana y la desviación estándar de ataque por cada tipo principal (Tipo 1).
#- ¿Qué tipo tiene el mayor promedio de velocidad?
#- Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?#

#Calculo de promedio, mediana y desviacion estandar de ataque por tipo 1
Promedio_ataque = df.groupby("Tipo 1")['Ataque'].mean().round(1)
#print("Promedio de ataque por tipo 1:\n", Promedio_ataque)

Mediana_ataque = df.groupby("Tipo 1")['Ataque'].median().round(1)
#print("\nMediana de ataque por tipo 1:\n", Mediana_ataque)

Desviacion_ataque = df.groupby("Tipo 1")['Ataque'].std().round(1)
#print("\nDesviación estándar de ataque por tipo 1:\n", Desviacion_ataque)

Tabla_resumen = pd.DataFrame({
    'Promedio ataque': Promedio_ataque,
    'Mediana ataque': Mediana_ataque,
    'Desviación estándar ataque': Desviacion_ataque
})
#print("\nTabla resumen de estadísticas de ataque por tipo 1:\n", Tabla_resumen)

# ¿Qué tipo tiene el mayor promedio de velocidad?
Promedio_velocidad = df.groupby("Tipo 1")['Velocidad'].mean().round(1)
#print("\nPromedio de velocidad por tipo 1:\n", Promedio_velocidad)
Mayor_promedio = df.groupby("Tipo 1")['Velocidad'].mean().idxmax()
print(
    f"El tipo de Pokemon con mayor promedio de velocidad es: {Mayor_promedio} "
    f"con un promedio de {Promedio_velocidad[Mayor_promedio]}"
)

# Para cada tipo principal, ¿cuál es el Pokémon con mayor y menor PS?
Mayor_ps = df.loc[df.groupby("Tipo 1")['PS'].idxmax()][['Tipo 1', 'Nombre', 'PS']]
Menor_ps = df.loc[df.groupby("Tipo 1")['PS'].idxmin()][['Tipo 1', 'Nombre', 'PS']]

Tabla_datos_ps = pd.DataFrame({
    'Pokemon con mayor PS': Mayor_ps.set_index('Tipo 1')['Nombre'],
    'Mayor PS': Mayor_ps.set_index('Tipo 1')['PS'],
    'Pokemon con menor PS': Menor_ps.set_index('Tipo 1')['Nombre'],
    'Menor PS': Menor_ps.set_index('Tipo 1')['PS']
})

print("\nTabla de Pokemon con mayor y menor PS por tipo 1:\n", Tabla_datos_ps)