
# archivo: main.py
# Archivo principal donde se crean los objetos y se prueba la funcionalidad

from persona import Persona
from estudiante import Estudiante

# Creación de objetos
persona1 = Persona("Carlos", 45)
estudiante1 = Estudiante("Ana", 20, "Ingeniería en Sistemas")

# Uso de métodos
print(persona1.descripcion())
print("Rol:", persona1.rol())

print(estudiante1.descripcion())
print("Rol:", estudiante1.rol())
