from collections import deque

# Definimos el problema de satisfacción de restricciones como un CSP simple
# Variables con sus respectivos dominios
variables = {
    'X1': [1, 2, 3],
    'X2': [2, 3, 4],
    'X3': [1, 2]
}

# Restricciones entre las variables, en este caso, cada restricción es una función
# que retorna True si se cumple, de lo contrario, False.
constraints = {
    ('X1', 'X2'): lambda x1, x2: x1 < x2,  # Restricción: X1 < X2
    ('X2', 'X3'): lambda x2, x3: x2 != x3  # Restricción: X2 != X3
}

# Función para revisar si el arco (Xi, Xj) es consistente
def revise(variables, Xi, Xj, constraint):
    revised = False  # Bandera para marcar si hubo cambios en el dominio
    # Recorremos cada valor en el dominio de Xi
    for x in variables[Xi][:]:  # [:] para evitar modificar la lista durante la iteración
        # Si no hay ningún valor en el dominio de Xj que satisfaga la restricción con Xi
        if not any(constraint(x, y) for y in variables[Xj]):
            # Eliminamos el valor de Xi porque no es consistente
            variables[Xi].remove(x)
            revised = True
    return revised

# Algoritmo AC-3 para asegurar la consistencia de arcos
def ac3(variables, constraints):
    # Inicializamos la cola con todos los arcos (par de variables)
    queue = deque(constraints.keys())
    
    while queue:
        # Obtenemos el arco (Xi, Xj) desde la cola
        Xi, Xj = queue.popleft()
        
        # Revisamos si este arco es consistente
        if revise(variables, Xi, Xj, constraints[(Xi, Xj)]):
            # Si se revisó el dominio de Xi y se eliminó algún valor
            # Verificamos si el dominio de Xi quedó vacío (no hay solución posible)
            if not variables[Xi]:
                return False  # No hay solución posible
            
            # Si hubo cambios, agregamos todos los arcos que afecten a Xi de nuevo a la cola
            for Xk in [X for X in variables if X != Xi and (X, Xi) in constraints]:
                queue.append((Xk, Xi))
    
    # Si el algoritmo termina sin problemas, los dominios son consistentes
    return True

# Ejecutamos el algoritmo AC-3
if ac3(variables, constraints):
    print("Los dominios son consistentes después de aplicar AC-3:")
    for var, domain in variables.items():
        print(f"{var}: {domain}")
else:
    print("No hay solución posible.")

