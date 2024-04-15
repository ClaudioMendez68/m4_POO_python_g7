"""
ABSTRACCIÓN: 
Una clase es abstracta si, al menos, tiene un MÉTODO ABSTRACTO.
Un Método Abstracto es aquel que sólo tiene la definición del método

Para poder crear una clase abstracta y un método abstracto importamos:

from abc import ABC, abstractmethod
"""
from abc import ABC, abstractmethod

class Pelota(ABC): # Clase Abstracta
    
    # Definicion del método abstracto
    @abstractmethod
    def rebotar(self, altura: int):
        pass
# Creando una subclase (Se crea a partir de una clase)
class PelotaDeJuguete(Pelota):
    def __init__(self) -> None:
        self.color = "Blanco"
    # Es obliigatorio implementar el método abstracto de la clase abstracta a la que pertenece la subclase
    def rebotar(self, altura: int):
        pass
    
    def imprimir(self):
        print('Método de la Subclase')
# Creación de un Objeto
pelotita = PelotaDeJuguete()
print(pelotita.rebotar(10))
print(pelotita.imprimir())