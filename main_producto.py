# Main producto
import sqlite3
import tkinter as tk
from tkinter import messagebox
import customtkinter
from PIL import Image, ImageTk

from controller.controlador_producto import Controlador

#Cree el main para el producto.
if __name__ == "__main__":
    app = Controlador()