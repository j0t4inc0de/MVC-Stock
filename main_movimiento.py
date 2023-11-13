import sqlite3
import tkinter as tk
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
from controller.controlador_movimiento import ContorladorMovimiento

#Cree el main para el producto.
if __name__ == "__main__":
    movimiento = tk.Tk()
    movimiento.resizable(height=True, width=True)
    app = ContorladorMovimiento(movimiento)
    movimiento.mainloop()