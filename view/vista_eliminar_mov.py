import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

class VistaEliminarMovimiento:
    def __init__(self, vista_principal, modelo_stock):
        self.ventanaDel = ThemedTk(theme="arc")
        self.ventanaDel.title("Eliminando Movimiento")
        self.ventanaDel.geometry("310x300")
        self.vista_principal = vista_principal
        self.modelo_stock = modelo_stock
        self.id_movimiento_seleccionado = None  # ID del movimiento seleccionado

        self.crear_formulario()

    def crear_formulario(self):
        ttk.Label(self.ventanaDel, text="Seleccione el movimiento:").place(x=1, y=5)
        self.movimiento_combobox = ttk.Combobox(self.ventanaDel, state="readonly")
        self.movimiento_combobox.place(x=150, y=5)
        self.populate_movimiento_combobox()
        ttk.Label(self.ventanaDel, text="Información a eliminar").place(x=1, y=42)

        ttk.Label(self.ventanaDel, text="Cantidad Movimiento:").place(x=1, y=72)
        self.entry_cantidad_movimiento = ttk.Entry(self.ventanaDel, state="readonly")
        self.entry_cantidad_movimiento.place(x=150, y=70)

        ttk.Label(self.ventanaDel, text="Fecha Movimiento:").place(x=1, y=102)
        self.entry_fecha_movimiento = ttk.Entry(self.ventanaDel, state="readonly")
        self.entry_fecha_movimiento.place(x=150, y=100)

        ttk.Label(self.ventanaDel, text="Descripción:").place(x=1, y=132)
        self.entry_descripcion = ttk.Entry(self.ventanaDel, state="readonly")
        self.entry_descripcion.place(x=150, y=130)

        ttk.Button(self.ventanaDel, text="Eliminar", command=self.eliminar_movimiento).place(x=154, y=250)

        # Enlazar evento de selección del Combobox
        self.movimiento_combobox.bind("<<ComboboxSelected>>", self.mostrar_datos_movimiento)

    def populate_movimiento_combobox(self):
        movimientos = self.modelo_stock.get_movimiento_data()
        self.movimiento_combobox['values'] = movimientos

    def mostrar_datos_movimiento(self, event):
        selected_id_movimiento = self.movimiento_combobox.get()

        # Verifica si selected_id_movimiento es una cadena no vacía antes de intentar desempaquetar
        if selected_id_movimiento:
            try:
                # Convierte el ID a entero
                id_movimiento = int(selected_id_movimiento)

                # Obtén los datos del movimiento seleccionado
                movimiento_info = self.modelo_stock.get_movimiento_info_by_id(id_movimiento)

                # Verifica si la información del movimiento es válida antes de desempaquetar
                if movimiento_info and len(movimiento_info) == 6:
                    # Desempaqueta los valores
                    id_movimiento, id_existencia, id_tipomov, cantidad_mov, fecha_mov, descripcion = movimiento_info

                    # Limpia los datos anteriores
                    self.limpiar_datos_movimiento()

                    # Actualiza las etiquetas con la información del movimiento seleccionado
                    ttk.Label(self.ventanaDel, text=f"ID de Movimiento: {id_movimiento}").place(x=1, y=50)
                    ttk.Label(self.ventanaDel, text=f"Cantidad Movimiento: {cantidad_mov}").place(x=1, y=72)
                    ttk.Label(self.ventanaDel, text=f"Fecha Movimiento: {fecha_mov}").place(x=1, y=102)
                    ttk.Label(self.ventanaDel, text=f"Descripción: {descripcion}").place(x=1, y=132)

                    # Almacena el ID del movimiento seleccionado
                    self.id_movimiento_seleccionado = id_movimiento
                else:
                    print("La información del movimiento no es válida")
            except ValueError:
                print("ID de movimiento no válido")
        else:
            print("Movimiento no seleccionado")

    def limpiar_datos_movimiento(self):
        # Limpiar los entrys cuando no hay movimiento seleccionado
        self.id_movimiento_seleccionado = None
        self.entry_cantidad_movimiento.config(state="normal")
        self.entry_cantidad_movimiento.delete(0, tk.END)
        self.entry_cantidad_movimiento.config(state="readonly")

        self.entry_fecha_movimiento.config(state="normal")
        self.entry_fecha_movimiento.delete(0, tk.END)
        self.entry_fecha_movimiento.config(state="readonly")

        self.entry_descripcion.config(state="normal")
        self.entry_descripcion.delete(0, tk.END)
        self.entry_descripcion.config(state="readonly")

    def eliminar_movimiento(self):
        # Agrega aquí la lógica para eliminar el movimiento
        # Puedes utilizar self.id_movimiento_seleccionado para obtener el ID del movimiento seleccionado
        # Luego, llama a un método en tu modelo para realizar la eliminación
        if self.id_movimiento_seleccionado is not None:
            respuesta = messagebox.askokcancel("Confirmar eliminación", f"¿Seguro que quieres eliminar el movimiento {self.id_movimiento_seleccionado}?")

            if respuesta:
                # El usuario hizo clic en "Aceptar"
                self.modelo_stock.eliminar_movimiento(self.id_movimiento_seleccionado)
                messagebox.showinfo("Eliminado", "Movimiento eliminado exitosamente.")
                self.limpiar_datos_movimiento()
                self.populate_movimiento_combobox()  # Actualiza el Combobox después de la eliminación
            else:
                # El usuario hizo clic en "Cancelar"
                messagebox.showinfo("Cancelado", "Operación de eliminación cancelada.")
