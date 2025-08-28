from clases.juguete import Juguete

class Didactico(Juguete):
    def aplicar_descuento(self, porcentaje):
        if porcentaje > 15:
            porcentaje = 15
        return super().aplicar_descuento(porcentaje)