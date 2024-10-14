# Definir el grafo como un diccionario de listas (Grafo no dirigido)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función de Búsqueda en Profundidad (DFS) usando un enfoque iterativo
def dfs(graph, start, goal):
    # Crear una pila para mantener los nodos a explorar (LIFO: Last In, First Out)
    stack = [[start]]  # Cada elemento en la pila es un camino
    visited = set()    # Conjunto para mantener un registro de los nodos visitados
    
    while stack:
        # Sacar el último camino de la pila (el más profundo)
        path = stack.pop()
        # Obtener el último nodo en el camino actual
        node = path[-1]
        
        # Si este nodo es el objetivo, devolver el camino
        if node == goal:
            return path
        
        # Si el nodo no ha sido visitado, lo marcamos como visitado
        if node not in visited:
            visited.add(node)
            
            # Obtener los vecinos del nodo y agregar los caminos a la pila
            for neighbor in graph[node]:
                new_path = list(path)  # Crear una copia del camino actual
                new_path.append(neighbor)  # Agregar el vecino al nuevo camino
                stack.append(new_path)  # Añadir el nuevo camino a la pila
                
    return None  # Si no se encuentra un camino, retornar None

# Ejemplo de uso: Encontrar el camino desde 'A' hasta 'F'
start_node = 'D'
goal_node = 'C'
path = dfs(graph, start_node, goal_node)

if path:
    print(f"El camino desde {start_node} hasta {goal_node} es: {path}")
else:
    print(f"No hay camino desde {start_node} hasta {goal_node}")
