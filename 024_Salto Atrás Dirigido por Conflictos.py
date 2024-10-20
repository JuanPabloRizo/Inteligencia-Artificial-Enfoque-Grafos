def print_board(board):
    """Imprime el tablero de Sudoku de manera formateada."""
    for row in board:
        print(" | ".join(str(num) if num != 0 else "." for num in row))  # Usar "." para celdas vacías
    print()  # Espacio extra para claridad

def is_safe(board, row, col, num):
    """Verifica si es seguro colocar el número 'num' en la celda (row, col)."""
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False  # Colisión en fila o columna
    
    # Verificar subcuadro de 3x3
    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False  # Colisión en el subcuadro

    return True  # Es seguro colocar el número

def conflict_directed_backjump(board, assignments, row, col):
    """Resuelve el Sudoku utilizando Salto Atrás Dirigido por Conflictos."""
    if row == 9:  # Si hemos asignado todos los números
        return True  # Sudoku resuelto

    if col == 9:  # Si hemos completado una fila
        return conflict_directed_backjump(board, assignments, row + 1, 0)

    if board[row][col] != 0:  # Si la celda ya está asignada
        return conflict_directed_backjump(board, assignments, row, col + 1)

    # Probar números del 1 al 9
    for num in range(1, 10):
        if is_safe(board, row, col, num):  # Verificar si es seguro colocar el número
            board[row][col] = num  # Colocar el número en la celda
            assignments.append((row, col, num))  # Registrar la asignación

            if conflict_directed_backjump(board, assignments, row, col + 1):
                return True  # Si se encontró una solución, retornar True

            # Deshacer la asignación (backtrack)
            board[row][col] = 0
            assignments.pop()  # Quitar la última asignación

    # Volver al conflicto anterior
    for r, c, _ in assignments[::-1]:  # Retroceder a la última variable que causó conflicto
        if board[r][c] == 0:  # Encontrar la primera celda vacía asignada
            return conflict_directed_backjump(board, assignments, r, c)

    return False  # Si no se pudo colocar ningún número, retornar False

# Ejemplo de uso
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Tablero inicial de Sudoku:")
print_board(sudoku_board)  # Imprimir el tablero inicial

assignments = []  # Lista para llevar el registro de las asignaciones
if conflict_directed_backjump(sudoku_board, assignments, 0, 0):
    print("Sudoku resuelto:")
    print_board(sudoku_board)  # Imprimir el tablero resuelto
else:
    print("No se encontró solución para el Sudoku.")
