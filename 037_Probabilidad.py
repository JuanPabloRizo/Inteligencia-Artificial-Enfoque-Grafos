# Definimos el espacio de eventos posibles para un dado de 6 caras
espacio_muestral = [1, 2, 3, 4, 5, 6]

# Definimos el conjunto de eventos favorables (números mayores que 4)
eventos_favorables = [5, 6]

# Calculamos la probabilidad de que salga un número mayor que 4
probabilidad = len(eventos_favorables) / len(espacio_muestral)

print(f"La probabilidad de obtener un número mayor que 4 es: {probabilidad:.2f}")
"""
Espacio Muestral: Es el conjunto de todos los resultados posibles al lanzar el dado. En este caso es {1, 2, 3, 4, 5, 6}.
Eventos Favorables: Son los resultados que cumplen la condición que estamos buscando, es decir, aquellos mayores que 4 (los números 5 y 6).
Probabilidad: Se calcula dividiendo el número de eventos favorables entre el número total de posibles resultados.
"""