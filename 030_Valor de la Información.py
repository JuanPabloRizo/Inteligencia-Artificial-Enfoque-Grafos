import numpy as np

# Probabilidad de que llueva (sin información adicional)
prob_lluvia = 0.3  # Probabilidad de lluvia 30%

# Decisiones posibles
decisiones = ['Tomar paraguas', 'No tomar paraguas']

# Función de utilidad
def utilidad(decision, llueve):
    """
    Calcula la utilidad basada en la decisión y si llueve o no.
    """
    if decision == 'Tomar paraguas':
        if llueve:
            return 10  # Utilidad alta por estar seco
        else:
            return 5   # Menor utilidad porque no llueve, pero llevas paraguas
    else:  # Decisión: No tomar paraguas
        if llueve:
            return -20  # Baja utilidad por mojarse
        else:
            return 0  # Neutro: No llevas paraguas y no lo necesitas

# Función para calcular la utilidad esperada sin información
def utilidad_esperada_sin_informacion(prob_lluvia):
    """
    Calcula la utilidad esperada sin tener información adicional.
    """
    utilidad_tomar_paraguas = (prob_lluvia * utilidad('Tomar paraguas', True)) + \
                              ((1 - prob_lluvia) * utilidad('Tomar paraguas', False))
    utilidad_no_tomar_paraguas = (prob_lluvia * utilidad('No tomar paraguas', True)) + \
                                 ((1 - prob_lluvia) * utilidad('No tomar paraguas', False))
    
    # Retorna la mayor utilidad esperada (la mejor decisión)
    return max(utilidad_tomar_paraguas, utilidad_no_tomar_paraguas)

# Función para calcular la utilidad esperada con información perfecta
def utilidad_esperada_con_informacion_perfecta(prob_lluvia):
    """
    Calcula la utilidad esperada suponiendo que tenemos información perfecta.
    """
    # Si llueve, la mejor decisión es tomar paraguas
    utilidad_si_llueve = prob_lluvia * utilidad('Tomar paraguas', True)
    
    # Si no llueve, la mejor decisión es no tomar paraguas
    utilidad_si_no_llueve = (1 - prob_lluvia) * utilidad('No tomar paraguas', False)
    
    # Suma de utilidades con información perfecta
    return utilidad_si_llueve + utilidad_si_no_llueve

# Calcular utilidades
utilidad_sin_info = utilidad_esperada_sin_informacion(prob_lluvia)
utilidad_con_info = utilidad_esperada_con_informacion_perfecta(prob_lluvia)

# Calcular el valor de la información
valor_informacion = utilidad_con_info - utilidad_sin_info

# Mostrar resultados
print(f"Utilidad esperada sin información: {utilidad_sin_info}")
print(f"Utilidad esperada con información perfecta: {utilidad_con_info}")
print(f"Valor de la información perfecta (VOI): {valor_informacion}")
