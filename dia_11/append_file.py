from datetime import datetime

try:
    edad = int(input("Ingrese su edad:\n"))
except Exception as e:
    with open("c:/Workspaces/Bootcamp/Fullstack_Python_G7/POO/dia_11/logs/error.log", "a+") as log:
        log.seek(0)        
        print(log.read())
        now = datetime.now()
        log.write(f"[{now.strftime('%Y-%m-%d %H:%M:%S')}] ERROR: {e}\n")
        log.seek(0) # El valor de Seek no tiene que ver con las líneas, sino que con los caracteres (bytes)
        print(log.read())