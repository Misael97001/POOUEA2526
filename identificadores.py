"""
Programa que calcula el área de un rectángulo
y determina si el área es mayor a un valor mínimo.
"""

# Solicitar datos al usuario
base_rectangulo = float(input("Ingrese la base del rectángulo: "))
altura_rectangulo = float(input("Ingrese la altura del rectángulo: "))

# Cálculo del área
area_rectangulo = base_rectangulo * altura_rectangulo

# Comparación lógica
area_minima = 50
es_area_grande = area_rectangulo > area_minima

# Mostrar resultados
print("El área del rectángulo es:", area_rectangulo)
print("¿El área es mayor a", area_minima, "?:", es_area_grande)
