class Juguete:
    def __init__(self, nombre, precio, stock):
        self._nombre = nombre
        self._precio = precio
        self._stock = stock
    
    def get_nombre(self):
        return self._nombre

    def get_precio(self):
        return self._precio
    
    def get_stock(self):
        return self._stock
    
    
    def vender(self, cantidad):
        if cantidad > 0 and cantidad <= self._stock:
            self._stock -= cantidad
            return f"Se vendieron {cantidad} {self._nombre}(s)."
        return "No hay elementos en el stock."
    
    def aplicar_descuento(self, porcentaje):
        if 0 < porcentaje < 100:
            self._precio -= self._precio * (porcentaje / 100)
            return f"Se aplicó el descuento. El precio nuevo es: {self._precio:.2f}"
        return "Porcentaje inválido. "
