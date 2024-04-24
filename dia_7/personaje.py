from abc import ABC, abstractmethod

class Perosnaje(ABC):
    def __init__(self, hp: int, atk: int, df: int, arma: str="") -> None:
        self.hp = hp
        self.atk = atk
        self.df = df
        self.arma = arma
        
    @abstractmethod
    def ataque(self):
        pass
    @abstractmethod
    def defensa(self, ataque: int):
        pass