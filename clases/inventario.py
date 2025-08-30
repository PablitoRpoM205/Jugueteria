from typing import List
from clases.juguete import Juguete

class Inventario:
    def __init__(self) -> None:
        self.juguetes: List[Juguete] = []

    def agregar_juguete(self, juguete: Juguete) -> None:
        self.juguetes.append(juguete)

    def mostrar_inventario(self) -> str:
        if not self.juguetes:
            return "¡El inventario está vacío! "
        lista = ""
        for j in self.juguetes:
            lista += f"{j.get_nombre()} - Precio: {j.get_precio()} - Stock: {j.get_stock()}\n"
        return lista
