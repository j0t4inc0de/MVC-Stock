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

        self.treeview = ttk.Treeview(self.VentanaMovimiento, columns=("Tipo", "Existencia", "Cantidad de existencia", "Descripción", "Fecha", "Cantidad de movimiento"), show="headings", height=16)
        self.treeview.heading("Tipo", text="Tipo")
        self.treeview.heading("Existencia", text="Existencia")
        self.treeview.heading("Cantidad de existencia", text="Cantidad de existencia")
        self.treeview.heading("Descripción", text="Descripción")
        self.treeview.heading("Fecha", text="Fecha")
        self.treeview.heading("Cantidad de movimiento", text="Cantidad de movimiento")

        self.treeview.place(x=0, y=50)


