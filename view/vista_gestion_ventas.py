# View ventas
import sqlite3
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk

class GestionVentas:
    def __init__(self, ventana, controlador):
        ventana.title("Nueva Gestion de ventas")
        ventana.geometry("1080x600")
        ventana.configure(bg="#2B2B2B")
        
        titulo = customtkinter.CTkLabel(ventana, text="Gestion de ventas", width=120, height=25, fg_color=("white", "gray75"), corner_radius=8)
        titulo.pack()
        
        self.btn_test =  customtkinter.CTkButton(ventana, text="Print test", fg_color="#1ace65", border_width=1, text_color="#F8F8FF", hover_color="#165c9e", border_color="#1A1A1A", width=30, height=30)
        self.btn_test.pack()