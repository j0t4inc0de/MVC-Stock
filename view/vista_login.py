# View login
import sqlite3
import tkinter as tk
from tkinter import  Label, ttk, PhotoImage, messagebox as mb
from PIL import Image, ImageTk
from ttkthemes import ThemedTk

class Login:
    def __init__(self, modelo_users):
        self.ventana = ThemedTk(theme="arc")
        self.ventana.title("AlaNorte")
        self.ventana.geometry("400x600")
        self.modelo_users=modelo_users

         # Blanco cabros
        # ventana.configure(bg="#2B2B2B") # Color oscuro cabros

        # Imagen de otro logo LOGO.PNG
        # self.imagen = PhotoImage(file='view/images/logo.png')
        # self.imagen.ajustada = self.imagen.subsample(6,5)
        # self.label_imagen = Label(ventana, image =self.imagen.ajustada)
        # self.label_imagen.pack()
        # self.label_imagen.place(x=115,y=5)
        
        # Rodrigo se arregla el error del tema llamando a la funcion ttk.
        self.imagen_logo = Image.open("view/images/logo.png")
        self.imagen_logo.thumbnail((250, 250))
        self.imagen_logo = ImageTk.PhotoImage(self.imagen_logo)
        self.label_logo = ttk.Button(self.ventana, image=self.imagen_logo).place(x=70,y=5)

        #Rodrigo - Nuevos labels y entrys para ventana sin el customtkinter.
        ttk.Label(self.ventana, text="Usuario:").place(x=130,y=270)
        self.entry_usuario = ttk.Entry(self.ventana).place(x=130,y=290)
        ttk.Label(self.ventana, text="Contraseña:").place(x=130,y=320)
        self.entry_contraseña = ttk.Entry(self.ventana).place(x=130,y=340)
        self.btn_ingresar=ttk.Button(self.ventana, text="  Ingresar  ").place(x=160, y=390)
    