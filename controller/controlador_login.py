# Controlador login
import tkinter as tk
from tkinter import messagebox as mb
from model.model_bd_stock import ModeloStock
from view.vista_login import Login
from view.view_menu import VistaPrincipal

class Controlador:
    def __init__(self):
        self.modelo_stock = ModeloStock('data/base.db')
        self.vista_login = Login(None, self.modelo_stock)
        self.vista_login.btn_ingresar["command"] = self.verificar_ingreso
        self.vista_login.ventana.mainloop()

        # self.vista_login.btn_ingresar.configure(command=self.verificar)

    # Verifica el ingreso del usuario y la contraseña.
    def verificar_ingreso(self):
        # mensaje pa validar
        print("Se apretó el boton verificar en la vista")
        # Obtiene el usuario y la contraseña del usuario.
        usuario = self.vista_login.entry_usuario.get().lower()
        contraseña = self.vista_login.entry_contraseña.get()
        # Verifica si el usuario y la contraseña son correctos.
        resultado = self.modelo_stock.verificar_credenciales(usuario, contraseña)
        # Verifica si el usuario y la contraseña están vacíos.
        if len(usuario) == 0 or len(contraseña) == 0:
            print('Acceso denegado')
            mb.showerror('Acceso Denegado', 'Usuario/Contraseña no puede estar vacío.')
        else:
            resultado = self.modelo_stock.verificar_credenciales(usuario, contraseña)
            # Si son correctos, abre la vista principal.
            if resultado:
                print("Acceso concedido.")
                self.vista_login.ventana.withdraw()
                print("Se oculto la ventana login")
                self.abrir_ventana_principal()
            # Si son incorrectos, muestra un mensaje de error.
            else:
                print('Acceso denegado')
                self.vista_login.entry_contraseña.delete(0, 'end')
                mb.showerror('Acceso Denegado', 'Usuario/Contraseña incorrectos.')
    # Abre la vista principal de la aplicación.
    def abrir_ventana_principal(self):
        # Cerrar la ventana de inicio de sesión
        self.vista_login.ventana.destroy()

        # Abrir la ventana principal
        vista_principal = VistaPrincipal(self.modelo_stock)
        vista_principal.ejecutar()