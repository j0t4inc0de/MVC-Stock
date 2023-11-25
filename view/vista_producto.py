#Vista producto
import tkinter as tk
from tkinter import Menu, ttk
from tkinter import messagebox as mb
from ttkthemes import ThemedTk

class  VistaProducto:
    def __init__(self, ventanaProducto, modelo_stock):
        self.ventanaProducto = ThemedTk(theme="arc")
        # agregue esto por si el tema sera en negro
        # self.ventanaProducto = ThemedTk(themebg=True)
        # self.ventanaProducto.set_theme('black')
        # funcion para mayor edicion sobre el tema -> self.ventanaProducto.set_theme_advanced(theme_name="dark")
        self.ventanaProducto.title("Agregando producto")
        self.ventanaProducto.geometry("310x300")
        self.modelo_stock = modelo_stock
        
        self.select_state = tk.StringVar() # Se crea la variable para estado
        self.select_category = tk.StringVar() # Se crea la variable para categoria
        self.crear_formulario() # Se llama el formulario para mostrar los botones y entrys del mismo

    def crear_formulario(self):
        ttk.Label(self.ventanaProducto, text="Nombre del Producto:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre_producto = ttk.Entry(self.ventanaProducto)
        self.entry_nombre_producto.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(self.ventanaProducto, text="Precio del Producto:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_precio_producto = ttk.Entry(self.ventanaProducto)
        self.entry_precio_producto.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.ventanaProducto, text="Cantidad:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_cantidad_producto = ttk.Entry(self.ventanaProducto)
        self.entry_cantidad_producto.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.ventanaProducto, text="Estado del Producto:").grid(row=3, column=0, padx=10, pady=10)
        self.state_combobox = ttk.Combobox(self.ventanaProducto)
        self.state_combobox.grid(row=3, column=1, padx=10, pady=10)
        self.populate_state_combobox()

        ttk.Label(self.ventanaProducto, text="Categoría del Producto:").grid(row=4, column=0, padx=10, pady=10)
        self.category_combobox = ttk.Combobox(self.ventanaProducto)
        self.category_combobox.grid(row=4, column=1, padx=10, pady=10)
        self.populate_category_combobox()

        ttk.Button(self.ventanaProducto, text="Listo", command=self.add_product).place(x=154, y=250) # Boton 'Listo' que llama la funcion para añadir los productos

    def populate_state_combobox(self):
        states = self.modelo_stock.get_estados() # Saca el estado de la base de datos
        self.state_combobox['values'] = states  # Le pone la lista de estados

    def populate_category_combobox(self):
        categories = self.modelo_stock.get_categorias()  # Saca las categorias de la base de datos
        self.category_combobox['values'] = categories # Le pone la lista de categorias

    def add_product(self): #  se encarga de agregar un nuevo producto al modelo
        selected_state_name = self.state_combobox.get()
        state_id = self.get_state_id(selected_state_name) #  Utiliza el nombre del estado para obtener el ID usa la funcion de abajo 'def get_state_id'

        selected_category_name = self.category_combobox.get()
        category_id = self.get_category_id(selected_category_name) #  Utiliza el nombre de la categoria para obtener el ID usa la funcion de abajo 'def get_category_id'

        product_name = self.entry_nombre_producto.get()
        product_price = float(self.entry_precio_producto.get())

        product_cantidad = self.entry_cantidad_producto.get()
        product_cantidad = int(self.entry_cantidad_producto.get())

        self.modelo_stock.add_producto(product_name, state_id, product_price, product_cantidad, category_id) # Utiliza la funcion del modelo para insertar los datos obtenidos en las anteriores lineas

        # Estas lineas limpian los campos
        self.entry_nombre_producto.delete(0, tk.END)
        self.entry_precio_producto.delete(0, tk.END)
        self.entry_cantidad_producto.delete(0, tk.END)
        self.state_combobox.set("")
        self.category_combobox.set("")
        
        #Rodrigo Cristobal: Se crea el mensaje al agregar un producto.
        mb.showinfo("Listo", "Producto agregado.")

    def get_state_id(self, state_name): #  Ejecuta una consulta SQL en la tabla Estado para obtener el ID del estado donde el nombre del estado coincide con el valor state_name
        self.modelo_stock.cursor.execute("SELECT id_estado FROM Estado WHERE nombre=?", (state_name,))
        return self.modelo_stock.cursor.fetchone()[0]
    def get_category_id(self, category_name): #  Ejecuta una consulta SQL en la tabla Categoria para obtener el ID de la categoria donde el nombre del estado coincide con el valor category_name
        self.modelo_stock.cursor.execute("SELECT id_categoria FROM Categoria WHERE nombre=?", (category_name,))
        return self.modelo_stock.cursor.fetchone()[0]