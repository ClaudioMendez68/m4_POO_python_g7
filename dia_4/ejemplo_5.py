class Pelota():
    def __init__(self, tamanio: int = 0) -> None:
        self.tamanio = tamanio
        
    def __add__(self, other):
        return self.tamanio + other.tamanio
    
p1 = Pelota(16)
p2 = Pelota(32)

print(p1 + p2)