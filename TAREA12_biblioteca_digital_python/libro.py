class Libro:
    """Representa un libro de la biblioteca"""
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para datos inmutables
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn
        self.prestado = False

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        estado = "Prestado" if self.prestado else "Disponible"
        return f"Título: {self.obtener_titulo()}, Autor: {self.obtener_autor()}, Categoría: {self.categoria}, ISBN: {self.isbn}, Estado: {estado}"