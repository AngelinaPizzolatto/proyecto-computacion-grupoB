class Mochila:
    def __init__(self):
        self.items = []

    def guardar(self, item):
        self.items.append(item)

    def esta_vacia(self):
        return len(self.items) == 0

    def sacar(self, posicion):
        return self.items.pop(posicion)
