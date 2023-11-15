# Main Login - login_main.py

# Instalaciones de modulos necesarias para el programa.
    # pip install ttkthemes
    # pip install pillow
    # pip install packaging
import sqlite3
from PIL import Image, ImageTk
from ttkthemes import ThemedTk
from controller.controlador_login import Controlador

if __name__ == "__main__":
    controlador = Controlador()
