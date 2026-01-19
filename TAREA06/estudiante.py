
# archivo: estudiante.py
# Clase derivada que demuestra herencia y polimorfismo

from persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Polimorfismo: se sobrescribe el método rol
    def rol(self):
        return "Estudiante"

    def descripcion(self):
        return f"{super().descripcion()}, Carrera: {self.carrera}"
