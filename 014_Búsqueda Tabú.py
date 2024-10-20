import random

# Definir una función de evaluación (heurística)
def objective_function(state, goal):
    return -abs(goal - state)  # Cuanto más cerca del objetivo, mejor es el estado

# Obtener los vecinos de un estado (en este caso, el número anterior y siguiente)
def get_neighbors(state):
    return [state - 1, state + 1]  # Los vecinos son el número anterior y el siguiente

# Implementar la Búsqueda Tabú
def tabu_search(start, goal, tabu_size, max_iterations):
    # Estado inicial
    current_state = start
    current_score = objective_function(current_state, goal)
    
    # Lista tabú para evitar reexplorar estados
    tabu_list = []
    
    best_state = current_state
    best_score = current_score
    
    for iteration in range(max_iterations):
        print(f"Iteración {iteration}: Estado actual = {current_state}, Heurística = {current_score}")
        
        # Obtener vecinos y elegir el mejor que no esté en la lista tabú
        neighbors = get_neighbors(current_state)
        best_candidate = None
        best_candidate_score = float('-inf')
        
        for neighbor in neighbors:
            # Evitar los estados en la lista tabú
            if neighbor not in tabu_list:
                score = objective_function(neighbor, goal)
                if score > best_candidate_score:
                    best_candidate = neighbor
                    best_candidate_score = score
        
        # Actualizar el estado y la lista tabú
        current_state = best_candidate
        current_score = best_candidate_score
        tabu_list.append(current_state)
        
        # Limitar el tamaño de la lista tabú
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)
        
        # Actualizar el mejor estado encontrado
        if current_score > best_score:
            best_state = current_state
            best_score = current_score
        
        # Si alcanzamos la meta, salimos del bucle
        if current_state == goal:
            print("¡Meta alcanzada!")
            break
    
    print(f"Mejor estado alcanzado: {best_state}, con heurística: {best_score}")
    return best_state

# Parámetros iniciales
start = random.randint(0, 20)  # Estado inicial aleatorio
goal = 15                      # Meta es alcanzar el estado 15
tabu_size = 5                  # Tamaño de la lista tabú
max_iterations = 20            # Número máximo de iteraciones

# Ejecutar la Búsqueda Tabú
final_state = tabu_search(start, goal, tabu_size, max_iterations)
print(f"Estado final alcanzado: {final_state}")
