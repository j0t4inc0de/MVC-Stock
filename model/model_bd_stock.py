# Model Stock

import sqlite3
import tkinter as tk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk
# Modelo
class ModeloStock:
    def __init__(self):
        # #Tabla Inventario
        self.conn = sqlite3.connect('data/alanorte.db')
        self.cur = self.conn.cursor()
        # self.cur.execute('''CREATE TABLE IF NOT EXISTS producto (id_producto INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, precio REAL)''')
        self.conn.commit()
    
    def insertar_prod(self, nombre, precio, cantidad):
        try:
            self.cur.execute("INSERT INTO producto (nombre, precio) VALUES (?, ?)", (nombre, precio))
            self.cur.execute("INSERT INTO existencias (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
        except sqlite3.Error as e:
            print("Error al insertar datos:", e)
            self.conn.rollback()  # Revertir cualquier cambio en caso de error
            return False
        finally:
            self.conn.commit()  # Confirmar la transacción

        return True