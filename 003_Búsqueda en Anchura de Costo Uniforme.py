import heapq  # Para la cola de prioridad (min heap)

# Definir el grafo como un diccionario donde los nodos están conectados a otros con sus costos asociados
graph = {
    'A': [('B', 1), ('C', 5)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('F', 3)],
    'D': [('B', 2)],
    'E': [('B', 5), ('F', 1)],
    'F': [('C', 3), ('E', 1)]
}

# Función de Búsqueda en Anchura de Costo Uniforme (UCS)
def ucs(graph, start, goal):
    # Crear una cola de prioridad para mantener los nodos a explorar (costo, nodo, camino)
    queue = [(0, start, [start])]  # El primer elemento es el costo, luego el nodo y el camino
    
    visited = set()  # Conjunto para mantener un registro de los nodos visitados
    
    while queue:
        # Extraer el nodo con el menor costo acumulado
        cost, node, path = heapq.heappop(queue)
        
        # Si el nodo ya fue visitado, lo saltamos
        if node in visited:
            continue
        
        # Si llegamos al nodo objetivo, devolvemos el costo y el camino
        if node == goal:
            return cost, path
        
        # Marcar el nodo como visitado
        visited.add(node)
        
        # Obtener los vecinos del nodo y agregar los caminos a la cola
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                new_cost = cost + edge_cost  # Actualizar el costo acumulado
                new_path = path + [neighbor]  # Crear un nuevo camino agregando el vecino
                heapq.heappush(queue, (new_cost, neighbor, new_path))  # Añadir el nuevo camino a la cola de prioridad
                
    return None  # Si no se encuentra un camino, retornar None

# Ejemplo de uso: Encontrar el camino de costo mínimo de 'A' a 'F'
start_node = 'A'
goal_node = 'F'
result = ucs(graph, start_node, goal_node)

if result:
    cost, path = result
    print(f"El camino de costo mínimo desde {start_node} hasta {goal_node} es: {path} con un costo de {cost}")
else:
    print(f"No hay camino desde {start_node} hasta {goal_node}")
