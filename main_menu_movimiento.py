#Rodrigo - Cristobal Main menu de movimiento
import tkinter
from model.model_bd_stock import ModeloStock
from view.vista_movimiento_menu import VistaMenuMov

if __name__ == "__main__":
    modelo_stock = ModeloStock('data/base.db')
    app_principal = VistaMenuMov(modelo_stock)
    app_principal.ventanaMenuMov.mainloop()