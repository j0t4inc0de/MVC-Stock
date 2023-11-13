from model.model_bd_stock import ModeloStock
from view.vista_producto import VistaProducto


class Controlador:
    def __init__(self):
        self.modelo_stock = ModeloStock('data/base.db')
        self.vista_producto = VistaProducto(None, self.modelo_stock)
        self.vista_producto.ventanaProducto.mainloop()