
from producto import Producto
import os

class Inventario:

    def __init__(self, archivo="inventario.txt"):
        self.productos = {}
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        if not os.path.exists(self.archivo):
            open(self.archivo, "w").close()
            return

        try:
            with open(self.archivo, "r") as f:
                for linea in f:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        try:
                            producto = Producto(
                                int(datos[0]),
                                datos[1],
                                int(datos[2]),
                                float(datos[3])
                            )
                            self.productos[producto.get_id()] = producto
                        except ValueError:
                            print("Línea inválida ignorada.")
        except PermissionError:
            print("No se tienen permisos para leer el archivo.")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos.values():
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
            return True
        except PermissionError:
            print("No se tienen permisos para escribir en el archivo.")
            return False

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            return False
        self.productos[producto.get_id()] = producto
        return self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            return self.guardar_en_archivo()
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            return self.guardar_en_archivo()
        return False

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos.values():
                print(p)
