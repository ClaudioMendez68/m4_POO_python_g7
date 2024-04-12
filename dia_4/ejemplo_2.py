class Pelota():
    # Método constructor de la clase Pelota()
    def __init__(self, color: str, material: str) -> None:
        self.color = color
        self. material = material
        
    @property
    def color_y_material(self):
        return f'Pelota {self.color} de {self.material}'
    
p = Pelota("Amarilla", "Plástico")
print(p.color_y_material)