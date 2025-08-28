from clases.electronico import Electronico
from clases.didactico import Didactico
from clases.coleccionable import Coleccionable
from clases.inventario import Inventario

def menu():
    inventario = Inventario()
    inventario.agregar_juguete(Electronico("Robot", 100000, 5))
    inventario.agregar_juguete(Didactico("Lego", 350000, 10))
    inventario.agregar_juguete(Coleccionable("Funko", 60000, 3))
    inventario.agregar_juguete(Electronico("Carro a control remoto", 200000, 6))
    inventario.agregar_juguete(Didactico("Cubo de Rubik", 15000, 18))
    inventario.agregar_juguete(Coleccionable("Goku", 97000, 2))


if __name__ == "__main__":
    menu()