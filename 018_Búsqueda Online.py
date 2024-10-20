import random

# Definimos el laberinto como una lista de listas (una matriz 5x5)
laberinto = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0]
]

# Movimientos posibles: arriba, abajo, izquierda, derecha
movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Función para imprimir el estado actual del laberinto
def imprimir_laberinto(laberinto, agente_pos, objetivo_pos):
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if (i, j) == agente_pos:
                print("A", end=" ")  # Representamos el agente con 'A'
            elif (i, j) == objetivo_pos:
                print("G", end=" ")  # Representamos el objetivo con 'G'
            elif laberinto[i][j] == 1:
                print("#", end=" ")  # Obstáculo o pared
            else:
                print(".", end=" ")  # Espacio libre
        print()
    print()

# Función para verificar si una celda es válida
def es_valido(laberinto, pos):
    x, y = pos
    return 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] == 0

# Búsqueda Online: El agente se mueve hasta encontrar el objetivo
def busqueda_online(laberinto, inicio, objetivo):
    agente_pos = inicio
    visitados = set()  # Para evitar visitar el mismo lugar más de una vez
    
    while agente_pos != objetivo:
        imprimir_laberinto(laberinto, agente_pos, objetivo)
        print(f"Agente en posición: {agente_pos}")
        
        # Marcar la posición actual como visitada
        visitados.add(agente_pos)
        
        # Obtener movimientos posibles (no visitados y válidos)
        posibles_movimientos = []
        for movimiento in movimientos:
            nueva_pos = (agente_pos[0] + movimiento[0], agente_pos[1] + movimiento[1])
            if es_valido(laberinto, nueva_pos) and nueva_pos not in visitados:
                posibles_movimientos.append(nueva_pos)
        
        # Si no hay movimientos disponibles, el agente está atrapado (backtracking necesario)
        if not posibles_movimientos:
            print("No hay más movimientos disponibles, el agente está atrapado.")
            return False
        
        # Elige un movimiento aleatorio entre los posibles
        agente_pos = random.choice(posibles_movimientos)
    
    # Imprimir el estado final
    imprimir_laberinto(laberinto, agente_pos, objetivo)
    print(f"Objetivo encontrado en: {agente_pos}")
    return True

# Definir la posición inicial del agente y el objetivo
inicio = (0, 0)
objetivo = (4, 4)

# Ejecutar la búsqueda online
encontrado = busqueda_online(laberinto, inicio, objetivo)

if encontrado:
    print("El agente ha encontrado el objetivo.")
else:
    print("El agente no pudo encontrar el objetivo.")
