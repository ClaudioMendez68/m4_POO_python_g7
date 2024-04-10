class OrdenCompra():
    # Se crea método de instancia para definir atributos
    def nueva_orden(self):
        # Se definen atributos de instancia
        self.identificador = 0
        self.total_productos = 0
        self.monto = 0
        
    def asigna_monto(self, nuevo_monto: int):
        self.monto = nuevo_monto
        self.codigo_descuento = ''
        
        if self.monto > 20000:
            self.codigo_descuento = '20PORCIENTO'
        elif self.monto > 10000:
            self.codigo_descuento = '10PORCIENTO'