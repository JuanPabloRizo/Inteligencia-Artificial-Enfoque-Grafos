import numpy as np

class MDP:
    def __init__(self, states, actions, transition_probs, rewards, gamma=0.9):
        """
        Inicializa el Proceso de Decisión de Markov (MDP).

        :param states: Lista de estados en el MDP.
        :param actions: Lista de acciones disponibles.
        :param transition_probs: Probabilidades de transición entre estados.
        :param rewards: Recompensas asociadas a los estados y acciones.
        :param gamma: Factor de descuento para las recompensas futuras.
        """
        self.states = states  # Conjunto de estados
        self.actions = actions  # Conjunto de acciones
        self.transition_probs = transition_probs  # Probabilidades de transición
        self.rewards = rewards  # Recompensas
        self.gamma = gamma  # Factor de descuento
        self.value_function = np.zeros(len(states))  # Función de valor inicializada en 0 para todos los estados

    def value_iteration(self, theta=0.01):
        """
        Método de Iteración de Valor para resolver el MDP.

        :param theta: Umbral de convergencia; el algoritmo se detiene cuando los cambios son menores que este valor.
        """
        while True:
            delta = 0  # Variable para rastrear el cambio máximo en la función de valor
            # Iterar sobre todos los estados
            for s in range(len(self.states)):
                v = self.value_function[s]  # Valor actual del estado s
                # Actualizar la función de valor para el estado s
                self.value_function[s] = max(
                    sum(self.transition_probs[s][a][s_next] * 
                        (self.rewards[s][a] + self.gamma * self.value_function[s_next]) 
                        for s_next in range(len(self.states)))
                    for a in range(len(self.actions))
                )
                # Calcular el cambio en la función de valor
                delta = max(delta, abs(v - self.value_function[s]))
            # Si el cambio máximo es menor que theta, se considera que ha convergido
            if delta < theta:
                break

    def get_optimal_policy(self):
        """
        Obtener la política óptima basada en la función de valor calculada.

        :return: Array de índices de las acciones que constituyen la política óptima.
        """
        policy = np.zeros(len(self.states), dtype=int)  # Inicializa la política como un arreglo de ceros
        for s in range(len(self.states)):
            # Para cada estado, encuentra la acción que maximiza la utilidad esperada
            policy[s] = np.argmax(
                [sum(self.transition_probs[s][a][s_next] * 
                     (self.rewards[s][a] + self.gamma * self.value_function[s_next]) 
                     for s_next in range(len(self.states))) 
                 for a in range(len(self.actions))]
            )
        return policy  # Devuelve la política óptima

# Definir los estados y acciones disponibles
states = ['S1', 'S2', 'S3']  # Estados en el MDP
actions = ['A1', 'A2']  # Acciones disponibles para los estados

# Definir las probabilidades de transición: P(s' | s, a)
# Esta estructura es un diccionario que mapea cada estado a un diccionario de acciones,
# que a su vez mapea a una lista de probabilidades de llegar a otros estados.
transition_probs = {
    0: {0: [0.8, 0.2, 0.0], 1: [0.5, 0.5, 0.0]},  # Desde S1, con A1 y A2
    1: {0: [0.0, 0.9, 0.1], 1: [0.0, 0.2, 0.8]},  # Desde S2, con A1 y A2
    2: {0: [0.0, 0.0, 1.0], 1: [0.0, 0.0, 1.0]}   # Desde S3, con A1 y A2
}

# Definir las recompensas para cada estado y acción
# Esta es una lista de listas, donde rewards[s][a] da la recompensa para el estado s al tomar la acción a.
rewards = [
    [5, 2],  # Recompensas para S1 al tomar A1 y A2
    [0, 10],  # Recompensas para S2 al tomar A1 y A2
    [0, 0]    # Recompensas para S3 al tomar A1 y A2 (sin recompensas)
]

# Crear el MDP con los parámetros definidos
mdp = MDP(states, actions, transition_probs, rewards)

# Ejecutar el algoritmo de Iteración de Valor
mdp.value_iteration()

# Obtener la política óptima calculada
optimal_policy = mdp.get_optimal_policy()

# Imprimir la función de valor para cada estado
print("Función de valor:")
print(mdp.value_function)
# Imprimir la política óptima en términos de índices de acción
print("Política óptima (índices de acción):")
print(optimal_policy)
# Imprimir la política óptima en términos de nombres de acción
print("Política óptima (acciones):")
print([actions[i] for i in optimal_policy])
"""
La salida del programa proporcionará la función de valor para cada estado 
y la política óptima que el agente debería seguir, mostrando tanto los 
índices de las acciones como los nombres correspondientes.
"""