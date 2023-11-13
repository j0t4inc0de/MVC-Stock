import tkinter as tk
from tkinter import ttk
import sqlite3

class StockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Stock")
        self.conn = sqlite3.connect('data/base.db')
        self.cursor = self.conn.cursor()

        # Crear una variable de cadena para la selección del estado
        self.selected_state = tk.StringVar()

        # Crear un formulario
        self.create_form()

    def create_form(self):
        # Etiqueta y entrada para el nombre del producto
        tk.Label(self.root, text="Nombre del Producto:").grid(row=0, column=0)
        self.product_name_entry = tk.Entry(self.root)
        self.product_name_entry.grid(row=0, column=1)

        # Etiqueta y entrada para el precio del producto
        tk.Label(self.root, text="Precio del Producto:").grid(row=1, column=0)
        self.product_price_entry = tk.Entry(self.root)
        self.product_price_entry.grid(row=1, column=1)

        # Etiqueta y desplegable para el estado del producto
        tk.Label(self.root, text="Estado del Producto:").grid(row=2, column=0)
        self.state_combobox = ttk.Combobox(self.root, textvariable=self.selected_state)
        self.state_combobox.grid(row=2, column=1)
        self.populate_state_combobox()

        # Botón para agregar el producto
        tk.Button(self.root, text="Agregar Producto", command=self.add_product).grid(row=3, column=0, columnspan=2)

    def populate_state_combobox(self):
        # Obtener estados desde la base de datos y agregarlos al desplegable
        self.cursor.execute("SELECT nombre FROM Estado")
        states = [state[0] for state in self.cursor.fetchall()]
        self.state_combobox['values'] = states

    def add_product(self):
        # Obtener el id_estado asociado al nombre seleccionado
        selected_state_name = self.selected_state.get()
        self.cursor.execute("SELECT id_estado FROM Estado WHERE nombre=?", (selected_state_name,))
        state_id = self.cursor.fetchone()[0]

        # Obtener otros datos del formulario
        product_name = self.product_name_entry.get()
        product_price = float(self.product_price_entry.get())

        # Insertar el nuevo producto en la tabla 'Producto'
        self.cursor.execute("INSERT INTO Producto (nombre, id_estado, precio) VALUES (?, ?, ?)",
                            (product_name, state_id, product_price))
        self.conn.commit()

        # Limpiar el formulario después de agregar el producto
        self.product_name_entry.delete(0, tk.END)
        self.product_price_entry.delete(0, tk.END)
        self.selected_state.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockApp(root)
    root.mainloop()
