from Limpieza import df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#7. Análisis exploratorio (EDA)
#------------------------------
#- ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
#- ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
#- ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
#- Identifica posibles outliers en los valores de ataque y PS usando boxplots.#

#1. ¿Existen tipos de Pokémon que tienden a tener mayor ataque o defensa? Justifica con estadísticas.
comparativa = df.groupby("Tipo 1")[["Ataque","Defensa"]].agg(["mean","median"]).round(1)#agg para usar las funciones mean y median a la vez

'''si hay tipos de pokemon que pueden tender a tener mayot ataque o defensa, como puede ser el caso de los pokemon de tipo lucha que promedio de ataque es de 102.9 pero una defensa mas baja
otro caso seria los pokemon tipo roca que tiene un mayor promedio en la defensa, siendo estos los dos tipos que mas resaltan en defensa y ataque, en cuanto a los demas tipos se puede decir que 
tienen un promedio mas balanceado entre ataque y defensa, igualmente tienes el tipo dragon con un buen promedio de ataque y el tipo tierra siendo otro buen tipo en defensa.'''

#2. ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.
correlacion = df["Ataque"].corr(df["Velocidad"])#utilizamos la herramienta de corr para buscar la correlacion entre columnas numericas 

'''debido al resultado arrojado es 0.2 se puede decir que no hay una relacion fuerte entre estos ya que esta demasiado cerca del 0 entonces con esto no se puede asegurar que haya una 
#correlacion entre ataque y velocidad.'''

#3. ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)
#Calculamos la desviacion estandar de PS por tipo y luego creamos un diagrama de dispersion
Desviacion_estandar_ps = df.groupby("Tipo 1")["PS"].std().round(1)
plt.figure(figsize=(10,5))
plt.scatter(df["Tipo 1"], df["PS"], color='green', alpha=0.5)
plt.title('Dispersión de PS por Tipo 1 de Pokemon de la Primera Generacion')
plt.xlabel('Tipo 1')
plt.ylabel('Puntos de Salud (PS)')
plt.xticks(rotation=45)
plt.tight_layout()#para que no se sobrepongan los textos
plt.savefig('Dispersión PS por Tipo 1.png')

#4. Identifica posibles outliers en los valores de ataque y PS usando boxplots.#
plt.figure(figsize=(10,5))
plt.boxplot([df["Ataque"], df["PS"]], tick_labels=["Ataque", "PS"])
plt.title('Boxplot de Ataque y PS de Pokemon de la Primera Generacion')
plt.ylabel('Valores')
plt.tight_layout()#para que no se sobrepongan los textos
plt.savefig('Boxplot Ataque y PS.png')

#Mostramos los resultados
print(f"Si existen tipos de Pokemon que tienden a tener mayor ataque o defensa: \n{comparativa}\n"
      f"El coeficiente de correlacion entre ataque y velocidad es: {correlacion.round(1)}"
      )
