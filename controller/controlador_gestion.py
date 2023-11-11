# Controller

import sqlite3
from tkinter import Menu
import tkinter as tk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk

from model.model_bd_stock import ModeloStock
from view.vista_gestion_stock import GestionStock
from view.vista_gestion_ventas import GestionVentas

class Controlador:
    def __init__(self, raiz):
        self.modelo = ModeloStock()
        self.vista = GestionStock(raiz, self)
        self.raiz = raiz  # Guardamos una referencia a la ventana raíz

        self.vista.btn_añadir.configure(command=self.insertar_prod)
    def insertar_prod(self):
        nombre = self.vista.entry_nombre.get().lower()
        precio = self.vista.entry_precio.get()
        cantidad = self.vista.entry_cantidad.get()
        resultado = self.modelo.insertar_prod(nombre, precio, cantidad)
        if resultado:
            mb.showinfo("Éxito", "Producto insertado con éxito.")
        else:
            mb.showerror("Error", "No se pudo insertar el producto.")

    # def irventa(self):
    #     self.raiz.destroy()
    #     self.raiz = tk.Tk()  # Crea una nueva ventana raíz
    #     from view.vista_gestion_ventas import GestionVentas
    #     self.vistaVentas = GestionVentas(self.raiz, self)  # Abre la nueva vista en la nueva ventana

    # def irstock(self):
    #     self.raiz.destroy()
    #     self.raiz = tk.Tk()  # Crea una nueva ventana raíz
    #     from view.vista_gestion_stock import GestionStock
    #     self.vistaStock = GestionStock(self.raiz, self)  # Abre la nueva vista en la nueva ventana

    # def salir(self):
    #     if mb.askyesno('Salir', 'Esta seguro de salir?'):
    #         self.raiz.destroy()