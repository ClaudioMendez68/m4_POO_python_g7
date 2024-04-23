import os
import time

'''
pagina = open(os.path.abspath('c:/Workspaces/Bootcamp/Fullstack_Python_G7/POO/dia_11/index2.html'), 'r')
with pagina as archivo:
    for line in archivo:
        print(line.strip())
archivo.close()
'''

archivo = open('c:/Workspaces/Bootcamp/Fullstack_Python_G7/POO/dia_11/nuevo_log.log', 'a')
try:
    edad = int(input('Ingrese su edad: '))
    with archivo as log:
        log.write(str(edad)+'\n')
except Exception as e:
    with open(f'{round(time.time())}.log', 'w') as log:
        log.write(f'ERROR: {e}')
log.close()