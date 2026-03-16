
# Aplicación GUI Básica con Tkinter
# Autor: Jefferson Chiluisa

import tkinter as tk
from tkinter import messagebox

class AplicacionGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Información - GUI Básica")
        self.root.geometry("400x350")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=5)

        # Campo de texto
        self.campo_texto = tk.Entry(root, width=40)
        self.campo_texto.pack(pady=5)

        # Botón agregar
        self.boton_agregar = tk.Button(root, text="Agregar", command=self.agregar_dato)
        self.boton_agregar.pack(pady=5)

        # Lista para mostrar datos
        self.lista_datos = tk.Listbox(root, width=45, height=10)
        self.lista_datos.pack(pady=10)

        # Botón eliminar seleccionado
        self.boton_eliminar = tk.Button(root, text="Eliminar seleccionado", command=self.eliminar_dato)
        self.boton_eliminar.pack(pady=5)

        # Botón limpiar
        self.boton_limpiar = tk.Button(root, text="Limpiar campo", command=self.limpiar_campo)
        self.boton_limpiar.pack(pady=5)

    def agregar_dato(self):
        dato = self.campo_texto.get()

        if dato.strip() == "":
            messagebox.showwarning("Advertencia", "Debe ingresar un texto.")
            return

        self.lista_datos.insert(tk.END, dato)
        self.campo_texto.delete(0, tk.END)

    def eliminar_dato(self):
        seleccion = self.lista_datos.curselection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Seleccione un elemento para eliminar.")
            return

        self.lista_datos.delete(seleccion)

    def limpiar_campo(self):
        self.campo_texto.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
