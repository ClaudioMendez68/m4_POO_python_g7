class PelotaDeDeporte():
    def __init__(self, color: str) -> None:
        self.__color = color
        
    @property
    def color(self) -> str:
        return self.__color
    
class PelotaDeFutbol(PelotaDeDeporte):
    def mostrar_color(self):
        print(f'El color de la pelota es {self.color}')
        
pdf = PelotaDeFutbol('Blanco y Negro')
pdf.mostrar_color()