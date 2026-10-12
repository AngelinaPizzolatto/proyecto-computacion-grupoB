class Estados: #pila de estados
    
    def __init__(self):
        self._estados  = []
        
    def apilar(self, estado):
        self._estados.append(estado)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self._estados.pop()

    def esta_vacia(self):
        return len(self._estados) == 0
        
    def ver_tope(self):
        if not self.esta_vacia():
            return self._estados[-1]
        return None