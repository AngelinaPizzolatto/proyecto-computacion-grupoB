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
            personaje.fuerza = personaje.fuerza + self.cantidad
        elif self.atributo == "defensa":
            personaje.defensa = personaje.defensa + self.cantidad
        elif self.atributo == "salud_max":
            personaje.salud_max = personaje.salud_max + self.cantidad
    