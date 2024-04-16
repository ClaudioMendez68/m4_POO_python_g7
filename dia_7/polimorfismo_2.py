class Madre():
    def __init__(self, color: str, **parametros) -> None:
        super().__init__(**parametros)
        self.__color = color
        
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self, color):
        self.__color = color
        
class Padre():
    
    def __init__(self, tamanio: int, **parametros) -> None:
        super().__init__(**parametros)
        self.__tamanio = tamanio
        
    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio
        
class Hija(Madre, Padre):
    # Sobreescritura de los constructores
    #def __init__(self, color: str, tamanio: int) -> None:
    #    Madre.__init__(self, color)
    #    Padre.__init__(self, tamanio)
    def __init__(self, deuda: int = 0, **parametros) -> None:
        super().__init__(**parametros)
        # Atributo de instancia propio de la clase Hija
        self.deuda = deuda
princesa = Hija(color = 'Rojo', tamanio =80, deuda = 230000)
print(princesa.tamanio)
print(princesa.color)
print(princesa.deuda)

# ISINSTANCE isinstance(objeto, tipo_clase_a_comparar)
print(isinstance(princesa, Hija))
print(isinstance(princesa, Madre))
print(isinstance(princesa, Padre))