from Enemigos import *
from Estados import *
class Combate:
    def __init__(self, equipo, enemigo):
        self.equipo = equipo
        self.enemigo = enemigo

    def turno_jugador(self, personaje, objetivo, accion="atacar"):
        if not personaje.vive():
            return False
        
        if accion == "atacar":
            personaje.atacar(objetivo)
            return True
        return False

    def turno_enemigo(self):
        if not self.enemigo.vive():
            return
        
        for personaje in self.equipo:
            if personaje.vive():
                self.enemigo.atacar(personaje)
                break
    
    def finalizar_combate(self):
        if not self.enemigo.vive():
            exp_ganada = getattr(self.enemigo, 'experiencia_asignada', 20)
            for personaje in self.equipo:
                if personaje.vive():
                    if hasattr(personaje, 'ganar_experiencia'):
                        personaje.ganar_experiencia(exp_ganada)
            return "victoria"   
        if not any(personaje.vive() for personaje in self.equipo):
            return "derrota"
        return "en_curso"         
    
    def combate_terminado(self):
        equipo_vivo = any(personaje.vive() for personaje in self.equipo)
        return not equipo_vivo or not self.enemigo.vive()