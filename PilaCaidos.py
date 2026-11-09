class PilaCaidos:
    def __init__(self):
        self.caidos = []

    def apilar(self, personaje):
        self.caidos.append(personaje)

    def desapilar(self):
        return self.caidos.pop()

    def esta_vacia(self):
        return len(self.caidos) == 0

    def contiene(self, personaje):
        return personaje in self.caidos
