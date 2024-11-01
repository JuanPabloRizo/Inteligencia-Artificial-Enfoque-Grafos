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

# Función de Búsqueda en Anchura (BFS)
def bfs(graph, start, goal):
    # Crear una cola para mantener los nodos a explorar
    queue = deque([[start]])  # Cada elemento en la cola es un camino
    visited = set()           # Conjunto para mantener un registro de los nodos visitados
    
    while queue:
        # Sacar el primer camino de la cola
        path = queue.popleft()
        # Obtener el último nodo en el camino actual
        node = path[-1]
        
        # Si este nodo es el objetivo, devolver el camino
        if node == goal:
            return path
        
        # Si el nodo no ha sido visitado, lo marcamos como visitado
        if node not in visited:
            visited.add(node)
            
            # Obtener los vecinos del nodo y agregar los caminos a la cola
            for neighbor in graph[node]:
                new_path = list(path)  # Crear una copia del camino actual
                new_path.append(neighbor)  # Agregar el vecino al nuevo camino
                queue.append(new_path)  # Añadir el nuevo camino a la cola
                
    return None  # Si no se encuentra un camino, retornar None

# Ejemplo de uso: Encontrar el camino más corto de 'A' a 'F'
start_node = 'A'
goal_node = 'F'
path = bfs(graph, start_node, goal_node)

if path:
    print(f"El camino más corto desde {start_node} hasta {goal_node} es: {path}")
else:
    print(f"No hay camino desde {start_node} hasta {goal_node}")
