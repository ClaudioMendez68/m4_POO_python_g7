class Pelota():
    """
    def __init__(self):
        self.color = "Blanco"
        self.tamanio = 20
        self.material = "Plástico"
    """
    """
    def __init__(self, color: str, tamanio: int, material: str) -> None:
        self.color = color
        self.tamanio = tamanio
        self.material = material
    """
    def __init__(self, color: str, tamanio = 20, material = "Plástico") -> None:
        self.color = color
        self.tamanio = tamanio
        self.material = material

p = Pelota("Amarillo", 16)

print(p.color)
print(p.tamanio)
print(p.material)

# p2 = Pelota() # TypeError: Pelota.__init__() missing 3 required positional arguments: 'color', 'tamanio', and 'material'