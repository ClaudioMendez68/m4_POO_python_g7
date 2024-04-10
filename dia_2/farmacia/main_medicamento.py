from medicamento import Medicamento

# Paso 1: Crear una instancia
medicamento_nuevo =  Medicamento()

# Paso 2 : Solicitud de ingreso de datos
precio = int(input('Ingrese el precio del medicamento >'))

# Paso 3: Pasar al método de instancia el valor capturado
medicamento_nuevo.asigna_precio(precio)
print(medicamento_nuevo.precio)