from biblioteca import Biblioteca
from libro import Libro
from usuario import Usuario

def main():

    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel Garcia Marquez", "Novela", "111")
    libro2 = Libro("1984", "George Orwell", "Distopia", "222")
    libro3 = Libro("Python Basico", "Juan Perez", "Programacion", "333")

    biblioteca.anadir_libro(libro1)
    biblioteca.anadir_libro(libro2)
    biblioteca.anadir_libro(libro3)

    # Crear usuarios
    usuario1 = Usuario("Jefferson", "U001")
    usuario2 = Usuario("Maria", "U002")

    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestamos
    biblioteca.prestar_libro("111", "U001")
    biblioteca.prestar_libro("222", "U001")

    print("Libros prestados:", biblioteca.listar_libros_usuario("U001"))

    biblioteca.devolver_libro("111", "U001")

    print("Después de devolver:", biblioteca.listar_libros_usuario("U001"))

    print("Buscar por autor Orwell")
    for libro in biblioteca.buscar_por_autor("Orwell"):
        print(libro)

if __name__ == "__main__":
    main()