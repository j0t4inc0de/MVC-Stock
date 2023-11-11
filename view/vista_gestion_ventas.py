# View Gestion VENTAS
import sqlite3
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mb
import customtkinter

class GestionVentas:
    def __init__(self, ventana, controlador):
        ventana.title("Nueva Gestion de ventas")
        ventana.geometry("1080x600")
        titulo = customtkinter.CTkLabel(ventana, text="Gestion de ventas", width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)  # Cambiado aquí
        titulo.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    
        self.menu = Menu(ventana)
        self.menuinicio = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='Inicio', menu=self.menuinicio)
        self.menuinicio.add_command(label='Ir a Stock', command=controlador.irstock)
        self.menuinicio.add_command(label='Salir', command=controlador.salir)
        ventana.config(menu=self.menu)
