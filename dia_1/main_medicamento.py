from medicamento import Medicamento
# Instancia de clase o creación de objetos
paracetamol = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento)
print(aspirina.descuento)

paracetamol.descuento = 0.1
print(paracetamol.descuento)

paracetamol.IVA = 0.19
print(paracetamol.IVA)