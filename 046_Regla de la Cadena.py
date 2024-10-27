# Importamos la librería random para simular eventos aleatorios
import random

# Definimos las probabilidades de los eventos
def probability_raining():
    """Devuelve la probabilidad de que esté lloviendo."""
    return 0.4  # 40% de probabilidad de que esté lloviendo

def probability_umbrella_given_rain():
    """Devuelve la probabilidad de llevar un paraguas dado que está lloviendo."""
    return 0.9  # 90% de probabilidad de llevar paraguas si llueve

def probability_getting_wet_given_rain_and_umbrella():
    """Devuelve la probabilidad de mojarse dado que está lloviendo y lleva paraguas."""
    return 0.1  # 10% de probabilidad de mojarse si llueve y lleva paraguas

def probability_getting_wet_given_rain_and_no_umbrella():
    """Devuelve la probabilidad de mojarse dado que está lloviendo y no lleva paraguas."""
    return 0.8  # 80% de probabilidad de mojarse si llueve y no lleva paraguas

def calculate_joint_probability():
    """Calcula la probabilidad conjunta de que esté lloviendo, se lleve paraguas y se moje."""
    # Primero, determinamos si está lloviendo
    if random.random() < probability_raining():  # Si llueve
        raining = True
    else:
        raining = False

    # Si está lloviendo, determinamos si se lleva un paraguas
    if raining:
        if random.random() < probability_umbrella_given_rain():  # Lleva paraguas
            umbrella = True
        else:  # No lleva paraguas
            umbrella = False
    else:
        umbrella = False  # Si no llueve, no es necesario el paraguas

    # Ahora, determinamos si se moja
    if raining and umbrella:
        wet = True if random.random() < probability_getting_wet_given_rain_and_umbrella() else False
    elif raining and not umbrella:
        wet = True if random.random() < probability_getting_wet_given_rain_and_no_umbrella() else False
    else:
        wet = False  # Si no llueve, no se moja

    # Calculamos la probabilidad conjunta utilizando la regla de la cadena
    joint_probability = (probability_raining() * 
                         probability_umbrella_given_rain() * 
                         probability_getting_wet_given_rain_and_umbrella())
    
    return raining, umbrella, wet, joint_probability

# Simulamos el evento y mostramos los resultados
raining, umbrella, wet, joint_probability = calculate_joint_probability()

print(f"¿Está lloviendo? {'Sí' if raining else 'No'}")
print(f"¿Lleva un paraguas? {'Sí' if umbrella else 'No'}")
print(f"¿Está mojado? {'Sí' if wet else 'No'}")
print(f"Probabilidad conjunta de que esté lloviendo, se lleve paraguas y se moje: {joint_probability:.2f}")
"""
Definición de Probabilidades:
Cada función devuelve una probabilidad específica para los eventos. 
Estas probabilidades se basan en supuestos razonables:
P(A): 40% de probabilidad de que esté lloviendo.
P(B∣A): 90% de probabilidad de que lleve un paraguas si está lloviendo.
P(C∣A,B): 10% de probabilidad de mojarse si está lloviendo y lleva paraguas. 
P(C∣A,¬B): 80% de probabilidad de mojarse si está lloviendo y no lleva paraguas.
Simulación de Eventos:

La función calculate_joint_probability simula si está lloviendo, si se lleva un paraguas y si se moja:
Se determina primero si está lloviendo.
Si está lloviendo, se determina si lleva un paraguas.
Luego, se determina si se moja basándose en si está lloviendo y si lleva un paraguas.
Cálculo de Probabilidad Conjunta:

Se calcula la probabilidad conjunta utilizando la regla de la cadena, que en este caso es la probabilidad de que esté lloviendo, se lleve paraguas y se moje.
Impresión de Resultados:

Finalmente, el código imprime si está lloviendo, si lleva un paraguas, si está mojado y la probabilidad conjunta calculada.
"""