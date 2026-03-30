import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task_event)

        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)
        self.listbox.bind("<Double-Button-1>", self.toggle_complete)

        self.btn_add = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.btn_add.pack(pady=5)

        self.btn_complete = tk.Button(root, text="Marcar como Completada", command=self.toggle_complete)
        self.btn_complete.pack(pady=5)

        self.btn_delete = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.btn_delete.pack(pady=5)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)

    def add_task_event(self, event):
        self.add_task()

    def toggle_complete(self, event=None):
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            if task.startswith("✔ "):
                self.listbox.delete(index)
                self.listbox.insert(index, task[2:])
            else:
                self.listbox.delete(index)
                self.listbox.insert(index, "✔ " + task)
        except:
            pass

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except:
            pass

root = tk.Tk()
app = App(root)
root.mainloop()