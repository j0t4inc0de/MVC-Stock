#Vista eliminar
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
from ttkthemes import ThemedTk
from tkinter import simpledialog as sd

class  VistaEliminar:
    def __init__(self, ventanaDel, modelo_stock):
        self.ventanaDel = ThemedTk(theme="arc")
        self.ventanaDel.title("Eliminando producto")
        self.ventanaDel.geometry("310x300")
        self.modelo_stock = modelo_stock
        self.crear_formulario() # Se llama el formulario para mostrar los botones y entrys del mismo

    def crear_formulario(self):
        ttk.Label(self.ventanaDel, text="Seleccione el producto:").place(x=1, y=5)
        self.existencia_combobox = ttk.Combobox(self.ventanaDel)
        self.existencia_combobox.place(x=130, y=5)
        self.populate_existencia_combobox()
        ttk.Label(self.ventanaDel, text="Informacion a eliminar").place(x=1, y=42)

        ttk.Label(self.ventanaDel, text="Existencia:").place(x=1, y=72)
        self.entry_cantidad_existencia = ttk.Entry(self.ventanaDel)
        self.entry_cantidad_existencia.place(x=130, y=70)

        ttk.Label(self.ventanaDel, text="Precio:").place(x=1, y=102)
        self.entry_precio_producto = ttk.Entry(self.ventanaDel)
        self.entry_precio_producto.place(x=130, y=100)

        ttk.Button(self.ventanaDel, text="Eliminar", command=self.del_producto).place(x=154, y=250)

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

        # Verifica que existencia_id sea un valor válido
        if existencia_id is not None:
            # Obtener la cantidad existente y mostrarla en el entry de cantidad
            cantidad_existente = self.modelo_stock.get_cantidad_existente(existencia_id)  
            self.entry_cantidad_existencia.delete(0, tk.END)
            self.entry_cantidad_existencia.insert(0, str(cantidad_existente))
            self.entry_cantidad_existencia.config(state="readonly")
            self.entry_cantidad_existencia.icursor(0)

            # Obtener el precio y mostrarlo en el entry de precio
            precio_producto = self.modelo_stock.get_precio_producto(selected_existencia)
            self.entry_precio_producto.delete(0, tk.END)
            self.entry_precio_producto.insert(0, str(precio_producto))
            self.entry_precio_producto.config(state="readonly")
            self.entry_precio_producto.icursor(0)
        else:
            print("ID de existencia no válido")
            
    def del_producto(self):
        selected_existencia = self.existencia_combobox.get()
        existencia_id = self.get_existencia_id(selected_existencia)
        respuesta = mb.askokcancel("Confirmar eliminación", f"¿Seguro que quieres eliminar el producto {selected_existencia}?")

        if respuesta:
            # El usuario hizo clic en "Aceptar"
            self.modelo_stock.del_producto(existencia_id)
            mb.showinfo("Éxito", "Producto eliminado con éxito.")
            self.ventanaDel.destroy()
        else:
            # El usuario hizo clic en "Cancelar"
            mb.showinfo("Cancelado", "Operación de eliminación cancelada.")