import numpy as np
import matplotlib.pyplot as plt

def P(x):
    """Función de densidad de probabilidad de la distribución objetivo (normal estándar)."""
    return (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

def metropolis_hastings(num_samples, proposal_std=1.0):
    """
    Algoritmo de Metropolis-Hastings para muestrear de una distribución normal estándar.
    
    num_samples: Número de muestras a generar.
    proposal_std: Desviación estándar de la distribución propuesta para los saltos.
    """
    samples = []
    current_sample = 0  # Empezamos en el estado 0 (punto de partida)
    
    for _ in range(num_samples):
        # Proponer un nuevo estado
        proposed_sample = np.random.normal(current_sample, proposal_std)
        
        # Calcular la probabilidad de aceptación
        acceptance_ratio = P(proposed_sample) / P(current_sample)
        
        # Aceptar o rechazar la muestra propuesta
        if np.random.rand() < acceptance_ratio:
            current_sample = proposed_sample
        
        samples.append(current_sample)
    
    return samples

# Parámetros
num_samples = 10000  # Número de muestras
proposal_std = 1.0   # Desviación estándar de la propuesta

# Generar muestras usando el algoritmo de Metropolis-Hastings
samples = metropolis_hastings(num_samples, proposal_std)

# Visualización de los resultados
x = np.linspace(-4, 4, 1000)
y = P(x)

plt.figure(figsize=(10, 6))
plt.hist(samples, bins=50, density=True, alpha=0.6, color='b', label='Muestras MCMC')
plt.plot(x, y, 'r', label='P(X) - Distribución Normal')
plt.title('Muestreo con Metropolis-Hastings')
plt.xlabel('X')
plt.ylabel('Densidad')
plt.legend()
plt.show()
"""
Función de Densidad P(x):

Definimos la función de densidad de la distribución normal estándar. Esta es la distribución objetivo de la que queremos muestrear.
Algoritmo Metropolis-Hastings:

La función metropolis_hastings toma el número de muestras a generar (num_samples) y la desviación estándar de la distribución propuesta (proposal_std).
Para cada muestra:
Se propone un nuevo estado basado en la distribución normal centrada en el estado actual.
Se calcula la probabilidad de aceptación, que es el cociente de la función de densidad del nuevo estado y el estado actual.
Si se acepta, el estado actual cambia al nuevo estado; si no, el estado se mantiene igual.
Finalmente, devuelve una lista de las muestras generadas.
Visualización:

Creamos un histograma de las muestras obtenidas por el algoritmo y lo superponemos con la función de densidad de la distribución normal.
Resultado Esperado
El gráfico resultante muestra el histograma de las muestras generadas por el algoritmo Metropolis-Hastings superpuesto con la curva de la distribución normal estándar. 
El histograma debería aproximarse bien a la función de densidad 
P(X) conforme aumenta el número de muestras.
"""