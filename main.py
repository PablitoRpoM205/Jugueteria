from clases.electronico import Electronico
from clases.didactico import Didactico
from clases.coleccionable import Coleccionable
from clases.inventario import Inventario

def menu() -> None:
    inventario = Inventario()
    inventario.agregar_juguete(Electronico("Robot", 100000, 5))
    inventario.agregar_juguete(Didactico("Lego", 350000, 10))
    inventario.agregar_juguete(Coleccionable("Funko", 60000, 3))
    inventario.agregar_juguete(Electronico("Carro", 200000, 6))
    inventario.agregar_juguete(Didactico("Rubik", 15000, 18))
    inventario.agregar_juguete(Coleccionable("Goku", 97000, 2))

    while True:
        print("\n--- Menú Juguetería ---")
        print("1. Mostrar inventario")
        print("2. Vender juguete")
        print("3. Aplicar descuento")
        print("4. Salir")

        opcion: str = input("Elige una opción: ")

        if opcion == "1":
            print(inventario.mostrar_inventario())
        elif opcion == "2":
            nombre: str = input("Nombre del juguete: ")
            entrada: str = input("Cantidad: ")
            if not entrada.isdigit():
                print("Debe ingresar un número válido.")
                continue
            cantidad: int = int(entrada)

            for j in inventario.juguetes:
                if j.get_nombre().lower() == nombre.lower():
                    print(j.vender(cantidad))
                    break
            else:
                print("Juguete no encontrado.")

        elif opcion == "3":
            nombre: str = input("Nombre del juguete: ").strip()
            entrada: str = input("Porcentaje de descuento: ")
            if not entrada.isdigit():
                print("Debe ingresar un número válido.")
                continue
            porcentaje: int = int(entrada)

            encontrado: bool = False
            for j in inventario.juguetes:
                if j.get_nombre().lower() == nombre.lower():
                    print(j.aplicar_descuento(porcentaje))
                    encontrado = True
                    break

            if not encontrado:
                print("Juguete no encontrado.")


        elif opcion == "4":
            print("¡Gracias por utilizar nuestra aplicación!" )
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()