import numpy as np

# Definimos la función de utilidad que toma el valor de un estado o recompensa y lo transforma en utilidad.
def funcion_utilidad(recompensa):
    # En este ejemplo, asumimos que la función de utilidad tiene una forma logarítmica
    # Esto refleja el comportamiento típico en el que una recompensa adicional genera menos utilidad marginal
    return np.log(recompensa)

# Simulamos diferentes decisiones con sus posibles recompensas y probabilidades
# Cada decisión tiene una lista de recompensas y sus respectivas probabilidades
# Decisión A: Tiene la posibilidad de una recompensa baja y otra alta
decision_A = {
    'recompensas': [10, 50],  # Posibles recompensas: 10 y 50 unidades monetarias
    'probabilidades': [0.8, 0.2]  # Probabilidad de cada recompensa
}

# Decisión B: Tiene la posibilidad de una recompensa moderada y otra alta
decision_B = {
    'recompensas': [30, 40],  # Posibles recompensas: 30 y 40 unidades monetarias
    'probabilidades': [0.5, 0.5]  # Probabilidad de cada recompensa
}

# Función para calcular la utilidad esperada de una decisión
def utilidad_esperada(decision):
    utilidad_total = 0
    
    # Iteramos sobre cada recompensa y su probabilidad
    for recompensa, probabilidad in zip(decision['recompensas'], decision['probabilidades']):
        utilidad = funcion_utilidad(recompensa)  # Calculamos la utilidad de cada recompensa
        utilidad_total += probabilidad * utilidad  # La multiplicamos por su probabilidad y la sumamos
    
    return utilidad_total

# Calculamos la utilidad esperada para ambas decisiones
utilidad_A = utilidad_esperada(decision_A)
utilidad_B = utilidad_esperada(decision_B)

# Mostramos las utilidades esperadas
print(f"Utilidad esperada de la decisión A: {utilidad_A:.2f}")
print(f"Utilidad esperada de la decisión B: {utilidad_B:.2f}")

# El agente seleccionará la opción con la mayor utilidad esperada
if utilidad_A > utilidad_B:
    print("El agente elige la Decisión A.")
else:
    print("El agente elige la Decisión B.")
