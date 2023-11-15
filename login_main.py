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

from view.vista_login import Login
from controller.controlador_login import Controlador


if __name__ == "__main__":
    app = Controlador()
