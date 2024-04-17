from abc import ABC, abstractmethod

class Material(ABC):
    @abstractmethod
    def romper(self):
        pass
    
class MaterialPlastico(Material):
    nombre = 'Plástico'
    duracion = 'Corta'
    def __init__(self, textura: str) -> None:
        self.textura = textura
    # Implementación del método abstarcto de la clase abstracta Material dentro de la subclase MaterialPlastico
    def romper(self):
        pass
    
class Pelota():
    def __init__(self, tamanio: int, color: str, textura: str) -> None:
        self.tamanio = tamanio
        self.color = color
        self.textura = textura
        # La clase Pelota está compuesta por un componente clase Material (MaterialPlastico)
        self.material = MaterialPlastico(self.textura) # Instancia de la clase MaterialPlastico
        
pelota = Pelota(16, 'Amarillo', 'Lisa')
print(pelota.material.nombre)
print(pelota.material.duracion)
print(pelota.material.textura)