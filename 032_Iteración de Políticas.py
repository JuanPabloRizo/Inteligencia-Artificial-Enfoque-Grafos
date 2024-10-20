import numpy as np

# Definir los parámetros del MDP
gamma = 0.9  # Factor de descuento

# Definir los estados, acciones, recompensas y el modelo de transición
states = [0, 1, 2]   # Lista de estados
actions = ['A', 'B']  # Lista de acciones

# Definir el modelo de transición P(s' | s, a) de forma determinista
# Cada acción en cada estado lleva a un estado particular
transition_probs = {
    0: {'A': 1, 'B': 2},  # Desde estado 0, A -> estado 1, B -> estado 2
    1: {'A': 0, 'B': 2},  # Desde estado 1, A -> estado 0, B -> estado 2
    2: {'A': 0, 'B': 1}   # Desde estado 2, A -> estado 0, B -> estado 1
}

# Definir las recompensas R(s, a)
rewards = {
    0: {'A': 10, 'B': 0},   # Recompensas desde estado 0
    1: {'A': -1, 'B': 1},   # Recompensas desde estado 1
    2: {'A': 5, 'B': -10}   # Recompensas desde estado 2
}

# Inicializar una política arbitraria (para cada estado, elegir una acción)
# Esta política asume que en todos los estados tomamos la acción 'A'
policy = ['A', 'A', 'A']  # Inicializar la política con la acción 'A' en todos los estados

# Inicializar los valores de los estados a 0
values = np.zeros(len(states))

def policy_evaluation(policy, values, gamma, states, actions, transition_probs, rewards, theta=1e-6):
    """
    Evalúa la política dada iterando hasta que los valores de los estados converjan.
    """
    while True:
        delta = 0  # Para registrar el mayor cambio en esta iteración
        # Iterar sobre todos los estados
        for s in states:
            v = values[s]  # Valor actual del estado s
            # Obtener la acción que sigue la política actual en este estado
            action = policy[s]
            # Calcular el nuevo valor del estado basado en la acción de la política
            new_value = rewards[s][action] + gamma * values[transition_probs[s][action]]
            # Actualizar el valor del estado
            values[s] = new_value
            # Calcular el cambio máximo
            delta = max(delta, abs(v - new_value))
        # Si el cambio es menor que theta, consideramos que hemos convergido
        if delta < theta:
            break
    return values

def policy_improvement(values, policy, states, actions, transition_probs, rewards, gamma):
    """
    Mejora la política dada los valores actuales de los estados.
    """
    policy_stable = True
    # Iterar sobre todos los estados
    for s in states:
        old_action = policy[s]  # Guardar la acción actual de la política
        # Probar todas las acciones y elegir la mejor basada en el valor del estado
        action_values = []
        for a in actions:
            action_value = rewards[s][a] + gamma * values[transition_probs[s][a]]
            action_values.append(action_value)
        # Elegir la acción que maximiza el valor
        best_action = actions[np.argmax(action_values)]
        # Actualizar la política si encontramos una mejor acción
        if best_action != old_action:
            policy_stable = False
        policy[s] = best_action
    return policy, policy_stable

def policy_iteration(states, actions, transition_probs, rewards, gamma):
    """
    Realiza la iteración de políticas para encontrar la política óptima.
    """
    # Inicializar una política arbitraria
    policy = ['A'] * len(states)
    values = np.zeros(len(states))  # Inicializar los valores de los estados
    while True:
        # Evaluar la política actual
        values = policy_evaluation(policy, values, gamma, states, actions, transition_probs, rewards)
        # Mejorar la política
        policy, policy_stable = policy_improvement(values, policy, states, actions, transition_probs, rewards, gamma)
        # Si la política no ha cambiado, terminamos
        if policy_stable:
            break
    return policy, values

# Ejecutar la iteración de políticas
policy_optima, valores_optimos = policy_iteration(states, actions, transition_probs, rewards, gamma)

# Mostrar los resultados
print("Política óptima:", policy_optima)
print("Valores de los estados:", valores_optimos)
