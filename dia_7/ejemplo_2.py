class PelotaDeDeporte():
    tipo = 'Deporte'
    
class PelotaDePlastico():
    tipo='Plástico'
    
class PelotaDePingPong(PelotaDePlastico, PelotaDeDeporte):
    pass

print(PelotaDePingPong.tipo)