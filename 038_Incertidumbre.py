# Importar librerías necesarias
import numpy as np

# Definición de probabilidades conocidas:
p_enfermedad = 0.01  # Probabilidad de tener la enfermedad (1% de la población)
p_prueba_positivo_enfermo = 0.99  # Probabilidad de que la prueba sea positiva si la persona está enferma
p_prueba_positivo_sano = 0.01  # Probabilidad de que la prueba sea positiva si la persona está sana
p_no_enfermedad = 1 - p_enfermedad  # Probabilidad de no tener la enfermedad

# Aplicación del Teorema de Bayes:
# Calculamos la probabilidad de obtener un resultado positivo de la prueba, sin importar si la persona está enferma o no:
p_prueba_positivo = (p_prueba_positivo_enfermo * p_enfermedad) + (p_prueba_positivo_sano * p_no_enfermedad)

# Ahora aplicamos el Teorema de Bayes para calcular la probabilidad de que la persona tenga la enfermedad dado que la prueba es positiva:
p_enfermedad_dado_prueba = (p_prueba_positivo_enfermo * p_enfermedad) / p_prueba_positivo

# Resultados
print(f"La probabilidad de tener la enfermedad dado que la prueba es positiva es: {p_enfermedad_dado_prueba:.4f}")

# Explicación adicional
print(f"Esta probabilidad es relativamente baja debido a la rareza de la enfermedad en la población, "
      f"a pesar de que la prueba tiene una alta precisión.")
"""
Probabilidades conocidas: p_enfermedad: Es la probabilidad previa de que una persona tenga la enfermedad, que es del 1% en nuestro caso. 
p_prueba_positivo_enfermo: Es la probabilidad de que la prueba sea positiva si la persona está enferma (99%). 
p_prueba_positivo_sano: Es la probabilidad de obtener un falso positivo, es decir, que la prueba sea positiva si la persona está sana (1%). 
Teorema de Bayes: Queremos calcular la probabilidad de que una persona tenga la enfermedad dado que la prueba fue positiva, es decir, 
P ( Enfermedad ∣ Prueba positiva ) P(Enfermedad∣Prueba positiva). 
Para hacerlo, primero calculamos la probabilidad general de que la prueba sea positiva, sin importar si la persona está enferma o no: 
P ( Prueba positiva ) = P ( Prueba positiva ∣ Enfermedad ) ⋅ P ( Enfermedad ) + P ( Prueba positiva ∣ No enfermedad ) ⋅ P ( No enfermedad ) P(Prueba positiva)=P(Prueba positiva∣Enfermedad)⋅P(Enfermedad)+P(Prueba positiva∣No enfermedad)⋅P(No enfermedad) 
Luego aplicamos la fórmula de Bayes para calcular la probabilidad actualizada:
"""