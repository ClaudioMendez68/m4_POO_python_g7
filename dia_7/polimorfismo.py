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
    def cambia_color(self, color: str):
        # if color != "": # Polimorfismo. Cambia el comportamiento del método heredado de la clase Padre
            self.color = color

class Hijo(Padre):
        deuda = 120000
        # Sobreescritura del constructor heredado de la clase Padre
        def __init__(self, tamanio: int, saldo: int = 0) -> None:
            super().__init__(tamanio) # Llamado al constructor de la clase Padre
            self.__saldo = saldo
            
        @property
        def saldo(self):
            return self.__saldo
        
class Nieto(Hija):
    vicios = 140000
    
# Instancia de la clase Hija (Creando un objeto)
hijita = Hija(100)
            
super(type(hijita),hijita).cambia_color("Gris")
print(f"el color de la clase hija es {hijita.color}")

regalon = Nieto(90)

hijito = Hijo(10, 1200)
print(hijito.tamanio)
print(hijito.saldo)
print(hijito.deuda)
print(hijito.color)
hijito.color = 'Azul'
print(hijito.color)
print("")
# ISINSTANCE isinstance(objeto, tipo_clase_a_comparar)
print(isinstance(hijita, Hija))
print(isinstance(hijita, Hijo))
print(isinstance(hijita, Padre))
print("")
print(isinstance(hijita, Nieto))
print(isinstance(hijito, Nieto))
print("")
print(isinstance(regalon, Padre))
print(isinstance(regalon, Hija))
print(isinstance(regalon, Hijo))