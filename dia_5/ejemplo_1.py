from abc import ABC, abstractmethod

class PelotaAbstracta(ABC):
    # Método abstracto que se debe implemetar en las subclases de la clase abstracta
    @abstractmethod
    def rebotar(self, altura: int):
        pass
    
class PelotasDeJuguete(PelotaAbstracta):
    def __init__(self) -> None:
        self.rebotes = []

    # Implementación del método abstracto en la subclase de la clase abstracta
    def rebotar(self, altura: float):
        #self.rebotes = []
        while altura > 0:
            self.rebotes.append(altura)
            self.rebotes.append(0)
            altura //= 2
        return self.rebotes

pelota_andy = PelotasDeJuguete()
print(pelota_andy.rebotar(10))