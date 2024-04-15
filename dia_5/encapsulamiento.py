class Auto():
    __color = "Blanco"
    
    def __cambiar_color(self, color):
        print('Nuevo color:', color)
        self.__color = color
    
    def imprimir_estado(self, nuevo_color):
        print(self.__color)
        self.__cambiar_color(nuevo_color)
        print(self.__color)
        
    # Getter
    @property
    def color(self):
        return self.__color
    
    
nissan = Auto()
#print(Auto.__color) # AttributeError: type object 'Auto' has no attribute '__color'
#print(nissan.__color) # AttributeError: 'Auto' object has no attribute '__color'
nissan.imprimir_estado('Negro')
print(nissan.color)  # Llamndo al getter

print(nissan._Auto__color)