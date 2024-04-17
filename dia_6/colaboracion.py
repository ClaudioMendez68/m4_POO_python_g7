class Superficie():
    def __init__(self) -> None:
        self.__resistencia = 2
        
    @property
    def resistencia(self):
        return self.__resistencia
    
class Pelota():
    def rebotar(self, altura: float):
        # Se instancia la clase que colabora con la clase Pelota
        s = Superficie()
        rebotes = []
        while altura > 0:
            rebotes.append(altura)
            rebotes.append(0)
            # La instancia de la clase Superficie colabora con la clase Pelota para rebotar
            altura //= s.resistencia
        return rebotes
    
p = Pelota()
print(p.rebotar(23))