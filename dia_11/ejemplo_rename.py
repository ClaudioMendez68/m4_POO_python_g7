import os

antiguo = os.path.join('C:\Workspaces\Bootcamp\Fullstack_Python_G7\POO\dia_11', 'nuevo_log.log')
nuevo = os.path.join('C:\Workspaces\Bootcamp\Fullstack_Python_G7\POO\dia_11', 'nuevo_log.txt')

os.rename(antiguo, nuevo)