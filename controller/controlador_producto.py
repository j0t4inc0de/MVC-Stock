import sqlite3
from tkinter import Menu
import tkinter as tk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk

from view.vista_producto import VistaProducto

class ControladorProducto:
    def __init__(self, Producto):
        self.vista = VistaProducto(Producto)
        self.producto = Producto  # Guardamos una referencia a la ventana raíz
