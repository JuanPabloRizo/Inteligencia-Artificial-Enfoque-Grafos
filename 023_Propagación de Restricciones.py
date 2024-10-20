class Graph:
    def __init__(self, vertices):
        """
        Inicializa un grafo con un número determinado de vértices.
        
        Parámetros:
        vertices: Número de vértices en el grafo.
        """
        self.V = vertices  # Almacenar el número de vértices
        self.graph = [[] for _ in range(vertices)]  # Lista de adyacencia para el grafo

    def add_edge(self, u, v):
        """
        Agrega una arista entre los vértices u y v.
        
        Parámetros:
        u: Vértice de inicio.
        v: Vértice de destino.
        """
        self.graph[u].append(v)  # Añadir vértice v a la lista de adyacencia de u
        self.graph[v].append(u)  # Añadir vértice u a la lista de adyacencia de v

    def is_safe(self, v, color, c):
        """
        Verifica si es seguro asignar el color c al vértice v.
        
        Parámetros:
        v: Vértice actual.
        color: Lista que contiene los colores asignados a cada vértice.
        c: Color que se intenta asignar al vértice v.

        Retorna:
        True si es seguro asignar el color, False en caso contrario.
        """
        for i in self.graph[v]:
            # Comprobar si el vértice adyacente ya tiene el mismo color
            if color[i] == c:
                return False  # Colisión de color, no es seguro

        return True  # Es seguro asignar el color c al vértice v

    def graph_coloring_util(self, m, color, v):
        """
        Función recursiva para intentar colorear el grafo.
        
        Parámetros:
        m: Número de colores disponibles.
        color: Lista que contiene los colores asignados a cada vértice.
        v: Vértice actual que se está coloreando.

        Retorna:
        True si se ha encontrado una solución, False en caso contrario.
        """
        # Si todos los vértices han sido coloreados
        if v == self.V:
            return True
        
        # Probar diferentes colores para el vértice v
        for c in range(1, m + 1):
            if self.is_safe(v, color, c):  # Verificar si es seguro asignar el color c
                color[v] = c  # Asignar color c al vértice v

                # Llamada recursiva para el siguiente vértice
                if self.graph_coloring_util(m, color, v + 1):
                    return True  # Si se encontró una solución, retornar True

                # Si no se pudo colorear, retroceder (backtrack)
                color[v] = 0  # Deshacer la asignación

        return False  # Si no se puede colorear, retornar False

    def graph_coloring(self, m):
        """
        Función para iniciar el proceso de coloración del grafo.
        
        Parámetros:
        m: Número de colores disponibles.
        """
        # Inicializar el color de cada vértice a 0 (sin color)
        color = [0] * self.V

        # Comenzar la coloración del grafo
        if not self.graph_coloring_util(m, color, 0):
            print("No se pudo encontrar una solución")
            return False

        # Mostrar la solución encontrada
        print("Se encontró una solución con los colores asignados:")
        print(color)
        return True

# Ejemplo de uso
g = Graph(4)  # Crear un grafo con 4 vértices
g.add_edge(0, 1)  # Agregar arista entre los vértices 0 y 1
g.add_edge(0, 2)  # Agregar arista entre los vértices 0 y 2
g.add_edge(1, 2)  # Agregar arista entre los vértices 1 y 2
g.add_edge(1, 3)  # Agregar arista entre los vértices 1 y 3

m = 3  # Número de colores disponibles
g.graph_coloring(m)  # Llamar a la función para colorear el grafo
