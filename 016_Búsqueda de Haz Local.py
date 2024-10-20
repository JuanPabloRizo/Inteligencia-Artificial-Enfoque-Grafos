import random

# Función objetivo que queremos minimizar
def objective_function(x):
    return x**2 + 10*random.random()  # Una función cuadrática con ruido aleatorio

# Genera sucesores para un estado dado
def generate_neighbors(x, num_neighbors=5):
    neighbors = []
    for _ in range(num_neighbors):
        # Generamos vecinos cercanos agregando un pequeño valor aleatorio a x
        neighbor = x + random.uniform(-1, 1)
        neighbors.append(neighbor)
    return neighbors

# Implementación de la Búsqueda de Haz Local
def local_beam_search(num_beams, max_iterations, num_neighbors):
    # Inicializar los haces con estados aleatorios
    beams = [random.uniform(-10, 10) for _ in range(num_beams)]
    
    for iteration in range(max_iterations):
        # Generar todos los sucesores para cada haz
        all_neighbors = []
        for beam in beams:
            all_neighbors.extend(generate_neighbors(beam, num_neighbors))

        # Seleccionar los mejores estados (los de menor valor de la función objetivo)
        all_neighbors.sort(key=lambda x: objective_function(x))
        beams = all_neighbors[:num_beams]  # Mantenemos solo los mejores haces
        
        # Mostrar el progreso
        print(f"Iteración {iteration+1}, Mejores haces: {beams}, Mejor valor objetivo: {objective_function(beams[0])}")
    
    # Devolver el mejor haz al final de la búsqueda
    best_beam = min(beams, key=lambda x: objective_function(x))
    return best_beam

# Parámetros de la búsqueda
num_beams = 3          # Número de haces (caminos) a mantener
max_iterations = 20    # Número máximo de iteraciones
num_neighbors = 5      # Número de vecinos generados para cada haz en cada iteración

# Ejecutar la Búsqueda de Haz Local
best_solution = local_beam_search(num_beams, max_iterations, num_neighbors)

print(f"\nMejor solución encontrada: {best_solution} con valor objetivo: {objective_function(best_solution)}")
