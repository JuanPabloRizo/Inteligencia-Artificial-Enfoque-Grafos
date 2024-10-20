# 1. Definimos los pagos del juego de entrada al mercado
payoffs = {
    ('Entrar', 'Entrar'): (1, 1),      # Ambas empresas entran
    ('Entrar', 'No Entrar'): (5, 0),   # A entra, B no entra
    ('No Entrar', 'Entrar'): (0, 5),   # A no entra, B entra
    ('No Entrar', 'No Entrar'): (3, 3)  # Ambas no entran
}

# 2. Función para determinar el equilibrio de Nash
def equilibrio_de_nash():
    # Estrategias posibles
    estrategias = ['Entrar', 'No Entrar']
    nash_equilibrio = []  # Lista para almacenar los equilibrios de Nash encontrados

    # 3. Comprobamos cada combinación de estrategias posibles
    for estrategia_a in estrategias:  # Estrategia de la empresa A
        for estrategia_b in estrategias:  # Estrategia de la empresa B
            # Obtener los pagos para ambas estrategias
            pago_a, pago_b = payoffs[(estrategia_a, estrategia_b)]

            # 4. Determinamos si el jugador A tiene un incentivo para cambiar su estrategia
            # Para la empresa A, calcular su mejor opción
            mejor_pago_a = max(
                payoffs[('No Entrar', estrategia_b)][0],  # A evalúa no entrar
                payoffs[('Entrar', estrategia_b)][0]       # A evalúa entrar
            )
            
            # Para la empresa B, calcular su mejor opción
            mejor_pago_b = max(
                payoffs[(estrategia_a, 'No Entrar')][1],  # B evalúa no entrar
                payoffs[(estrategia_a, 'Entrar')][1]      # B evalúa entrar
            )  

            # Comprobamos si ninguno de los jugadores tiene incentivos para cambiar su estrategia
            # Equilibrio de Nash: nadie tiene incentivos para desviarse de su estrategia actual
            if (pago_a >= mejor_pago_a) and (pago_b >= mejor_pago_b):
                nash_equilibrio.append((estrategia_a, estrategia_b))  # Agregar el equilibrio a la lista

    return nash_equilibrio  # Retornamos la lista de equilibrios de Nash encontrados

# 5. Ejecutar la función y mostrar los resultados
nash = equilibrio_de_nash()  # Llamamos a la función para encontrar los equilibrios
if nash:  # Verificamos si se encontraron equilibrios
    print("Equilibrio de Nash encontrado:", nash)  # Imprimimos los resultados
else:
    print("No se encontraron equilibrios de Nash.")
