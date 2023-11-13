#Main producto
import sqlite3
import tkinter as tk
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
from controller.controlador_producto import ControladorProducto

#Cree el main para el producto.
if __name__ == "__main__":
    Producto = tk.Tk()
    Producto.resizable(height=True, width=True)
    app = ControladorProducto(Producto)
    Producto.mainloop()

#wena rodrigo lolero