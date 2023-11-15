from model.model_bd_stock import ModeloStock_dos
from view.vista_movimiento import VistaMovimiento
class Controlador:
    def __init__(self):
        self.modelo_stock = ModeloStock_dos('data/base.db')
        self.vista_movimiento =VistaMovimiento (None, self.modelo_stock)
        self.vista_movimiento.ventanaMovimiento.mainloop()