import random
import numpy as np
import matplotlib.pyplot as plt

def p(x):
    """Función de densidad de probabilidad: P(X) = 3x^2 para 0 <= x <= 1."""
    return np.where((0 <= x) & (x <= 1), 3 * x ** 2, 0)

def direct_sampling(num_samples):
    """Muestreo directo de la distribución P(X)."""
    samples = []
    for _ in range(num_samples):
        x = random.uniform(0, 1)  # Muestreo uniforme entre 0 y 1
        y = random.uniform(0, 1)  # Muestreo uniforme para la altura de la función
        if y < p(x):  # Aceptamos el punto si está bajo la curva
            samples.append(x)
    return samples

def rejection_sampling(num_samples, m):
    """Muestreo por rechazo de la distribución P(X)."""
    samples = []
    while len(samples) < num_samples:
        x = random.uniform(0, 1)  # Muestreo uniforme entre 0 y 1
        y = random.uniform(0, m)  # Muestreo uniforme para la altura
        if y < p(x):  # Aceptamos el punto si está bajo la curva
            samples.append(x)
    return samples

# Número de muestras a generar
num_samples = 1000
m = 3  # Valor máximo de la función de densidad de probabilidad

# Realizamos el muestreo directo
direct_samples = direct_sampling(num_samples)

# Realizamos el muestreo por rechazo
rejection_samples = rejection_sampling(num_samples, m)

# Visualizamos los resultados
x = np.linspace(0, 1, 100)
y = p(x)

plt.figure(figsize=(12, 6))

# Muestreo directo
plt.subplot(1, 2, 1)
plt.hist(direct_samples, bins=30, density=True, alpha=0.7, color='b', label='Muestreo Directo')
plt.plot(x, y, 'r', label='P(X) = 3x²')
plt.title('Muestreo Directo')
plt.xlabel('X')
plt.ylabel('Densidad')
plt.legend()

# Muestreo por rechazo
plt.subplot(1, 2, 2)
plt.hist(rejection_samples, bins=30, density=True, alpha=0.7, color='g', label='Muestreo por Rechazo')
plt.plot(x, y, 'r', label='P(X) = 3x²')
plt.title('Muestreo por Rechazo')
plt.xlabel('X')
plt.ylabel('Densidad')
plt.legend()

plt.tight_layout()
plt.show()
"""
Función de Densidad de Probabilidad:

Usé numpy.where para manejar la condición de que x esté entre 0 y 1. Esto permite que x sea un arreglo y devuelve el valor correcto en función de la condición.
Otras partes del código:

No hubo cambios necesarios en las funciones de muestreo directo o por rechazo, ya que ya estaban implementadas correctamente.
Resultado Esperado
Al ejecutar este código, deberías obtener dos gráficos que muestran la 
distribución de las muestras obtenidas por muestreo directo y muestreo por 
rechazo, ambas aproximándose a la función de densidad de probabilidad 
P(X)=3x 2
 
"""