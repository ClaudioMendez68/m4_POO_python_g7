import json

class Producto():
    def __init__(self, nombre: str, precio: float) -> None:
        self.nombre = nombre
        self.precio = precio
        
instancias = []

with open('C:\Workspaces\Bootcamp\Fullstack_Python_G7\POO\dia_11/productos.txt', 'r') as productos:
    linea = productos.readline()
    while linea:
        producto = json.loads(linea)
        instancias.append(Producto(producto.get("nombre"), producto.get("precio")))
        linea = productos.readline()
        
for instancia in instancias:
    print(f'{instancia.nombre} : ${instancia.precio}')