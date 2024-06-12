
from PRODUCTO import Producto
#Se crea la clase hija Electronico.
class Electronico(Producto):
    def __init__(self, nombre, precio, cantidad, marca, modelo):
        super().__init__(nombre, precio, cantidad)
        self.marca = marca
        self.modelo = modelo
#Funcion para mostrar la informacion de productos electronicos.
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")