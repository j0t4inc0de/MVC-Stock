#Rodrigo - Cristobal Creamos la vista menu movimiento.
from tkinter import ttk
from ttkthemes import ThemedTk

class VistaMenuMov:
    def __init__(self, modelo_stock):
        self.VentanaMovimiento = ThemedTk(theme="arc")
        self.VentanaMovimiento.title("Lista de Movimientos")
        self.VentanaMovimiento.geometry("1230x500")
        self.VentanaMovimiento.resizable(width=False, height=False)
        self.modelo_stock = modelo_stock

        self.treeview = ttk.Treeview(self.VentanaMovimiento, columns=("Tipo", "Nombre", "Cantidad actual", "Descripción", "Fecha", "Cantidad de movimiento"), show="headings", height=16)
        self.treeview.heading("Tipo", text="Tipo")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Cantidad actual", text="Cantidad actual")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Cantidad de movimiento", text="Cantidad de movimiento")

        self.treeview.place(x=0, y=50)
        self.mostrar_datos_mov()
        self.entry_buscar = ttk.Entry(self.VentanaMovimiento, width=46)
        self.entry_buscar.place(x=1, y=19)
        self.entry_buscar.insert(0, "Buscador")

    def mostrar_datos_mov(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        datos = self.modelo_stock.obtener_datos_mov() # obtiene los datos del model

        # inserta los datos al treiview
        for dato in datos:
            self.treeview.insert("", "end", values=dato)