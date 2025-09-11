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


#2. ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.

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