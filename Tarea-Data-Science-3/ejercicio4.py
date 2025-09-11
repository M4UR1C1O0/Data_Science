from Limpieza import df
#4. Visualización de datos
#-------------------------
#- Haz un histograma de los valores de ataque.
#- Realiza un gráfico de dispersión entre ataque y velocidad.
#- Haz un boxplot de los PS por tipo principal (Tipo 1).
#- Grafica la distribución de la defensa usando un diagrama de violín.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Limpieza import df
import seaborn as sns
tipos = ["Normal", "Fuego", "Agua", "Planta", "Electrico", "Hielo",
    "Lucha", "Veneno", "Tierra", "Volador", "Psiquico",
    "Bicho", "Roca", "Fantasma", "Dragon",]
datos = [df[df["Tipo 1"] == tipo]["PS"] for tipo in tipos]

#utilizamos .hist para histogramas, .scatter para dispersion, .boxplot para cajas con persentiles y .violinplot para diagrama de violin
#
plt.figure(figsize=(10,5))
plt.hist(df["Ataque"], bins=15, color='blue', edgecolor='black')#hist de histograma bins es la cantidad de barras #muestra cuanto pokemon tiene una cantidad de ataque en un rango
plt.title('Distribución de Ataque de Pokemon de la Primera Generacion')#tutulo
plt.xlabel('Ataque')#x
plt.ylabel('Numero de Pokemon')#y
plt.savefig('Diagrama Histograma.png')#guarda la imagen ya que estoy usando un codespace y no se abre una ventana extra

#grafico de dispersion
plt.figure(figsize=(10,5))
plt.scatter(df["Ataque"], df["Velocidad"], color='red', alpha=0.5)#scatter es dispercion solo cambia eso y los valores entrantes
plt.title('Relación entre Ataque y Velocidad de Pokemon de la Primera Generacion')#titulo
plt.xlabel('Ataque')
plt.ylabel('Velocidad')
plt.savefig('Diagrama de dispersion.png')

#boxplot cajas tipo persentiles
plt.figure(figsize=(10,5))
plt.boxplot(datos, tick_labels = tipos)
plt.title('Distribucion de PS por Tipo 1 de Pokemon de la Primera Generacion')
plt.xlabel('Tipo 1')
plt.ylabel('Puntos de Salud')
plt.xticks(rotation=45)
plt.tight_layout()#para que no se sobrepongan los textos
plt.savefig('Diagrama Boxplot.png')
plt.show()

#diagrama violin 
plt.figure(figsize=(10,5))
sns.violinplot(x="Tipo 1", y="Defensa", data=df)
plt.title('Distribución de Defensa por Tipo 1 de Pokemon de la Primera Generacion')#usamos la libreria seaborn ya que es mas simple crearlo
plt.xlabel('Tipo 1')
plt.ylabel('Defensa')
plt.tight_layout()
plt.savefig('Diagrama Violin.png')
plt.show()



