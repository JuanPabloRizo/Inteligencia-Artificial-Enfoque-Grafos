import numpy as np

# Definición de los posibles estados ocultos
states = ['Parado', 'Moviéndose']  # El vehículo puede estar 'Parado' o 'Moviéndose'

# Definición de las posibles observaciones que podemos hacer
observations = ['Nada', 'Sensor activo']  # El sensor puede detectar 'Nada' o estar 'Sensor activo'

# Probabilidades iniciales P(X0)
# Esto representa la creencia inicial sobre el estado del sistema antes de recibir cualquier observación
start_prob = {'Parado': 0.6, 'Moviéndose': 0.4}

# Matriz de transición de estados P(Xt | Xt-1)
# Define las probabilidades de cambiar de un estado a otro de un instante de tiempo al siguiente
# Por ejemplo, si el vehículo está 'Parado' ahora, tiene un 70% de probabilidad de continuar parado y un 30% de comenzar a moverse
transition_prob = {
    'Parado': {'Parado': 0.7, 'Moviéndose': 0.3},
    'Moviéndose': {'Parado': 0.4, 'Moviéndose': 0.6}
}

# Matriz de observación P(Yt | Xt)
# Define las probabilidades de ver una observación dada en función del estado oculto
# Por ejemplo, si el vehículo está 'Parado', hay un 80% de probabilidad de que el sensor no detecte nada ('Nada') y un 20% de que el sensor esté activo
observation_prob = {
    'Parado': {'Nada': 0.8, 'Sensor activo': 0.2},
    'Moviéndose': {'Nada': 0.3, 'Sensor activo': 0.7}
}

# Secuencia de observaciones que recibimos del mundo real
# Esta es la entrada del sensor en varios pasos de tiempo
observed_sequence = ['Nada', 'Nada', 'Sensor activo', 'Nada']

# Algoritmo de filtrado (Forward Algorithm) para calcular las probabilidades de los estados ocultos
# basado en las observaciones que hemos recibido hasta el momento
def forward(observed_sequence, states, start_prob, transition_prob, observation_prob):
    # Inicializar una lista que guardará las probabilidades hacia adelante en cada instante de tiempo
    fwd = [{}]

    # Paso 1: Inicialización
    # Usamos las probabilidades iniciales y la primera observación para calcular la probabilidad de cada estado en t=0
    for state in states:
        # La probabilidad de estar en 'state' al inicio es el producto de la probabilidad inicial y la probabilidad de la observación dada ese estado
        fwd[0][state] = start_prob[state] * observation_prob[state][observed_sequence[0]]
    
    # Paso 2: Recursión sobre el tiempo
    # Para cada instante de tiempo t, calculamos la probabilidad de estar en cada estado 'curr_state'
    # utilizando las probabilidades del estado anterior y las transiciones
    for t in range(1, len(observed_sequence)):
        # Añadimos una nueva entrada a la lista de probabilidades para el tiempo t
        fwd.append({})
        
        # Para cada estado actual 'curr_state', calculamos su probabilidad basada en los estados anteriores
        for curr_state in states:
            # La probabilidad de estar en 'curr_state' en el tiempo t es la suma de las probabilidades de haber estado en
            # cualquier estado anterior multiplicado por la probabilidad de transición hacia 'curr_state' y la probabilidad de observar lo que observamos
            fwd[t][curr_state] = sum(
                fwd[t-1][prev_state] * transition_prob[prev_state][curr_state] * observation_prob[curr_state][observed_sequence[t]]
                for prev_state in states  # Consideramos todas las transiciones posibles desde el estado anterior
            )
    
    # Paso opcional: Normalización
    # Al final del proceso, podemos normalizar las probabilidades para asegurarnos de que sumen 1 (una distribución de probabilidad válida)
    final_prob = sum(fwd[-1].values())  # Suma de todas las probabilidades al final del tiempo
    for state in states:
        fwd[-1][state] /= final_prob  # Normalizamos cada probabilidad dividiéndola por la suma total
    
    return fwd

# Ejecutar el algoritmo de filtrado sobre la secuencia de observaciones
fwd_probabilities = forward(observed_sequence, states, start_prob, transition_prob, observation_prob)

# Imprimir los resultados
print("Probabilidades filtradas en cada paso de tiempo:")
for t, probs in enumerate(fwd_probabilities):
    print(f"Tiempo {t}: {probs}")
"""
Estados y Observaciones:

Tenemos dos estados ocultos: 'Parado' y 'Moviéndose', y dos observaciones: 'Nada' y 'Sensor activo'.
Los estados ocultos representan el verdadero estado del vehículo, y las observaciones son lo que nuestros sensores detectan.
Probabilidades Iniciales:

La distribución inicial nos dice que el vehículo tiene un 60% de probabilidad de estar parado y un 40% de estar en movimiento al inicio.
Matriz de Transición:

Define las probabilidades de transición entre los estados ocultos. Por ejemplo, si el vehículo está parado en un momento dado, hay un 70% de probabilidad de que permanezca parado y un 30% de probabilidad de que empiece a moverse.
Matriz de Observación:

Define la probabilidad de observar 'Nada' o 'Sensor activo' dado el estado oculto. Por ejemplo, si el vehículo está parado, hay un 80% de probabilidad de que no detectemos nada (sensor inactivo) y un 20% de que el sensor esté activo.
Algoritmo de Filtrado:

Usamos el algoritmo hacia adelante (Forward Algorithm) para actualizar nuestras creencias sobre el estado del vehículo en función de las observaciones a lo largo del tiempo.
Este algoritmo recursivo comienza con las probabilidades iniciales y avanza en el tiempo actualizando las creencias en función de las observaciones.
Salida:

El programa imprime las probabilidades filtradas de los estados ocultos para cada instante de tiempo, basándose en las observaciones dadas.
Resultado
Este código calculará las probabilidades de que el vehículo esté parado o 
en movimiento en cada momento, dado un conjunto de observaciones. De esta 
manera, podemos hacer inferencias sobre los estados ocultos (posición del 
vehículo) a partir de las observaciones.
"""