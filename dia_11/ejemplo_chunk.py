chunk_size = 70
with open('C:\Workspaces\Bootcamp\Fullstack_Python_G7\POO\dia_11/error.log', 'rb') as archivo:
    chunk = archivo.read(chunk_size)
    while chunk:
        print(chunk)
        chunk = archivo.read(chunk_size)