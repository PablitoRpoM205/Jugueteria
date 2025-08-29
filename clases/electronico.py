from clases.juguete import Juguete

class Electronico(Juguete):
    def aplicar_descuento(self, porcentaje: int) -> str:
        if porcentaje > 20:
            porcentaje = 20
            print("Error. El porcentaje máximo de descuento para los juguetes electrónicos es del 20%.")
        return super().aplicar_descuento(porcentaje)