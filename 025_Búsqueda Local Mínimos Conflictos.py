import random

def print_assignments(assignments):
    """
    Imprime las asignaciones actuales de trabajadores a tareas de manera organizada.
    
    Parámetros:
    - assignments: Diccionario que mapea trabajadores a tareas asignadas. 
      Ejemplo: {'A': 1, 'B': 2, 'C': 3} significa que A está asignado a la tarea 1, B a la tarea 2, y así sucesivamente.
    """
    print("Asignaciones de trabajadores a tareas:")
    for worker, task in assignments.items():
        print(f"Trabajador {worker} -> Tarea {task}")
    print()  # Imprimir una línea en blanco al final para mayor claridad visual

def conflicts(assignments, worker, task, constraints):
    """
    Calcula el número de conflictos que tendría si se asigna una tarea específica a un trabajador dado.
    
    Parámetros:
    - assignments: Diccionario actual de asignaciones de trabajadores a tareas.
    - worker: El trabajador que estamos evaluando.
    - task: La tarea que queremos asignar al trabajador.
    - constraints: Diccionario de restricciones que indica qué tareas no pueden ser realizadas por ciertos trabajadores.
    
    Retorna:
    - Número de conflictos (0 si no hay conflictos, más si existen restricciones violadas o tareas repetidas).
    
    Conflictos:
    1. Si el trabajador tiene restricciones sobre la tarea (no puede hacerla).
    2. Si la tarea ya está asignada a otro trabajador.
    """
    conflict_count = 0  # Iniciamos con 0 conflictos
    
    # Verificar si la tarea está en las restricciones del trabajador
    if task in constraints.get(worker, []):  # Si la tarea está en la lista de tareas prohibidas para este trabajador
        conflict_count += 1  # Aumentamos el conteo de conflictos en 1
    
    # Verificar si algún otro trabajador ya tiene esta tarea asignada
    for other_worker, other_task in assignments.items():
        if other_worker != worker and other_task == task:
            # Si otro trabajador ya tiene esta tarea asignada, es un conflicto
            conflict_count += 1
    
    return conflict_count  # Retornamos el número total de conflictos

def min_conflicts(assignments, workers, tasks, constraints, max_steps=10000):
    """
    Algoritmo de Mínimos-Conflictos para resolver el problema de asignación de tareas.
    
    Parámetros:
    - assignments: Diccionario que mapea trabajadores a sus tareas actuales.
    - workers: Lista de trabajadores. Ejemplo: ['A', 'B', 'C', 'D', 'E']
    - tasks: Lista de tareas disponibles. Ejemplo: [1, 2, 3, 4, 5]
    - constraints: Diccionario que define las restricciones para cada trabajador.
    - max_steps: Número máximo de pasos para intentar resolver el problema (por defecto 1000).
    
    Retorna:
    - True si se encuentra una solución válida sin conflictos.
    - False si no se encuentra una solución en el número máximo de pasos.
    """
    # Comenzamos un bucle que intentará resolver el problema hasta un máximo de max_steps
    for step in range(max_steps):
        # Encontrar todos los trabajadores que tienen conflictos con sus asignaciones actuales
        conflicted_workers = [worker for worker in workers
                              if conflicts(assignments, worker, assignments[worker], constraints) > 0]
        
        # Si no hay trabajadores con conflictos, significa que hemos encontrado una solución
        if not conflicted_workers:
            return True  # Problema resuelto sin conflictos
        
        # Si hay conflictos, seleccionamos un trabajador al azar de los que tienen conflictos
        worker = random.choice(conflicted_workers)
        
        # Ahora buscamos la tarea con menos conflictos para este trabajador
        min_conflict_task = assignments[worker]  # Inicialmente, la tarea asignada actual
        min_conflicts_count = conflicts(assignments, worker, min_conflict_task, constraints)
        
        # Exploramos todas las posibles tareas (1 a 5) para encontrar la tarea con menos conflictos
        for task in tasks:
            conflict_count = conflicts(assignments, worker, task, constraints)
            if conflict_count < min_conflicts_count:
                # Si encontramos una tarea que tiene menos conflictos, la seleccionamos
                min_conflicts_count = conflict_count
                min_conflict_task = task
        
        # Asignamos al trabajador la tarea con el menor número de conflictos
        assignments[worker] = min_conflict_task
    
    # Si llegamos aquí, significa que no se pudo resolver el problema dentro del límite de max_steps
    return False

# Lista de trabajadores y lista de tareas disponibles
workers = ['A', 'B', 'C', 'D', 'E']
tasks = [1, 2, 3, 4, 5]

# Restricciones: diccionario que asigna a cada trabajador las tareas que no puede hacer
constraints = {
    'A': [1, 2],  # El trabajador A no puede hacer las tareas 1 ni 2
    'B': [3],     # El trabajador B no puede hacer la tarea 3
    'C': [4, 5],  # El trabajador C no puede hacer las tareas 4 ni 5
    'D': [],      # El trabajador D no tiene restricciones
    'E': [1, 5]   # El trabajador E no puede hacer las tareas 1 ni 5
}

# Generar una asignación aleatoria inicial para cada trabajador
assignments = {worker: random.choice(tasks) for worker in workers}

print("Asignaciones iniciales:")
print_assignments(assignments)  # Imprimir las asignaciones iniciales

# Intentar resolver el problema utilizando el algoritmo de Mínimos-Conflictos
if min_conflicts(assignments, workers, tasks, constraints):
    # Si se encuentra una solución, imprimir el resultado
    print("Asignaciones resueltas sin conflictos:")
    print_assignments(assignments)
else:
    # Si no se encuentra solución, informarlo
    print("No se pudo encontrar una solución en el máximo número de pasos.")
