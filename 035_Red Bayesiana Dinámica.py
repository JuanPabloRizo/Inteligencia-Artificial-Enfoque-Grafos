import random

# 1. Definimos las probabilidades iniciales
# Probabilidad de que llueva en el tiempo T1
p_lluvia_t1 = 0.3  # 30% de probabilidad de lluvia en T1

# Probabilidades de accidente dado lluvia en T1
p_accidente_t1_lluvia = 0.6  # 60% de probabilidad de accidente si llueve
p_accidente_t1_no_lluvia = 0.1  # 10% de probabilidad de accidente si no llueve

# 2. Función para simular el primer tiempo (T1)
def simular_t1():
    # Determinamos si llueve en T1
    lluvia_t1 = 1 if random.random() < p_lluvia_t1 else 0  # 1 representa lluvia, 0 representa no lluvia
    
    # Determinamos si hay un accidente basado en el estado de lluvia
    if lluvia_t1 == 1:
        # Si llueve, usamos la probabilidad de accidente dado que llueve
        accidente_t1 = 1 if random.random() < p_accidente_t1_lluvia else 0
    else:
        # Si no llueve, usamos la probabilidad de accidente dado que no llueve
        accidente_t1 = 1 if random.random() < p_accidente_t1_no_lluvia else 0

    return lluvia_t1, accidente_t1  # Retornamos el estado de lluvia y el accidente en T1

# 3. Probabilidades de lluvia en T2 basado en T1
# Asumimos que la lluvia en T1 afecta la probabilidad de lluvia en T2
def probabilidad_lluvia_t2(lluvia_t1):
    if lluvia_t1 == 1:
        return 0.5  # 50% de probabilidad de lluvia en T2 si llovió en T1
    else:
        return 0.2  # 20% de probabilidad de lluvia en T2 si no llovió en T1

# 4. Función para simular el segundo tiempo (T2)
def simular_t2(lluvia_t1):
    # Calculamos la probabilidad de lluvia en T2 basada en el resultado de T1
    p_lluvia_t2 = probabilidad_lluvia_t2(lluvia_t1)
    
    # Determinamos si llueve en T2 usando la probabilidad calculada
    lluvia_t2 = 1 if random.random() < p_lluvia_t2 else 0  # 1 para lluvia, 0 para no lluvia

    # Determinamos si hay un accidente basado en el estado de lluvia en T2
    if lluvia_t2 == 1:
        # Si llueve en T2, usamos la misma probabilidad de accidente que en T1
        accidente_t2 = 1 if random.random() < p_accidente_t1_lluvia else 0
    else:
        # Si no llueve en T2, usamos la probabilidad de accidente dada la ausencia de lluvia
        accidente_t2 = 1 if random.random() < p_accidente_t1_no_lluvia else 0

    return lluvia_t2, accidente_t2  # Retornamos el estado de lluvia y el accidente en T2

# 5. Simular un ciclo de dos tiempos
def simular_dbn():
    # Simulación para el primer tiempo (T1)
    lluvia_t1, accidente_t1 = simular_t1()  # Llamamos a la función para T1
    print(f"T1: Lluvia = {lluvia_t1}, Accidente = {accidente_t1}")  # Imprimimos los resultados de T1

    # Simulación para el segundo tiempo (T2) basada en el resultado de T1
    lluvia_t2, accidente_t2 = simular_t2(lluvia_t1)  # Llamamos a la función para T2
    print(f"T2: Lluvia = {lluvia_t2}, Accidente = {accidente_t2}")  # Imprimimos los resultados de T2

# 6. Ejecutar la simulación
simular_dbn()  # Llamamos a la función principal para iniciar la simulación
"""se obtendra una salida que indica si llovió y si hubo un accidente en 
T1 y T2. Como el proceso es aleatorio, cada ejecución puede generar 
diferentes resultados.
"""