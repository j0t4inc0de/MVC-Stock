# View Menu
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
class VistaPrincipal:
    def __init__(self, modelo_stock):
        self.ventanaPrincipal = ThemedTk(theme="arc")
        self.ventanaPrincipal.title("Gestión de Stock")
        self.ventanaPrincipal.geometry("1010x400")
        self.modelo_stock = modelo_stock

        # Treeview es la tabla donde pondremos los datos de la bd
        self.treeview = ttk.Treeview(self.ventanaPrincipal, columns=("Nombre", "Precio", "Cantidad", "Estado", "Categoría"), show="headings")
        self.treeview.heading("Nombre", text="Nombre")
        self.treeview.heading("Precio", text="Precio")
        self.treeview.heading("Cantidad", text="Cantidad")
        self.treeview.heading("Estado", text="Estado")
        self.treeview.heading("Categoría", text="Categoría")
        self.treeview.pack(pady=10)

        self.mostrar_datos()
        # boton para actualizar la tabal
        ttk.Button(self.ventanaPrincipal, text="Actualizar", command=self.mostrar_datos).pack(pady=10)
        ttk.Button(self.ventanaPrincipal, text="Añadir Producto", command=self.abrir_vista_producto).pack(pady=10)
        


        # Rodrigo- Se agrega la imagen para boton actualizar
        self.imagen_actualizar = Image.open("view/images/Actualizar24px.png")
        self.imagen_actualizar.thumbnail((250, 250))
        self.imagen_actualizar = ImageTk.PhotoImage(self.imagen_actualizar)
        self.label_actualizar = ttk.Button(self.ventanaPrincipal, image=self.imagen_actualizar).place(x=390,y=289)
        
        # Rodrigo- Se agrega la imagen para boton Añadir.
        self.imagen_anadir = Image.open("view/images/Anadir.png")
        self.imagen_anadir.thumbnail((250, 250))
        self.imagen_anadir = ImageTk.PhotoImage(self.imagen_anadir)
        self.label_anadir = ttk.Button(self.ventanaPrincipal, image=self.imagen_anadir).place(x=600,y=338)

        # Rodrigo Se agrega la imagen para boton Eliminar.
        self.imagen_eliminar = Image.open("view/images/Eliminar.png")
        self.imagen_eliminar.thumbnail((250, 250))
        self.imagen_eliminar = ImageTk.PhotoImage(self.imagen_eliminar)
        self.label_eliminar = ttk.Button(self.ventanaPrincipal, image=self.imagen_eliminar).place(x=600,y=289)

        # Rodrigo Se agrega la imagen para boton Editar.
        self.imagen_editar = Image.open("view/images/Editar.png")
        self.imagen_editar.thumbnail((250, 250))
        self.imagen_editar = ImageTk.PhotoImage(self.imagen_editar)
        self.label_editar = ttk.Button(self.ventanaPrincipal, image=self.imagen_editar).place(x=100,y=289)

        # Imagen Lupa
        self.imagen_buscar = Image.open("view/images/Buscar24px.png")
        self.imagen_buscar.thumbnail((250, 250))
        self.imagen_buscar = ImageTk.PhotoImage(self.imagen_buscar)
        self.label_buscar = ttk.Button(self.ventanaPrincipal, image=self.imagen_buscar).place(x=390,y=338)

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

