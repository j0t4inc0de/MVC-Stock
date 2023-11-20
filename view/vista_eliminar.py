#Vista eliminar
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
from ttkthemes import ThemedTk

class  VistaEliminar:
    def __init__(self, ventanaDel, modelo_stock):
        self.ventanaDel = ThemedTk(theme="arc")
        self.ventanaDel.title("Eliminando producto")
        self.ventanaDel.geometry("310x300")
        self.modelo_stock = modelo_stock
        
        self.crear_formulario() # Se llama el formulario para mostrar los botones y entrys del mismo

    def crear_formulario(self):
        ttk.Label(self.ventanaDel, text="Producto:").grid(row=2, column=0, padx=10, pady=10)
        self.existencia_combobox = ttk.Combobox(self.ventanaDel)
        self.existencia_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.populate_existencia_combobox()

        ttk.Label(self.ventanaDel, text="Info Existencia:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_cantidad_existencia = ttk.Entry(self.ventanaDel)
        self.entry_cantidad_existencia.grid(row=3, column=1, padx=10, pady=10 )

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
        else:
            print("ID de existencia no válido")

    def add_movimiento(self):
        selected_tipo_movimiento = self.tipo_movimiento_combobox.get()
        tipo_movimiento_id = self.get_tipo_movimiento_id(selected_tipo_movimiento)

        selected_existencia = self.existencia_combobox.get()
        existencia_id = self.get_existencia_id(selected_existencia)

        descripcion_movimiento = self.entry_descripcion_movimiento.get()
        fecha_movimiento = self.entry_fecha_movimiento.get()
        cantidad_movimientos = int(self.entry_cantidad_movimientos.get())

        self.modelo_stock.add_movimiento(tipo_movimiento_id, existencia_id, descripcion_movimiento, fecha_movimiento, cantidad_movimientos)

        self.tipo_movimiento_combobox.set("")
        self.existencia_combobox.set("")
        self.entry_cantidad_existencia.delete(0, tk.END)
        self.entry_descripcion_movimiento.delete(0, tk.END)
        self.entry_fecha_movimiento.delete(0, tk.END)
        self.entry_cantidad_movimientos.delete(0, tk.END)

    def del_producto(self):
        selected_existencia = self.existencia_combobox.get()
        existencia_id = self.get_existencia_id(selected_existencia)

        self.modelo_stock.del_producto(existencia_id)