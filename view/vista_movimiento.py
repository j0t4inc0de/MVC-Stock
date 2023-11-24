# Vista Movimiento
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from ttkthemes import ThemedTk

class VistaMovimiento:
    def __init__(self, ventanaMovimiento, modelo_stock):
        self.ventanaMovimiento = ThemedTk(theme="arc")
        self.ventanaMovimiento.title("Agregando movimiento")
        self.ventanaMovimiento.geometry("400x350")
        self.modelo_stock = modelo_stock
        
        self.select_tipo_movimiento = tk.StringVar()
        self.select_existencia = tk.StringVar()
        self.crear_formulario()

    def crear_formulario(self):

        ttk.Label(self.ventanaMovimiento, text="Tipo de Movimiento:").grid(row=1, column=0, padx=10, pady=10)
        self.tipo_movimiento_combobox = ttk.Combobox(self.ventanaMovimiento)
        self.tipo_movimiento_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.populate_tipo_movimiento_combobox()

        ttk.Label(self.ventanaMovimiento, text="Producto:").grid(row=2, column=0, padx=10, pady=10)
        self.existencia_combobox = ttk.Combobox(self.ventanaMovimiento)
        self.existencia_combobox.grid(row=2, column=1, padx=10, pady=10)
        self.populate_existencia_combobox()

        ttk.Label(self.ventanaMovimiento, text="Cantidad:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_cantidad_existencia = ttk.Entry(self.ventanaMovimiento)
        self.entry_cantidad_existencia.grid(row=3, column=1, padx=10, pady=10 )

        ttk.Label(self.ventanaMovimiento, text="Descripción del Movimiento:").grid(row=4, column=0, padx=10, pady=10)
        self.entry_descripcion_movimiento = ttk.Entry(self.ventanaMovimiento)
        self.entry_descripcion_movimiento.grid(row=4, column=1, padx=10, pady=10)

        ttk.Label(self.ventanaMovimiento, text="Fecha del Movimiento:").grid(row=5, column=0, padx=10, pady=10)
        self.entry_fecha_movimiento = ttk.Entry(self.ventanaMovimiento)
        self.entry_fecha_movimiento.grid(row=5, column=1, padx=10, pady=10)

        ttk.Label(self.ventanaMovimiento, text="Cantidad movida:").grid(row=6, column=0, padx=10, pady=10)
        self.entry_cantidad_movimientos = ttk.Entry(self.ventanaMovimiento)
        self.entry_cantidad_movimientos.grid(row=6, column=1, padx=10, pady=10)

        ttk.Button(self.ventanaMovimiento, text="Listo", command=self.add_movimiento).place(x=180, y=300)

    def populate_tipo_movimiento_combobox(self):
        tipos_movimiento = self.modelo_stock.get_tipo_movimientos() 
        self.tipo_movimiento_combobox['values'] = tipos_movimiento

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

        self.ventanaMovimiento.destroy()

    def get_tipo_movimiento_id(self, tipo_movimiento_name):
        self.modelo_stock.cursor.execute("SELECT id_tipomov FROM TipoMovimiento WHERE nombre=?", (tipo_movimiento_name,))
        return self.modelo_stock.cursor.fetchone()[0]

    def get_existencia_id(self, existencia_name):
        self.modelo_stock.cursor.execute("SELECT id_existencia FROM Existencia WHERE nombre=?", (existencia_name,))
        return self.modelo_stock.cursor.fetchone()[0]
