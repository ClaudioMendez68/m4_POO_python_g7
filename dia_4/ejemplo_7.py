class Pelota():
    def __init__(self, tamanio: int = 0) -> None:
        self.tamanio = tamanio
        
    def __eq__(self, other) -> bool:
        return self.tamanio == other.tamanio
        
p1 = Pelota(16)
p2 = Pelota(16)
p3 = p2

print(p1 == p2)
print(p2 == p3)