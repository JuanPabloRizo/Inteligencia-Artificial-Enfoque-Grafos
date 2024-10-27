import numpy as np

# Definir los estados ocultos y las observaciones
estados_ocultos = ['Soleado', 'Lluvioso']
observaciones = ['Gafas de sol', 'Paraguas']

# Probabilidades iniciales (distribución inicial de estados ocultos)
prob_inicial = np.array([0.6, 0.4])  # P(Soleado) = 0.6, P(Lluvioso) = 0.4

# Matriz de transición de estados (P(Estado_t|Estado_t-1))
transiciones = np.array([[0.7, 0.3],  # Soleado -> Soleado, Soleado -> Lluvioso
                         [0.4, 0.6]]) # Lluvioso -> Soleado, Lluvioso -> Lluvioso

# Matriz de emisión de observaciones (P(Observación|Estado))
emisiones = np.array([[0.8, 0.2],  # Soleado -> Gafas de sol, Soleado -> Paraguas
                      [0.4, 0.6]]) # Lluvioso -> Gafas de sol, Lluvioso -> Paraguas

# Secuencia de observaciones (lo que ve el meteorólogo)
evidencia = ['Gafas de sol', 'Paraguas', 'Gafas de sol']

# Función para calcular las probabilidades forward usando el Algoritmo Forward
def algoritmo_forward(evidencia, prob_inicial, transiciones, emisiones):
    T = len(evidencia)  # Número de observaciones
    N = len(prob_inicial)  # Número de estados
    alpha = np.zeros((T, N))  # Matriz para almacenar las probabilidades forward

    # Paso 1: Inicialización (probabilidades iniciales)
    for i in range(N):
        if evidencia[0] == 'Gafas de sol':
            alpha[0, i] = prob_inicial[i] * emisiones[i, 0]
        else:
            alpha[0, i] = prob_inicial[i] * emisiones[i, 1]

    # Paso 2: Recursión (para cada observación posterior)
    for t in range(1, T):
        for j in range(N):
            suma = 0
            for i in range(N):
                suma += alpha[t-1, i] * transiciones[i, j]
            if evidencia[t] == 'Gafas de sol':
                alpha[t, j] = suma * emisiones[j, 0]
            else:
                alpha[t, j] = suma * emisiones[j, 1]

    return alpha

# Ejecutar el algoritmo forward
probabilidades_forward = algoritmo_forward(evidencia, prob_inicial, transiciones, emisiones)

# Mostrar los resultados
print("Probabilidades forward (delante en el tiempo):\n", probabilidades_forward)

# Calcular la probabilidad de la secuencia de observaciones completa
prob_total_observaciones = np.sum(probabilidades_forward[-1])
print("\nProbabilidad total de la secuencia de observaciones:", prob_total_observaciones)

"""
Inicialización:

Se define el conjunto de estados ocultos (Soleado, Lluvioso) y las posibles observaciones (Gafas de sol, Paraguas).
Se establece una distribución de probabilidad inicial sobre los estados.
Se configuran las matrices de transición de estados y de emisiones, que indican las probabilidades condicionales.
Algoritmo Forward:

Este algoritmo computa la probabilidad de observar la secuencia de evidencia dada una secuencia de estados ocultos.
Inicialmente se calcula la probabilidad de comenzar en un estado dado y ver la primera observación.
Luego se itera sobre las observaciones restantes, calculando para cada estado la probabilidad de estar en ese estado 
dado las observaciones pasadas.
Salida esperada:

El algoritmo devuelve las probabilidades "forward", que indican la probabilidad de estar en un estado dado en cada 
paso de tiempo, dado todo lo que se ha observado hasta ese punto.
También calcula la probabilidad total de observar la secuencia de evidencia.
"""