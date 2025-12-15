# promedio_clima_poo.py
# Programación Orientada a Objetos (POO) para calcular el promedio semanal del clima

class Clima:
    def __init__(self):
        # Encapsulamiento: atributo protegido
        self._temperaturas = []

    def ingresar_temperatura(self, temperatura):
        """Agrega una temperatura diaria."""
        self._temperaturas.append(temperatura)

    def calcular_promedio(self):
        """Calcula el promedio semanal."""
        if not self._temperaturas:
            return 0
        return sum(self._temperaturas) / len(self._temperaturas)


class ClimaSemanal(Clima):
    """Herencia: extiende la clase Clima para una semana completa."""
    def ingresar_semana(self):
        for dia in range(1, 8):
            temp = float(input(f"Ingrese la temperatura del día {dia}: "))
            self.ingresar_temperatura(temp)


def main():
    print("=== Promedio Semanal del Clima (POO) ===")
    clima = ClimaSemanal()
    clima.ingresar_semana()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()
