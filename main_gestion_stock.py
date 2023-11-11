
import sqlite3
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk
from controller.controlador_gestion import Controlador
if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.resizable(height=True, width=True)
    app = Controlador(raiz)
    raiz.mainloop()