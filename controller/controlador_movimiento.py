import sqlite3
from tkinter import Menu
import tkinter as tk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk

from view.vista_movimiento import VistaMovimiento

class ContorladorMovimiento:
    def __init__(self, movimiento):
        self.movimiento = VistaMovimiento(movimiento)
        self.movimiento = movimiento  # Guardamos una referencia a la ventana raíz
