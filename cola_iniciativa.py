class ColaIniciativa:
    def __init__(self):
        self.cola = []
        
    def cargar_combatientes(self, lista_combatientes):        
        self.cola = sorted(lista_combatientes, key=lambda c: getattr(c, 'fuerza', 0), reverse=True)
        
    def siguiente(self):
        if self.cola:
            return self.cola.pop(0)
        return None


cola_iniciativa = ColaIniciativa