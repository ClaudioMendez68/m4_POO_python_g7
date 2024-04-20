'''
class MisExcepciones(Exception):

    def imprimir_promedio(self, dividendo, divisor):
        promedio = dividendo/divisor 
        print(f'El promedio es {promedio}')
        
calcular_promedio = MisExcepciones()

calcular_promedio.imprimir_promedio(100, 0) # ZeroDivisionError: division by zero
'''
class Error(Exception):
    pass

class DivisorError(Error):
    def __init__(self, mensaje, divisor) -> None:
        self.divisor = divisor
        self.mensaje = mensaje

class MisExcepciones(Exception):

    def imprimir_promedio(self, dividendo, divisor):
        try:
            promedio = dividendo/divisor 
            print(f'El promedio es {promedio}')
        except ZeroDivisionError:
            print('El divisor no puede tener el valor 0')
        # Captura genérica de error
        except Exception as error:
            print(f'Se ha producido un error "{error}"')
                        
calcular_promedio = MisExcepciones()

valido = True
while valido:
    try:
        dividendo = int(input('Ingrese el dividendo: > '))
        valido = False
    except ValueError:
        print('Error en el ingreso de datos')

valido = True
while valido:
    try:
        divisor = int(input('Ingrese el divisor: > '))
        if divisor == 0:
            raise DivisorError('El divisor no puede tener el valor 0', divisor)
        valido = False
    except DivisorError as error:
        print('Error en el ingreso del divisor. ', error.mensaje)
    except ValueError:
        print('Error en el ingreso de datos')
    
calcular_promedio.imprimir_promedio(dividendo, divisor)