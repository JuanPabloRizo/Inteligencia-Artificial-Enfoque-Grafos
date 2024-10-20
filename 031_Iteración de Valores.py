import numpy as np

# Definir los parámetros del MDP
gamma = 0.9  # Factor de descuento

# Definir los estados, acciones y las recompensas
# Estados: 0, 1, 2
# Acciones: 'A', 'B'
states = [0, 1, 2]
actions = ['A', 'B']

# Matriz de transición P(s' | s, a)
# Probabilidades de transición: P(s' | s, a)
# Por simplicidad, se asume determinista en este ejemplo.
transition_probs = {
    0: {'A': 1, 'B': 2},  # Desde el estado 0, acción A -> estado 1, acción B -> estado 2
    1: {'A': 0, 'B': 2},  # Desde el estado 1, acción A -> estado 0, acción B -> estado 2
    2: {'A': 0, 'B': 1}   # Desde el estado 2, acción A -> estado 0, acción B -> estado 1
}

# Recompensas: R(s, a)
rewards = {
    0: {'A': 10, 'B': 0},
    1: {'A': -1, 'B': 1},
    2: {'A': 5, 'B': -10}
}

# Inicializar los valores de los estados a 0
values = np.zeros(len(states))

# Función para realizar una iteración de la ecuación de Bellman
def value_iteration(values, gamma, states, actions, transition_probs, rewards, theta=1e-6):
    """
    Realiza iteración de valores hasta que los valores converjan.
    """
    # Bucle hasta que los valores converjan
    while True:
        delta = 0  # Para monitorear el mayor cambio en esta iteración
        # Iterar sobre todos los estados
        for s in states:
            # Guardar el valor actual del estado
            v = values[s]
            
            # Inicializar la mejor acción
            best_action_value = float('-inf')
            
            # Probar todas las acciones posibles
            for a in actions:
                # Calcular el valor esperado para la acción
                new_value = rewards[s][a] + gamma * values[transition_probs[s][a]]
                
                # Guardar el valor máximo
                best_action_value = max(best_action_value, new_value)
            
            # Actualizar el valor del estado s
            values[s] = best_action_value
            
            # Calcular el cambio máximo (delta)
            delta = max(delta, abs(v - values[s]))
        
        # Verificar si el cambio es menor que un umbral theta (convergencia)
        if delta < theta:
            break  # Los valores han convergido

    return values

# Ejecutar la iteración de valores
valores_optimos = value_iteration(values, gamma, states, actions, transition_probs, rewards)

# Mostrar los valores de los estados
for i, v in enumerate(valores_optimos):
    print(f"Valor del estado {i}: {v:.2f}")
"""
El valor del estado 0 es mayor que los otros, 
lo que significa que es más beneficioso (en términos de recompensa esperada) 
para el agente estar en el estado 0, dado que se toman las decisiones óptimas
"""