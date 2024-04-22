'''
Función OPEN
file = open(ruta, argumento o modo de apertura)
'''

import os

try:
    log_file = open(os.path.abspath('c:/Workspaces/Bootcamp/Fullstack_Python_G7/POO/dia_11/logs/error.log'))
    print(log_file)
    print(type(log_file))
except FileNotFoundError as fnfe:
    print('Archivo o directorio no encontrado')
    print(fnfe)

# ARGUMENTO
print('=======================================')
log_file2 = open(os.path.abspath('c:/Workspaces/Bootcamp/Fullstack_Python_G7/POO/dia_11/html/index.html'), 'r')
print(log_file2.read())
log_file2.close()
print('=======================================')
log_file3 = open(os.path.abspath('c:/Workspaces/Bootcamp/Fullstack_Python_G7/POO/dia_11/html/index.html'), 'r')
print(log_file3.readline()) # Se debe utilizar un for para mostrar el contenido línea a línea
log_file3.close()
print('=======================================')
log_file4 = open(os.path.abspath('c:/Workspaces/Bootcamp/Fullstack_Python_G7/POO/dia_11/html/index.html'), 'r')
print(log_file4.readlines()) # Retorna una lista de cada una de las líneas como str
log_file4.close()
print('=======================================')
with open(os.path.abspath('c:/Workspaces/Bootcamp/Fullstack_Python_G7/POO/dia_11/html/index.html'), 'r') as archivo:
    # print(archivo) # <_io.TextIOWrapper name='c:\\Workspaces\\Bootcamp\\Fullstack_Python_G7\\POO\\dia_11\\html\\index.html' mode='r' encoding='cp1252'>
    for line in archivo:
        print(line.strip())
        
# ARGUMENTO 'w' SOLO ESCRITURA
# La ruta donde se creará el archivo DEBE EXISTIR
print('=======================================')
log_file5 = open(os.path.abspath('c:/Workspaces/Bootcamp/Fullstack_Python_G7/POO/dia_11/html/assets/css/style.css'), 'w')
log_file5.write('/*Este es otro comentario*/\n')
log_file5.write('*{\n\tmargin: 0px\n}')
log_file5.close()

import time
try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open(f"{round(time.time())}.log", "w") as log:
        log.write(f"ERROR: {e}")
        
# Para hacer uso de 'r+' en reemplazo de 'w', el archivo DEBE EXISTIR