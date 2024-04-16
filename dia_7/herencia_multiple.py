class Madre():
    def __init__(self, color: str) -> None:
        self.__color = color
        
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color
        
class Padre():
    def __init__(self, tamanio: int) -> None:
        self.__tamanio = tamanio
        
    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio
        
class Hija(Madre, Padre):
    pass

class Nieto(Hija):
    vicios = 140000

princesa = Hija('Rojo')
princesa.tamanio = 80
print(princesa.tamanio)

regalon = Nieto(90)
# ISINSTANCE isinstance(objeto, tipo_clase_a_comparar)

print(isinstance(princesa, Nieto))
print(isinstance(regalon, Padre))
print(isinstance(regalon, Madre))
print(isinstance(regalon, Hija))
