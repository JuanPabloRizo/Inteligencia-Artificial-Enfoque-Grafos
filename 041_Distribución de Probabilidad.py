import numpy as np
import matplotlib.pyplot as plt

# Definir los posibles resultados de lanzar un dado
resultados = [1, 2, 3, 4, 5, 6]

# Probabilidades de cada resultado (lanzamiento justo)
probabilidades = [1/6] * 6

# Crear un gráfico de barras
plt.bar(resultados, probabilidades, color='blue', alpha=0.7)

# Agregar etiquetas y título
plt.xlabel('Resultado')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad - Lanzamiento de un Dado')

# Mostrar el gráfico
plt.show()
"""
Explicación:
Posibles resultados: Los números 1 a 6 son los posibles resultados de lanzar un dado.
Probabilidades: Como el dado es justo, la probabilidad de obtener cualquier número es 
1/6
Gráfico de barras: Muestra la probabilidad de cada resultado con barras del mismo tamaño.
"""