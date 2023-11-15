# Main Login

# Usuario: admin || Contraseña: 1
# pip install customtkinter
# pip install pillow
# pip install packaging

import tkinter as tk
from model.model_bd_usuarios import Modelo
from view.vista_login import Login

def run_login_app():
    modelo_users = Modelo('data/base.db')
    app = Login(modelo_users)
    app.ventana.mainloop()

if __name__ == "__main__":
    run_login_app()