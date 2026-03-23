
"""
Aplicación de Agenda Personal con Tkinter
Autor: Generado por ChatGPT
Descripción:
Permite agregar, visualizar y eliminar eventos con fecha, hora y descripción.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # pip install tkcalendar

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame principal
        frame_main = tk.Frame(root)
        frame_main.pack(pady=10)

        # TreeView para mostrar eventos
        self.tree = ttk.Treeview(frame_main, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.pack()

        # Frame de entrada
        frame_inputs = tk.Frame(root)
        frame_inputs.pack(pady=10)

        tk.Label(frame_inputs, text="Fecha:").grid(row=0, column=0)
        self.date_entry = DateEntry(frame_inputs)
        self.date_entry.grid(row=0, column=1)

        tk.Label(frame_inputs, text="Hora:").grid(row=1, column=0)
        self.hour_entry = tk.Entry(frame_inputs)
        self.hour_entry.grid(row=1, column=1)

        tk.Label(frame_inputs, text="Descripción:").grid(row=2, column=0)
        self.desc_entry = tk.Entry(frame_inputs)
        self.desc_entry.grid(row=2, column=1)

        # Frame de botones
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=10)

        tk.Button(frame_buttons, text="Agregar Evento", command=self.add_event).grid(row=0, column=0, padx=5)
        tk.Button(frame_buttons, text="Eliminar Evento", command=self.delete_event).grid(row=0, column=1, padx=5)
        tk.Button(frame_buttons, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

    def add_event(self):
        fecha = self.date_entry.get()
        hora = self.hour_entry.get()
        desc = self.desc_entry.get()

        if fecha and hora and desc:
            self.tree.insert("", "end", values=(fecha, hora, desc))
            self.hour_entry.delete(0, tk.END)
            self.desc_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Completa todos los campos")

    def delete_event(self):
        selected = self.tree.selection()
        if selected:
            confirm = messagebox.askyesno("Confirmar", "¿Eliminar evento seleccionado?")
            if confirm:
                self.tree.delete(selected)
        else:
            messagebox.showwarning("Error", "Selecciona un evento")

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
