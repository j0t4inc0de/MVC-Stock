# View Menu
import tkinter as tk
from tkinter import ttk, Label, Button
from ttkthemes import ThemedTk
from PIL import Image, ImageTk

class VistaPrincipal:
    def __init__(self, modelo_stock):
        self.ventanaPrincipal = ThemedTk(theme="arc")
        self.ventanaPrincipal.title("Gestión de Stock")
        self.ventanaPrincipal.geometry("1100x430")
        self.ventanaPrincipal.resizable(width=False, height=False)
        self.modelo_stock = modelo_stock

        # Treeview es la tabla donde pondremos los datos de la bd
        self.treeview = ttk.Treeview(self.ventanaPrincipal, columns=("Nombre", "Precio", "Cantidad", "Estado", "Categoría"), show="headings", height=16)
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.column("Nombre", width=280)
        self.treeview.heading("Precio", text="Precio")
        self.treeview.heading("Cantidad", text="Cantidad")
        self.treeview.heading("Estado", text="Estado")
        self.treeview.heading("Categoría", text="Categoría")
        self.treeview.place(x=0, y=50)

        self.mostrar_datos()

        # Botones
        # Movimientos
        self.imagen_mov = Image.open("view/images/movimientos-512px.png")
        self.imagen_mov.thumbnail((30, 30))
        self.imagen_mov.resize((30, 30))
        self.imagen_mov = ImageTk.PhotoImage(self.imagen_mov)
        self.label_mov = ttk.Button(self.ventanaPrincipal, image=self.imagen_mov, command=self.abrir_vista_movimiento).place(x=630,y=2)

        # Buscar
        #Entry del Buscar
        self.entry_buscar = ttk.Entry(self.ventanaPrincipal, width=46)
        self.entry_buscar.place(x=1, y=19)
        self.entry_buscar.insert(0, "Buscador")
        self.entry_buscar.bind('<FocusIn>', self.on_entry_click)
        self.entry_buscar.bind('<FocusOut>', self.on_focusout)
        self.imagen_buscar = Image.open("view/images/buscar-512px.png")
        self.imagen_buscar.thumbnail((30, 30))
        self.imagen_buscar.resize((30, 30))
        self.imagen_buscar = ImageTk.PhotoImage(self.imagen_buscar)
        self.label_buscar = ttk.Button(self.ventanaPrincipal, image=self.imagen_buscar).place(x=295,y=2)

        # Actualizar
        self.imagen_actualizar = Image.open("view/images/actualizar-512px.png")
        self.imagen_actualizar.thumbnail((30, 30))
        self.imagen_actualizar.resize((30, 30))
        self.imagen_actualizar = ImageTk.PhotoImage(self.imagen_actualizar)
        self.label_actualizar = ttk.Button(self.ventanaPrincipal, image=self.imagen_actualizar, command=self.mostrar_datos).place(x=360,y=2)
        
        # Añadir.
        self.imagen_anadir = Image.open("view/images/añadir-512px.png")
        self.imagen_anadir.thumbnail((30, 30))
        self.imagen_anadir.resize((30, 30))
        self.imagen_anadir = ImageTk.PhotoImage(self.imagen_anadir)
        self.label_anadir = ttk.Button(self.ventanaPrincipal, image=self.imagen_anadir, command=self.abrir_vista_producto).place(x=450,y=2)

        # Eliminar.
        self.imagen_eliminar = Image.open("view/images/eliminar-512px.png")
        self.imagen_eliminar.thumbnail((30, 30))
        self.imagen_eliminar.resize((30, 30))
        self.imagen_eliminar = ImageTk.PhotoImage(self.imagen_eliminar)
        self.label_eliminar = ttk.Button(self.ventanaPrincipal, image=self.imagen_eliminar, command=self.abrir_vista_del).place(x=510,y=2)

        # Editar.
        self.imagen_editar = Image.open("view/images/editar-512px.png")
        self.imagen_editar.thumbnail((30, 30))
        self.imagen_editar.resize((30, 30))
        self.imagen_editar = ImageTk.PhotoImage(self.imagen_editar)
        self.label_editar = ttk.Button(self.ventanaPrincipal, image=self.imagen_editar, command=self.abrir_vista_editar).place(x=570,y=2)

    def mostrar_datos(self):
        # Llamada a la función obtener_datos del modelo_stock
        datos = self.modelo_stock.obtener_datos()

        for item in self.treeview.get_children():
            self.treeview.delete(item)
            
        for dato in datos:
            self.treeview.insert("", "end", values=dato)

            
    def abrir_vista_producto(self):
        from view.vista_producto import VistaProducto
        vista_producto = VistaProducto(self,self.modelo_stock)  
        vista_producto.ventanaProducto.grab_set()
        vista_producto.ventanaProducto.wait_window(vista_producto.ventanaProducto)
        
    # Abre la vista menu movimiento
    def abrir_vista_movimiento(self):
        self.ventanaPrincipal.destroy()
        from view.vista_movimiento_menu import VistaMenuMov
        vista_movimiento = VistaMenuMov(self, self.modelo_stock)
        vista_movimiento.ventanaMenuMov.grab_set()
        vista_movimiento.ventanaMenuMov.wait_window(vista_movimiento.ventanaMenuMov)

    def abrir_vista_del(self):
        from view.vista_eliminar import VistaEliminar
        vista_del = VistaEliminar(self, self.modelo_stock)
        vista_del.ventanaDel.grab_set()
        vista_del.ventanaDel.wait_window(vista_del.ventanaDel)
        
    def abrir_vista_editar(self):
        from view.vista_editar import VistaEditar
        vista_editar = VistaEditar(self, self.modelo_stock)
        vista_editar.ventanaED.grab_set()
        vista_editar.ventanaED.wait_window(vista_editar.ventanaED)
        
    def ejecutar(self):
        self.ventanaPrincipal.mainloop()

    def on_entry_click(self, event):
        """Function that gets called whenever entry is clicked"""
        if self.entry_buscar.get() == 'Buscador':
            self.entry_buscar.delete(0, "end")  # delete all the text in the entry
            self.entry_buscar.insert(0, '')  # Insert blank for user input

    def on_focusout(self, event):
        if self.entry_buscar.get() == '':
            self.entry_buscar.insert(0, 'Buscador')


    