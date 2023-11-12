# Controller Ventas

import sqlite3
from tkinter import Menu
import tkinter as tk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk

from model.model_bd_stock import ModeloStock
from view.vista_gestion_ventas import GestionVentas

class Controlador:
    def __init__(self, ventana):
        self.modelo = ModeloStock()
        self.vista_ventas = GestionVentas(ventana, self)
        self.ventana = ventana  # Guardamos una referencia a la ventana ventana

        self.vista_ventas.btn_test.configure(command=self.print_test)
        
    def print_test(self):
        print("Se presiono el boton 'Print test' de la vista gestion ventas...")

        