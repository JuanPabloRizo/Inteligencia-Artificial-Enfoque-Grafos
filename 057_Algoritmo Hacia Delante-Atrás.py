import numpy as np

# Definición de los estados y las observaciones
estados = ['A', 'B']
observaciones = ['X', 'Y']

# Probabilidades iniciales de los estados (distribución inicial)
estado_inicial = np.array([0.6, 0.4])  # P(A) = 0.6, P(B) = 0.4

# Matriz de transición entre estados (P(X_t|X_t-1))
transicion = np.array([[0.7, 0.3],  # Desde A a A, B
                       [0.4, 0.6]]) # Desde B a A, B

# Matriz de observación (P(e_t|X_t))
observacion = np.array([[0.8, 0.2],  # P(X|A), P(Y|A)
                        [0.3, 0.7]]) # P(X|B), P(Y|B)

# Secuencia de observaciones
evidencia = ['X', 'Y', 'X']

# Función para el paso hacia adelante (Forward)
def paso_hacia_adelante(evidencia, estado_inicial, transicion, observacion):
    T = len(evidencia)  # Número de observaciones
    N = len(estado_inicial)  # Número de estados
    alpha = np.zeros((T, N))  # Inicialización de las probabilidades forward
    
    # Paso 1: Inicialización con las probabilidades iniciales y la primera observación
    for i in range(N):
        if evidencia[0] == 'X':
            alpha[0, i] = estado_inicial[i] * observacion[i, 0]
        else:
            alpha[0, i] = estado_inicial[i] * observacion[i, 1]
    
    # Paso 2: Recurrencia para los siguientes tiempos
    for t in range(1, T):
        for j in range(N):
            suma = 0
            for i in range(N):
                suma += alpha[t-1, i] * transicion[i, j]
            if evidencia[t] == 'X':
                alpha[t, j] = suma * observacion[j, 0]
            else:
                alpha[t, j] = suma * observacion[j, 1]

    return alpha

# Función para el paso hacia atrás (Backward)
def paso_hacia_atras(evidencia, transicion, observacion):
    T = len(evidencia)  # Número de observaciones
    N = len(transicion)  # Número de estados
    beta = np.zeros((T, N))  # Inicialización de las probabilidades backward
    
    # Paso 1: Inicialización (último tiempo)
    beta[T-1, :] = 1  # P(e_T+1 | X_T) = 1 para todos los estados
    
    # Paso 2: Recurrencia hacia atrás
    for t in range(T-2, -1, -1):
        for i in range(N):
            suma = 0
            for j in range(N):
                if evidencia[t+1] == 'X':
                    suma += transicion[i, j] * observacion[j, 0] * beta[t+1, j]
                else:
                    suma += transicion[i, j] * observacion[j, 1] * beta[t+1, j]
            beta[t, i] = suma

    return beta

# Función para combinar forward y backward
def hacia_adelante_atras(evidencia, estado_inicial, transicion, observacion):
    # Paso hacia adelante (Forward)
    alpha = paso_hacia_adelante(evidencia, estado_inicial, transicion, observacion)
    print(f"Alpha (Forward probabilities):\n{alpha}\n")
    
    # Paso hacia atrás (Backward)
    beta = paso_hacia_atras(evidencia, transicion, observacion)
    print(f"Beta (Backward probabilities):\n{beta}\n")
    
    # Calcular la probabilidad conjunta para cada estado en cada tiempo
    T = len(evidencia)
    probabilidad_posterior = np.zeros(alpha.shape)
    for t in range(T):
        probabilidad_posterior[t, :] = alpha[t, :] * beta[t, :]
        probabilidad_posterior[t, :] /= np.sum(probabilidad_posterior[t, :])  # Normalización
    
    return probabilidad_posterior

# Ejecutar el algoritmo hacia adelante-atrás
resultado = hacia_adelante_atras(evidencia, estado_inicial, transicion, observacion)
print(f"Probabilidades posteriores (Forward-Backward):\n{resultado}\n")
"""
Definición de estados y observaciones:
Los estados son A y B, y las observaciones son X y Y.
Paso hacia adelante (Forward):
Calcula las probabilidades de llegar a cada estado en cada momento dado 
todas las observaciones anteriores. La función paso_hacia_adelante 
implementa esta fase, utilizando las probabilidades de transición y observación.
Paso hacia atrás (Backward):
Calcula la probabilidad de observar el resto de la secuencia de observaciones 
dado el estado en un momento específico. Esto se hace en la función paso_hacia_atras.
Combinación hacia adelante y atrás:
Las probabilidades finales se calculan multiplicando los valores de alpha y
beta en cada paso de tiempo y luego normalizando para obtener probabilidades válidas.
Salida esperada:
El algoritmo te dará la probabilidad de estar en cada estado en cada paso de 
tiempo, dadas las observaciones.
"""