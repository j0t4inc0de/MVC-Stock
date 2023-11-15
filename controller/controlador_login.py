# Controlador login
import sqlite3
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk

from model.model_bd_usuarios import Modelo
from view.vista_login import Login

class Controlador:
    def __init__(self):
        self.modelo_usuarios = Modelo('data/base.db')
        self.vista_login = Login(None, self.modelo_usuarios)

        self.vista_login.btn_ingresar.configure(command=self.verificar)
        self.vista_login.ventana.mainloop()

    def verificar(self):
        print("Se apretó el boton verificar en la vista")
        usuario = self.vista_login.entry_usuario.get().lower()
        contraseña = self.vista_login.entry_contraseña.get()

        resultado = self.modelo_usuarios.verificar(usuario, contraseña)

        if len(usuario) == 0 or len(contraseña) == 0:
            print('Acceso denegado')
            mb.showerror('Acceso Denegado', 'Usuario/Contraseña no puede estar vacío.')
        else:
            resultado = self.modelo_usuarios.verificar(usuario, contraseña)
            if resultado:
                print("Acceso concedido.")
                self.vista_login.ventana.withdraw()
                print("Se oculto la ventana login")
                self.mostrar_gestion_stock()
            else:
                print('Acceso denegado')
                self.vista_login.entry_contraseña.delete(0, 'end')
                mb.showerror('Acceso Denegado', 'Usuario/Contraseña incorrectos.')

    def mostrar_gestion_stock(self):
        from view.view_menu import VistaPrincipal
        top = tk.Toplevel()
        self.vista_menu = VistaPrincipal(top, self)
        top.deiconify()
        top.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)
        print("Se abrió 'view_menu.py' ")
    
    def cerrar_aplicacion(self):
        # cierre de la aplicación
        self.vista_login.ventana.destroy()