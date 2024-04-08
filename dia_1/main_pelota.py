# import pelota
from pelota import Pelota
# INSTANCIA o crear OBJETO
# pelota_de_andy = pelota.Pelota()
pelota_de_andy = Pelota()

print(pelota_de_andy) # <pelota.Pelota object at 0x000001FB97D09E50>
print(type(pelota_de_andy)) # <class 'pelota.Pelota'>
print(pelota_de_andy.forma) # redondeada
print(pelota_de_andy.material)

pelota_de_andy.material = "Plástico"
print(pelota_de_andy.material)

pelota_tenis = Pelota()
print(pelota_tenis.material)
pelota_tenis.material = "Caucho"
print(pelota_tenis.material)

# Método estático
# NO es necesario cerar un objetop para invocar un método estático
print(Pelota.crear_rebote)
print(Pelota.crear_rebote())

Pelota.imprimir_posiciones()
Pelota.posiciones = [2, 4, 6]
print(Pelota.posiciones)

pelota_basket = Pelota()
print(pelota_basket.posiciones)

# Método NO estático
pelota_basket.rebotar()
print(pelota_basket.posiciones)

pelota_pin_pon = Pelota()
print(pelota_pin_pon.posiciones)
# Los métodos NO estáticos permiten crear atributos de tipo 'atributo de instancia'
pelota_pin_pon.nuevo_atributo()
print(pelota_pin_pon.color)
print(pelota_tenis.color)