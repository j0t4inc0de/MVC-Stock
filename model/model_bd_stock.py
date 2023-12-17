# Model Stock

import sqlite3
import tkinter as tk
from tkinter import messagebox as mb
from PIL import Image, ImageTk

# Modelo
class ModeloStock:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path) # 'db_path' es la ruta que se le especifica en el controlador
        self.cursor = self.conn.cursor()

    def get_estados(self): # Obtiene los datos de la tabala estado
        self.cursor.execute("SELECT nombre FROM Estado")
        return [state[0] for state in self.cursor.fetchall()]
    
    def get_categorias(self): # Obtiene los datos de la tabla categoria
        self.cursor.execute("SELECT nombre FROM Categoria")
        return [state[0] for state in self.cursor.fetchall()]
    
    def add_producto(self, nombre, id_estado, precio, cantidad, id_categoria): # Mete los datos
        self.cursor.execute("INSERT INTO Producto (nombre, id_estado, precio, id_categoria) VALUES (?, ?, ?, ?)",
                            (nombre, id_estado, precio, id_categoria))
        self.cursor.execute("INSERT INTO Existencia (nombre, cantidad) VALUES (?, ?)", (nombre, cantidad))
        self.conn.commit()

    def obtener_datos(self): # Obtiene todos los datos de esas tablas
        self.cursor.execute("""
            SELECT Producto.nombre, Producto.precio, Existencia.cantidad, Estado.nombre, Categoria.nombre
            FROM Producto
            JOIN Existencia ON Producto.nombre = Existencia.nombre
            JOIN Estado ON Producto.id_estado = Estado.id_estado
            JOIN Categoria ON Producto.id_categoria = Categoria.id_categoria
        """)
        return self.cursor.fetchall()
    
    def obtener_datos_mov(self): # Obtiene todos los datos de esas tablas
        self.cursor.execute("""
            SELECT TipoMovimiento.nombre, Existencia.nombre, Existencia.cantidad, Movimientos.descripcion, Movimientos.fecha_mov, Movimientos.cantidad_mov
            FROM Movimientos
            JOIN Existencia ON Movimientos.id_existencia = Existencia.id_existencia
            JOIN TipoMovimiento ON Movimientos.id_tipomov = TipoMovimiento.id_tipomov                                                         
        """)
        return self.cursor.fetchall()

    def buscar_nombre(self, nombre_buscador): # Busca el nombre en la base de datos
        nombre_buscador = nombre_buscador.strip()
        self.cursor.execute(f"""
            SELECT Producto.nombre, Producto.precio, Existencia.cantidad, Estado.nombre, Categoria.nombre
            FROM Producto
            JOIN Existencia ON Producto.nombre = Existencia.nombre
            JOIN Estado ON Producto.id_estado = Estado.id_estado
            JOIN Categoria ON Producto.id_categoria = Categoria.id_categoria WHERE Producto.nombre like '{nombre_buscador}%' """
            )
        resultado = self.cursor.fetchall() 
        return resultado  

    def get_precio_producto(self, nombre_producto):
        self.cursor.execute("SELECT precio FROM Producto WHERE nombre=?", (nombre_producto,))
        precio = self.cursor.fetchone()
        return precio[0] if precio is not None else None

    def verificar_credenciales(self, usuario, contraseña): # Query para verificar que los datos ingresados usuario/contraseña estan en la base de datos
        self.cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?", (usuario, contraseña))
        resultado = self.cursor.fetchone()
        self.conn.commit()
        return resultado
    
    def has_movimientos(self, id_existencia):
        self.cursor.execute("SELECT COUNT(*) FROM Movimientos WHERE id_existencia=?", (id_existencia,))
        count = self.cursor.fetchone()[0]
        return count > 0
    def del_producto(self, id_existencia):
        if self.has_movimientos(id_existencia):
            # Si hay movimientos, actualizar el estado a inactivo
            self.cursor.execute("UPDATE Producto SET id_estado = 3 WHERE nombre = (SELECT nombre FROM Existencia WHERE id_existencia = ?)", (id_existencia,))
            self.conn.commit()
            mb.showinfo("Éxito", "Producto desactivado con éxito debido a la existencia de movimientos.")
        else:
            # Si no hay movimientos, eliminar el producto
            self.cursor.execute("DELETE FROM Movimientos WHERE id_existencia = ?", (id_existencia,))
            self.cursor.execute("DELETE FROM Producto WHERE nombre = (SELECT nombre FROM Existencia WHERE id_existencia = ?)", (id_existencia,))
            self.cursor.execute("DELETE FROM Existencia WHERE id_existencia = ?", (id_existencia,))
            self.conn.commit()
            mb.showinfo("Éxito", "Producto eliminado con éxito.")
            
    def get_existencias(self):
        self.cursor.execute("SELECT nombre FROM Existencia")
        return [existencia[0] for existencia in self.cursor.fetchall()]

    def get_cantidad_existente(self, id_existencia):
        self.cursor.execute("SELECT cantidad FROM Existencia WHERE id_existencia=?", (id_existencia,))
        cantidad = self.cursor.fetchone()
        return cantidad[0] if cantidad is not None else None
    
    def get_tipo_movimientos(self):
        self.cursor.execute("SELECT nombre FROM TipoMovimiento")
        return [tipo_mov[0] for tipo_mov in self.cursor.fetchall()]

    def update_existencia_cantidad(self, id_existencia, nueva_cantidad):
        self.cursor.execute("UPDATE Existencia SET cantidad=? WHERE id_existencia=?", (nueva_cantidad, id_existencia))
        self.conn.commit()

    def add_existencia(self, nombre_producto, cantidad, id_existencia):
        self.cursor.execute("INSERT INTO Existencia (nombre, cantidad, id_existencia) VALUES (?, ?, ?)",
                            (nombre_producto, cantidad, id_existencia))
        self.conn.commit()

    def get_existencia_data(self):
        self.cursor.execute("SELECT nombre, cantidad FROM Existencia")
        return [existencia[0] for existencia in self.cursor.fetchall()]

    def get_tipo_movimientos(self):
        self.cursor.execute("SELECT nombre FROM TipoMovimiento")
        return [tipo_mov[0] for tipo_mov in self.cursor.fetchall()]

    def get_tipomov_data(self):
        self.cursor.execute("SELECT nombre, id_tipomov FROM TipoMovimiento")
        return self.cursor.fetchall()

    def add_movimiento(self, id_tipomov, id_existencia, descripcion, fecha, cantidad_movimientos):
        # Obtener la cantidad existente antes del movimiento
        cantidad_existente = self.get_cantidad_existente(id_existencia)

        # Actualizar la cantidad en la tabla Existencia
        nueva_cantidad_existente = cantidad_existente + cantidad_movimientos
        self.cursor.execute("UPDATE Existencia SET cantidad=? WHERE id_existencia=?", (nueva_cantidad_existente, id_existencia))

        # Agregar el nuevo movimiento
        self.cursor.execute("""
            INSERT INTO Movimientos (id_tipomov, id_existencia, descripcion, fecha_mov, cantidad_mov)
            VALUES (?, ?, ?, ?, ?)
        """, (id_tipomov, id_existencia, descripcion, fecha, cantidad_movimientos))

        self.conn.commit()

    def get_movimiento_data(self):
        self.cursor.execute("SELECT id_tipomov, id_existencia, descripcion, fecha_mov, cantidad_mov FROM Movimientos")
        return self.cursor.fetchall()

    
    def edit_producto(self, id_existencia, nueva_cantidad, nuevo_precio, nuevo_estado,nueva_categoria):
        # Actualizar la cantidad en la tabla Existencia
        self.cursor.execute("UPDATE Existencia SET cantidad=? WHERE id_existencia=?", (nueva_cantidad, id_existencia))
        
        self.cursor.execute("SELECT id_categoria FROM Categoria WHERE nombre=?", (nueva_categoria,))
        id_categoria = self.cursor.fetchone()[0]

        # Obtener el id del nuevo estado
        self.cursor.execute("SELECT id_estado FROM Estado WHERE nombre=?", (nuevo_estado,))
        result = self.cursor.fetchone()
        if result is None:
            print(f"No se encontró un estado con el nombre {nuevo_estado}")
            return

        id_estado = result[0]
        # Actualizar el precio y el estado en la tabla Producto
        self.cursor.execute("UPDATE Producto SET precio=?, id_estado=?, id_categoria=? WHERE nombre = (SELECT nombre FROM Existencia WHERE id_existencia = ?)", (nuevo_precio, id_estado, id_categoria, id_existencia))

        self.conn.commit()

    def get_estado_producto(self, nombre_producto):
        self.cursor.execute("""
            SELECT Estado.nombre
            FROM Producto
            JOIN Estado ON Producto.id_estado = Estado.id_estado
            WHERE Producto.nombre=?
        """, (nombre_producto,))
        estado = self.cursor.fetchone()
        return estado[0] if estado is not None else None
    
    def get_categoria_producto(self, nombre_producto):
        self.cursor.execute("""
            SELECT Categoria.nombre
            FROM Producto
            JOIN Categoria ON Producto.id_categoria = Categoria.id_categoria
            WHERE Producto.nombre=?
        """, (nombre_producto,))
        categoria = self.cursor.fetchone()
        return categoria[0] if categoria is not None else None
    
    def get_all_categorias(self):
        self.cursor.execute("SELECT nombre FROM Categoria")
        categorias = self.cursor.fetchall()
        return [categoria[0] for categoria in categorias]
    
    
    def get_movimiento_info_by_id(self,id_movimiento):
        self.cursor.execute("""
            SELECT id_mov, id_existencia, id_tipomov, cantidad_mov, fecha_mov, descripcion
            FROM Movimientos
            WHERE id_mov = ?
        """, (id_movimiento,))
        return self.cursor.fetchone()


    
   