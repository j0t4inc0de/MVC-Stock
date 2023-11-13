#Vista del movimiento 
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
import customtkinter

class  VistaMovimiento:
    def __init__(self,ventanaMovimiento):
        self.ventanaMovimiento = ventanaMovimiento
        self.ventanaMovimiento.title("Añadir Movimiento")
        ventanaMovimiento.configure(bg="#2B2B2B")
        ventanaMovimiento.geometry("400x350")
        
        self.entry_nombre_movimiento = customtkinter.CTkEntry(ventanaMovimiento, placeholder_text="nombre", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        self.entry_nombre_movimiento.place(x=90, y=50)
        self.entry_nombre_existencia = customtkinter.CTkEntry(ventanaMovimiento, placeholder_text="Nombre Existencia", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        self.entry_nombre_existencia.place(x=90, y=90)
        self.entry_cantidad_mov = customtkinter.CTkEntry(ventanaMovimiento, placeholder_text="Cantidad Movimiento", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        self.entry_cantidad_mov.place(x=90, y=130)
        self.entry_fecha = customtkinter.CTkEntry(ventanaMovimiento, placeholder_text="Fecha", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        self.entry_fecha.place(x=90, y=170)
        self.entry_descripcion = customtkinter.CTkEntry(ventanaMovimiento, placeholder_text="Descripcion", text_color=("gray51", "#DCE4EE"),   width=220, height=30)  
        self.entry_descripcion.place(x=90, y=210)

        bton_listo = customtkinter.CTkButton(ventanaMovimiento, text="Listo", fg_color="SpringGreen3", border_width=1, text_color="white smoke", hover_color="#165c9e", border_color="#1A1A1A", width=80, height=30, command=self.listo_click)
        bton_listo.place(x=90, y=250)

    def listo_click(self):
        nombremovimiento = self.entry_nombre_movimiento.get()
        nombrexistencia = self.entry_nombre_existencia.get()
        cantidad_movi = self.entry_cantidad_mov.get()
        fecha = self.entry_fecha.get()
        descripcion = self.entry_descripcion.get()

        print(f"Nombre: {nombremovimiento},  Precio: {nombrexistencia}, Estado:{cantidad_movi}, Cateogria:{fecha} , Cantidad: {descripcion}")

