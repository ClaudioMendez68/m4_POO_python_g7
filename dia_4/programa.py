from medicamento import Medicamento

opcion_ingreso = int(input('¿Desea agregar un medicamento?''\n1. Si\n2. No\n'))
ingresados = []

while opcion_ingreso == 1:
    nombre = input('Ingrese nombre del medicamento:\n')
    stock = int(input('Ingrese stock del medicamento:\n'))
    m = Medicamento(nombre, stock)
    
    if m in ingresados:
        indice = ingresados.indice(m)
        ingresados[indice] += m
    else:
        ingresados.append(m)
        precio_bruto = int(input('Ingrese el precio bruto del medicamento:\n'))
        m.precio = precio_bruto
        
    print(f'\n ******** DATOS MEDICAMENTO {m.nombre.upper()}********')
    print(f'PRECIO BRUTO: ${m.precio_bruto}.-')
    if m.descuento:
        print(f'DESCUENTO: {m.descuento*100}%')
    print(f'PRECIO FINAL: ${m.precio_final}.-')
    print(f'STOCK: {m.stock}')
    opcion_ingreso = int(input('¿Desea agregar un medicamento?''\n1. Si\n2. No\n'))
    
# print(f'El precio bruto del medicamento {m.nombre} es $ {m.precio_bruto}.-')


print(f'La farmacia cuenta con {len(ingresados)} medicamento(s)\n')
