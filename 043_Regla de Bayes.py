# Probabilidades conocidas
P_A = 0.01  # Probabilidad de tener la enfermedad (P(A))
P_not_A = 1 - P_A  # Probabilidad de no tener la enfermedad (P(~A))
P_B_given_A = 0.9  # Probabilidad de que el test sea positivo dado que tiene la enfermedad (P(B|A))
P_B_given_not_A = 0.05  # Probabilidad de que el test sea positivo dado que no tiene la enfermedad (P(B|~A))

# Aplicar la Regla de Bayes
# Primero calculamos P(B)
P_B = (P_B_given_A * P_A) + (P_B_given_not_A * P_not_A)

# Ahora calculamos P(A|B), que es lo que queremos
P_A_given_B = (P_B_given_A * P_A) / P_B

# Imprimir el resultado
print(f"La probabilidad de tener la enfermedad dado un test positivo es: {P_A_given_B:.4f}")

"""
Definir las probabilidades:
P(A): La probabilidad de que una persona tenga la enfermedad (1%).
P(B∣A): La probabilidad de que el test sea positivo si la persona tiene la enfermedad (90%).
P(B∣¬A): La probabilidad de que el test sea positivo si la persona no tiene la enfermedad (5%).
Calcular P(B): Para aplicar la Regla de Bayes, necesitamos primero calcular la probabilidad total de que el test sea positivo 
P(B), que incluye los casos donde la persona tiene y no tiene la enfermedad:
P(B)=P(B∣A)⋅P(A)+P(B∣¬A)⋅P(¬A)
Aplicar la Regla de Bayes: Ahora que conocemos P(B), podemos calcular 
la probabilidad de que la persona tenga la enfermedad dado que el test es 
positivo P(A∣B).
Resultado: Finalmente, imprimimos el valor calculado de 
P(A∣B), que nos da la probabilidad actualizada.
Resultado:La probabilidad de que una persona tenga la enfermedad, 
dado que su test resultó positivo, será mucho menor que 90%, 
porque la Regla de Bayes tiene en cuenta tanto la precisión del test 
como la baja probabilidad de que alguien tenga la enfermedad en 
primer lugar.
"""