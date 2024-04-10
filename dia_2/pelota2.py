class Pelota2():
    # Atributo de clase
    forma = 'Redondeada'
    # Método de instancia que asigna color
    def asigna_color(self, nuevo_color: str):
        self.color = nuevo_color
    
    def lee_color_y_forma(self):
        print('El color de est pelota es {}'.format(self.color))
        print('La forma de esta pelota es {}'.format(self.forma))
    # Método de instancia que lee color asignado
    def lee_color(self):
        print('El color de esta pelota es {}'.format(self.color))
        
    def lee_color_local_y_atributo(self, color_local: str):
        color = color_local
        self.lee_color()
        print('El color {} NO es el color de ESTA pelota'.format(color))
        
if __name__ == '__main__':
    pelota_multicolor = Pelota2()
    pelota_multicolor.asigna_color('Rojo')
    pelota_multicolor.lee_color()
    
    pelota_multicolor.asigna_color('Verde')
    pelota_multicolor.lee_color_local_y_atributo('Verde')
