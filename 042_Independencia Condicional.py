import numpy as np

# Definir los posibles valores de las variables
# A, B, y C pueden tomar valores 0 o 1 (binarios)

# Generar los valores para C de manera aleatoria
C = np.random.randint(0, 2, 1000)

# Si conocemos C, entonces A y B no están directamente relacionadas
# Generar A y B basados en C de manera condicional
A = np.array([np.random.choice([0, 1], p=[0.7, 0.3]) if c == 0 else np.random.choice([0, 1], p=[0.4, 0.6]) for c in C])
B = np.array([np.random.choice([0, 1], p=[0.6, 0.4]) if c == 0 else np.random.choice([0, 1], p=[0.3, 0.7]) for c in C])

# Verificar la independencia condicional
# Comparamos la correlación de A y B cuando conocemos C (es decir, por cada valor de C)

# Para C = 0
A_given_C0 = A[C == 0]
B_given_C0 = B[C == 0]
correlacion_C0 = np.corrcoef(A_given_C0, B_given_C0)[0, 1]

# Para C = 1
A_given_C1 = A[C == 1]
B_given_C1 = B[C == 1]
correlacion_C1 = np.corrcoef(A_given_C1, B_given_C1)[0, 1]

print(f"Correlación entre A y B dado C = 0: {correlacion_C0}")
print(f"Correlación entre A y B dado C = 1: {correlacion_C1}")

"""
Definir Variables: Generamos 1000 valores binarios aleatorios para las variables 
A, B y C. Aquí A y B dependen de C.
Condicionalidad: A y B se generan basados en C, pero no tienen una relación directa entre sí.
Por ejemplo, cuando C=0, la probabilidad de que A=1 es mayor, pero lo mismo ocurre con 
B, sin que una dependa de la otra.
Correlación: Calculamos la correlación de A y B para cada valor de 
C. Si son condicionalmente independientes, la correlación entre A y 
B debe ser baja para cada valor de C, lo que indica que no tienen 
relación directa una vez que C es conocido.
"""