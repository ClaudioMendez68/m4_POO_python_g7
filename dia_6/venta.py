class DetalleVentaItem():
    def __init__(self, producto: str, cantidad: int) -> None:
        self.__producto = producto
        self.__cantidad = cantidad
        
    # Getters
    @property
    def producto(self):
        return self.__producto
    @property
    def cantidad(self):
        return self.__cantidad
    
class DetalleVenta():
    def __init__(self) -> None:
        self.__items = []
    # Agregación
    def agregar_item(self, item: DetalleVentaItem):
        self.__items.append(item)
    # Sobrecarga del método __str__ para que se muestre en pantalla los ítems ingresados
    def __str__(self):
        retorno = (':::::::: DETALLE DE ESTA VENTA ::::::::\n'
                'PRODUCTO\tCANTIDAD\n')
        items = [f'{i.producto}\t\t{i.cantidad}\n' for i in self.__items]
        return f'{retorno}{''.join(items)}'
    
class Venta():
    # Composición
    def __init__(self) -> None:
        self.__detalle = DetalleVenta()
        
    def modificar_detalle(self, producto: str, cantidad: int):
        detalle_venta_item = DetalleVentaItem(producto, cantidad)
        self.__detalle.agregar_item(detalle_venta_item)
    
    @property
    def detalle(self):
        return self.__detalle