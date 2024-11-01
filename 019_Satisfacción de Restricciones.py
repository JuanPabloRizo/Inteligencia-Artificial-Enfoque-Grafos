class CSP:
    def __init__(self, variables, dominios, restricciones):
        self.variables = variables  # Lista de variables
        self.dominios = dominios  # Diccionario que asigna un dominio a cada variable
        self.restricciones = restricciones  # Lista de restricciones

    def es_consistente(self, variable, valor, asignacion):
        # Verificar si el valor propuesto es consistente con las restricciones
        for (var1, var2) in self.restricciones:
            if var1 == variable and var2 in asignacion:
                if asignacion[var2] == valor:
                    return False
            elif var2 == variable and var1 in asignacion:
                if asignacion[var1] == valor:
                    return False
        return True

    def resolver(self, asignacion={}):
        # Si la asignación está completa, hemos encontrado una solución
        if len(asignacion) == len(self.variables):
            return asignacion

        # Seleccionar la siguiente variable que necesita una asignación
        variable = self.seleccionar_variable(asignacion)

        for valor in self.dominios[variable]:
            # Comprobar si la asignación es consistente
            if self.es_consistente(variable, valor, asignacion):
                # Asignar valor a la variable
                asignacion[variable] = valor

                # Recursivamente resolver el resto
                resultado = self.resolver(asignacion)
                if resultado:
                    return resultado

                # Si no hay solución, eliminar la asignación (backtracking)
                del asignacion[variable]

        return None  # No se encontró solución

    def seleccionar_variable(self, asignacion):
        # Seleccionar la siguiente variable sin asignar
        for variable in self.variables:
            if variable not in asignacion:
                return variable
        return None

# Ejemplo de uso
if __name__ == "__main__":
    # Definir variables, dominios y restricciones para un grafo
    variables = ['A', 'B', 'C', 'D']  # Nodos del grafo
    dominios = {
        'A': ['Rojo', 'Verde', 'Azul'],
        'B': ['Rojo', 'Verde', 'Azul'],
        'C': ['Rojo', 'Verde', 'Azul'],
        'D': ['Rojo', 'Verde', 'Azul']
    }
    
    # Definir las restricciones (nodos adyacentes no pueden tener el mismo color)
    restricciones = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'C'),
        ('B', 'D'),
        ('C', 'D')
    ]

    # Crear el CSP
    problema = CSP(variables, dominios, restricciones)

    # Resolver el problema
    solucion = problema.resolver()

    if solucion:
        print("Solución encontrada:")
        for variable, valor in solucion.items():
            print(f"{variable}: {valor}")
    else:
        print("No se encontró solución.")
"""
Clase CSP:

Almacena las variables, dominios y restricciones del problema.
El método es_consistente verifica si la asignación de un valor a una variable es consistente con las restricciones del problema.
El método resolver utiliza un enfoque de backtracking para encontrar una solución. Si encuentra una solución completa, la devuelve. De lo contrario, prueba diferentes asignaciones hasta encontrar una que funcione o hasta que se determine que no hay solución.
El método seleccionar_variable selecciona la siguiente variable que necesita ser asignada.
Ejemplo de Uso:

Define un conjunto de variables (nodos del grafo), sus dominios (colores) y las restricciones (nodos adyacentes).
Crea una instancia de CSP y llama al método resolver para encontrar una asignación de colores válida.
"""