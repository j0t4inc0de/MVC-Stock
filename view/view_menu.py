# View Menu
import re
import tkinter as tk
from tkinter import ttk, Label, Button
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import xlsxwriter
import os

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
        self.aviso_stock()
        self.ventanaPrincipal.after(6000000, self.aviso_stock)# da tiempo para que se genere el aviso denuevo desspues de avierto
       
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
        self.label_buscar = ttk.Button(self.ventanaPrincipal, image=self.imagen_buscar, command=self.buscar_nombre).place(x=295,y=2)

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

        # Excel.
        self.imagen_imprimir = Image.open("view/images/excel512px.png")
        self.imagen_imprimir.thumbnail((30, 30))
        self.imagen_imprimir.resize((30, 30))
        self.imagen_imprimir = ImageTk.PhotoImage(self.imagen_imprimir)
        self.label_imprimir = ttk.Button(self.ventanaPrincipal, image=self.imagen_imprimir, command=self.Excel_Datos).place(x=700,y=2)     
        
    

    def mostrar_datos(self):
        # Llamada a la función obtener_datos del modelo_stock
        datos = self.modelo_stock.obtener_datos()

        for item in self.treeview.get_children():
            self.treeview.delete(item)
            
        for dato in datos:
            self.treeview.insert("", "end", values=dato)

    # Abre la vista       
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

    # Abre la vista delete
    def abrir_vista_del(self):
        from view.vista_eliminar import VistaEliminar
        vista_del = VistaEliminar(self, self.modelo_stock)
        vista_del.ventanaDel.grab_set()
        vista_del.ventanaDel.wait_window(vista_del.ventanaDel)
        
    # Abre la vista editar    
    def abrir_vista_editar(self):
        from view.vista_editar import VistaEditar
        vista_editar = VistaEditar(self, self.modelo_stock)
        vista_editar.ventanaED.grab_set()
        vista_editar.ventanaED.wait_window(vista_editar.ventanaED)
        
    def ejecutar(self):
        self.ventanaPrincipal.mainloop()

    def on_entry_click(self, event):
        if self.entry_buscar.get() == 'Buscador':
            self.entry_buscar.delete(0, "end")
            self.entry_buscar.insert(0, '')

    def on_focusout(self, event):
        if self.entry_buscar.get() == '':
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
    
    def Excel_Datos(self):
        datos = self.modelo_stock.obtener_datos()
        data=[]
        for dato in datos:
            data.append(dato)
        tabla=data
        nombres=[]
        precios=[]
        cantidad=[]
        estados=[]
        categoria=[]
        for i in range(len(tabla)):
            a,b,c,d,e=tabla[i]
            nombres.append(a)
            precios.append(b)
            cantidad.append(c)
            estados.append(d)
            categoria.append(e)
        workbook = xlsxwriter.Workbook('Productos.xlsx')
        worksheet = workbook.add_worksheet()
        
        worksheet.write('A1', 'Nombre')
        worksheet.write('B1', 'Precio')
        worksheet.write('C1', 'Cantidad')
        worksheet.write('D1', 'Estado')
        worksheet.write('E1', 'Categoria')

        for i in range(len(nombres)):
            cell=str(i+2)

            nombre_dato=str(nombres[i])
            worksheet.write('A'+cell,nombre_dato)

            precio_dato=str(precios[i])  
            worksheet.write('B'+cell,precio_dato)

            cantidad_dato=cantidad[i]
            worksheet.write('C'+cell,cantidad_dato)

            estado_dato=estados[i]
            worksheet.write('D'+cell,estado_dato)

            categoria_dato=categoria[i]
            worksheet.write('E'+cell,categoria_dato)
            
        workbook.close()
        os.system("start EXCEL.EXE Productos.xlsx")
        
    def aviso_stock(self):
        datos = self.modelo_stock.obtener_datos()
        stock_bajo = 10
        
        for dato in datos:
            nombre, precio, cantidad, estado, categoria = dato
            if cantidad <= stock_bajo:
                messagebox.showwarning("Stock bajo", f"El producto '{nombre}' tiene un stock bajo ({cantidad}).")


