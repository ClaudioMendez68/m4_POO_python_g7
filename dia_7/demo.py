from jugador import Jugador
from monstruo import Monstruo

m = Monstruo(hp =1000, atk = 1, df = 8, nombre ='Bégimo')
m.mostrar_dialogo('GRAAAWR')

enfrentados = [Jugador(500, 10, 5, 'espada'), m]
atk = 0

while any(e.hp <= 0 for e in enfrentados) == False:
    for e in enfrentados:
        if atk:
            e.defensa(atk)
        if e.hp > 0:
            atk = e.ataque()
            # print(f'Puntos de vida de: {e.__class__.__name__}: {e.hp}')
        else:
            if isinstance(e, Monstruo):
                print('¡FELICIDADES!, ¡Has ganado la batalla!')
            elif isinstance(e, Jugador):
                print('¡Oh no!, ¡Has perdido la batalla! :(')