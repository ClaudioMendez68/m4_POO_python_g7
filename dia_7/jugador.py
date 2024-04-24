import random
from personaje import Perosnaje

class Jugador(Perosnaje):
    def ataque(self):
        if self.arma:
            return self.atk + random.randint(1, 5)
        else:
            return self.atk
    
    def defensa(self, ataque: int):
        self.hp -= max(ataque - random.randint(1, self.df), 0)


if __name__ == '__main__':
    cirilo = Jugador(500, 10, 5, 'Cuchuflí Venenoso')
    print(cirilo.ataque())