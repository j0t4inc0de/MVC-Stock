import tkinter as tk
from tkinter import ttk, Label, Button
from tkinter import Button
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

class VistaMenuMov:
    def __init__(self, ventanaMenuMov, modelo_stock):
        self.ventanaMenuMov = ThemedTk(theme="arc")
        self.ventanaMenuMov.title("Lista de Movimientos")
        self.ventanaMenuMov.geometry("1230x500")
        self.ventanaMenuMov.resizable(width=False, height=False)
        self.modelo_stock = modelo_stock

        self.treeviewMov = ttk.Treeview(self.ventanaMenuMov, columns=("Tipo", "Nombre", "Cantidad actual", "Descripción", "Fecha", "Movimiento"), show="headings", height=16)
        self.treeviewMov.heading("Tipo", text="Tipo")
        self.treeviewMov.heading("Nombre", text="Nombre")
        self.treeviewMov.heading("Cantidad actual", text="Cantidad actual")
        self.treeviewMov.heading("Descripción", text="Descripción")
        self.treeviewMov.heading("Fecha", text="Fecha")
        self.treeviewMov.heading("Movimiento", text="Movimiento")
        self.treeviewMov.place(x=0, y=50)

        self.mostrar_datos_mov()

    def mostrar_datos_mov(self):
        for item in self.treeviewMov.get_children():
            self.treeviewMov.delete(item)
        datos = self.modelo_stock.obtener_datos_mov()  # obtiene los datos del modelo

        # inserta los datos al treeviewMov
        for dato in datos:
            self.treeviewMov.insert("", "end", values=dato)