class Padre():
    # Atributo de clase
    color = 'verde'
    # Constructor
    def __init__(self, tamanio: int) -> None:
        # Atributo de instancia
        self.__tamanio = tamanio # Atributo oculto o privado
    
    # Métodos Estáticos
    
    # Método de instancia
    def cambia_color(self, color: str):
        if color != "":
            self.color = color
            
    # Sobrecarga
    
    # Getter - Setter
    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self, tamanio: int):
        if tamanio > 0:
            self.__tamanio = tamanio
        else:
            self.__tamanio = 0
            
# HERENCIA La clase hija hereda TODO. Cada uno de los hijos puede tener sus propios métodos y atributos
class Hija(Padre):
        peso = 47
    
class Hijo(Padre):
        deuda = 120000
        
class Nieto(Hija):
    vicios = 140000
    
# Instancia de la clase Hija (Creando un objeto)
hijita = Hija(100)
print(f'El color de la clase hija es {hijita.color}')
print(hijita.tamanio)
hijita.tamanio = 50
print(hijita.tamanio)

regalon = Nieto(90)
print(regalon.color)
print(regalon.peso)