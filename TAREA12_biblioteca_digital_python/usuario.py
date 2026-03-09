class Usuario:
    """Representa un usuario de la biblioteca"""
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)

    def listar_libros(self):
        return [libro.obtener_titulo() for libro in self.libros_prestados]

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.user_id}, Libros prestados: {len(self.libros_prestados)}"