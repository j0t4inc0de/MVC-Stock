# View Menu
import re
import tkinter as tk
from tkinter import ttk, Label, Button
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import xlsxwriter
import os
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
# Inicializa la ventana principal.        
class VistaPrincipal:
    def __init__(self, modelo_stock):
        self.ventanaPrincipal = ThemedTk(theme="arc")
        self.ventanaPrincipal.title("Gestión de Stock")
        self.ventanaPrincipal.geometry("1100x430")
        self.ventanaPrincipal.resizable(width=False, height=False)
        self.modelo_stock = modelo_stock

        # Treeview es la tabla donde pondremos los datos de la bd
        self.treeview = ttk.Treeview(self.ventanaPrincipal, columns=("Producto", "Precio", "Cantidad", "Estado", "Categoría"), show="headings", height=16)
        self.treeview.heading("Producto", text="Producto")
        self.treeview.column("Producto", width=280)
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
        self.imagen_mov = ImageTk.PhotoImage(self.imagen_mov)
        self.label_mov = ttk.Button(self.ventanaPrincipal, image=self.imagen_mov, command=self.abrir_vista_movimiento)
        self.label_mov.place(x=630,y=2)
        CustomHovertip(self.label_mov, text="Movimiento", hover_delay=50)

        # Buscar
        #Entry del Buscar
        self.entry_buscar = ttk.Entry(self.ventanaPrincipal, width=46)
        self.entry_buscar.place(x=1, y=19)
        self.entry_buscar.insert(0, "Buscador")
        self.entry_buscar.bind('<FocusIn>', self.on_entry_click)
        self.entry_buscar.bind('<FocusOut>', self.on_focusout)
        self.imagen_buscar = Image.open("view/images/buscar-512px.png")
        self.imagen_buscar.thumbnail((30, 30))
        self.imagen_buscar = ImageTk.PhotoImage(self.imagen_buscar)
        self.label_buscar = ttk.Button(self.ventanaPrincipal, image=self.imagen_buscar, command=self.buscar_nombre)
        self.label_buscar.place(x=295,y=2)
        CustomHovertip(self.label_buscar, text="Buscar", hover_delay=50)


        # Actualizar
        self.imagen_actualizar = Image.open("view/images/actualizar-512px.png")
        self.imagen_actualizar.thumbnail((30, 30))
        self.imagen_actualizar = ImageTk.PhotoImage(self.imagen_actualizar)
        self.label_actualizar = ttk.Button(self.ventanaPrincipal, image=self.imagen_actualizar, command=self.mostrar_datos)
        self.label_actualizar.place(x=360,y=2)
        CustomHovertip(self.label_actualizar, text="Actualizar", hover_delay=50)#Asina lo que se quiera mostrar al pasar el cursor por encima del boton
        
        # Añadir.
        self.imagen_anadir = Image.open("view/images/añadir-512px.png")
        self.imagen_anadir.thumbnail((30, 30))
        self.imagen_anadir = ImageTk.PhotoImage(self.imagen_anadir)
        self.label_anadir = ttk.Button(self.ventanaPrincipal, image=self.imagen_anadir, command=self.abrir_vista_producto)
        self.label_anadir.place(x=450,y=2)
        CustomHovertip(self.label_anadir, text="Añadir", hover_delay=50)#Asina lo que se quiera mostrar al pasar el cursor por encima del boton

        #Eliminar
        self.imagen_eliminar = Image.open("view/images/eliminar-512px.png")
        self.imagen_eliminar.thumbnail((30, 30))
        self.imagen_eliminar = ImageTk.PhotoImage(self.imagen_eliminar)
        # Crear el botón sin colocarlo directamente, para poder asignar el CustomHovertip
        self.label_eliminar = ttk.Button(self.ventanaPrincipal, image=self.imagen_eliminar, command=self.abrir_vista_del)
        self.label_eliminar.place(x=510, y=2)
        # Aplicar el CustomHovertip
        CustomHovertip(self.label_eliminar, text="Eliminar", hover_delay=50)

        # Editar.
        self.imagen_editar = Image.open("view/images/editar-512px.png")
        self.imagen_editar.thumbnail((30, 30))
        self.imagen_editar = ImageTk.PhotoImage(self.imagen_editar)
        self.label_editar = ttk.Button(self.ventanaPrincipal, image=self.imagen_editar, command=self.abrir_vista_editar)
        self.label_editar.place(x=570,y=2)
        CustomHovertip(self.label_editar, text="Editar", hover_delay=50)#Asina lo que se quiera mostrar al pasar el cursor por encima del boton
        

        # Excel.
        self.imagen_imprimir = Image.open("view/images/excel512px.png")
        self.imagen_imprimir.thumbnail((30, 30))
        self.imagen_imprimir = ImageTk.PhotoImage(self.imagen_imprimir)
        self.label_imprimir = ttk.Button(self.ventanaPrincipal, image=self.imagen_imprimir, command=self.Excel_Datos)
        self.label_imprimir.place(x=690,y=2)
        CustomHovertip(self.label_imprimir, text="Imprimir Excel", hover_delay=50)#Asina lo que se quiera mostrar al pasar el cursor por encima del boton
        
    
        self.ventanaPrincipal.after(500, self.aviso_stock) # Da tiempo para que se genere el aviso denuevo desspues de avierto 7 MINUTOS 420000
        self.ventanaPrincipal.after(420000, self.aviso_stock) # Da tiempo para que se genere el aviso denuevo desspues de avierto 7 MINUTOS 420000
           
    # Función `mostrar_datos()`: Muestra los datos de la base de datos en la tabla.
    def mostrar_datos(self):
        # Obtiene los datos de la base de datos.
        datos = self.modelo_stock.obtener_datos()

        # Elimina todos los elementos de la tabla.
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        # Agrega los datos a la tabla.
        for dato in datos:
            self.treeview.insert("", "end", values=dato)

    # Función `abrir_vista_producto()`:       
    def abrir_vista_producto(self):
        from view.vista_producto import VistaProducto
        # Crea un objeto de la clase `VistaProducto`.
        vista_producto = VistaProducto(self,self.modelo_stock)  
        # Muestra la ventana de `VistaProducto`.
        vista_producto.ventanaProducto.grab_set()
        vista_producto.ventanaProducto.wait_window(vista_producto.ventanaProducto)
        
    # Función `abrir_vista_movimiento()`:
    def abrir_vista_movimiento(self):
        # Cierra la ventana actual.
        self.ventanaPrincipal.destroy()
        from view.vista_movimiento_menu import VistaMenuMov
        # Crea un objeto de la clase `VistaMenuMov`.
        vista_movimiento = VistaMenuMov(self, self.modelo_stock)
        vista_movimiento.ventanaMenuMov.grab_set()
        vista_movimiento.ventanaMenuMov.wait_window(vista_movimiento.ventanaMenuMov)

    # Función `abrir_vista_del()`:
    def abrir_vista_del(self):
        from view.vista_eliminar import VistaEliminar
        # Crea un objeto de la clase `VistaEliminar`.
        vista_del = VistaEliminar(self, self.modelo_stock)
        # Muestra la ventana de `VistaEliminar`.
        vista_del.ventanaDel.grab_set()
        vista_del.ventanaDel.wait_window(vista_del.ventanaDel)
        
    # Función `abrir_vista_editar()`: 
    def abrir_vista_editar(self):
        from view.vista_editar import VistaEditar
        # Crea un objeto de la clase `VistaEditar`.
        vista_editar = VistaEditar(self, self.modelo_stock)
        # Muestra la ventana de `VistaEditar`.
        vista_editar.ventanaED.grab_set()
        vista_editar.ventanaED.wait_window(vista_editar.ventanaED)
    # Inicia el bucle principal de la ventana.
    def ejecutar(self):
        self.ventanaPrincipal.mainloop()
    # Maneja el evento de clic en el cuadro de búsqueda.
    def on_entry_click(self, event):
        # Verifica si el texto del cuadro de búsqueda es el placeholder "Buscador".
        if self.entry_buscar.get() == 'Buscador':
            # Borra el texto del placeholder.
            self.entry_buscar.delete(0, "end")
            self.entry_buscar.insert(0, '')
    # Maneja el evento de pérdida de foco del cuadro de búsqueda.
    def on_focusout(self, event):
        # Verifica si el texto del cuadro de búsqueda está vacío.
        if self.entry_buscar.get() == '':
            # Reemplaza el texto vacío con el placeholder "Buscador".
            self.entry_buscar.insert(0, 'Buscador')

    def buscar_nombre(self):
        # Busca por nombre al apretar la lupa
        global tree
        nombre_buscador = self.entry_buscar.get().lower()
        palabras = nombre_buscador.split()
        datos = self.modelo_stock.buscar_nombre(nombre_buscador)
        # Verifica que la entrada del usuario no sea vacía
        if not palabras:
            messagebox.showwarning("Ups!", "No ingresaste nada.")
            self.entry_buscar.delete(0, "end")
            self.entry_buscar.insert(0, 'Buscador')
            self.mostrar_datos()
            return
        # Verifica que la entrada del usuario no sea el placeholder
        if palabras[0] == "buscador":
            messagebox.showwarning("Ups!", "No ingresaste nada.")
            self.entry_buscar.delete(0, "end")
            self.entry_buscar.insert(0, 'Buscador')
            self.mostrar_datos()
            return
        if not datos:
            messagebox.showwarning("Ups!", "El producto no existe.")
            self.entry_buscar.delete(0, "end")
            self.entry_buscar.insert(0, "Buscador")
            self.mostrar_datos()
            return
        # Verifica que cada palabra sea alfabética
        for palabra in palabras:
            if not palabra.isalpha():
                messagebox.showwarning("Ups!", "Ingresa un nombre valido.")
                self.entry_buscar.delete(0, "end")
                self.entry_buscar.insert(0, 'Buscador')
                self.mostrar_datos()
                return
        # Si todo está bien, realiza la búsqueda
        print(f"Se escribio un producto: '{nombre_buscador}'")
        datos = self.modelo_stock.buscar_nombre(nombre_buscador)
        for item in self.treeview.get_children():
            self.treeview.delete(item)
        for dato in datos:
            self.treeview.insert("", "end", values=dato)
            self.entry_buscar.delete(0, "end")
            self.entry_buscar.insert(0, 'Buscador')
    
    def Excel_Datos(self):
        # Obtiene todos los datos del modelo de stock utilizando el método `obtener_datos()`.
        datos = self.modelo_stock.obtener_datos()
        # Crea una lista vacía para almacenar los datos a exportar.
        data=[]
        # Itera sobre la lista de datos del modelo de stock y agrega cada dato a la lista `data`.
        for dato in datos:
            data.append(dato)
        # Crea una lista vacía para cada columna del archivo de Excel.
        tabla=data
        nombres=[]
        precios=[]
        cantidad=[]
        estados=[]
        categoria=[]
        # Itera sobre la lista `data` y separa cada elemento en sus componentes individuales (nombre, precio, cantidad, estado y categoría) y los agrega a las listas correspondientes.
        for i in range(len(tabla)):
            a,b,c,d,e=tabla[i]
            nombres.append(a)
            precios.append(b)
            cantidad.append(c)
            estados.append(d)
            categoria.append(e)
        # Crea un objeto de libro de trabajo de Excel con el nombre "Productos.xlsx".
        workbook = xlsxwriter.Workbook('Productos.xlsx')
        # Crea una hoja de trabajo dentro del libro de trabajo.
        worksheet = workbook.add_worksheet()
        # Escribe los encabezados de las columnas (`Nombre`, `Precio`, `Cantidad`, `Estado` y `Categoría`) en la primera fila de la hoja de trabajo.
        worksheet.write('A1', 'Nombre')
        worksheet.write('B1', 'Precio')
        worksheet.write('C1', 'Cantidad')
        worksheet.write('D1', 'Estado')
        worksheet.write('E1', 'Categoria')
        # Itera sobre las listas de datos de cada columna y escribe cada elemento en la fila correspondiente de la hoja de trabajo.
        for i in range(len(nombres)):
            cell=str(i+2) # Crea la celda a partir del índice + 2 (para evitar la fila de encabezados)
            nombre_dato=str(nombres[i])
            worksheet.write('A'+cell,nombre_dato) # Escribe el nombre del producto en la celda correspondiente
            precio_dato=str(precios[i])  
            worksheet.write('B'+cell,precio_dato)
            cantidad_dato=cantidad[i]
            worksheet.write('C'+cell,cantidad_dato)
            estado_dato=estados[i]
            worksheet.write('D'+cell,estado_dato)
            categoria_dato=categoria[i]
            worksheet.write('E'+cell,categoria_dato)
        # Cierra el libro de trabajo.
        workbook.close()
        os.system("start EXCEL.EXE Productos.xlsx")
    # Función `aviso_stock()`: Muestra un aviso cuando el stock de un producto es bajo.
    def aviso_stock(self):
        # Obtiene los datos de la base de datos.
        datos = self.modelo_stock.obtener_datos()
        # Stock bajo.
        stock_bajo = 10
        # Itera sobre los datos.
        for dato in datos:
            nombre, precio, cantidad, estado, categoria = dato
            # Verifica si la cantidad es menor o igual al stock bajo.
            if cantidad <= stock_bajo:
                # Muestra un mensaje de advertencia.
                messagebox.showwarning("Stock bajo", f"El producto '{nombre}' tiene un stock bajo ({cantidad}).")
                return