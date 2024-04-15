from abc import ABC, abstractmethod

class PelotaAbstracta(ABC):
    
    @abstractmethod
    def rebotar(self, altura: int):
        pass
    
    
class PelotaDeJuguete(PelotaAbstracta):
    
    def __init__(self, color) -> None:
        self.__color = color
        
    # Getter
    @property
    def color(self):
        return self.__color
    # Setter
    @color.setter
    def color(self, nuevo_color: str):
        self.__color = nuevo_color
        
    def rebotar(self, altura: float):
        pass
    
pelota = PelotaDeJuguete('Amarilla')
# print(pelota.__color) # AttributeError: 'PelotaDeJuguete' object has no attribute '__color'
print(pelota.color)
print(pelota._PelotaDeJuguete__color)