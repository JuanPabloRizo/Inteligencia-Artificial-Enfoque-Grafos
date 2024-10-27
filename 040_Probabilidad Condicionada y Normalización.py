import numpy as np

# Definimos las probabilidades iniciales (no normalizadas) para tres eventos
P_A = 2
P_B = 3
P_C = 5

# Calculamos la suma total (antes de la normalización)
suma_total = P_A + P_B + P_C

# Normalizamos las probabilidades para que sumen 1
P_A_normalizado = P_A / suma_total
P_B_normalizado = P_B / suma_total
P_C_normalizado = P_C / suma_total

# Mostramos las probabilidades normalizadas
print(f"Probabilidad normalizada de A: {P_A_normalizado:.2f}")
print(f"Probabilidad normalizada de B: {P_B_normalizado:.2f}")
print(f"Probabilidad normalizada de C: {P_C_normalizado:.2f}")

# Ahora supongamos que ocurre el evento B, y queremos calcular la probabilidad condicionada de A dado B
# Usando el Teorema de Bayes: P(A|B) = P(A ∩ B) / P(B)

# Definimos la probabilidad conjunta de A y B
P_A_y_B = 0.1  # Suponiendo que P(A ∩ B) es 0.1

# Calculamos la probabilidad condicionada de A dado B
P_A_dado_B = P_A_y_B / P_B_normalizado

# Mostramos la probabilidad condicionada
print(f"Probabilidad condicionada de A dado B: {P_A_dado_B:.2f}")
 
"""
 Probabilidades iniciales: Definimos las probabilidades iniciales para tres eventos 
A, B, y C, que no están normalizadas.
Normalización: Sumamos las probabilidades y luego dividimos cada una por la suma total 
para obtener probabilidades normalizadas.
Probabilidad condicionada: Calculamos la probabilidad de que ocurra 
A dado que sabemos que ocurrió B. Usamos una probabilidad conjunta 
P(A∩B) para aplicar el Teorema de Bayes y obtener P(A∣B).
 """