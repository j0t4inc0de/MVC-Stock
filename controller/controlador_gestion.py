# Controller Gestion

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
        self.vista_stock = GestionStock(raiz, self)
        self.raiz = raiz  # Guardamos una referencia a la ventana raíz

        self.vista_stock.btn_añadir.configure(command=self.insertar_prod)
        self.vista_stock.btn_abrirTest.configure(command=self.abrirTest)

    def insertar_prod(self):
        nombre = self.vista_stock.entry_nombre.get().lower()
        precio = self.vista_stock.entry_precio.get()
        cantidad = self.vista_stock.entry_cantidad.get()
        resultado = self.modelo.insertar_prod(nombre, precio, cantidad)
        if resultado:
            mb.showinfo("Éxito", "Producto insertado con éxito.")
        else:
            mb.showerror("Error", "No se pudo insertar el producto.")

    def abrirTest(self):
        # Primera forma         Abre la ventana y sale el mismo error que le PREGUNTE al PROFE, NO deja usar botones
        # self.raiz.destroy()
        # print("se destruye la ventana stock\n")
        # from view.vista_gestion_ventas import GestionVentas
        # print("se importa ventas\n")
        # self.ventana = tk.Tk()
        # self.vista_ventas = GestionVentas(self.ventana, self)

        # Segunda forma     Mismo error que le PREGUNTE al PROFE, PERO SI funcionan los botones
        self.raiz.destroy()
        from controller.controlador_ventas import Controlador
        self.ventana = tk.Tk()
        self.ventana.resizable(height=True, width=True)
        app = Controlador(self.ventana)
        self.ventana.mainloop()