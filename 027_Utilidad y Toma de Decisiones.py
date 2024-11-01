class Decision:
    def __init__(self, opciones):
        """
        Inicializa la clase de decisión con las opciones disponibles.
        
        :param opciones: Diccionario de opciones y sus utilidades.
        """
        self.opciones = opciones

    def utilidad_esperada(self, inversion):
        """
        Calcula la utilidad esperada para una inversión dada en cada opción.
        
        :param inversion: Monto de la inversión.
        :return: Diccionario de utilidades esperadas por opción.
        """
        utilidades = {}
        for opcion, valores in self.opciones.items():
            # Verificar si la inversión está disponible en las utilidades de la opción
            if inversion in valores:
                utilidades[opcion] = valores[inversion]
            else:
                utilidades[opcion] = 0  # Utilidad 0 si la inversión no está disponible
        return utilidades

    def mejor_opcion(self, inversion):
        """
        Determina la mejor opción basado en la utilidad esperada.
        
        :param inversion: Monto de la inversión.
        :return: Opción con la mayor utilidad.
        """
        utilidades = self.utilidad_esperada(inversion)
        mejor_opcion = max(utilidades, key=utilidades.get)  # Encuentra la opción con la mayor utilidad
        return mejor_opcion, utilidades[mejor_opcion]

# Ejemplo de uso
if __name__ == "__main__":
    # Definir las opciones y sus utilidades
    opciones = {
        'Opción A': {100: 5, 200: 10},
        'Opción B': {100: 3, 200: 8}
    }

    decision = Decision(opciones)

    # Definir la inversión
    inversion = 200
    mejor_opcion, utilidad = decision.mejor_opcion(inversion)

    print(f"La mejor opción para una inversión de ${inversion} es: {mejor_opcion} con utilidad {utilidad}.")
"""
Clase Decision:

Se inicializa con un diccionario de opciones, donde cada opción tiene un sub-diccionario de inversiones y sus utilidades correspondientes.
El método utilidad_esperada calcula la utilidad esperada para una inversión específica en cada opción.
El método mejor_opcion determina cuál opción proporciona la mayor utilidad para una inversión dada.
Ejemplo de Uso:

Se definen dos opciones de inversión y se especifican las utilidades asociadas.
Se determina cuál opción es la mejor para una inversión de $200.
"""