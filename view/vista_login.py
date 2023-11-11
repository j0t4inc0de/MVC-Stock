# View login
import sqlite3
import tkinter as tk
from tkinter import  Label, PhotoImage, messagebox as mb
import customtkinter
from PIL import Image, ImageTk

class Login:
    def __init__(self, ventana):
        ventana.title("AlaNorte")
        ventana.geometry("400x600")
        ventana.configure(bg="#cfe7e9") # Blanco cabros
        # ventana.configure(bg="#2B2B2B") # Color oscuro cabros
        
        # Imagen de otro logo LOGO.PNG
        # self.imagen = PhotoImage(file='view/images/logo.png')
        # self.imagen.ajustada = self.imagen.subsample(6,5)
        # self.label_imagen = Label(ventana, image =self.imagen.ajustada)
        # self.label_imagen.pack()
        # self.label_imagen.place(x=115,y=5)
        
        # Imagen logo 2
        self.imagen_logo = Image.open("view/images/logo.png")
        self.imagen_logo.thumbnail((250, 250))
        self.imagen_logo = ImageTk.PhotoImage(self.imagen_logo)
        self.label_logo = tk.Button(ventana, image=self.imagen_logo, borderwidth=0, highlightthickness=0)
        self.label_logo.place(x=75,y=0)

        self.entry_usuario = customtkinter.CTkEntry(ventana, placeholder_text="Usuario", text_color=("gray10", "#DCE4EE"),  width=220, height=30)
        self.entry_usuario.place(x=90,y=270)
        self.entry_contraseña = customtkinter.CTkEntry(ventana, placeholder_text="Contraseña", text_color=("gray10", "#DCE4EE"),  width=220, height=30 ,show='*')
        self.entry_contraseña.place(x=90,y=320)
        self.btn_ingresar =  customtkinter.CTkButton(ventana, text="Ingresar", fg_color="#3f3d3d", border_width=1, text_color="#F8F8FF", hover_color="#196fbe", border_color="#1b1b1b", width=90, height=30)
        self.btn_ingresar.place(x=155, y=370)