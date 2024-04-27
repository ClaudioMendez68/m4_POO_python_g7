class PelotaDeDeporte():
    def __init__(self, tamanio: int) -> None:
        print('Creando la pelota de deporte')
        self.__tamanio = tamanio
        
    @property
    def tamanio(self):
        return self.__tamanio
        
class PelotaDePlastico():
    def __init__(self, material: str) -> None:
        print('Creando al pelota de plástico')
        self.material = material
        
class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, tamanio: int, material: str, timbre: str) -> None:
        PelotaDeDeporte.__init__(self, tamanio)
        PelotaDePlastico.__init__(self, material)
        print('Creando pelota de ping pong')
        self.timbre = timbre
        
pdpp = PelotaDePingPong(4, 'celuloide', 'POWERTI')
print(pdpp.tamanio)
print(pdpp.material)
print(pdpp.timbre)