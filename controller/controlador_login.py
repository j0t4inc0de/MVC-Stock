# Controlador login
import tkinter as tk
from tkinter import messagebox as mb
from model.model_bd_usuarios import Modelo
from view.vista_login import Login
from view.view_menu import VistaPrincipal

class Controlador:
    def __init__(self):
        self.modelo_usuarios = Modelo('data/base.db')
        self.vista_login = Login(None, self.modelo_usuarios)
        self.vista_login.btn_ingresar.configure(command=self.verificar)
        
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
                self.mostrar_menu()
            else:
                print('Acceso denegado')
                self.vista_login.entry_contraseña.delete(0, 'end')
                mb.showerror('Acceso Denegado', 'Usuario/Contraseña incorrectos.')

    def mostrar_menu(self):
        pass

    def cerrar_aplicacion(self):
        # cierre de la aplicación
        self.menu_principal.ventana.destroy()

    def run(self):
        self.vista_login.ventana.mainloop()

if __name__ == "__main__":
    app = Controlador()
    app.run()
