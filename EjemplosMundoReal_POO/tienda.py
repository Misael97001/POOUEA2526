# Sistema de Tienda - Programación Orientada a Objetos
# Este programa modela una tienda simple usando clases y objetos.

class Producto:
    # Clase que representa un producto de la tienda
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}"


class Carrito:
    # Clase que representa un carrito de compras
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total

    def mostrar_carrito(self):
        for producto in self.productos:
            print(producto.mostrar_info())
        print("Total a pagar: $", self.calcular_total())


# Uso de las clases
if __name__ == "__main__":
    p1 = Producto("Pan", 0.50)
    p2 = Producto("Leche", 1.20)

    carrito = Carrito()
    carrito.agregar_producto(p1)
    carrito.agregar_producto(p2)

    carrito.mostrar_carrito()
