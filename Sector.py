from Enemigos import generar_enemigo

class Sector:
    def __init__(self, nombre, clave_enemigos, cantidad_encuentros, texto_transicion):
        self.nombre = nombre
        self.clave_enemigos = clave_enemigos # pista_verde, pista amarilla, pista roja
        self.cantidad_encuentros = cantidad_encuentros
        self.texto_transicion = texto_transicion # lo que se muestra al pasar al sector que sigue
        self.siguiente_sector = None
        
    def get_siguiente(self):
        return self.siguiente_sector
    
    def set_siguiente(self, sector):
        self.siguiente_sector = sector
        
    def tiene_siguiente(self):
        return self.siguiente_sector is not None
    
    def generar_enemigo_normal(self):
        return generar_enemigo(self.clave_enemigos)
        