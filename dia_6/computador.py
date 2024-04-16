class Ram():
    def __init__(self, velocidad) -> None:
        self.velocidad = velocidad
        self.bite = 32
        
class DiscoDuro():
    def __init__(self, capacidad) -> None:
        self.capacidad = capacidad
        self.tipo = "ssd"

class Teclado():
    def __init__(self, idioma: str, cant_teclas: int) -> None:
        self.idioma = 'esp'
        self.cant_teclas = 100
        
class Mouse():
    def __init__(self, tipo: str, conectividad: str) -> None:
        self.tipo = ""
        self.conectividad = ""
    
class Computador():
    def __init__(self, teclado: Teclado, mouse: Mouse) -> None:
        # El computador está compuesto por:
        self.ram = Ram(1500) # Composición
        self.disco_duro = DiscoDuro(1024) # Composición
        
        self.teclado = teclado # Agregación
        self.mouse = mouse # Agregación
# Instancias de clase
teclado = Teclado('latino', 120)
mouse = Mouse('gamer', 'bluetooth')

computador_gamer = Computador(teclado, mouse)

print(computador_gamer.ram.velocidad)
print(computador_gamer.teclado.cant_teclas)