# Model Usuarios

import sqlite3
import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageTk
# Modelo
class Modelo:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()

    def verificar(self, usuario, contraseña):
        self.cur.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contraseña))
        resultado = self.cur.fetchone()
        self.conn.commit()
        return resultado