class Estados:

    def __init__(self):
        self._estados = {}

    def agregar(self, estado, turnos=4):
        self._estados[estado] = turnos

    def tiene(self, estado):
        return estado in self._estados

    def quitar(self, estado):
        self._estados.pop(estado, None)

    def limpiar(self):
        self._estados.clear()

    def pasar_turno(self):
        for estado in list(self._estados):
            if estado != "Necrosis":
                self._estados[estado] -= 1
                if self._estados[estado] == 0:
                    self.quitar(estado)

    def texto(self):
        if not self._estados:
            return ""
        return " [" + ", ".join(self._estados) + "]"
