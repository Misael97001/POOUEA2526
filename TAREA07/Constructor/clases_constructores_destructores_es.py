# Este programa demuestra el uso de constructores (__init__) y destructores (__del__)
# en clases de Python, con comentarios explicativos y buenas prácticas.

class GestorArchivo:
    """
    Esta clase simula la gestión de un recurso del sistema: un archivo.
    Permite ver cómo el constructor abre un recurso y el destructor lo libera.
    """

    def __init__(self, nombre_archivo, modo):
        """
        MÉTODO CONSTRUCTOR
        ------------------
        Se ejecuta automáticamente cuando se crea el objeto.
        Su función es inicializar atributos y adquirir recursos.

        Parámetros:
        nombre_archivo (str): Nombre del archivo a abrir
        modo (str): Modo de apertura ('w', 'r', etc.)
        """
        self.nombre_archivo = nombre_archivo
        self.modo = modo
        self.archivo = open(self.nombre_archivo, self.modo)  # Adquisición de recurso
        print(f"[INIT] Archivo '{self.nombre_archivo}' abierto en modo '{self.modo}'.")

    def escribir_datos(self, datos):
        """
        Escribe datos en el archivo si está abierto.
        """
        if self.archivo:
            self.archivo.write(datos + "\n")
            print("[WRITE] Datos escritos en el archivo.")

    def __del__(self):
        """
        MÉTODO DESTRUCTOR
        -----------------
        Se ejecuta cuando el objeto va a ser destruido.
        Sirve para liberar recursos como archivos o conexiones.
        """
        if hasattr(self, 'archivo') and self.archivo:
            self.archivo.close()
            print(f"[DEL] Archivo '{self.nombre_archivo}' cerrado.")


class Estudiante:
    """
    Clase adicional para mostrar constructores y destructores
    sin necesidad de recursos externos.
    """

    def __init__(self, nombre, nota):
        """
        Constructor que inicializa los atributos del estudiante.
        """
        self.nombre = nombre
        self.nota = nota
        print(f"[INIT] Objeto Estudiante creado para {self.nombre}.")

    def estudiar(self):
        """
        Método que representa una acción del estudiante.
        """
        print(f"{self.nombre} está estudiando y mejorando su rendimiento.")

    def __del__(self):
        """
        Destructor que muestra cuándo el objeto es eliminado de memoria.
        """
        print(f"[DEL] Objeto Estudiante de {self.nombre} destruido.")


# ---------------- PROGRAMA PRINCIPAL ----------------
# Aquí se observa cuándo se activan los constructores y destructores.

if __name__ == "__main__":
    print("Programa iniciado.\n")

    # Creación de objetos → se ejecutan los constructores
    gestor = GestorArchivo("ejemplo.txt", "w")
    gestor.escribir_datos("Esta es una línea de prueba.")

    estudiante1 = Estudiante("Jefferson", 9.5)
    estudiante1.estudiar()

    print("\nEliminando objeto estudiante explícitamente...")
    del estudiante1  # Aquí puede ejecutarse el destructor

    print("\nEl programa está finalizando. Los destructores restantes pueden ejecutarse ahora.")
