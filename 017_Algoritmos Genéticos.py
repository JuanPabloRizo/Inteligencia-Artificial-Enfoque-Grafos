import random

# Función objetivo: queremos maximizar f(x) = x^2
def fitness(individual):
    x = int("".join(map(str, individual)), 2)  # Convertir de binario a entero
    return x ** 2

# Crear un individuo aleatorio (cromosoma de 5 bits)
def create_individual():
    return [random.randint(0, 1) for _ in range(5)]

# Crear una población de individuos
def create_population(size):
    return [create_individual() for _ in range(size)]

# Selección por torneo: selecciona dos individuos y elige el mejor
def tournament_selection(population):
    i, j = random.sample(range(len(population)), 2)
    return population[i] if fitness(population[i]) > fitness(population[j]) else population[j]

# Cruza (crossover) entre dos individuos
def crossover(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)  # Punto de cruce
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

# Mutación: cambiar un bit aleatorio en el cromosoma
def mutate(individual, mutation_rate=0.01):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Cambiar de 0 a 1 o de 1 a 0

# Algoritmo Genético
def genetic_algorithm(pop_size, generations, mutation_rate):
    population = create_population(pop_size)
    
    for generation in range(generations):
        new_population = []
        
        # Crear la nueva generación
        while len(new_population) < pop_size:
            # Selección
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            
            # Cruce
            child1, child2 = crossover(parent1, parent2)
            
            # Mutación
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            
            # Añadir a la nueva población
            new_population.append(child1)
            new_population.append(child2)
        
        # Reemplazar la población con la nueva generación
        population = new_population[:pop_size]
        
        # Mostrar el mejor individuo de la generación actual
        best_individual = max(population, key=fitness)
        best_value = int("".join(map(str, best_individual)), 2)
        print(f"Generación {generation + 1}: Mejor valor x = {best_value}, f(x) = {fitness(best_individual)}")
    
    # Devolver el mejor individuo encontrado
    best_individual = max(population, key=fitness)
    return best_individual

# Ejecutar el Algoritmo Genético
pop_size = 10  # Tamaño de la población
generations = 20  # Número de generaciones
mutation_rate = 0.01  # Tasa de mutación

best_individual = genetic_algorithm(pop_size, generations, mutation_rate)

# Mostrar la mejor solución final
best_value = int("".join(map(str, best_individual)), 2)
print(f"\nMejor solución final: x = {best_value}, f(x) = {best_value ** 2}")
