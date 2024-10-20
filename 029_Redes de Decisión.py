import numpy as np

# Probabilidades (nodos de probabilidad)
# Probabilidad de que llueva (P(lluvia))
prob_lluvia = 0.3  # Hay un 30% de probabilidad de que llueva

# Decisiones posibles (nodos de decisión)
decisiones = ['Tomar paraguas', 'No tomar paraguas']

# Función que calcula la utilidad
# Esta función depende de la decisión y del estado del tiempo (lluvia o no)
def utilidad(decision, llueve):
    if decision == 'Tomar paraguas':
        if llueve:
            return 10  # Alta utilidad por estar seco
        else:
            return 5   # Utilidad menor porque no llueve pero llevas paraguas
    else:  # Decisión: No tomar paraguas
        if llueve:
            return -20  # Muy baja utilidad por mojarse
        else:
            return 0  # Neutral: No llueve y no llevas paraguas

# Función para calcular la utilidad esperada de una decisión
def utilidad_esperada(decision, prob_lluvia):
    # Calcular la utilidad cuando llueve y cuando no llueve
    utilidad_con_lluvia = utilidad(decision, True)  # Utilidad si llueve
    utilidad_sin_lluvia = utilidad(decision, False) # Utilidad si no llueve

    # Utilidad esperada (usando probabilidad)
    # UE(decision) = P(lluvia) * U(lluvia) + P(no llueve) * U(no llueve)
    utilidad_total = (prob_lluvia * utilidad_con_lluvia) + \
                     ((1 - prob_lluvia) * utilidad_sin_lluvia)

    return utilidad_total

# Evaluar la utilidad esperada para cada decisión
utilidad_paraguas = utilidad_esperada('Tomar paraguas', prob_lluvia)
utilidad_no_paraguas = utilidad_esperada('No tomar paraguas', prob_lluvia)

# Mostrar los resultados de la utilidad esperada
print(f"Utilidad esperada al tomar el paraguas: {utilidad_paraguas}")
print(f"Utilidad esperada al no tomar el paraguas: {utilidad_no_paraguas}")

# Decidir la mejor opción basada en la utilidad esperada
if utilidad_paraguas > utilidad_no_paraguas:
    print("La mejor decisión es: Tomar el paraguas")
else:
    print("La mejor decisión es: No tomar el paraguas")
