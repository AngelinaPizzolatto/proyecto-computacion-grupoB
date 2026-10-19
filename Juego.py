import Narrativa
from Personaje import Rescatista, Instructor, Rider
from Sector import Sector
from Enemigo import generar_jefe
from Combate import Combate

class Juego:
    def __init__(self):
        self.equipo = []
        self.sector_inicial = None
        
    def crear_equipo(self):
        self.equipo = [Rescatista(), Instructor(), Rider()]
        
    def crear_mapa(self):
        sector1 = Sector("Sendero del bosque muerto", "pista_verde", 3, Narrativa.TRANSICION_1)
        sector2 = Sector("Campamento Minero Abandonado", "pista_amarilla", 3, Narrativa.TRANSICION_2)
        sector3 = Sector("Cumbre del Glaciar Corrupto", "pista_roja", 3, Narrativa.APARICION_YETI)
        sector1.set_siguiente(sector2)
        sector2.set_siguiente(sector3)
        self.sector_inicial = sector1
        
    def equipo_vivo(self):
        for personaje in self.equipo:
            if personaje.vive():
                return True
        return False

    def pelear(self, enemigo):
        print(f"¡Comienza el combate contra {enemigo.nombre}!")
        combate = Combate(self.equipo, enemigo)
        return combate.iniciar()

    def recorrer_mapa(self):
        sector = self.sector_inicial
        while sector is not None:
            print("=== " + sector.nombre + " ===")
            
            for i in range(sector.cantidad_encuentros):
                enemigo = sector.generar_enemigo_normal()
                if not self.pelear(enemigo):
                    return False
                
            if not sector.tiene_siguiente() and sector.texto_transicion:
                print(sector.texto_transicion)

            jefe = generar_jefe(sector.clave_enemigos)
            if not self.pelear(jefe):
                return False
            
            if sector.tiene_siguiente():
                print(sector.texto_transicion)
            sector = sector.get_siguiente()
        return True
    
    def jugar(self):
        while True:
            self.crear_equipo()
            self.crear_mapa()
            print(Narrativa.INTRODUCCION)
            if self.recorrer_mapa():
                print(Narrativa.VICTORIA)
                break
            print(Narrativa.DERROTA)


if __name__ == "__main__":
    Juego().jugar()