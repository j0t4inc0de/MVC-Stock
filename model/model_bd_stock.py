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
        self.conn = sqlite3.connect('data/base.db')
        self.cur = self.conn.cursor()
        self.conn.commit()
    
    def insertar_prod(self, nombre, precio, cantidad):
        try:
            self.cur.execute("INSERT INTO Producto (nombre, precio) VALUES (?, ?)", (nombre, precio))
            self.cur.execute("INSERT INTO Existencia (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
        except sqlite3.Error as e:
            print("Error al insertar datos:", e)
            self.conn.rollback()  # Revertir cualquier cambio en caso de error
            return False
        finally:
            self.conn.commit()  # Confirmar la transacción

        return True