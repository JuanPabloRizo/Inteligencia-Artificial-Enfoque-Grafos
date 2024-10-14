# Definir el grafo como un diccionario de listas (Grafo no dirigido)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función auxiliar: Búsqueda en Profundidad Limitada (DLS)
def dls_recursive(graph, node, goal, depth, limit, path, visited):
    # Si hemos llegado al objetivo, devolvemos el camino
    if node == goal:
        return path
    
    # Si hemos alcanzado el límite de profundidad, detenemos la búsqueda en esta rama
    if depth == limit:
        return None
    
    # Marcamos el nodo como visitado
    visited.add(node)
    
    # Recorremos los vecinos del nodo actual
    for neighbor in graph[node]:
        if neighbor not in visited:  # Evitar ciclos
            new_path = path + [neighbor]  # Agregar el vecino al camino actual
            result = dls_recursive(graph, neighbor, goal, depth + 1, limit, new_path, visited)
            if result:
                return result
    
    return None  # No se encontró el objetivo en esta rama

# Función de Búsqueda en Profundidad Iterativa (IDS)
def ids(graph, start, goal, max_depth):
    # Probar todos los límites de profundidad desde 0 hasta max_depth
    for limit in range(max_depth + 1):
        visited = set()  # Reiniciar el conjunto de nodos visitados en cada iteración
        result = dls_recursive(graph, start, goal, 0, limit, [start], visited)
        if result:
            return result  # Retornar el camino si se encuentra
    return None  # Si no se encuentra el camino dentro del límite de profundidad

# Ejemplo de uso: Búsqueda desde 'A' a 'F' con un límite máximo de profundidad de 4
start_node = 'D'
goal_node = 'F'
max_depth = 3
path = ids(graph, start_node, goal_node, max_depth)

if path:
    print(f"El camino desde {start_node} hasta {goal_node} es: {path}")
else:
    print(f"No se encontró un camino desde {start_node} hasta {goal_node} dentro del límite de profundidad {max_depth}")
