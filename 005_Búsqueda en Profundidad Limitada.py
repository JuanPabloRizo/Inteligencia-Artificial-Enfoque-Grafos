# Definir el grafo como un diccionario de listas (Grafo no dirigido)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función de Búsqueda en Profundidad Limitada (DLS)
def dls(graph, start, goal, limit):
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

    # Iniciamos la búsqueda recursiva con la profundidad inicial 0
    visited = set()  # Conjunto de nodos visitados para evitar ciclos
    return dls_recursive(graph, start, goal, 0, limit, [start], visited)


# Ejemplo de uso: Búsqueda desde 'A' a 'F' con un límite de profundidad de 3
start_node = 'A'
goal_node = 'F'
depth_limit = 3
path = dls(graph, start_node, goal_node, depth_limit)

if path:
    print(f"El camino desde {start_node} hasta {goal_node} es: {path}")
else:
    print(f"No se encontró un camino desde {start_node} hasta {goal_node} dentro del límite de profundidad {depth_limit}")
