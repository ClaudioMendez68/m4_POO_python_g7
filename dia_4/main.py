from pelota import Pelota

nueva_pelota = Pelota("Negra")

nueva_pelota.setColor("Blanco")
print(nueva_pelota.color)

nueva_pelota.color = "Naranja"
print(nueva_pelota.color)

nueva_pelota.color = "Amarillo"
print(nueva_pelota.color)

del nueva_pelota.color
print(nueva_pelota.color)

nueva_pelota.__password = "admin1234"
# print(nueva_pelota.__password)