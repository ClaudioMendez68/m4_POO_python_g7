class Pelota():
    # Atributos de Clase
    
    # Método Constructor
    def __init__(self, color: str, tamanio = 20, material = "Plástico") -> None: # Siempre deben ir los parámetros obligatorios primero
        print('Método constructor al crear un objeto de la clase')
        self.__color = color # Aquí estamos ocultando el atributo
        self.tamanio = tamanio
        self.material = material
        self._password = "qwerty"
    
    # Método oculto    
    def __getColor(self):
        return self.__color
    
    def setColor(self, color):
        self.__color = color
    
    # Getter. Nos da acceso a un atributo oculto
    @property
    def color(self):
        return self.__color
    
    # Setter
    @color.setter
    def color(self, color: str):
        self.__color = color if color != "" else "Verde"
        
    # Deleter
    @color.deleter
    def color(self):
        del self.__color
        
pelota_futbol = Pelota("Amarillo", 16, "plástico")
print(pelota_futbol.color) # SIN paréntesis como si fuera un atributo (Gracias a @property)
print(pelota_futbol.tamanio)

# pelota2 = Pelota() # TypeError: Pelota.__init__() missing 3 required positional arguments: 'color', 'tamanio', and 'material'

pelota3 = Pelota('Roja', material = 'Cuero')
print(pelota3.color)
print(pelota3.tamanio)
print(pelota3.material)