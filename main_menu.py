# Main menu
import tkinter
from model.model_bd_stock import ModeloStock
from view.view_menu import VistaPrincipal

if __name__ == "__main__":
    modelo_stock = ModeloStock('data/base.db')
    app_principal = VistaPrincipal(modelo_stock)
    app_principal.ventanaPrincipal.mainloop()


