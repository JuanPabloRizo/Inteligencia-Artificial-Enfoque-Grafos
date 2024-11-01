import heapq

class Nodo:
    def __init__(self, nombre, costo, heuristica, padre=None):
        self.nombre = nombre  # Nombre del nodo
        self.costo = costo  # Costo acumulado para llegar a este nodo
        self.heuristica = heuristica  # Valor heurístico
        self.padre = padre  # Nodo padre para reconstruir el camino

    def costo_total(self):
        return self.costo + self.heuristica  # Costo total es la suma del costo y la heurística

    def __lt__(self, otro):
        return self.costo_total() < otro.costo_total()  # Para que funcione el heapq

class Grafo:
    def __init__(self):
        self.adjacencias = {}  # Diccionario que representa el grafo

    def agregar_arista(self, origen, destino, costo):
        if origen not in self.adjacencias:
            self.adjacencias[origen] = {}
        self.adjacencias[origen][destino] = costo

    def obtener_vecinos(self, nodo):
        return self.adjacencias.get(nodo, {})

def buscar_a_star(grafo, inicio, objetivo, heuristicas):
    # Inicializar la cola de prioridad
    cola = []
    # Agregar el nodo de inicio
    heapq.heappush(cola, Nodo(inicio, 0, heuristicas[inicio]))
    visitados = set()  # Conjunto para rastrear nodos visitados

    while cola:
        nodo_actual = heapq.heappop(cola)  # Extraer el nodo con el costo total más bajo

        # Si llegamos al objetivo, reconstruimos el camino
        if nodo_actual.nombre == objetivo:
            camino = []
            while nodo_actual:
                camino.append(nodo_actual.nombre)
                nodo_actual = nodo_actual.padre
            return camino[::-1]  # Devolver el camino en orden correcto

        visitados.add(nodo_actual.nombre)  # Marcar el nodo actual como visitado

        # Explorar los vecinos del nodo actual
        for vecino, costo in grafo.obtener_vecinos(nodo_actual.nombre).items():
            if vecino not in visitados:
                # Calcular el nuevo costo total para llegar al vecino
                nuevo_costo = nodo_actual.costo + costo
                # Crear un nuevo nodo con el vecino
                nuevo_nodo = Nodo(vecino, nuevo_costo, heuristicas[vecino], nodo_actual)
                heapq.heappush(cola, nuevo_nodo)  # Agregar el nodo a la cola

    return None  # No se encontró un camino

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un grafo
    grafo = Grafo()
    # Agregar aristas al grafo
    grafo.agregar_arista('A', 'B', 1)
    grafo.agregar_arista('A', 'C', 4)
    grafo.agregar_arista('B', 'C', 2)
    grafo.agregar_arista('B', 'D', 5)
    grafo.agregar_arista('C', 'D', 1)

    # Heurísticas (distancias estimadas al objetivo)
    heuristicas = {
        'A': 3,
        'B': 2,
        'C': 1,
        'D': 0
    }

    # Ejecutar la búsqueda A*
    inicio = 'A'
    objetivo = 'D'
    camino = buscar_a_star(grafo, inicio, objetivo, heuristicas)

    if camino:
        print(f"Camino encontrado: {' -> '.join(camino)}")
    else:
        print("No se encontró un camino.")
"""
Clase Nodo:

Representa un nodo en el grafo, con un nombre, costo acumulado, valor heurístico y un puntero al nodo padre.
El método costo_total calcula el costo total sumando el costo acumulado y el valor heurístico.
El método __lt__ permite que los nodos se comparen entre sí según su costo total, lo que es necesario para que funcione heapq.
Clase Grafo:

Almacena las adyacencias del grafo como un diccionario de diccionarios.
El método agregar_arista añade una arista con un costo determinado entre dos nodos.
El método obtener_vecinos devuelve los nodos adyacentes a un nodo dado.
Función buscar_a_star:

Inicializa una cola de prioridad (cola) y agrega el nodo de inicio.
Mientras haya nodos en la cola, extrae el nodo con el menor costo total.
Si el nodo actual es el objetivo, reconstruye y devuelve el camino desde el nodo objetivo hasta el inicio.
Marca el nodo actual como visitado y explora sus vecinos.
Para cada vecino, calcula el nuevo costo total y crea un nuevo nodo que se agrega a la cola.
Ejemplo de Uso:

Se crea un grafo y se agregan aristas con costos.
Se definen heurísticas para cada nodo.
Se ejecuta la búsqueda A* desde el nodo 'A' al nodo 'D'.
"""