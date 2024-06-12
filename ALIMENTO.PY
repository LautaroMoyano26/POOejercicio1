
from PRODUCTO import Producto
#Se crea la clase hija Alimento.
class Alimento(Producto):
    def __init__(self, nombre, precio, cantidad, fecha_expiracion):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion
#Funcion para mostrar la informacion de Alimentos.
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Fecha de expiración: {self.fecha_expiracion}")

