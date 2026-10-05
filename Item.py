class Item:
    def __init__ (self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion
        
    def aplicar(self, personaje):
        pass # esta clase base no hace nada, cada subclase define su propio efecto

class ItemConsumible(Item):
    def __init__(self, nombre, descripcion, cantidad_salud):
        super().__init__(nombre, descripcion)
        self.cantidad_salud = cantidad_salud
        
    def aplicar(self, personaje):
        personaje.salud = personaje.salud + self.cantidad_salud
        if personaje.salud > personaje.salud_max:
            personaje.salud = personaje.salud_max

class ItemPermanente(Item):
    def __init__(self, nombre, descripcion, atributo, cantidad):
        super().__init__(nombre, descripcion)
        self.atributo = atributo
        self.cantidad = cantidad
        
    def aplicar(self, personaje):
        if self.atributo == "fuerza":
            valor_actual = personaje.get_fuerza()
            personaje.set_fuerza(valor_actual + self.cantidad)
        elif self.atributo == "defensa":
            valor_actual = personaje.get_defensa()
            personaje.set_defensa(valor_actual + self.cantidad)
        elif self.atributo == "salud_max":
            valor_actual = personaje.get_salud_max()
            personaje.set_salud_max(valor_actual + self.cantidad)

ITEMS = [
    ItemConsumible("Termo caliente", "Restaura calor corporal", cantidad_salud=25),
    ItemConsumible("Barrita energética", "Restaura calor corporal", cantidad_salud=15),
    ItemPermanente("Piolet reforzado", "Mejora la técnica de forma permanente", atributo="fuerza", cantidad=5),
    ItemPermanente("Campera térmica", "Mejora el equipamiento de forma permanente", atributo="defensa", cantidad=4),
    ItemPermanente("Botas de alta montaña", "Aumenta el calor corporal máximo", atributo="salud_max", cantidad=20),
]