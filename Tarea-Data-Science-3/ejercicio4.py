import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from Limpieza import df

#utilizamos .hist para histogramas, .scatter para dispersion, .boxplot para cajas con persentiles

plt.subplot(1,2,1)#se me unian los 2 graficos esto hace que se genere uno por separado, 1 fila, 2 columnas, 1 grafico
#muestra cuanto pokemon tiene una cantidad de ataque en un rango
plt.hist(df["Ataque"], bins=15, color='blue', edgecolor='black')#hist de histograma bins es la cantidad de barras
plt.title('Distribución de Ataque de Pokémon de la Primera Generación')#tutulo
plt.xlabel('Valor de Ataque')#x
plt.ylabel('Número de Pokémon')#y
#plt.savefig('histograma_ataque.png')#guarda la imagen ya que estoy usando un codespace y no se abre una ventana extra
plt.show()

plt.subplot(1,2,2)
plt.scatter(df["Ataque"], df["Velocidad"], color='red', alpha=0.5)#scatter es dispercion solo cambia eso y los valores entrantes
plt.title('Relación entre Ataque y Velocidad de Pokémon de la Primera Generación')#titulo
plt.xlabel('Valor de Ataque')
plt.ylabel('Valor de Velocidad')
plt.savefig('prueba.png')
plt.show()

#boxplot cajas tipo persentiles
