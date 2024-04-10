import os
from orden_compra import OrdenCompra

oc = OrdenCompra()
oc.nueva_orden()

oc.identificador = int(input('Ingrese identificador de la Orden de Compra: '))
oc.total_productos = int(input('Ingrese el total de productos: '))
monto = int(input('Ingrese el monto: '))
oc.asigna_monto(monto)

os.system('cls')
    
print(f'Id orden de compra: {oc.identificador}')
print(f'Total de Productos: {oc.total_productos}')
print(f'Monto: ${oc.monto}.-')
print(f'El código de descuento es: {oc.codigo_descuento}')