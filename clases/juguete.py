class Juguete:
    def __init__(self, nombre: str, precio: float, stock: int) -> None:
        self._nombre: str = nombre
        self._precio: float = precio
        self._stock: int = stock
    
    def get_nombre(self) -> str:
        return self._nombre

    def get_precio(self) -> float:
        return self._precio
    
    def get_stock(self) -> int:
        return self._stock
    
    
    def vender(self, cantidad: int) -> str:
        if cantidad > 0 and cantidad <= self._stock:
            self._stock -= cantidad
            return f"Se vendieron {cantidad} {self._nombre}(s)."
        return "No hay elementos en el stock."
    
    def aplicar_descuento(self, porcentaje: int) -> str:
        if 0 < porcentaje < 100:
            self._precio -= self._precio * (porcentaje / 100)
            return f"Se aplicó el descuento. El precio nuevo es: {self._precio:.2f}"
        return "Porcentaje inválido. "
