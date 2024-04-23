from datetime import datetime

try:
    edad = int(input('Ingrese su edad: '))
except Exception as e:
    with open('C:\Workspaces\Bootcamp\Fullstack_Python_G7\POO\dia_11/error.log', 'a+') as log:
        log.seek(0)
        print(log.read())
        now = datetime.now()        
        log.write(f'[{now.strftime("%d-%m-%Y %H:%M:%S")}] ERROR: {e}\n')
        log.seek(0)
        print(log.read(20))
        print(log.read(20))
        print(log.read(20))

        log.close()