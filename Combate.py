from Enemigos import *
from Mochila import *
class Combate:
    def __init__(self, equipo, enemigo):
        self.equipo = equipo
        self.enemigo = enemigo

    def turno_jugador(self, personaje, objetivo):
        personaje.atacar(objetivo)

    def turno_enemigo(self):
        for personaje in self.equipo:
            if personaje.vive():
                self.enemigo.atacar(personaje)
                break

    def combate_terminado(self):
        equipo_vivo = any(personaje.vive() for personaje in self.equipo)
        return not equipo_vivo or not self.enemigo.vive()