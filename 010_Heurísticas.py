import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name        # Nombre del nodo
        self.parent = parent    # Nodo padre
        self.g = g              # Costo desde el inicio
        self.h = h              # Heurística
        self.f = g + h          # Costo total

    def __lt__(self, other):
        return self.f < other.f  # Comparar nodos por el costo total

def heuristic(node, goal):
    # Heurística simple: distancia en línea recta (valor ficticio)
    distances = {
        'A': 7,
        'B': 6,
        'C': 2,
        'D': 1,
        'E': 0,
        'F': 1
    }
    return distances.get(node, float('inf'))  # Devuelve infinito si el nodo no está en el diccionario

def a_star(graph, start, goal):
    open_set = []
    closed_set = set()
    
    # Nodo inicial
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)
    
    while open_set:
        current_node = heapq.heappop(open_set)  # Sacar el nodo con el costo más bajo
        
        if current_node.name == goal:  # Si alcanzamos el nodo objetivo
            path = []
            while current_node:  # Reconstruir el camino
                path.append(current_node.name)
                current_node = current_node.parent
            return path[::-1]  # Retornar el camino en orden
        
        closed_set.add(current_node.name)  # Marcar el nodo actual como visitado

        for neighbor in graph[current_node.name]:
            if neighbor in closed_set:
                continue
            
            g = current_node.g + 1  # Suponemos un costo uniforme de 1 para cada paso
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, current_node, g, h)

            # Si el vecino no está en open_set o se ha encontrado un camino mejor
            if neighbor_node not in open_set:
                heapq.heappush(open_set, neighbor_node)

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
path = a_star(graph, start, goal)

if path:
    print(f"El camino más corto desde {start} hasta {goal} es: {path}")
else:
    print(f"No hay camino desde {start} hasta {goal}")
