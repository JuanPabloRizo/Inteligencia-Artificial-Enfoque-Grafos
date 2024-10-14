from collections import deque

# Definir el grafo como un diccionario de listas (Grafo no dirigido)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función para realizar la búsqueda bidireccional
def bidirectional_search(graph, start, goal):
    # Colas para las búsquedas desde el inicio y desde el objetivo
    queue_start = deque([[start]])  # Cola de la búsqueda desde el inicio
    queue_goal = deque([[goal]])    # Cola de la búsqueda desde el objetivo
    
    # Conjuntos para los nodos visitados desde el inicio y el objetivo
    visited_start = {start}  
    visited_goal = {goal}  
    
    # Mientras ambas colas tengan elementos
    while queue_start and queue_goal:
        # Expandir desde el inicio
        path_from_start = queue_start.popleft()
        node_from_start = path_from_start[-1]
        
        if node_from_start in visited_goal:  # Si hay intersección con el objetivo
            # Devolver el camino combinado desde inicio y objetivo
            path_from_goal = next(path for path in queue_goal if path[-1] == node_from_start)
            return path_from_start + path_from_goal[::-1][1:]  # Combinar caminos
        
        # Expandir los vecinos del nodo actual desde el inicio
        for neighbor in graph[node_from_start]:
            if neighbor not in visited_start:
                visited_start.add(neighbor)
                queue_start.append(path_from_start + [neighbor])
        
        # Expandir desde el objetivo
        path_from_goal = queue_goal.popleft()
        node_from_goal = path_from_goal[-1]
        
        if node_from_goal in visited_start:  # Si hay intersección con el inicio
            # Devolver el camino combinado desde inicio y objetivo
            path_from_start = next(path for path in queue_start if path[-1] == node_from_goal)
            return path_from_start + path_from_goal[::-1][1:]  # Combinar caminos
        
        # Expandir los vecinos del nodo actual desde el objetivo
        for neighbor in graph[node_from_goal]:
            if neighbor not in visited_goal:
                visited_goal.add(neighbor)
                queue_goal.append(path_from_goal + [neighbor])

    return None  # Si no se encuentra un camino

# Ejemplo de uso: Encontrar el camino más corto de 'A' a 'F'
start_node = 'D'
goal_node = 'C'
path = bidirectional_search(graph, start_node, goal_node)

if path:
    print(f"El camino más corto desde {start_node} hasta {goal_node} es: {path}")
else:
    print(f"No hay camino desde {start_node} hasta {goal_node}")
