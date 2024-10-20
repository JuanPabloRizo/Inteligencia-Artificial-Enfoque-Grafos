import heapq

# Definir el grafo como un diccionario de diccionarios (grafo con pesos)
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 4},
    'C': {'F': 6},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

# Definir una heurística (h(n)), la estimación del costo restante hasta 'F'
heuristic = {
    'A': 5,
    'B': 2,
    'C': 4,
    'D': 6,
    'E': 1,
    'F': 0  # El nodo objetivo tiene una heurística de 0
}

def a_star(graph, start, goal):
    # Crear una cola de prioridad
    queue = []
    heapq.heappush(queue, (0, start))
    
    # Diccionarios para el costo y el camino
    cost_so_far = {start: 0}
    came_from = {start: None}
    
    while queue:
        # Obtener el nodo con el menor costo total (f(n) = g(n) + h(n))
        current_cost, current_node = heapq.heappop(queue)
        
        # Si encontramos el nodo objetivo, reconstruir el camino
        if current_node == goal:
            path = []
            while current_node:
                path.append(current_node)
                current_node = came_from[current_node]
            return path[::-1]  # Invertimos el camino para mostrar de inicio a fin
        
        # Expandir los vecinos del nodo actual
        for neighbor, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost  # g(n)
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]  # f(n) = g(n) + h(n)
                heapq.heappush(queue, (priority, neighbor))
                came_from[neighbor] = current_node
    
    return None  # No se encontró un camino

# Ejecutar A* para encontrar el camino de 'A' a 'F'
path = a_star(graph, 'A', 'F')
print("Camino encontrado:", path)
