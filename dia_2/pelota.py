class Pelota():
    # Método de instancia que asigna color
    def asigna_color(self, nuevo_color: str):
        self.color = nuevo_color
    # Método de instancia que lee color de la instancia
    
    def lee_color(self):
        print("El color de esta pelota es {}".format(self.color))
        
    def lee_color_local_y_atributo(self, color_local: str):
    # Esta variable "color" sólo existe en el alcance del método
        color = color_local
    # Un método de instancia puede llamar a otros métodos
        self.lee_color()
        print("El color {} NO es el color de ESTA pelota".format(color))
        
        
# Se crea instancia
pelota_multicolor = Pelota()
# Se asigna color a la instancia
pelota_multicolor.asigna_color("rojo")
# Se lee color. La salida será "El color de esta pelota es rojo"
pelota_multicolor.lee_color()
pelota_multicolor.asigna_color("verde")
# Las salidas serán:
# El color de esta pelota es verde
# El color amarillo NO es el color de ESTA pelota
pelota_multicolor.lee_color_local_y_atributo("amarillo")