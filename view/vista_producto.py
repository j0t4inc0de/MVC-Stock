#View producto.
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
from ttkthemes import ThemedTk

class  VistaProducto:
    def __init__(self, ventanaProducto, modelo_stock):
        self.ventanaProducto = ThemedTk(theme="arc")
        self.ventanaProducto.title("Gestión de Stock")
        self.ventanaProducto.geometry("400x350")
        self.modelo_stock = modelo_stock
        
        self.select_state = tk.StringVar()
        self.select_category = tk.StringVar()
        self.crear_formulario()

    def crear_formulario(self):
        ttk.Label(self.ventanaProducto, text="Nombre del Producto:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre_producto = ttk.Entry(self.ventanaProducto)
        self.entry_nombre_producto.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.ventanaProducto, text="Precio del Producto:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_precio_producto = ttk.Entry(self.ventanaProducto)
        self.entry_precio_producto.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.ventanaProducto, text="Cantidad:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_cantidad_producto = ttk.Entry(self.ventanaProducto)
        self.entry_cantidad_producto.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.ventanaProducto, text="Estado del Producto:").grid(row=3, column=0, padx=10, pady=10)
        self.state_combobox = ttk.Combobox(self.ventanaProducto)
        self.state_combobox.grid(row=3, column=1, padx=10, pady=10)
        self.populate_state_combobox()

        ttk.Label(self.ventanaProducto, text="Categoría del Producto:").grid(row=4, column=0, padx=10, pady=10)
        self.category_combobox = ttk.Combobox(self.ventanaProducto)
        self.category_combobox.grid(row=4, column=1, padx=10, pady=10)
        self.populate_category_combobox()

        ttk.Button(self.ventanaProducto, text="Agregar Producto", command=self.add_product).grid(row=5, column=0, columnspan=2, pady=10)

    def populate_state_combobox(self):
        states = self.modelo_stock.get_estados()
        self.state_combobox['values'] = states

    def populate_category_combobox(self):
        categories = self.modelo_stock.get_categorias()
        self.category_combobox['values'] = categories

    def add_product(self):
        selected_state_name = self.state_combobox.get()
        state_id = self.get_state_id(selected_state_name)

        selected_category_name = self.category_combobox.get()
        category_id = self.get_category_id(selected_category_name)

        product_name = self.entry_nombre_producto.get()
        product_price = float(self.entry_precio_producto.get())

        product_cantidad = self.entry_cantidad_producto.get()
        product_cantidad = int(self.entry_cantidad_producto.get())

        self.modelo_stock.add_producto(product_name, state_id, product_price, product_cantidad, category_id)

        self.entry_nombre_producto.delete(0, tk.END)
        self.entry_precio_producto.delete(0, tk.END)
        self.entry_cantidad_producto.delete(0, tk.END)
        self.state_combobox.set("")
        self.category_combobox.set("")

    def get_state_id(self, state_name):
        self.modelo_stock.cursor.execute("SELECT id_estado FROM Estado WHERE nombre=?", (state_name,))
        return self.modelo_stock.cursor.fetchone()[0]
    def get_category_id(self, category_name):
        self.modelo_stock.cursor.execute("SELECT id_categoria FROM Categoria WHERE nombre=?", (category_name,))
        return self.modelo_stock.cursor.fetchone()[0]