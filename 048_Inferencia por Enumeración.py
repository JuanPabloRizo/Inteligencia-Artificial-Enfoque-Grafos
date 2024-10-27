# Definimos las probabilidades condicionales
# P(Tráfico | Lluvia)
P_trafico_dado_lluvia = {
    True: 0.7,   # Probabilidad de tráfico dado que hay lluvia
    False: 0.2   # Probabilidad de no tráfico dado que hay lluvia
}

# P(Tráfico | No Lluvia)
P_trafico_dado_no_lluvia = {
    True: 0.3,   # Probabilidad de tráfico dado que no hay lluvia
    False: 0.8   # Probabilidad de no tráfico dado que no hay lluvia
}

# P(Lluvia)
P_lluvia = 0.5  # Probabilidad de lluvia

def inferencia_por_enumeracion():
    """Realiza inferencia por enumeración para calcular la probabilidad de tráfico dado lluvia."""
    
    # Calculamos P(Tráfico)
    P_trafico = 0

    # Iterar sobre los posibles estados de lluvia (True o False)
    for lluvia in [True, False]:
        # Calculamos la probabilidad de tráfico para cada caso
        if lluvia:  # Si está lloviendo
            P_trafico += P_lluvia * P_trafico_dado_lluvia[True]  # P(Lluvia) * P(Tráfico | Lluvia)
        else:  # Si no está lloviendo
            P_trafico += (1 - P_lluvia) * P_trafico_dado_no_lluvia[True]  # P(No Lluvia) * P(Tráfico | No Lluvia)

    return P_trafico

# Realizamos la inferencia
probabilidad_trafico = inferencia_por_enumeracion()
print(f'La probabilidad de que haya tráfico dado que ha llovido es: {probabilidad_trafico:.2f}')
"""
Definición de Probabilidades:

Se definen las probabilidades condicionales de que haya tráfico dado si está lloviendo o no, junto con la probabilidad de que llueva.
Función inferencia_por_enumeracion:

Se inicializa una variable P_trafico para acumular la probabilidad total de tráfico.
Se itera sobre los posibles estados de la variable Lluvia (True o False).
Para cada estado de lluvia, se calcula la contribución a la probabilidad de tráfico y se acumula en P_trafico.
Resultado:

Se imprime la probabilidad calculada de que haya tráfico dado que ha llovido.
Este resultado indica que hay un 50% de probabilidad de que haya tráfico dado que 
ha llovido, según las probabilidades definidas en el modelo.
"""
