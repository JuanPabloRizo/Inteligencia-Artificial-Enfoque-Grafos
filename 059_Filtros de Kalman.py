import numpy as np

class FiltroKalman:
    def __init__(self, A, B, H, Q, R, P, x0):
        """
        Inicialización del filtro de Kalman.
        
        Parámetros:
        A - Matriz de transición de estado.
        B - Matriz de control.
        H - Matriz de observación.
        Q - Covarianza del ruido del proceso.
        R - Covarianza del ruido de observación.
        P - Matriz de covarianza inicial.
        x0 - Estado inicial.
        """
        self.A = A  # Matriz de transición del sistema
        self.B = B  # Matriz de control
        self.H = H  # Matriz de observación
        self.Q = Q  # Covarianza del proceso
        self.R = R  # Covarianza de las observaciones
        self.P = P  # Matriz de covarianza inicial
        self.x = x0  # Estado inicial

    def prediccion(self, u=0):
        """
        Predicción del siguiente estado usando la dinámica del sistema.
        
        Parámetros:
        u - Control (opcional).
        """
        # Predicción del estado
        self.x = np.dot(self.A, self.x) + np.dot(self.B, u)
        
        # Predicción de la covarianza del error
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q
        
        return self.x

    def correccion(self, z):
        """
        Corrección de la predicción basada en la nueva observación.
        
        Parámetros:
        z - Nueva observación.
        """
        # Ganancia de Kalman
        S = np.dot(np.dot(self.H, self.P), self.H.T) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        
        # Actualización del estado estimado
        y = z - np.dot(self.H, self.x)
        self.x = self.x + np.dot(K, y)
        
        # Actualización de la covarianza del error
        I = np.eye(self.P.shape[0])
        self.P = np.dot((I - np.dot(K, self.H)), self.P)
        
        return self.x

# Parámetros iniciales del sistema
A = np.array([[1, 1],  # Matriz de transición del estado
              [0, 1]])
B = np.array([[0.5],   # Matriz de control
              [1]])
H = np.array([[1, 0]])  # Matriz de observación
Q = np.array([[0.001, 0],   # Covarianza del proceso
              [0, 0.001]])
R = np.array([[0.1]])   # Covarianza de la observación
P = np.array([[1, 0],   # Matriz de covarianza inicial
              [0, 1]])
x0 = np.array([0, 1])   # Estado inicial: posición = 0, velocidad = 1

# Inicializar el filtro de Kalman
kf = FiltroKalman(A, B, H, Q, R, P, x0)

# Simulación de mediciones ruidosas de la posición
mediciones = [1.0, 2.2, 3.1, 3.9, 5.0]
estimaciones = []

# Iterar sobre las mediciones
for z in mediciones:
    # Predicción
    prediccion = kf.prediccion()
    print(f"Predicción del estado: {prediccion}")
    
    # Corrección basada en la observación
    estimacion = kf.correccion(np.array([z]))
    print(f"Estimación corregida: {estimacion}")
    estimaciones.append(estimacion)

print("\nEstimaciones finales:", estimaciones)
"""
Inicialización del filtro:
Creamos la matriz de transición del estado A, que modela cómo el estado 
evoluciona en el tiempo.
La matriz de control B modela cómo la entrada externa (control) afecta el sistema.
La matriz de observación H relaciona el estado con la observación.
Las matrices de covarianza Q y R representan el ruido en el proceso y las observaciones, respectivamente.
Predicción:
Utilizamos la dinámica del sistema para predecir el estado del sistema en el próximo paso de tiempo. Esta predicción se realiza antes de recibir una nueva observación.
Corrección:
Tras recibir una nueva observación, se ajusta la predicción del estado en función de esta 
observación, aplicando la ganancia de Kalman para corregir el estado estimado.
Salida:
Imprimimos tanto la predicción del estado antes de recibir la observación, 
como la estimación corregida después de aplicar la observación.
"""