class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        self.__color = color
        
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color
        
class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color: str, cantidad_de_hexagonos: int) -> None:
        super().__init__(color)
        self.__cantidad_de_hexagonos = cantidad_de_hexagonos
        
    @property
    def cantidad_de_hexagonos(self):
        return self.__cantidad_de_hexagonos    
    @cantidad_de_hexagonos.setter
    def cantidad_de_hexagonos(self, cantidad_de_hexagonos):
        self.__cantidad_de_hexagonos = cantidad_de_hexagonos
        
    def hacer_pase(self, destino: str, fuerza: int) -> tuple:
        return (destino, fuerza * 0.5)
    
class PelotaDeTenis(PelotaDeDeporte):
    def __init__(self) -> None:
        self.__color = 'Amarillo'
        
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color: str):
        pass
    
    def hacer_saque(self, altura: int, fuerza: int) -> tuple:
        return (altura, altura * fuerza)