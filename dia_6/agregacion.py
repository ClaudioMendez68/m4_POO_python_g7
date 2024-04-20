class Material():
    def __init__(self, nombre: str, duracion: str, textura: str) -> None:
        self. nombre = nombre
        self. duracion = duracion
        self.textura = textura
        
        
class Pelota():
    def __init__(self, tamanio: int, color: str, material: Material) -> None:
        self.tamanio = tamanio
        self.color = color
        # La pelota tiene un material (Clase Material)
        self.material = material
        
# El material existe de manera independiente de la pelota
mater = Material('Plástico', 'Corta', 'Lisa')
pelota = Pelota(16, 'Amarillo', mater)

print(type(pelota.material)) # <class '__main__.Material'>
print(pelota.material.nombre)
print(pelota.material.duracion)
print(pelota.material.textura)