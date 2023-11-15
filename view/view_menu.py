# View Menu
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
class VistaPrincipal:
    def __init__(self, modelo_stock):
        self.ventanaPrincipal = ThemedTk(theme="arc")
        self.ventanaPrincipal.title("Gestión de Stock")
        self.ventanaPrincipal.geometry("1100x430")
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
        # boton para actualizar la tabal
        # ttk.Button(self.ventanaPrincipal, text="Actualizar", command=self.mostrar_datos).pack(pady=10)
        # ttk.Button(self.ventanaPrincipal, text="Añadir Producto", command=self.abrir_vista_producto).pack(pady=10)
        
        # Entry para buscar - funcionalidad para buscar NO ECHA
        self.entry_buscar = ttk.Entry(self.ventanaPrincipal, width=46)
        self.entry_buscar.place(x=0, y=18)

        # Imagen Lupa
        self.imagen_buscar = Image.open("view/images/buscar-512px.png")
        self.imagen_buscar.thumbnail((30, 30))
        self.imagen_buscar.resize((30, 30))
        self.imagen_buscar = ImageTk.PhotoImage(self.imagen_buscar)
        self.label_buscar = ttk.Button(self.ventanaPrincipal, image=self.imagen_buscar).place(x=295,y=0)

        # Rodrigo- Se agrega la imagen para boton actualizar
        self.imagen_actualizar = Image.open("view/images/actualizar-512px.png")
        self.imagen_actualizar.thumbnail((30, 30))
        self.imagen_actualizar.resize((30, 30))
        self.imagen_actualizar = ImageTk.PhotoImage(self.imagen_actualizar)
        self.label_actualizar = ttk.Button(self.ventanaPrincipal, image=self.imagen_actualizar, command=self.mostrar_datos).place(x=360,y=0)
        
        # Rodrigo- Se agrega la imagen para boton Añadir.
        self.imagen_anadir = Image.open("view/images/añadir-512px.png")
        self.imagen_anadir.thumbnail((30, 30))
        self.imagen_anadir.resize((30, 30))
        self.imagen_anadir = ImageTk.PhotoImage(self.imagen_anadir)
        self.label_anadir = ttk.Button(self.ventanaPrincipal, image=self.imagen_anadir, command=self.abrir_vista_producto).place(x=450,y=0)

        # Rodrigo Se agrega la imagen para boton Eliminar.
        self.imagen_eliminar = Image.open("view/images/eliminar-512px.png")
        self.imagen_eliminar.thumbnail((30, 30))
        self.imagen_eliminar.resize((30, 30))

        self.imagen_eliminar = ImageTk.PhotoImage(self.imagen_eliminar)
        self.label_eliminar = ttk.Button(self.ventanaPrincipal, image=self.imagen_eliminar).place(x=510,y=0)

        # Rodrigo Se agrega la imagen para boton Editar.
        self.imagen_editar = Image.open("view/images/editar-512px.png")
        self.imagen_editar.thumbnail((30, 30))
        self.imagen_editar.resize((30, 30))

        self.imagen_editar = ImageTk.PhotoImage(self.imagen_editar)
        self.label_editar = ttk.Button(self.ventanaPrincipal, image=self.imagen_editar).place(x=570,y=0)

    def mostrar_datos(self):
        for item in self.treeview.get_children():
            self.treeview.delete(item)

        datos = self.modelo_stock.obtener_datos() # obtiene los datos del model

        # inserta los datos al treiview
        for dato in datos:
            self.treeview.insert("", "end", values=dato)
            
    def abrir_vista_producto(self):
        from view.vista_producto import VistaProducto
        vista_producto = VistaProducto(self.ventanaPrincipal, self.modelo_stock)
        vista_producto.ventanaProducto.grab_set()
        vista_producto.ventanaProducto.wait_window(vista_producto.ventanaProducto)

    def ejecutar(self):
        self.ventanaPrincipal.mainloop()