# ==========================================================
# Ejemplos Sencillos de POO en Python
# ==========================================================

# 1. ABSTRACCIÓN: Mostrar solo la información esencial

class Animal:
    """Clase base que define la interfaz de un animal."""
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        """Método abstracto: define lo que debe hacer un animal."""
        # Un usuario de la clase solo necesita saber que existe este método.
        # Los detalles de CÓMO se hace el sonido se ocultan en las subclases.
        raise NotImplementedError("Este método debe ser sobrescrito por la subclase.")

    def moverse(self):
        print(f"{self.nombre} se está moviendo.")

# 2. ENCAPSULACIÓN: Proteger los datos y controlar el acceso

class CuentaBancaria:
    """Controla el acceso al saldo (dato privado)."""
    def __init__(self, saldo_inicial):
        # El saldo es un atributo "privado" (usando __ en Python).
        # Esto indica que no debe modificarse directamente.
        self.__saldo = saldo_inicial

    # Método público para consultar el saldo
    def consultar_saldo(self):
        return self.__saldo

    # Método público para depositar
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.__saldo}")
        else:
            print("Error: La cantidad a depositar debe ser positiva.")

    # No hay un método para cambiar el saldo directamente.
    # El único control es a través de depositar/retirar (si existiera).

# 3. HERENCIA: Reutilización de código

class Perro(Animal): # Perro hereda de Animal
    """Una clase más específica que hereda propiedades de Animal."""
    def hacer_sonido(self):
        # Implementación específica de un Perro
        return "Guau Guau"

class Gato(Animal): # Gato hereda de Animal
    """Otra clase más específica que hereda propiedades de Animal."""
    def hacer_sonido(self):
        # Implementación específica de un Gato
        return "Miau Miau"

# 4. POLIMORFISMO: Diferentes objetos responden al mismo mensaje

def describir_animal(animal):
    """Una función que acepta cualquier objeto que tenga el método hacer_sonido()."""
    print(f"El animal {animal.nombre} hace: {animal.hacer_sonido()}")
    animal.moverse() # Llama al método heredado

# ==========================================================
# Ejecución y Prueba de los Ejemplos
# ==========================================================

print("--- 1. Abstracción y 3. Herencia ---")
mi_perro = Perro("Fido")
mi_gato = Gato("Garfield")

print(f"Perro dice: {mi_perro.hacer_sonido()}")
mi_perro.moverse() # Usa el método moverse de la clase base Animal

print("\n--- 4. Polimorfismo ---")
describir_animal(mi_perro) # La misma función...
describir_animal(mi_gato)  # ...funciona con diferentes objetos (Perro y Gato)

print("\n--- 2. Encapsulación ---")
mi_cuenta = CuentaBancaria(100) # Saldo inicial 100
print(f"Saldo inicial: {mi_cuenta.consultar_saldo()}")

mi_cuenta.depositar(50) # Modificación controlada
# Intentar acceder directamente al saldo (debería evitarse)
# print(mi_cuenta.__saldo) # Esto causaría un error o no mostraría el valor real

mi_cuenta.depositar(-10) # El método controla que la cantidad sea positiva