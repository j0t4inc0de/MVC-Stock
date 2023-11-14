# Main Login

#Usuario: admin || Contraseña: 1
#pip install customtkinter
#pip install pillow
#pip install packaging

import sqlite3
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkthemes
from model.model_bd_usuarios import Modelo
from view.vista_login import Login 


if __name__ == "__main__":
    modelo_users = Modelo('data/base.db')
    app_principal = Login(modelo_users)
    app_principal.ventana.mainloop()
