def is_safe(board, row, col, n):
    # Verificar si es seguro colocar una reina en la posición (row, col)
    for i in range(row):
        # Comprobar la columna
        if board[i] == col:
            return False  # Hay otra reina en la misma columna
        
        # Comprobar la diagonal superior izquierda
        if board[i] - i == col - row:
            return False  # Hay otra reina en la diagonal superior izquierda

        # Comprobar la diagonal superior derecha
        if board[i] + i == col + row:
            return False  # Hay otra reina en la diagonal superior derecha

    return True  # Es seguro colocar la reina en la posición especificada

def forward_checking(board, row, n):
    # Intentar colocar reinas en el tablero de manera recursiva utilizando Comprobación Hacia Delante
    if row == n:
        return True  # Se han colocado todas las reinas correctamente, se ha encontrado una solución

    for col in range(n):
        if is_safe(board, row, col, n):  # Verificar si es seguro colocar la reina en (row, col)
            board[row] = col  # Asignar la reina en la posición (row, col)

            # Aquí se podría implementar la lógica de Comprobación Hacia Delante
            # (no implementado en este ejemplo, pero se puede extender)
            
            # Llamada recursiva para intentar colocar la siguiente reina en la siguiente fila
            if forward_checking(board, row + 1, n):
                return True  # Si se encontró una solución, retornar True

            # Si no se pudo colocar la reina, deshacer la asignación (backtrack)
            board[row] = -1  # Marcar como sin asignar (es decir, sin reina)

    return False  # Si no se puede colocar la reina en ninguna columna de esta fila, retornar False

def solve_n_queens(n):
    # Inicializar el tablero como una lista de -1, donde -1 significa que no hay reina asignada
    board = [-1] * n  
    if forward_checking(board, 0, n):
        print("Solución encontrada:")
        print_board(board, n)  # Imprimir la configuración de las reinas en el tablero
    else:
        print("No se encontró solución")  # Mensaje si no se encuentra solución

def print_board(board, n):
    # Función para imprimir el tablero usando letras
    letters = [chr(i) for i in range(65, 65 + n)]  # Generar letras A, B, C, D, etc.
    for i in range(n):
        row = ['.' for _ in range(n)]  # Inicializar la fila con puntos
        if board[i] != -1:
            row[board[i]] = letters[i]  # Colocar la letra correspondiente a la reina
        print(" ".join(row))  # Imprimir la fila

# Ejemplo de uso
n = 4  # Tamaño del tablero (4x4)
solve_n_queens(n)  # Llamar a la función para intentar resolver el problema
