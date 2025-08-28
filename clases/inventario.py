class Inventario:
    def __init__(self):
        self.juguetes = []

    def agregar_juguete(self, juguete):
        self.juguetes.append(juguete)

    def mostrar_inventario(self):
        if not self.juguetes:
            return "¡El inventario está vacío!"
        lista = ""
        for j in self.juguetes:
            lista += f"{j.get_nombre()} - Precio: {j.get_precio()} - Stock: {j.get_stock()}\n"
        return lista
