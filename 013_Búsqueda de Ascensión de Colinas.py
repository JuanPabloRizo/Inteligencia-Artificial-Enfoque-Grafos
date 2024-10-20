import random

# Definir una función heurística: en este ejemplo simple, el valor es más alto cuanto más cerca estemos de la meta
def heuristic(state, goal):
    # Heurística inversa: menor es la distancia a la meta, mayor es el valor
    return -abs(goal - state)

# Definir el espacio de estados: en este caso, un espacio unidimensional simple
def get_neighbors(state):
    return [state - 1, state + 1]  # Los vecinos son el número anterior y siguiente

# Implementar la Búsqueda de Ascensión de Colinas
def hill_climbing(start, goal):
    current_state = start
    current_heuristic = heuristic(current_state, goal)
    
    while True:
        print(f"Estado actual: {current_state}, Heurística: {current_heuristic}")
        
        # Obtener los vecinos del estado actual
        neighbors = get_neighbors(current_state)
        
        # Evaluar la heurística de los vecinos
        next_state = None
        next_heuristic = float('-inf')  # Inicializar con un valor muy bajo
        
        for neighbor in neighbors:
            neighbor_heuristic = heuristic(neighbor, goal)
            if neighbor_heuristic > next_heuristic:
                next_heuristic = neighbor_heuristic
                next_state = neighbor
        
        # Si no podemos mejorar, hemos alcanzado un máximo local y terminamos
        if next_heuristic <= current_heuristic:
            print(f"Máximo local alcanzado en el estado: {current_state}")
            break
        
        # Actualizar el estado y la heurística
        current_state = next_state
        current_heuristic = next_heuristic
    
    return current_state

# Configuración inicial
start = random.randint(0, 20)  # Comenzar en un estado aleatorio entre 0 y 20
goal = 15                      # Meta: queremos alcanzar el estado 15

# Ejecutar la Búsqueda de Ascensión de Colinas
final_state = hill_climbing(start, goal)
print(f"Estado final alcanzado: {final_state}")
