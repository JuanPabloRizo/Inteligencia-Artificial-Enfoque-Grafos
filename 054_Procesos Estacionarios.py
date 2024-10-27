import numpy as np
import matplotlib.pyplot as plt

# Definir el número de puntos en el tiempo
n = 100

# Media y varianza constantes para el proceso estacionario
media = 10
varianza = 5

# Generar una serie de tiempo estacionaria
# Esto es básicamente una serie de números aleatorios con media constante y varianza constante
np.random.seed(42)  # Para obtener resultados reproducibles
serie_temporal = np.random.normal(media, np.sqrt(varianza), n)

# Graficar la serie temporal
plt.plot(serie_temporal)
plt.title("Serie Temporal Estacionaria (Media = 10, Varianza = 5)")
plt.xlabel("Tiempo")
plt.ylabel("Valor")
plt.grid(True)
plt.show()

# Calcular la media y varianza
media_estimada = np.mean(serie_temporal)
varianza_estimada = np.var(serie_temporal)

print(f"Media estimada: {media_estimada}")
print(f"Varianza estimada: {varianza_estimada}")

"""
Generación de la serie temporal:

Usamos np.random.normal(media, np.sqrt(varianza), n) para generar una 
serie de números aleatorios distribuidos normalmente (gaussianos) con una 
media constante (10) y una varianza constante (5).
Graficado:

La serie generada se grafica para mostrar cómo varía con el tiempo. En este 
caso, debería mostrar fluctuaciones alrededor de la media 10.
Cálculo de la media y varianza:

Al final, se calculan y se imprimen la media y la varianza estimadas de la 
serie para verificar que se mantienen constantes.
Salida Esperada:
Un gráfico donde los valores fluctúan alrededor de la media (10),
con variaciones dentro de los límites dictados por la varianza (5).
Una media estimada cercana a 10 y una varianza estimada cercana a 5.
"""