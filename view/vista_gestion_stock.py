#View Gestion Stock
import sqlite3
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
import customtkinter
from PIL import Image, ImageTk

class GestionStock:
    def __init__(self, raiz, controlador):
        raiz.title("Gestion de inventario")
        raiz.geometry("1080x660")
        raiz.configure(bg="#2B2B2B")
        # raiz.resizable(width=False, height=False) #Esta linea hace q la ventana no se pueda agrandar/achicar

        self.entry_buscador = customtkinter.CTkEntry(raiz, placeholder_text="Buscador", text_color=("gray10", "#DCE4EE"),  width=380, height=30)
        self.entry_buscador.place(x=10, y=5)
        
        self.entry_nombre = customtkinter.CTkEntry(raiz, placeholder_text="Nombre", text_color=("gray10", "#DCE4EE"),  width=220, height=30)
        self.entry_nombre.place(x=10,y=600)
        self.entry_precio = customtkinter.CTkEntry(raiz, placeholder_text="Precio", text_color=("gray10", "#DCE4EE"),  width=220, height=30)
        self.entry_precio.place(x=240,y=600)
        self.entry_cantidad = customtkinter.CTkEntry(raiz, placeholder_text="Cantidad", text_color=("gray10", "#DCE4EE"),  width=220, height=30)
        self.entry_cantidad.place(x=470,y=600)

        self.imagen_lupa = Image.open("view/images/lupa.png")
        self.imagen_lupa = ImageTk.PhotoImage(self.imagen_lupa)
        self.label_lupa = tk.Button(raiz, image=self.imagen_lupa, borderwidth=0, highlightthickness=0)
        self.label_lupa.place(x=400,y=2)
        # self.imagen_logo = Image.open("view/images/logo.png")
        # self.imagen_logo.thumbnail((200, 200))
        # self.imagen_logo = ImageTk.PhotoImage(self.imagen_logo)
        # self.label_logo = tk.Button(raiz, image=self.imagen_logo, borderwidth=0, highlightthickness=0)
        # self.label_logo.place(x=10,y=10)


        self.btn_añadir =  customtkinter.CTkButton(raiz, text="+", fg_color="#1ace65", border_width=1, text_color="#F8F8FF", hover_color="#165c9e", border_color="#1A1A1A", width=30, height=30)
        self.btn_añadir.place(x=680, y=6)
        self.btn_modificar =  customtkinter.CTkButton(raiz, text="Modificar", fg_color="#a1a313", border_width=1, text_color="#F8F8FF", hover_color="#165c9e", border_color="#1A1A1A", width=90, height=30)
        self.btn_modificar.place(x=750, y=6)
        self.btn_eliminar =  customtkinter.CTkButton(raiz, text="-", fg_color="#af2424", border_width=1, text_color="#F8F8FF", hover_color="#165c9e", border_color="#1A1A1A", width=30, height=30)
        self.btn_eliminar.place(x=715, y=6)

        # self.menu = Menu(raiz)
        # self.menuinicio = Menu(self.menu, tearoff=0)
        # self.menu.add_cascade(label='Inicio', menu=self.menuinicio)
        # self.menuinicio.add_command(label='Ir a Ventas', command=controlador.irventa)
        # self.menuinicio.add_command(label='Salir', command=controlador.salir)
        # raiz.config(menu=self.menu)

        style = ttk.Style(raiz)
        style.theme_use("clam")
        style.configure("Treeview", background="#2B2B2B", fieldbackground="#2B2B2B", foreground="white")
        
        tree_frame = tk.Frame(raiz)
        tree_frame.place(x=230, y=43)
        tree = ttk.Treeview(raiz, show='headings')  
        tree["columns"]=("#1", "#2", "#3", "#4")
        tree.column("#1", width=50)
        tree.column("#2", width=399)
        tree.column("#3", width=399)
        tree.heading("#1", text="ID")
        tree.heading("#2", text="Nombre")
        tree.heading("#3", text="Precio")
        tree.heading("#4", text="Cantidad")
        tree.place(x=10, y=43, height=540)