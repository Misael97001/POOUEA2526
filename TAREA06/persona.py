
# archivo: persona.py
# Clase base que demuestra definición de clase, objeto y encapsulación

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.__edad = edad  # Encapsulación (atributo privado)

    def get_edad(self):
        return self.__edad

    def descripcion(self):
        return f"Persona: {self.nombre}, Edad: {self.__edad}"

    def rol(self):
        return "Persona general"
