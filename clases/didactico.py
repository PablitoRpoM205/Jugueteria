from clases.juguete import Juguete

class Didactico(Juguete):
    def aplicar_descuento(self, porcentaje: int) -> str:
        if porcentaje > 15:
            porcentaje = 15
            print("Error. El porcentaje máximo de descuento para los juguetes didácticos es del 15%.")
        return super().aplicar_descuento(porcentaje)