# Este es el main que solo hace correr el ventas

import sqlite3
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
from controller.controlador_ventas import Controlador
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.resizable(height=True, width=True)
    app = Controlador(ventana)
    ventana.mainloop()