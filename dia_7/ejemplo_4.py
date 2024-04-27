class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        self.__color = color
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color = color
        
        
class PelotaDeTenis(PelotaDeDeporte):
    def __init__(self) -> None:
        self.__color = 'Amarillo'
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        pass
    
    
class PelotaDeFutbol(PelotaDeDeporte):
    def __init__(self, color: str, cantidad_de_hexagonos: int) -> None:
        super().__init__(color)
        self.__cantidad_de_hexagonos = cantidad_de_hexagonos
    
    @property
    def cantidad_de_hexagonos(self):
        return self.__cantidad_de_hexagonos
    
        
pdd = PelotaDeDeporte('Blanco')
print(pdd.color)
pdd.color = 'Rojo'
print(pdd.color)

pdt = PelotaDeTenis()
print(pdt.color)
pdt.color = 'Rojo'
print(pdt.color)

print('==============================')
print(pdd.color)
pdf = PelotaDeFutbol('Blanco y Negro', 15)
print(pdf.color)
print(pdf.cantidad_de_hexagonos)