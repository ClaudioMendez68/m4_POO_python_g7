import random
from personaje import Perosnaje

class Jugador(Perosnaje):
    def __init__(self, hp: int, atk: int, df: int, arma: str = None) -> None:
        super().__init__(hp, atk, df)
        self.__arma = arma
    
    @property
    def arma(self):
        return self.__arma
    
    def ataque(self) -> int:
        if self.arma:
            return self.atk + random.randint(1, 5)
        else:
            return self.atk
    
    def defensa(self, ataque: int) -> int:
        self.hp -= max(ataque - random.randint(1, self.df), 0)


if __name__ == '__main__':
    cirilo = Jugador(500, 10, 5, 'Cuchuflí Venenoso')
    print(cirilo.ataque())