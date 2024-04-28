from ejemplo_5_instance_pelota import PelotaDeFutbol, PelotaDeTenis

pdf = PelotaDeFutbol('Blanco y Negro', 15)
pdt = PelotaDeTenis()

pelotas = [pdf, pdf, pdt, pdt, pdf]

# p = PelotaDeTenis('Roja') # TypeError: PelotaDeTenis.__init__() takes 1 positional argument but 2 were given
# print(p.color)

for p in pelotas:
    if isinstance(p, PelotaDeTenis) == False:
        p.color = 'Roja'
        print(p.color)
    if isinstance(p, PelotaDeFutbol):
        print(p.hacer_pase('Jugador 2', 3))
    elif isinstance(p, PelotaDeTenis):
        print(p.hacer_saque(2, 3))
    print('=============================')