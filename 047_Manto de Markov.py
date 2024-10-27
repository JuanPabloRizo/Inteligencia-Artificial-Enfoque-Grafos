import random

# Definimos los estados ocultos y las observaciones
# Estados ocultos representan el clima
states = ['Soleado', 'Nublado', 'Lluvioso']
# Observaciones representan las acciones de las personas
observations = ['Lleva paraguas', 'Camisa de manga corta']

# Definimos las probabilidades de transición entre estados
# Estas probabilidades determinan la probabilidad de pasar de un estado a otro
transition_probs = {
    'Soleado': {'Soleado': 0.6, 'Nublado': 0.3, 'Lluvioso': 0.1},  # Probabilidades desde 'Soleado'
    'Nublado': {'Soleado': 0.4, 'Nublado': 0.4, 'Lluvioso': 0.2},  # Probabilidades desde 'Nublado'
    'Lluvioso': {'Soleado': 0.2, 'Nublado': 0.5, 'Lluvioso': 0.3}  # Probabilidades desde 'Lluvioso'
}

# Definimos las probabilidades de emisión de observaciones dado un estado oculto
# Estas probabilidades determinan qué acción se puede observar en un estado dado
emission_probs = {
    'Soleado': {'Lleva paraguas': 0.1, 'Camisa de manga corta': 0.9},  # Emisiones desde 'Soleado'
    'Nublado': {'Lleva paraguas': 0.5, 'Camisa de manga corta': 0.5},  # Emisiones desde 'Nublado'
    'Lluvioso': {'Lleva paraguas': 0.8, 'Camisa de manga corta': 0.2}   # Emisiones desde 'Lluvioso'
}

def generate_sequence(num_days):
    """Genera una secuencia de estados y observaciones a lo largo de los días."""
    
    # Elegir un estado inicial aleatorio de la lista de estados
    current_state = random.choice(states)
    
    # Almacenar la secuencia de estados y observaciones generadas
    state_sequence = []  # Lista para los estados ocultos
    observation_sequence = []  # Lista para las observaciones

    # Iterar sobre el número de días especificado
    for _ in range(num_days):
        # Almacenar el estado actual en la lista de estados
        state_sequence.append(current_state)

        # Generar una observación basada en el estado actual
        if current_state == 'Soleado':
            # Elegir la observación basada en la probabilidad de emisión
            observation = 'Lleva paraguas' if random.random() < emission_probs['Soleado']['Lleva paraguas'] else 'Camisa de manga corta'
        elif current_state == 'Nublado':
            observation = 'Lleva paraguas' if random.random() < emission_probs['Nublado']['Lleva paraguas'] else 'Camisa de manga corta'
        else:  # Estado 'Lluvioso'
            observation = 'Lleva paraguas' if random.random() < emission_probs['Lluvioso']['Lleva paraguas'] else 'Camisa de manga corta'
        
        # Almacenar la observación generada en la lista de observaciones
        observation_sequence.append(observation)

        # Elegir el siguiente estado basado en las probabilidades de transición
        rand_num = random.random()  # Generar un número aleatorio entre 0 y 1
        cumulative_prob = 0.0  # Inicializar la probabilidad acumulada

        # Iterar sobre los estados posibles y sus probabilidades de transición
        for next_state, prob in transition_probs[current_state].items():
            cumulative_prob += prob  # Acumular la probabilidad

            # Si el número aleatorio es menor que la probabilidad acumulada, cambiar al siguiente estado
            if rand_num < cumulative_prob:
                current_state = next_state  # Actualizar el estado actual
                break  # Salir del bucle una vez que se haya decidido el siguiente estado

    return state_sequence, observation_sequence  # Retornar las secuencias generadas

# Generamos una secuencia de 10 días
num_days = 10
states_generated, observations_generated = generate_sequence(num_days)  # Llamar a la función para generar la secuencia

# Imprimimos los resultados
print("Secuencia de estados ocultos (clima):", states_generated)
print("Secuencia de observaciones:", observations_generated)
"""
Definición de Estados y Observaciones:

Se definen los estados ocultos (clima) y las observaciones (acciones de las personas).
Probabilidades de Transición:

Se definen las probabilidades de pasar de un estado a otro en el diccionario transition_probs.
Probabilidades de Emisión:

Se definen las probabilidades de observar un evento dado un estado oculto en el diccionario emission_probs.
Generación de Secuencia:

La función generate_sequence genera una secuencia de estados y observaciones:
Se elige un estado inicial aleatorio.
Para cada día, se almacena el estado actual y se genera una observación basada en el estado.
Luego, se elige el siguiente estado utilizando las probabilidades de transición.
Simulación:

Se simula la secuencia de 10 días y se imprimen los estados y las observaciones generadas.
"""