from sin_gluten import SinGluten
from abc import ABC, abstractmethod

class Chocolate(ABC):
    @abstractmethod
    def validar_porc_cacao(self, porc: float) -> float:
        pass
    def __init__(self, porc_cacao: float) -> None:
        self.porc_cacao = self.validar_porc_cacao(porc_cacao)
        
class ChocolateAmargo(Chocolate):
    def validar_porc_cacao(self, porc: float):
        return min(max(0.75, porc), 0.85)
    
class ChocolateAmargoSinGluten(ChocolateAmargo, SinGluten):
    pass
c1 = ChocolateAmargo(0.3)
c2 = ChocolateAmargoSinGluten(0.80)
print(c1.porc_cacao)
print(c2.porc_cacao)
print(c2.tipo_producto)