import numpy as np

# Definir los estados ocultos y las observaciones
estados = ['A', 'B']
observaciones = ['X', 'Y']

# Probabilidades iniciales de los estados
estado_inicial = np.array([0.6, 0.4])  # P(A) = 0.6, P(B) = 0.4

# Matriz de transición entre estados (P(s'|s))
transicion = np.array([[0.7, 0.3],  # Probabilidades desde A
                       [0.4, 0.6]]) # Probabilidades desde B

# Matriz de observación (P(o|s))
observacion = np.array([[0.8, 0.2],  # Probabilidad de observar X dado A
                        [0.3, 0.7]]) # Probabilidad de observar X dado B

# Observaciones reales en el tiempo
evidencia = ['X', 'Y', 'X']

# Paso de filtrado para cada observación
def filtrado(evidencia, estado_inicial, transicion, observacion):
    # Vector de creencias iniciales
    belief = estado_inicial

    # Iterar sobre las observaciones
    for obs in evidencia:
        # Paso de predicción: P(X_t) = sum(P(X_t|X_t-1) * P(X_t-1))
        belief = np.dot(belief, transicion)

        # Paso de corrección: Actualizar con la observación P(X_t|e_t)
        if obs == 'X':
            belief = belief * observacion[:, 0]  # Si la observación es 'X'
        else:
            belief = belief * observacion[:, 1]  # Si la observación es 'Y'

        # Normalizar la probabilidad para que sume 1
        belief = belief / np.sum(belief)
        print(f"Después de observar {obs}, creencias actualizadas: {belief}")

    return belief

# Ejecutar el filtrado
filtrado(evidencia, estado_inicial, transicion, observacion)

"""
Definición de los estados:
Hay dos posibles estados ocultos A y B, y dos posibles observaciones X y Y.
Estado inicial:
La creencia inicial (estado inicial) se define con probabilidades 
P(A)=0.6 y P(B)=0.4.
Matriz de transición:
La matriz de transición especifica cómo las probabilidades cambian de un estado a otro en cada paso de tiempo.
Matriz de observación:
La matriz de observación relaciona los estados con las probabilidades de realizar una observación 
X o Y.
Filtrado:
En cada iteración, primero hacemos un paso de predicción utilizando la matriz de 
transición. Luego, ajustamos nuestra predicción con la observación actual en el paso de corrección.
Normalizamos las creencias para que representen una distribución válida de probabilidad.
Salida esperada:
El proceso de filtrado actualizará las creencias del sistema sobre cuál es el estado actual 
después de cada observación:
"""