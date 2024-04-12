class Pelota():
    # Método constructor de la clase Pelota()
    def __init__(self) -> None:
        self.tamanio_pelota = 1
        
    # Getter
    @property
    def tamanio(self):
        return self.tamanio_pelota
    
    # Setter
    @tamanio.setter
    def tamanio(self, tamanio: int):
        self.tamanio_pelota = tamanio if tamanio > 0 else 1
        
p = Pelota(16)

print(p.tamanio) # 1

p.tamanio = 10
print(p.tamanio)