#Vista eliminar
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
from ttkthemes import ThemedTk
from tkinter import simpledialog as sd


class VistaEditar:
    def __init__(self, vista_principal, modelo_stock):
        self.ventanaED = ThemedTk(theme="arc")
        self.ventanaED.title("Editando producto")
        self.ventanaED.geometry("310x300")
        self.vista_principal = vista_principal
        self.modelo_stock = modelo_stock
        self.crear_formulario()

    def crear_formulario(self):
        ttk.Label(self.ventanaED, text="Seleccione el producto:").place(x=1, y=5)
        self.existencia_combobox = ttk.Combobox(self.ventanaED)
        self.existencia_combobox.place(x=130, y=5)
        self.populate_existencia_combobox()

        ttk.Label(self.ventanaED, text="Informacion a editar").place(x=1, y=42)

        ttk.Label(self.ventanaED, text="Existencia:").place(x=1, y=72)
        self.entry_cantidad_existencia = ttk.Entry(self.ventanaED)
        self.entry_cantidad_existencia.place(x=130, y=70)

        ttk.Label(self.ventanaED, text="Precio:").place(x=1, y=102)
        self.entry_precio_producto = ttk.Entry(self.ventanaED)
        self.entry_precio_producto.place(x=130, y=100)

        ttk.Label(self.ventanaED, text="Estado:").place(x=1, y=132)
        self.estado_combobox = ttk.Combobox(self.ventanaED, values=['activo', 'inactivo'])
        self.estado_combobox.place(x=130, y=130)
        
        ttk.Label(self.ventanaED, text="Categoría:").place(x=1, y=162)
        self.categoria_combobox = ttk.Combobox(self.ventanaED, values=self.modelo_stock.get_all_categorias())
        self.categoria_combobox.place(x=130, y=160)
       


        ttk.Button(self.ventanaED, text="Editar", command=self.edit_producto).place(x=154, y=250)

    def get_existencia_id(self, existencia_name):
        self.modelo_stock.cursor.execute("SELECT id_existencia FROM Existencia WHERE nombre=?", (existencia_name,))
        return self.modelo_stock.cursor.fetchone()[0]
    

    def populate_existencia_combobox(self):
        existencias = self.modelo_stock.get_existencias()
        self.existencia_combobox['values'] = existencias
        self.existencia_combobox.bind("<<ComboboxSelected>>", self.update_cantidad_existencia)

    def update_cantidad_existencia(self, event):
        selected_existencia = self.existencia_combobox.get()
        existencia_id = self.get_existencia_id(selected_existencia)
        
        if existencia_id is not None:
            cantidad_existente = self.modelo_stock.get_cantidad_existente(existencia_id)
            self.entry_cantidad_existencia.delete(0, tk.END)
            self.entry_cantidad_existencia.insert(0, str(cantidad_existente))

            precio_producto = self.modelo_stock.get_precio_producto(selected_existencia)
            self.entry_precio_producto.delete(0, tk.END)
            self.entry_precio_producto.insert(0, str(precio_producto))

            estado_producto = self.modelo_stock.get_estado_producto(selected_existencia)
            self.estado_combobox.set(estado_producto)

            # Obtener la categoría del producto seleccionado
            categoria_producto = self.modelo_stock.get_categoria_producto(selected_existencia)
            self.categoria_combobox.set(categoria_producto)  # Asegúrate de tener un combobox para la categoría
        else:
            print("ID de existencia no válido")

    def edit_producto(self):
        selected_existencia = self.existencia_combobox.get()
        existencia_id = self.get_existencia_id(selected_existencia)
        nueva_cantidad = self.entry_cantidad_existencia.get()
        nuevo_precio = self.entry_precio_producto.get()
        nuevo_estado = self.estado_combobox.get()
        nueva_categoria = self.categoria_combobox.get()  # Obtener la nueva categoría del combobox
       

        self.modelo_stock.edit_producto(existencia_id, nueva_cantidad, nuevo_precio, nuevo_estado,nueva_categoria,)
        self.vista_principal.mostrar_datos()
       
        self.ventanaED.destroy()
