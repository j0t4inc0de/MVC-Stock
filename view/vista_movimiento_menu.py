import tkinter as tk
from tkinter import PhotoImage, ttk, Label, Button
from tkinter import Button
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip


# Funcion para visualizar un mensaje al pasar cursor por encima de un boton
class CustomHovertip(Hovertip):
    def showcontents(self):
        label = tk.Label(
            self.tipwindow, text=f' "{self.text}" ', justify=tk.LEFT,
            bg="#c2c2c2", fg="#000000", relief=tk.SOLID, borderwidth=1,
            font=("Arial", 10)
        )
        label.pack()
        
        
ruta = "view/images/anadir.gif"

class VistaMenuMov:
    def __init__(self, ventanaPrincipal, modelo_stock):
        self.ventanaMenuMov = ThemedTk(theme="arc")
        self.ventanaMenuMov.title("Lista de Movimientos")
        self.ventanaMenuMov.geometry("1230x500")
        self.ventanaMenuMov.resizable(width=False, height=False)
        self.modelo_stock = modelo_stock

        self.treeviewMov = ttk.Treeview(self.ventanaMenuMov, columns=("Tipo", "Producto", "Cantidad actual", "Descripción", "Fecha", "Movimiento"), show="headings", height=20)
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
        self.imagen_volver = ImageTk.PhotoImage(self.imagen_volver)
        self.label_volver = ttk.Button(self.ventanaMenuMov, image=self.imagen_volver, command=self.abrir_vista_principal)
        self.label_volver.place(x=2, y=2)
        CustomHovertip(self.label_volver, text="Regresar al menu", hover_delay=50)#Asina lo que se quiera mostrar al pasar el cursor por encima del boton
        # Boton imagen actualizar
        self.imagen_actualizar = Image.open("view/images/actualizar-512px.png")
        self.imagen_actualizar.thumbnail((30, 30))
        self.imagen_actualizar = ImageTk.PhotoImage(self.imagen_actualizar)
        self.label_actualizar = ttk.Button(self.ventanaMenuMov, image=self.imagen_actualizar, command=self.mostrar_datos_mov)
        self.label_actualizar.place(x=80,y=2)
        CustomHovertip(self.label_actualizar, text="Actualizar", hover_delay=50)#Asina lo que se quiera mostrar al pasar el cursor por encima del boton
        # Boton imagen añadir
        self.imagen_anadir = Image.open("view/images/añadir-512px.png")
        self.imagen_anadir.thumbnail((30, 30))
        self.imagen_anadir = ImageTk.PhotoImage(self.imagen_anadir)
        self.label_anadir = ttk.Button(self.ventanaMenuMov, image=self.imagen_anadir, command=self.abrir_vista_movimiento)
        self.label_anadir.place(x=155,y=2)
        CustomHovertip(self.label_anadir, text="Añadir", hover_delay=50)#Asina lo que se quiera mostrar al pasar el cursor por encima del boton
        
         #Eliminar
        # self.imagen_eliminar = Image.open("view/images/eliminar-512px.png")
        # self.imagen_eliminar.thumbnail((30, 30))
        # self.imagen_eliminar = ImageTk.PhotoImage(self.imagen_eliminar)
        # self.label_eliminar = ttk.Button(self.ventanaMenuMov, image=self.imagen_eliminar, command=self.abrir_vista_del)
        # self.label_eliminar.place(x=225, y=2)
        # Aplicar el CustomHovertip
        # CustomHovertip(self.label_eliminar, text="Eliminar", hover_delay=50)

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
    
    #vuelve a abrir la ventana principal y desruye la ventana de movimientos
    def abrir_vista_principal(self):
        self.ventanaMenuMov.destroy()
        from view.view_menu import VistaPrincipal
        vista_principla = VistaPrincipal(self.modelo_stock)
        vista_principla.ventanaPrincipal.grab_set()
        vista_principla.ventanaPrincipal.wait_window(vista_principla.ventanaPrincipal)
        
    def abrir_vista_del(self):
        # from view.vista_eliminar_mov import VistaEliminarMovimiento

        # # Liberar el evento de grab_set() en la ventana actual
        # self.ventanaMenuMov.grab_release()

        # # Crea un objeto de la clase `VistaEliminar`.
        # vista_del = VistaEliminarMovimiento(self, self.modelo_stock)
        
        # # Muestra la ventana de `VistaEliminar`.
        # vista_del.ventanaDel.grab_set()
        # vista_del.ventanaDel.wait_window(vista_del.ventanaDel)
        
        # # Después de cerrar la ventana de eliminación, actualiza la vista principal
        # self.mostrar_datos_mov()
        pass