# Model Stock

import sqlite3
import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
# Modelo
class ModeloStock:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path) # 'db_path' es la ruta que se le especifica en el controlador
        self.cursor = self.conn.cursor()

    def get_estados(self): # Obtiene los datos de la tabala estado
        self.cursor.execute("SELECT nombre FROM Estado")
        return [state[0] for state in self.cursor.fetchall()]
    
    def get_categorias(self): # Obtiene los datos de la tabla categoria
        self.cursor.execute("SELECT nombre FROM Categoria")
        return [state[0] for state in self.cursor.fetchall()]
    
    def add_producto(self, nombre, id_estado, precio, cantidad, id_categoria): # Mete los datos
        self.cursor.execute("INSERT INTO Producto (nombre, id_estado, precio, id_categoria) VALUES (?, ?, ?, ?)",
                            (nombre, id_estado, precio, id_categoria))
        self.cursor.execute("INSERT INTO Existencia (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
        self.conn.commit()

    def obtener_datos(self): # Obtiene todos los datos de esas tablas
        self.cursor.execute("""
            SELECT Producto.nombre, Producto.precio, Existencia.cantidad, Estado.nombre, Categoria.nombre
            FROM Producto
            JOIN Existencia ON Producto.nombre = Existencia.nombre
            JOIN Estado ON Producto.id_estado = Estado.id_estado
            JOIN Categoria ON Producto.id_categoria = Categoria.id_categoria
        """)
        return self.cursor.fetchall()

    def verificar_credenciales(self, usuario, contraseña): # Query para verificar que los datos ingresados usuario/contraseña estan en la base de datos
        self.cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contraseña))
        resultado = self.cursor.fetchone()
        self.conn.commit()
        return resultado