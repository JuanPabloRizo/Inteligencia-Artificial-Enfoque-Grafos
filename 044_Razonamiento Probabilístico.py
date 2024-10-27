# Definimos las probabilidades a priori y condicionales
P_enfermo = 0.01  # Probabilidad de tener la enfermedad (P(A))
P_sano = 1 - P_enfermo  # Probabilidad de estar sano (P(~A))
P_positivo_dado_enfermo = 0.9  # Probabilidad de test positivo dado que está enfermo (P(B|A))
P_positivo_dado_sano = 0.05  # Probabilidad de test positivo dado que está sano (P(B|~A))

# Aplicar la Regla de Bayes
# Primero, calculamos P(B), la probabilidad de obtener un resultado positivo en general
P_positivo = (P_positivo_dado_enfermo * P_enfermo) + (P_positivo_dado_sano * P_sano)

# Ahora calculamos la probabilidad a posteriori de estar enfermo dado un resultado positivo (P(A|B))
P_enfermo_dado_positivo = (P_positivo_dado_enfermo * P_enfermo) / P_positivo

# Imprimir resultado
print(f"La probabilidad de estar enfermo dado un test positivo es: {P_enfermo_dado_positivo:.4f}")
"""
Probabilidades a priori:
P(enfermo)=0.01: 1% de la población tiene la enfermedad.
P(sano)=0.99: 99% de la población está sana.
Probabilidad condicional:
P(positivo∣enfermo)=0.9: El test tiene una precisión del 90% para personas enfermas.
P(positivo∣sano)=0.05: Hay un 5% de falsos positivos.
Aplicar la Regla de Bayes:
Calculamos P(positivo), que es la probabilidad de obtener un resultado 
positivo (tanto para personas enfermas como sanas).
Luego usamos la Regla de Bayes para calcular la probabilidad de estar enfermo dado un resultado positivo.
Resultado: Este cálculo arroja una probabilidad significativamente menor 
de lo que la precisión del test podría sugerir inicialmente. 
Aunque el test es bastante preciso, la baja probabilidad inicial de 
tener la enfermedad (solo el 1% de la población está enferma) hace que 
incluso con un test positivo, la probabilidad real de estar enfermo sea 
mucho menor.
"""