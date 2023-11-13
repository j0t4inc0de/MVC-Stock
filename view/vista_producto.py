#View producto.
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
import customtkinter

class  VistaProducto:
    def __init__(self,ventanaProducto):
        self.ventanaProducto = ventanaProducto
        self.ventanaProducto.title("Añadir Producto")
        #cambio de color de la vista producto.
        ventanaProducto.configure(bg="#2B2B2B")
        ventanaProducto.geometry("400x350")

        self.select_estado = customtkinter.StringVar()

        # self.entry_nombre_producto = customtkinter.CTkEntry(ventanaProducto, placeholder_text="nombre", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        # self.entry_nombre_producto.place(x=90, y=50)
        # self.entry_precio_producto = customtkinter.CTkEntry(ventanaProducto, placeholder_text="precio", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        # self.entry_precio_producto.place(x=90, y=90)

        # self.entry_nombre_estado = customtkinter.CTkEntry(ventanaProducto, placeholder_text="estado", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        # self.entry_nombre_estado.place(x=90, y=130)
        # self.entry_nombre_ctg = customtkinter.CTkEntry(ventanaProducto, placeholder_text="categoría", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        # self.entry_nombre_ctg.place(x=90, y=170)
        # self.entry_cantidad_existencia = customtkinter.CTkEntry(ventanaProducto, placeholder_text="existencia", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        # self.entry_cantidad_existencia.place(x=90, y=210)

        bton_listo = customtkinter.CTkButton(ventanaProducto, text="Listo", fg_color="SpringGreen3", border_width=1, text_color="white smoke", hover_color="#165c9e", border_color="#1A1A1A", width=80, height=30, command=self.listo_click)
        bton_listo.place(x=90, y=250)


        self.entry_nombre_producto = customtkinter.CTkEntry(ventanaProducto, placeholder_text="nombre", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        self.entry_nombre_producto.place(x=90, y=50)

        self.entry_precio_producto = customtkinter.CTkEntry(ventanaProducto, placeholder_text="precio", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        self.entry_precio_producto.place(x=90, y=90)
        
        self.combobox_estado = customtkinter.CTkComboBox(ventanaProducto, variable=)