class Mochila:
    
    def __init__(self):
        self._items = []
        
    def guardar(self,item):
        self._items.append(item)
        
    def sacar_ultimo(self):
        if self.esta_vacia() == True:
            return None
        else:
            return self._items.pop()
        
    def esta_vacia(self):
        return len(self._elements) == 0