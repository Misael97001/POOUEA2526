from libro import Libro
from usuario import Usuario

class Biblioteca:

    def __init__(self):
        # Diccionario ISBN -> Libro
        self.libros = {}
        # Usuarios
        self.usuarios = {}
        # Conjunto para IDs únicos
        self.ids_usuarios = set()

    # -------- LIBROS --------

    def anadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print("Libro añadido correctamente")
        else:
            print("El libro ya existe")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado")
        else:
            print("Libro no encontrado")

    # -------- USUARIOS --------

    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.ids_usuarios:
            self.ids_usuarios.add(usuario.user_id)
            self.usuarios[usuario.user_id] = usuario
            print("Usuario registrado")
        else:
            print("ID ya registrado")

    def eliminar_usuario(self, user_id):
        if user_id in self.ids_usuarios:
            self.ids_usuarios.remove(user_id)
            del self.usuarios[user_id]
            print("Usuario eliminado")
        else:
            print("Usuario no encontrado")

    # -------- PRESTAMOS --------

    def prestar_libro(self, isbn, user_id):
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[user_id]

            if not libro.prestado:
                libro.prestado = True
                usuario.prestar_libro(libro)
                print("Libro prestado")
            else:
                print("El libro ya está prestado")
        else:
            print("Libro o usuario no existe")

    def devolver_libro(self, isbn, user_id):
        if isbn in self.libros and user_id in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[user_id]

            if libro in usuario.libros_prestados:
                libro.prestado = False
                usuario.devolver_libro(libro)
                print("Libro devuelto")
            else:
                print("El usuario no tiene ese libro")
        else:
            print("Libro o usuario no existe")

    # -------- BUSQUEDAS --------

    def buscar_por_titulo(self, titulo):
        return [libro for libro in self.libros.values() if titulo.lower() in libro.obtener_titulo().lower()]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros.values() if autor.lower() in libro.obtener_autor().lower()]

    def buscar_por_categoria(self, categoria):
        return [libro for libro in self.libros.values() if categoria.lower() in libro.categoria.lower()]

    # -------- LISTAR LIBROS DE USUARIO --------

    def listar_libros_usuario(self, user_id):
        if user_id in self.usuarios:
            return self.usuarios[user_id].listar_libros()
        return []