# Sistema de Reservas - Programación Orientada a Objetos
# Este programa simula un sistema simple de reservas.

class Cliente:
    # Clase que representa a un cliente
    def __init__(self, nombre):
        self.nombre = nombre


class Reserva:
    # Clase que representa una reserva
    def __init__(self, cliente, lugar):
        self.cliente = cliente
        self.lugar = lugar

    def mostrar_reserva(self):
        return f"Reserva a nombre de {self.cliente.nombre} para {self.lugar}"


# Uso de las clases
if __name__ == "__main__":
    cliente1 = Cliente("Juan")
    reserva1 = Reserva(cliente1, "Hotel Central")

    print(reserva1.mostrar_reserva())
