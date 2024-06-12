
from PRODUCTO import Producto
from ELECTRONICO import Electronico
from ALIMENTO import Alimento
#Aca se le da el valor de cada atributo. (Nombre, Precio, Cantidad)
producto_atributos = Producto("Sombrero", 4500, 10)
#Se inicia la funcion para mostrar esos valores.
producto_atributos.mostrar_informacion()
                        #(Nombre, Precio, Cantidad, Marca, Modelo)
electronico_atributos = Electronico("MacBook", 2350000, 5, "Apple", "M1")
electronico_atributos.mostrar_informacion()
                    #(Nombre, Precio, Cantidad, Fecha de expiracion.)
alimento_atributos = Alimento("Chocolate", 2550, 50, "2024-09-26")
alimento_atributos.mostrar_informacion()
