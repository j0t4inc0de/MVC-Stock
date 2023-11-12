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
    def __init__(self, ventana_principal):
        self.modelo = Modelo()
        self.ventana_principal = ventana_principal
        self.vista = Login(ventana_principal)
        self.vista.btn_ingresar.configure(command=self.verificar)

    def verificar(self):
        usuario = self.vista.entry_usuario.get().lower()
        contraseña = self.vista.entry_contraseña.get()

        resultado = self.modelo.verificar(usuario, contraseña)

        if len(usuario) == 0 or len(contraseña) == 0:
            print('Acceso denegado')
            mb.showerror('Acceso Denegado', 'Usuario/Contraseña no puede estar vacío.')
        else:
            resultado = self.modelo.verificar(usuario, contraseña)
            if resultado:
                print("Acceso concedido.")
                self.ventana_principal.withdraw()
                print("Se oculto la ventana login")
                self.mostrar_gestion_stock()
            else:
                print('Acceso denegado')
                self.vista.entry_contraseña.delete(0, 'end')
                mb.showerror('Acceso Denegado', 'Usuario/Contraseña incorrectos.')

    def mostrar_gestion_stock(self):
        from view.vista_gestion_stock import GestionStock
        top = tk.Toplevel()
        self.vista_gestion_stock = GestionStock(top, self)
        top.deiconify()
        top.protocol("WM_DELETE_WINDOW", self.cerrar_aplicacion)
        print("Se abrió gestion stock")
    
    def cerrar_aplicacion(self):
    # cierre de la aplicación
        self.ventana_principal.destroy()