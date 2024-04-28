class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        if isinstance(self, PelotaDeTenis):
            self.__color = 'Amarillo'
        else:
            self.__color = color
            
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class PelotaDeTenis(PelotaDeDeporte):
    pass

p = PelotaDeTenis('Rojo')
print(p.color)
p.color = 'Azul'
print(p.color)