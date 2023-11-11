# Main Login
#pip install customtkinter
#pip install pillow
#pip install packaging
import sqlite3
import tkinter as tk
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk


from controller.controlador_login import Controlador
if __name__ == "__main__":
    ventana = tk.Tk()
    app = Controlador(ventana)
    ventana.mainloop() 