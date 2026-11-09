class TurnosCombate:  #Cola utilizada para manejar el orden de los turnos
    def __init__(self):
        self._combatientes = []
        
    def encolar(self, combatiente):
        self._combatientes.append(combatiente)

    def desencolar(self):
        if self.esta_vacia():
            return None
        return self._combatientes.pop(0)

    def esta_vacia(self):
        return len(self._combatientes) == 0