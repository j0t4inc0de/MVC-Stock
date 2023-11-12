# View Ventas
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
