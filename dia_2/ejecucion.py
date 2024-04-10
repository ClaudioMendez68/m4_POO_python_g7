from medicamento import Medicamento

medicamento_nuevo = Medicamento()

precio = int(input('Ingrese el precio del medicamento > '))

medicamento_nuevo.asigna_precio(precio)

if medicamento_nuevo.validar_mayor_a_cero(precio):
    print(medicamento_nuevo.precio)
    print(medicamento_nuevo.descuento)
    
