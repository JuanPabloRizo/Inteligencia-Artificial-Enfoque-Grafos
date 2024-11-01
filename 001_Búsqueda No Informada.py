from collections import deque

class Grafo:
    def __init__(self):
        # Inicializar un diccionario para almacenar la lista de adyacencia
        self.adjacencias = {}

    def agregar_arista(self, origen, destino):
        # Agregar una arista del nodo 'origen' al nodo 'destino'
        if origen not in self.adjacencias:
            self.adjacencias[origen] = []
        self.adjacencias[origen].append(destino)

    def buscar_amplitud(self, inicio, objetivo):
        # Inicializar una cola para los nodos por explorar
        cola = deque([inicio])
        # Crear un conjunto para rastrear los nodos visitados
        visitados = set()

        while cola:
            # Extraer el nodo actual de la cola
            nodo_actual = cola.popleft()
            print(f"Visitando: {nodo_actual}")

            # Si el nodo actual es el objetivo, retornar True
            if nodo_actual == objetivo:
                return True

            # Marcar el nodo como visitado
            visitados.add(nodo_actual)

            # Explorar los nodos adyacentes
            for vecino in self.adjacencias.get(nodo_actual, []):
                if vecino not in visitados and vecino not in cola:
                    cola.append(vecino)

        # Si el objetivo no fue encontrado, retornar False
        return False

# Ejemplo de uso
if __name__ == "__main__":
    grafo = Grafo()
    # Agregar aristas al grafo
    grafo.agregar_arista('A', 'B')
    grafo.agregar_arista('A', 'C')
    grafo.agregar_arista('B', 'D')
    grafo.agregar_arista('C', 'E')
    grafo.agregar_arista('D', 'F')
    grafo.agregar_arista('E', 'F')

    # Ejecutar búsqueda en amplitud
    inicio = 'A'
    objetivo = 'F'
    encontrado = grafo.buscar_amplitud(inicio, objetivo)

    if encontrado:
        print(f"Se encontró el objetivo '{objetivo}' comenzando desde '{inicio}'.")
    else:
        print(f"No se encontró el objetivo '{objetivo}' comenzando desde '{inicio}'.")
"""
Clase Grafo:

Contiene un diccionario adjacencias que representa las aristas del grafo, donde cada clave es un nodo y su valor es una lista de nodos adyacentes.
Método agregar_arista:

Este método agrega una arista del nodo origen al nodo destino. Si el nodo origen no existe en el grafo, lo inicializa.
Método buscar_amplitud:

Se inicializa una cola (cola) con el nodo de inicio.
Se utiliza un conjunto (visitados) para llevar el control de los nodos que ya se han explorado.
En un bucle, se extrae el nodo actual de la cola, se marca como visitado y se revisan sus vecinos. Si un vecino no ha sido visitado ni está en la cola, se añade a la cola.
Si se encuentra el objetivo, se retorna True. Si se termina de explorar el grafo sin encontrar el objetivo, se retorna False.
Ejemplo de Uso:

Se crea un grafo y se le añaden aristas.
Se ejecuta la búsqueda en amplitud desde el nodo 'A' buscando llegar al nodo 'F'.
"""