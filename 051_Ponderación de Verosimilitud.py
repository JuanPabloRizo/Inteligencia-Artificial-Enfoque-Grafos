import numpy as np
import matplotlib.pyplot as plt

# Definir la función de densidad de la distribución objetivo P(x)
def P(x):
    """Densidad de probabilidad de una normal con media 0 y desviación estándar 1."""
    return (1 / (2 * np.pi)**0.5) * np.exp(-0.5 * x**2)

# Definir la función de densidad de la distribución de muestreo Q(x)
def Q(x):
    """Densidad de probabilidad de una uniforme entre -3 y 3."""
    return 0.1666666667 if -3 <= x <= 3 else 0  # 1/6 para uniforme entre -3 y 3

def likelihood_weighted_sampling(num_samples):
    """Muestreo con ponderación de verosimilitud."""
    samples = []
    weights = []
    
    # Muestreo desde Q
    for _ in range(num_samples):
        x = np.random.uniform(-3, 3)  # Muestreo uniforme entre -3 y 3
        weight = P(x) / Q(x)  # Ponderación
        samples.append(x)
        weights.append(weight)

    return samples, weights

# Número de muestras a generar
num_samples = 1000

# Realizamos el muestreo con ponderación de verosimilitud
samples, weights = likelihood_weighted_sampling(num_samples)

# Visualizamos los resultados
x = np.linspace(-4, 4, 100)
y = P(x)

plt.figure(figsize=(12, 6))
plt.hist(samples, bins=30, density=True, alpha=0.7, color='b', label='Muestras con Ponderación')
plt.plot(x, y, 'r', label='P(X) - Distribución Normal')
plt.title('Muestreo con Ponderación de Verosimilitud')
plt.xlabel('X')
plt.ylabel('Densidad')
plt.legend()
plt.show()
"""
Funciones de Densidad:

P(x): Función de densidad de la distribución normal estándar.
Q(x): Función de densidad de la distribución uniforme entre -3 y 3. Esta función devuelve 
1
6
para el rango deseado, que es la densidad de la distribución uniforme.
Muestreo con Ponderación:

La función likelihood_weighted_sampling realiza el muestreo desde la distribución 
Q (uniforme).
Para cada muestra, calcula el peso w usando la fórmula 
w= Q(x)/P(x)
Almacena las muestras y sus respectivos pesos en listas.
Visualización:
Se generan histogramas que muestran cómo las muestras obtenidas mediante ponderación se distribuyen en relación con la 
función de densidad de la distribución objetivo 
P(X).
Resultado Esperado
Cuando ejecutes este código, deberías obtener un gráfico que muestra la 
distribución de las muestras ponderadas superpuestas con la densidad de la
distribución normal. Esto demostrará cómo la ponderación de verosimilitud 
ajusta las muestras para que se alineen más estrechamente con la 
distribución objetivo.
"""