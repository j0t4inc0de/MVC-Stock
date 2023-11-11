# Model

import sqlite3
import tkinter as tk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk
# Modelo
class Modelo:
    def __init__(self):
        # Tabla Usuarios
        self.conn = sqlite3.connect('data/base.db')
        self.cur = self.conn.cursor()
        # self.cur.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, contraseña INTEGER)")

    def verificar(self, usuario, contraseña):
        self.cur.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contraseña))
        resultado = self.cur.fetchone()
        self.conn.commit()
        return resultado