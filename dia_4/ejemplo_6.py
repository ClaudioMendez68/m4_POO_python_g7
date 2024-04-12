class Coordenada():
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y
        
    def __add__(self, other):
        nuevo_x = self.x + other.x
        nuevo_y = self.y + other.y
        return Coordenada(nuevo_x, nuevo_y)
    
    def __eq__(self, other) -> bool:
        compara_x = self.x == other.x
        compara_y = self.y == other.y
        return compara_x and compara_y
    
c1 = Coordenada(5, 10)
c2 = Coordenada(-5, 10)
suma_coordenadas = c1 + c2

print(suma_coordenadas)
print(type(suma_coordenadas))
print(f'({suma_coordenadas.x}, {suma_coordenadas.y})')

c3 = Coordenada(-5, 10)
print(c2 == c3)