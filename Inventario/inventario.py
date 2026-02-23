from producto import Producto
import os

class Inventario:
    """
    Gestiona los productos del inventario y su almacenamiento en archivo.
    """

    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()
                return

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
                            self.productos.append(producto)
                        except ValueError:
                            print("Advertencia: línea inválida ignorada.")
        except PermissionError:
            print("Error: no se tienen permisos para leer el archivo.")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos:
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
            return True
        except PermissionError:
            print("Error: no se tienen permisos para escribir en el archivo.")
            return False

    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                return False
        self.productos.append(producto)
        return self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                return self.guardar_en_archivo()
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                return self.guardar_en_archivo()
        return False

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)
