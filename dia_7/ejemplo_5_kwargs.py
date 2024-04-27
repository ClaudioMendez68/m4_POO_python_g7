class PelotaDeDeporte():
    def __init__(self, tamanio: int, **kwargs) -> None:
        super().__init__(**kwargs)
        print('Creando la pelota de deporte')
        self.__tamanio = tamanio
        
    @property
    def tamanio(self):
        return self.__tamanio
        
class PelotaDePlastico():
    def __init__(self, material: str, **kwargs) -> None:
        super().__init__(**kwargs)
        print('Creando al pelota de plástico')
        self.material = material
        
class PelotaDePingPong(PelotaDeDeporte, PelotaDePlastico):
    def __init__(self, timbre: str, **kwargs) -> None:
        super().__init__(**kwargs)
        print('Creando pelota de ping pong')
        self.timbre = timbre
        
pdpp = PelotaDePingPong(tamanio = 4, material = 'celuloide', timbre = 'POWERTI')
print(pdpp.tamanio)
print(pdpp.material)
print(pdpp.timbre)