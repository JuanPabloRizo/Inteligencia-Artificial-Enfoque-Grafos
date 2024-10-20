# Grafo AND-OR como un diccionario (AND-OR significa que algunos nodos tienen ramas obligatorias, otros no)
ao_graph = {
    'A': {'B': ('C', 'D')},  # AND: Para resolver A, debes resolver tanto C como D
    'B': ('E', 'F'),         # OR: Para resolver B, puedes resolver E o F
    'C': {},
    'D': {},
    'E': {},
    'F': {}
}

def ao_star(graph, node, path):
    if not graph[node]:  # Si el nodo no tiene hijos, es una hoja
        return True
    
    for subgoal, branches in graph.get(node, {}).items():
        if isinstance(branches, tuple):  # AND: Todos los hijos deben resolverse
            all_resolved = True
            for child in branches:
                if not ao_star(graph, child, path):
                    all_resolved = False
                    break
            if all_resolved:
                path.append(subgoal)
                return True
        else:  # OR: Solo uno de los hijos debe resolverse
            if ao_star(graph, branches, path):
                path.append(subgoal)
                return True
    
    return False

# Ejecutar la búsqueda AO* comenzando desde 'A'
path = []
ao_star(ao_graph, 'A', path)
print("Solución encontrada en AO*:", path[::-1])
