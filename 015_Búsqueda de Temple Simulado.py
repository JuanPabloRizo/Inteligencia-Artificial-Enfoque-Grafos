import math
import random

# Función objetivo (heurística) que queremos minimizar
def objective_function(x):
    return x**2 + 4*math.sin(5*x)

# Generar un vecino cercano al estado actual (por ejemplo, agregar un pequeño valor aleatorio)
def get_neighbor(x):
    return x + random.uniform(-1, 1)  # Cambiar aleatoriamente el estado actual

# Implementar la Búsqueda de Temple Simulado
def simulated_annealing(start_state, initial_temperature, cooling_rate, max_iterations):
    # Estado inicial
    current_state = start_state
    current_energy = objective_function(current_state)
    
    best_state = current_state
    best_energy = current_energy
    
    temperature = initial_temperature
    
    for iteration in range(max_iterations):
        # Obtener un vecino cercano
        neighbor = get_neighbor(current_state)
        neighbor_energy = objective_function(neighbor)
        
        # Calcular la diferencia de energía entre el estado vecino y el estado actual
        energy_difference = neighbor_energy - current_energy
        
        # Decidir si aceptamos el estado vecino
        if energy_difference < 0:  # Si es una mejor solución, siempre la aceptamos
            current_state = neighbor
            current_energy = neighbor_energy
        else:
            # Si no es una mejor solución, la aceptamos con una probabilidad que depende de la temperatura
            acceptance_probability = math.exp(-energy_difference / temperature)
            if random.random() < acceptance_probability:
                current_state = neighbor
                current_energy = neighbor_energy
        
        # Actualizar el mejor estado encontrado
        if current_energy < best_energy:
            best_state = current_state
            best_energy = current_energy
        
        # Reducir la temperatura
        temperature *= cooling_rate
        
        # Imprimir el progreso
        print(f"Iteración {iteration}: Estado = {current_state}, Energía = {current_energy}, Temperatura = {temperature}")
    
    return best_state, best_energy

# Parámetros iniciales
start_state = random.uniform(-10, 10)  # Estado inicial aleatorio entre -10 y 10
initial_temperature = 1000             # Temperatura inicial
cooling_rate = 0.95                    # Tasa de enfriamiento (debe ser menor a 1)
max_iterations = 100                   # Número máximo de iteraciones

# Ejecutar la Búsqueda de Temple Simulado
best_state, best_energy = simulated_annealing(start_state, initial_temperature, cooling_rate, max_iterations)

print(f"Mejor estado encontrado: {best_state} con energía: {best_energy}")
