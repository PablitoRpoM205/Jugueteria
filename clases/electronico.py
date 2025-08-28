from clases.juguete import Juguete

class Electronico(Juguete):
    def aplicar_descuento(self, porcentaje):
        if porcentaje > 20:
            porcentaje = 20
        return super().aplicar_descuento(porcentaje)