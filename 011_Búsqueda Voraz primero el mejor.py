class Node:
    def __init__(self, name):
        self.name = name  # Nombre del nodo

def heuristic(node, goal):
    # Heurística simple: distancia ficticia al nodo objetivo
    distances = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 1,
        'E': 0,
        'F': 1
    }
    return distances.get(node.name, float('inf'))  # Devuelve infinito si el nodo no está en el diccionario

def greedy_best_first_search(graph, start, goal):
    open_set = []
    closed_set = set()
    
    # Nodo inicial
    start_node = Node(start)
    open_set.append(start_node)
    
    while open_set:
        # Ordenar los nodos en open_set por la heurística
        open_set.sort(key=lambda x: heuristic(x, goal))
        
        # Sacar el nodo con la menor heurística
        current_node = open_set.pop(0)

        # Si alcanzamos el nodo objetivo
        if current_node.name == goal:
            return current_node.name
        
        closed_set.add(current_node.name)  # Marcar el nodo actual como visitado
        
        # Explorar los vecinos
        for neighbor in graph[current_node.name]:
            if neighbor in closed_set:
                continue
            
            neighbor_node = Node(neighbor)

            # Agregar el vecino a open_set si no está ya
            if neighbor_node not in open_set:
                open_set.append(neighbor_node)

    return None  # Si no se encuentra un camino

# Grafo de ejemplo
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start = 'A'  # Nodo de inicio
goal = 'E'   # Nodo objetivo
path = greedy_best_first_search(graph, start, goal)

if path:
    print(f"El camino encontrado desde {start} hasta {goal} es: {path}")
else:
    print(f"No hay camino desde {start} hasta {goal}")
