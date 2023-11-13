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
        print("se destruye la view stock\n")
        from controller.controlador_ventas import Controlador
        print("se importa CONTROLADOR\n")
        self.ventana = tk.Tk()
        self.ventana.resizable(height=True, width=True)
        app = Controlador(self.ventana)
        print("Se hace mainloop de controlador a la ventana\n")
        self.ventana.mainloop()
        print("se hizo mainloop (este print se ejecuto al cerrar la view ventas, raro¿?)")