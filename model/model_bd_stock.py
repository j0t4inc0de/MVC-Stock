# Model Stock

import sqlite3
import tkinter as tk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk
# Modelo
class ModeloStock:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def get_estados(self):
        self.cursor.execute("SELECT nombre FROM Estado")
        return [state[0] for state in self.cursor.fetchall()]
    
    def add_producto(self, nombre, id_estado, precio):
        self.cursor.execute("INSERT INTO Producto (nombre, id_estado, precio) VALUES (?, ?, ?)",
                            (nombre, id_estado, precio))
        self.conn.commit()