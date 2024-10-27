# Definimos las probabilidades a priori y condicionales
p_enfermedad = 0.01  # Probabilidad a priori de tener la enfermedad (1%)
p_prueba_positivo_enfermo = 0.99  # Probabilidad de que la prueba sea positiva si la persona está enferma
p_prueba_positivo_sano = 0.05  # Probabilidad de que la prueba sea positiva si la persona está sana
p_no_enfermedad = 1 - p_enfermedad  # Probabilidad de no tener la enfermedad

# Calculamos la probabilidad total de obtener un resultado positivo en la prueba
p_prueba_positivo = (p_prueba_positivo_enfermo * p_enfermedad) + (p_prueba_positivo_sano * p_no_enfermedad)

# Aplicamos el teorema de Bayes para calcular la probabilidad a posteriori de tener la enfermedad dado un resultado positivo
p_enfermedad_dado_prueba = (p_prueba_positivo_enfermo * p_enfermedad) / p_prueba_positivo

# Mostramos los resultados
print(f"La probabilidad a priori de tener la enfermedad es: {p_enfermedad:.2f}")
print(f"La probabilidad de tener la enfermedad dado un resultado positivo en la prueba es: {p_enfermedad_dado_prueba:.4f}")
""""
Probabilidad a priori (p_enfermedad): Representa nuestra creencia inicial sobre la prevalencia de la enfermedad en la población (1%).

Probabilidad condicional (p_prueba_positivo_enfermo y p_prueba_positivo_sano): Estas son las probabilidades de obtener un resultado positivo en la prueba dependiendo de si la persona está enferma o sana.

Probabilidad total de obtener un resultado positivo (p_prueba_positivo): Esta es la probabilidad de que una persona, sin importar si está enferma o no, obtenga un resultado positivo en la prueba.

Teorema de Bayes: Aplicamos la fórmula para actualizar nuestra probabilidad a priori, obteniendo la probabilidad de que la persona tenga la enfermedad dado que el resultado de la prueba es positivo (p_enfermedad_dado_prueba).
"""