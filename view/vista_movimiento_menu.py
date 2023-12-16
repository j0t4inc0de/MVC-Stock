import tkinter as tk
from tkinter import PhotoImage, ttk, Label, Button
from tkinter import Button
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
ruta = "view/images/anadir.gif"
class VistaMenuMov:
    def __init__(self, ventanaPrincipal, modelo_stock):
        self.ventanaMenuMov = ThemedTk(theme="arc")
        self.ventanaMenuMov.title("Lista de Movimientos")
        self.ventanaMenuMov.geometry("1230x500")
        self.ventanaMenuMov.resizable(width=False, height=False)
        self.modelo_stock = modelo_stock

        self.treeviewMov = ttk.Treeview(self.ventanaMenuMov, columns=("Tipo", "Producto", "Cantidad actual", "Descripción", "Fecha", "Movimiento"), show="headings", height=16)
        self.treeviewMov.heading("Tipo", text="Tipo")
        self.treeviewMov.heading("Producto", text="Producto")
        self.treeviewMov.heading("Cantidad actual", text="Cantidad actual")
        self.treeviewMov.heading("Descripción", text="Descripción")
        self.treeviewMov.heading("Fecha", text="Fecha")
        self.treeviewMov.heading("Movimiento", text="Movimiento")
        self.treeviewMov.place(x=0, y=50)

        # Boton imagen volver
        self.imagen_volver = Image.open("view/images/regresar1.png")
        self.imagen_volver.thumbnail((30, 30))
        self.imagen_volver.resize((30, 30))
        self.imagen_volver = ImageTk.PhotoImage(self.imagen_volver)
        self.label_anadir = ttk.Button(self.ventanaMenuMov, image=self.imagen_volver).place(x=2,y=2)
        # Boton imagen actualizar
        self.imagen_actualizar = Image.open("view/images/actualizar-512px.png")
        self.imagen_actualizar.thumbnail((30, 30))
        self.imagen_actualizar.resize((30, 30))
        self.imagen_actualizar = ImageTk.PhotoImage(self.imagen_actualizar)
        self.label_actualizar = ttk.Button(self.ventanaMenuMov, image=self.imagen_actualizar, command=self.mostrar_datos_mov).place(x=80,y=2)
        # Boton imagen añadir
        self.imagen_anadir = Image.open("view/images/añadir-512px.png")
        self.imagen_anadir.thumbnail((30, 30))
        self.imagen_anadir.resize((30, 30))
        self.imagen_anadir = ImageTk.PhotoImage(self.imagen_anadir)
        self.label_anadir = ttk.Button(self.ventanaMenuMov, image=self.imagen_anadir, command=self.abrir_vista_movimiento).place(x=155,y=2)

        self.mostrar_datos_mov()

    def mostrar_datos_mov(self):
        for item in self.treeviewMov.get_children():
            self.treeviewMov.delete(item)
        datos = self.modelo_stock.obtener_datos_mov()  # obtiene los datos del modelo

        # inserta los datos al treeviewMov
        for dato in datos:
            self.treeviewMov.insert("", "end", values=dato)

    def abrir_vista_movimiento(self):
        from view.vista_movimiento import VistaMovimiento
        vista_movimiento = VistaMovimiento(self, self.modelo_stock)
        vista_movimiento.ventanaMovimiento.wait_window(vista_movimiento.ventanaMovimiento)
        
        self.ventanaMenuMov.mainloop()