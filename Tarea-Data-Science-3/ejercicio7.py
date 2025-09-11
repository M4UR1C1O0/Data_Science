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
tipos = ["Normal", "Fuego", "Agua", "Planta", "Electrico", "Hielo",
    "Lucha", "Veneno", "Tierra", "Volador", "Psiquico",
    "Bicho", "Roca", "Fantasma", "Dragon",]
Promedio_ataque_tipo = df.groupby("Tipo 1")["Ataque"].mean().reindex(tipos)

#2. ¿Hay correlación entre ataque y velocidad? Calcula el coeficiente de correlación.

#3. ¿Qué tan dispersos están los PS dentro de cada tipo? (compara la desviación estándar de PS por tipo)

#4. Identifica posibles outliers en los valores de ataque y PS usando boxplots.#