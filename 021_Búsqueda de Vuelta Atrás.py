def print_solution(board):
    # Imprime la solución actual del tablero de ajedrez
    for row in board:
        print(" ".join(row))  # Une los elementos de cada fila en una cadena y los imprime
    print()  # Imprime una línea en blanco para separar soluciones

def is_safe(board, row, col):
    # Comprueba si es seguro colocar una reina en la posición (row, col)

    # Comprobar la columna
    for i in range(row):
        if board[i][col] == 'Q':  # Si hay una reina en la misma columna
            return False  # No es seguro colocarla aquí

    # Comprobar la diagonal superior izquierda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':  # Si hay una reina en la diagonal
            return False  # No es seguro colocarla aquí

    # Comprobar la diagonal superior derecha
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 'Q':  # Si hay una reina en la diagonal
            return False  # No es seguro colocarla aquí

    return True  # Si no se encontraron conflictos, es seguro colocar la reina

def solve_n_queens_util(board, row):
    # Intenta colocar reinas en el tablero de manera recursiva
    if row >= len(board):
        # Si se ha colocado una reina en cada fila, se ha encontrado una solución
        print_solution(board)  # Imprime la solución
        return True  # Retorna True para indicar que se encontró al menos una solución

    found_solution = False  # Variable para rastrear si se encontró al menos una solución
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 'Q'  # Coloca una reina en la posición (row, col)
            # Llama recursivamente para colocar reinas en la siguiente fila
            found_solution = solve_n_queens_util(board, row + 1) or found_solution
            # Si no se encontró una solución, retira la reina (retroceso)
            board[row][col] = '.'  # Marca la posición como vacía nuevamente

    return found_solution  # Retorna si se encontró una solución

def solve_n_queens(n):
    # Inicializa el tablero de ajedrez
    board = [['.' for _ in range(n)] for _ in range(n)]  # Crea un tablero n x n lleno de espacios vacíos ('.')
    if not solve_n_queens_util(board, 0):
        # Si no se encontró solución, imprime un mensaje
        print("No hay solución")

# Ejemplo de uso
n = 4  # Define el tamaño del tablero (n x n)
solve_n_queens(n)  # Llama a la función para resolver el problema
