from pelota import Pelota

# Creación de Objeto o Instancia de la Clase
pelota_multicolor = Pelota()

print(pelota_multicolor)
# print(pelota_multicolor.color) # AttributeError: 'Pelota' object has no attribute 'color'
pelota_multicolor.asigna_color('rojo')
print(pelota_multicolor.color)

pelota_multicolor.lee_color()

pelota_multicolor.asigna_color('verde')
pelota_multicolor.lee_color_local_y_atributo('amarillo')

pelota_negra = Pelota()
pelota_negra.lee_color_local_y_atributo('negro') # AttributeError: 'Pelota' object has no attribute 'color'