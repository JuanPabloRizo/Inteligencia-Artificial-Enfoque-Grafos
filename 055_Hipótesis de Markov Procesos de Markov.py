import numpy as np

# Definir la matriz de transición
# Las filas representan el estado actual y las columnas el estado futuro
P = np.array([[0.1, 0.6, 0.3],  # Probabilidades desde el estado A
              [0.4, 0.4, 0.2],  # Probabilidades desde el estado B
              [0.3, 0.3, 0.4]]) # Probabilidades desde el estado C

# Definir el espacio de estados
estados = ['A', 'B', 'C']

# Definir el estado inicial
estado_actual = 0  # Comenzamos en el estado 'A'

# Número de pasos (iteraciones)
num_pasos = 10

# Historial de estados
historial = [estados[estado_actual]]

# Simulación de la Cadena de Markov
for _ in range(num_pasos):
    estado_futuro = np.random.choice([0, 1, 2], p=P[estado_actual])
    historial.append(estados[estado_futuro])
    estado_actual = estado_futuro

# Mostrar el historial de estados visitados
print("Historial de estados visitados:", historial)

"""
Matriz de transición:
La matriz P es una matriz 3×3 que describe las probabilidades de transición 
entre tres estados. Cada fila corresponde a un estado actual, y las columnas 
representan el estado futuro al que se podría transitar.
Por ejemplo, desde el estado  A, hay un 10% de probabilidad de quedarse en 
A, un 60% de probabilidad de ir al estado B, y un 30% de ir al estado C.
Espacio de estados:
Los tres estados posibles son A, B, y C, representados por la lista estados.
Estado inicial:
Iniciamos el proceso en el estado 
A, lo que corresponde al índice 0 en la lista estados.
Simulación:
En cada paso del bucle for, elegimos el estado futuro basado en la fila de 
la matriz de transición que corresponde al estado actual. Utilizamos np.random.choice 
para seleccionar el próximo estado de acuerdo con las probabilidades definidas en P.
Historial:
Guardamos el historial de los estados visitados en la lista historial y lo imprimimos al final.
"""