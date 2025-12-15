# promedio_clima_tradicional.py
# Programación Tradicional para calcular el promedio semanal del clima

def ingresar_temperaturas():
    """Solicita al usuario ingresar las temperaturas de 7 días."""
    temperaturas = []
    for dia in range(1, 8):
        temp = float(input(f"Ingrese la temperatura del día {dia}: "))
        temperaturas.append(temp)
    return temperaturas

def calcular_promedio(temperaturas):
    """Calcula el promedio de una lista de temperaturas."""
    return sum(temperaturas) / len(temperaturas)

def main():
    print("=== Promedio Semanal del Clima (Programación Tradicional) ===")
    temps = ingresar_temperaturas()
    promedio = calcular_promedio(temps)
    print(f"El promedio semanal de temperatura es: {promedio:.2f} °C")

if __name__ == "__main__":
    main()
