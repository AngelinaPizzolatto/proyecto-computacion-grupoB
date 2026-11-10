import random
from Enemigo import generar_enemigo

class Sector:
    def __init__(self, nombre, clave_enemigos, cantidad_encuentros, texto_transicion):
        self.nombre = nombre
        self.clave_enemigos = clave_enemigos 
        self.cantidad_encuentros = cantidad_encuentros
        self.texto_transicion = texto_transicion 
        self.siguiente_sector = None
        
    def get_siguiente(self):
        return self.siguiente_sector
    
    def set_siguiente(self, sector):
        self.siguiente_sector = sector
        
    def tiene_siguiente(self):
        return self.siguiente_sector is not None
    
    def generar_horda(self):
        cantidad = random.randint(1, 2)
        horda = []
        for i in range(cantidad):
            horda.append(generar_enemigo(self.clave_enemigos))
        return horda
        