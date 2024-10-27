# Definimos las probabilidades condicionales
P_trafico_dado_lluvia = {
    True: 0.7,   # Probabilidad de tráfico dado que hay lluvia
    False: 0.2   # Probabilidad de no tráfico dado que hay lluvia
}

P_trafico_dado_no_lluvia = {
    True: 0.3,   # Probabilidad de tráfico dado que no hay lluvia
    False: 0.8   # Probabilidad de no tráfico dado que no hay lluvia
}

P_lluvia = 0.5  # Probabilidad de lluvia

def eliminacion_de_variables():
    """Calcula la probabilidad de tráfico dado que ha llovido usando eliminación de variables."""
    
    # Inicializamos la probabilidad total de tráfico
    P_trafico = 0

    # Iterar sobre los posibles estados de la variable Lluvia (True o False)
    for lluvia in [True, False]:
        # Calcular la probabilidad de tráfico para cada estado de lluvia
        if lluvia:  # Si está lloviendo
            prob_trafico = P_lluvia * P_trafico_dado_lluvia[True]  # P(Lluvia) * P(Tráfico | Lluvia)
        else:  # Si no está lloviendo
            prob_trafico = (1 - P_lluvia) * P_trafico_dado_no_lluvia[True]  # P(No Lluvia) * P(Tráfico | No Lluvia)
        
        # Acumular la probabilidad total de tráfico
        P_trafico += prob_trafico

    return P_trafico

# Realizamos la eliminación de variables
probabilidad_trafico = eliminacion_de_variables()
print(f'La probabilidad de que haya tráfico es: {probabilidad_trafico:.2f}')
"""
Definición de Probabilidades:

Se definen las probabilidades condicionales de tráfico dado que hay lluvia o no, junto con la probabilidad de que llueva.
Función eliminacion_de_variables:

Se inicializa la variable P_trafico para acumular la probabilidad total de tráfico.
Se itera sobre los posibles estados de la variable Lluvia (True o False).
Para cada estado de lluvia, se calcula la probabilidad de tráfico correspondiente, multiplicando la probabilidad de lluvia (o no lluvia) por la probabilidad de tráfico dado el estado de lluvia.
Se acumula la probabilidad en P_trafico.
Resultado:

Se imprime la probabilidad calculada de que haya tráfico.
Este resultado indica que hay un 50% de probabilidad de que haya tráfico, 
según las probabilidades definidas en el modelo.
"""