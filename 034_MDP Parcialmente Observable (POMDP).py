import numpy as np

class POMDP:
    def __init__(self, states, actions, observations, transition_probs, observation_probs, rewards):
        """
        Inicializa el POMDP.

        :param states: Lista de estados en el POMDP.
        :param actions: Lista de acciones disponibles.
        :param observations: Lista de observaciones posibles.
        :param transition_probs: Probabilidades de transición entre estados.
        :param observation_probs: Probabilidades de observación.
        :param rewards: Recompensas asociadas a los estados y acciones.
        """
        self.states = states
        self.actions = actions
        self.observations = observations
        self.transition_probs = transition_probs
        self.observation_probs = observation_probs
        self.rewards = rewards

    def belief_update(self, belief, action, observation):
        """
        Actualiza la creencia del agente basada en la acción tomada y la observación recibida.

        :param belief: Distribución de probabilidad actual sobre los estados.
        :param action: Acción tomada.
        :param observation: Observación recibida.
        :return: Nueva distribución de creencia.
        """
        new_belief = np.zeros(len(self.states))  # Inicializar nueva creencia
        for s in range(len(self.states)):
            # Calcular la nueva creencia
            total = 0
            for s_prev in range(len(self.states)):
                # P(s | a, o) ∝ P(o | s) * ∑ P(s' | s_prev, a) * belief[s_prev]
                total += self.observation_probs[s][action][observation] * self.transition_probs[s_prev][action][s] * belief[s_prev]
            new_belief[s] = total
        
        # Normalizar la nueva creencia
        return new_belief / np.sum(new_belief)

    def select_action(self, belief):
        """
        Selecciona la mejor acción basada en la creencia actual.

        :param belief: Distribución de probabilidad actual sobre los estados.
        :return: Índice de la acción seleccionada.
        """
        action_values = np.zeros(len(self.actions))
        for a in range(len(self.actions)):
            for s in range(len(self.states)):
                action_values[a] += self.rewards[s][a] * belief[s]
        
        return np.argmax(action_values)  # Acción que maximiza la recompensa esperada

# Definir los estados, acciones y observaciones
states = ['S1', 'S2']  # Dos estados posibles
actions = ['A1', 'A2']  # Dos acciones posibles
observations = ['O1', 'O2']  # Dos observaciones posibles

# Probabilidades de transición: P(s' | s, a)
transition_probs = [
    [[0.8, 0.2], [0.4, 0.6]],  # Desde S1 con A1 y A2
    [[0.3, 0.7], [0.5, 0.5]]   # Desde S2 con A1 y A2
]

# Probabilidades de observación: P(o | s, a)
observation_probs = [
    [[0.9, 0.1], [0.6, 0.4]],  # Observaciones desde S1 para A1 y A2
    [[0.7, 0.3], [0.2, 0.8]]   # Observaciones desde S2 para A1 y A2
]

# Recompensas: R(s, a)
rewards = [
    [10, 0],  # Recompensas para S1 al tomar A1 y A2
    [0, 5]    # Recompensas para S2 al tomar A1 y A2
]

# Crear el POMDP
pomdp = POMDP(states, actions, observations, transition_probs, observation_probs, rewards)

# Inicializar la creencia en S1
belief = np.array([1.0, 0.0])  # 100% de creencia en S1

# Seleccionar acciones basadas en creencias
for _ in range(5):  # Iterar para 5 pasos
    action = pomdp.select_action(belief)  # Seleccionar la acción óptima
    print(f"Acción seleccionada: {actions[action]}")

    # Simular una observación (aquí solo un ejemplo aleatorio)
    observation = np.random.choice(range(len(observations)), p=[0.5, 0.5])  # Simulación de observación
    print(f"Observación recibida: {observations[observation]}")

    # Actualizar la creencia basándose en la acción y la observación
    belief = pomdp.belief_update(belief, action, observation)
    print(f"Nueva creencia: {belief}\n")
