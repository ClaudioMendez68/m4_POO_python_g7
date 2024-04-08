from medicamento import Medicamento
# Instancia de clase o creación de objetos
paracetamol = Medicamento()
aspirina = Medicamento()

print(paracetamol.descuento)
print(aspirina.descuento)
# Modificación del ESTADO de un objeto
paracetamol.descuento = 0.1
print(paracetamol.descuento)

Medicamento.descuento = 0.1

# paracetamol.IVA = 0.19
# print(paracetamol.IVA)

precio = int(input("Ingrese el precio a validar: "))
es_valido = Medicamento.validar_mayor_a_cero(precio)
if es_valido:
    print("El precio ES válido")
else:
    print("El precio NO es válido")
    
print(paracetamol.descuento, aspirina.descuento)
    
if paracetamol.IVA == aspirina.IVA and paracetamol.descuento == aspirina.descuento:
    print("Los medicamentos tienen los mismos valores")
    print(f"El valor del IVA es: {Medicamento.IVA}")
    print(f"El valor del descuento es: {Medicamento.descuento}")

Medicamento.IVA = 0.19
ibuprofeno = Medicamento()
# ibuprofeno.modificar_atributo()
print(ibuprofeno.IVA)
print(aspirina.IVA)