import random
"""
Vamos a implementar una red bayesiana que considera las siguientes variables:
A: Preparación (1 si está preparado, 0 si no)
B: Nervios (1 si está nervioso, 0 si no)
C: Aprobar (1 si aprueba, 0 si no)
Probabilidades
Supongamos las siguientes probabilidades:
Probabilidades de Preparación y Nervios:
P(A=1)=0.6 (probabilidad de estar preparado)
P(A=0)=0.4 (probabilidad de no estar preparado)
P(B=1)=0.3 (probabilidad de estar nervioso)
P(B=0)=0.7 (probabilidad de no estar nervioso)
Probabilidades de Aprobar (C) Dadas A y B:
P(C=1∣A=1,B=0)=0.9
P(C=1∣A=1,B=1)=0.7
P(C=1∣A=0,B=0)=0.8
P(C=1∣A=0,B=1)=0.4
"""
# Definimos las probabilidades
def probability_preparation():
    """Devuelve si el estudiante está preparado o no."""
    return 1 if random.random() < 0.6 else 0  # 60% preparado, 40% no preparado

def probability_nervous():
    """Devuelve si el estudiante está nervioso o no."""
    return 1 if random.random() < 0.3 else 0  # 30% nervioso, 70% no nervioso

def probability_pass(a, b):
    """Devuelve la probabilidad de aprobar basado en preparación (A) y nervios (B)."""
    if a == 1 and b == 0:
        return 0.9  # Preparado y no nervioso
    elif a == 1 and b == 1:
        return 0.7  # Preparado y nervioso
    elif a == 0 and b == 0:
        return 0.8  # No preparado y no nervioso
    elif a == 0 and b == 1:
        return 0.4  # No preparado y nervioso

def simulate_exam():
    """Simula el examen y devuelve si se aprueba o no."""
    # Determinar si el estudiante está preparado y nervioso
    a = probability_preparation()  # A: Preparación
    b = probability_nervous()       # B: Nervios

    # Obtener la probabilidad de aprobar
    pass_probability = probability_pass(a, b)

    # Decidir si aprueba o no basado en la probabilidad
    return 1 if random.random() < pass_probability else 0  # 1 = aprobar, 0 = no aprobar

# Simulamos el examen varias veces
num_trials = 1000
results = [simulate_exam() for _ in range(num_trials)]

# Calculamos la proporción de aprobados
pass_rate = sum(results) / num_trials
print(f"Tasa de aprobación en {num_trials} simulaciones: {pass_rate:.2f}")

"""
Probabilidades:
Las funciones probability_preparation y probability_nervous simulan si el estudiante está preparado y si está nervioso, respectivamente, usando un número aleatorio para determinar el estado basado en las probabilidades especificadas.
La función probability_pass toma en cuenta los estados de preparación y nervios para determinar la probabilidad de aprobar el examen.
Simulación del Examen:
La función simulate_exam simula un examen. Primero, determina si el estudiante está preparado y nervioso. Luego, usa la probabilidad calculada para decidir si aprueba el examen.
Ejecutar Simulaciones:
Ejecutamos múltiples simulaciones del examen (1,000 en este caso) y recopilamos los resultados. Al final, calculamos la tasa de aprobación.
Resultados:
La tasa de aprobación se imprime al final, mostrando cuántos estudiantes aprobaron el examen en función de las condiciones simuladas.
"""