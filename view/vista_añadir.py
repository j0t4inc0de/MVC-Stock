# Vista añadir
import sqlite3
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk

class VistaAñadir:
    def __init__(self, ventanaAñadir):
        self.ventanaAñadir = ventanaAñadir
        self.ventanaAñadir.title("Añadir producto")
        ventanaAñadir.configure(bg="#cfe7e9")
        ventanaAñadir.geometry("400x250")
        
        self.entry_nombre = customtkinter.CTkEntry(ventanaAñadir, placeholder_text="Nombre", text_color=("gray10", "#DCE4EE"),  width=220, height=30)
        self.entry_nombre.place(x=90, y=50)
        self.entry_cantidad = customtkinter.CTkEntry(ventanaAñadir, placeholder_text="Cantidad", text_color=("gray10", "#DCE4EE"),  width=220, height=30)
        self.entry_cantidad.place(x=90, y=90)
        self.entry_precio = customtkinter.CTkEntry(ventanaAñadir, placeholder_text="Precio", text_color=("gray10", "#DCE4EE"),  width=220, height=30)
        self.entry_precio.place(x=90, y=130)

        # Botón "Listo" que llama a la función listo_click
        boton_listo = customtkinter.CTkButton(ventanaAñadir, text="Listo", fg_color="#1ace65", border_width=1, text_color="#F8F8FF", hover_color="#165c9e", border_color="#1A1A1A", width=80, height=30, command=self.listo_click)
        boton_listo.place(x=90, y=180)

    # Esta funcion se va a eliminar
    def listo_click(self):
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()
        cantidad = self.entry_cantidad.get()

        print(f"Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}")