class Graph: 
    def __init__(self, vertices):
        # Constructor que inicializa el grafo
        self.V = vertices  # Número total de vértices en el grafo
        self.graph = [[] for _ in range(vertices)]  # Lista de adyacencia para almacenar el grafo

    def add_edge(self, u, v):
        # Método para agregar una arista entre los vértices u y v
        self.graph[u].append(v)  # Añade v a la lista de adyacencia de u
        self.graph[v].append(u)  # Añade u a la lista de adyacencia de v (grafo no dirigido)

    def is_safe(self, v, color, c):
        # Verifica si se puede asignar el color c al vértice v
        # Se revisan los vértices adyacentes de v
        for i in self.graph[v]:
            if color[i] == c:  # Si algún vecino ya tiene el color c
                return False  # No se puede asignar el color c a v
        return True  # Es seguro asignar el color c a v

    def graph_coloring_util(self, m, color, v):
        # Método recursivo para intentar colorear el grafo
        # m es el número de colores disponibles
        # color es la lista que mantiene los colores asignados a cada vértice

        # Si todos los vértices están asignados, se ha encontrado una solución
        if v == self.V:
            return True
        
        # Probar diferentes colores para el vértice v
        for c in range(1, m + 1):  # Iterar a través de los colores del 1 al m
            if self.is_safe(v, color, c):  # Verificar si el color c se puede asignar
                color[v] = c  # Asignar el color c al vértice v

                # Recursión para intentar colorear el siguiente vértice
                if self.graph_coloring_util(m, color, v + 1):
                    return True  # Si se encuentra una solución, retornar True

                # Si no se pudo colorear, retroceder (backtrack)
                color[v] = 0  # Deshacer la asignación del color a v

        return False  # Si no se puede colorear el vértice v, retornar False

    def graph_coloring(self, m):
        # Método para iniciar el proceso de coloración del grafo
        # m es el número de colores disponibles
        color = [0] * self.V  # Inicializa el color de cada vértice a 0 (sin color)

        # Llama al método recursivo para colorear el grafo
        if not self.graph_coloring_util(m, color, 0):
            print("No se pudo encontrar una solución")  # Si no se encuentra solución
            return False

        print("Se encontró una solución con los colores asignados:")  # Si se encontró solución
        print(color)  # Imprimir la asignación de colores
        return True  # Retornar True indicando que se encontró una solución


# Ejemplo de uso
g = Graph(4)  # Crear un grafo con 4 vértices
g.add_edge(0, 1)  # Añadir arista entre el vértice 0 y 1
g.add_edge(0, 2)  # Añadir arista entre el vértice 0 y 2
g.add_edge(1, 2)  # Añadir arista entre el vértice 1 y 2
g.add_edge(1, 3)  # Añadir arista entre el vértice 1 y 3

m = 3  # Número de colores disponibles
g.graph_coloring(m)  # Llamar a la función para intentar colorear el grafo
