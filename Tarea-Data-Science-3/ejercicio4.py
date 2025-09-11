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

tipos = ["Normal", "Fuego", "Agua", "Planta", "Electrico", "Hielo",
    "Lucha", "Veneno", "Tierra", "Volador", "Psiquico",
    "Bicho", "Roca", "Fantasma", "Dragon",]

datos = [df[df["Tipo 1"] == tipo]["PS"] for tipo in tipos]
#utilizamos .hist para histogramas, .scatter para dispersion, .boxplot para cajas con persentiles
plt.figure(figsize=(10,5))
#plt.subplot(1,2,1)#se me unian los 2 graficos esto hace que se genere uno por separado, 1 fila, 2 columnas, 1 grafico
#muestra cuanto pokemon tiene una cantidad de ataque en un rango
plt.hist(df["Ataque"], bins=15, color='blue', edgecolor='black')#hist de histograma bins es la cantidad de barras
plt.title('Distribución de Ataque de Pokemon de la Primera Generacion')#tutulo
plt.xlabel('Valor de Ataque')#x
plt.ylabel('Número de Pokemon')#y
plt.savefig('historigrama.png')#guarda la imagen ya que estoy usando un codespace y no se abre una ventana extra

plt.figure(figsize=(10,5))
#plt.subplot(1,2,2)
plt.scatter(df["Ataque"], df["Velocidad"], color='red', alpha=0.5)#scatter es dispercion solo cambia eso y los valores entrantes
plt.title('Relación entre Ataque y Velocidad de Pokemon de la Primera Generacion')#titulo
plt.xlabel('Valor de Ataque')
plt.ylabel('Valor de Velocidad')
plt.savefig('prueba.png')

#boxplot cajas tipo persentiles
plt.figure(figsize=(10,5))
plt.boxplot(datos, tick_labels = tipos)
plt.title('Distribucion de PS por Tipo 1 de Pokemon de la Primera Generacion')
plt.xlabel('Tipo 1')
plt.ylabel('Puntos de Salud')
plt.xticks(rotation=45)
plt.tight_layout()#para que no se sobrepongan los textos
plt.savefig('prueba2.png')
plt.show()



