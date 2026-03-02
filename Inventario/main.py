
from inventario import Inventario
from producto import Producto

def menu():
    print("\n--- SISTEMA AVANZADO DE GESTIÓN DE INVENTARIO ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar inventario")
    print("6. Salir")

def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_p = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_p, nombre, cantidad, precio)
                if inventario.agregar_producto(producto):
                    print("Producto agregado correctamente.")
                else:
                    print("El ID ya existe.")

            elif opcion == "2":
                id_p = int(input("ID del producto a eliminar: "))
                if inventario.eliminar_producto(id_p):
                    print("Producto eliminado correctamente.")
                else:
                    print("Producto no encontrado.")

            elif opcion == "3":
                id_p = int(input("ID del producto: "))
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                if inventario.actualizar_producto(id_p, cantidad, precio):
                    print("Producto actualizado correctamente.")
                else:
                    print("Producto no encontrado.")

            elif opcion == "4":
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)
                if resultados:
                    for p in resultados:
                        print(p)
                else:
                    print("No se encontraron productos.")

            elif opcion == "5":
                inventario.mostrar_todos()

            elif opcion == "6":
                print("Saliendo del sistema.")
                break

            else:
                print("Opción inválida.")

        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()
