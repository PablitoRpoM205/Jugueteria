from clases.juguete import Juguete

class Coleccionable(Juguete):
    def aplicar_descuento(self, porcentaje):
        if porcentaje > 4:
            porcentaje = 4
            print("El porcentaje máximo de descuento para los juguetes coleccionables es del 4%.")
        return super().aplicar_descuento(porcentaje)