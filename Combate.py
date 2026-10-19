from TurnosCombate import TurnosCombate


class Combate:
    def __init__(self, equipo, enemigo):
        self.equipo = equipo
        self.enemigo = enemigo
        self.orden_turnos = TurnosCombate()
        self.preparar_combate()

    def preparar_combate(self):
        self.orden_turnos = TurnosCombate()
        for personaje in self.equipo:
            if personaje.vive():
                self.orden_turnos.encolar(personaje)
        if self.enemigo.vive():
            self.orden_turnos.encolar(self.enemigo)

    def turno_jugador(self, personaje, objetivo, accion="atacar"):
        if not personaje.vive():
            return False
        
        if accion == "atacar":
            return personaje.atacar(objetivo)
        return False

    def obtener_siguiente_turno(self):
        return self.orden_turnos.desencolar()

    def ejecutar_turno_enemigo(self, enemigo):
        if not enemigo.vive():
            return
        
        for personaje in self.equipo:
            if personaje.vive():
                danio = enemigo.atacar(personaje)
                print(f"{enemigo.nombre} ataca a {personaje.nombre} y causa {danio} de daño.")
                break
    
    def finalizar_combate(self):
        if not self.enemigo.vive():
            exp_ganada = getattr(self.enemigo, 'experiencia_asignada', 20)
            for personaje in self.equipo:
                if personaje.vive():
                    if hasattr(personaje, 'ganar_experiencia'):
                        personaje.ganar_experiencia(exp_ganada)
            return "victoria"   
        if not any(p.vive() for p in self.equipo):
            return "derrota"
        return "en_curso"         
    
    def combate_terminado(self):
        equipo_vivo = any(p.vive() for p in self.equipo)
        return not equipo_vivo or not self.enemigo.vive()

    def iniciar(self):
        while not self.combate_terminado():
            self.preparar_combate()
            combatiente = self.obtener_siguiente_turno()

            while combatiente is not None:
                if combatiente.vive():
                    if combatiente is self.enemigo:
                        self.ejecutar_turno_enemigo(combatiente)
                    else:
                        danio = self.turno_jugador(combatiente, self.enemigo)
                        if danio:
                            print(
                                f"{combatiente.nombre} ataca a {self.enemigo.nombre} "
                                f"y causa {danio} de daño."
                            )

                resultado = self.finalizar_combate()
                if resultado != "en_curso":
                    if resultado == "victoria":
                        print(f"{self.enemigo.nombre} fue derrotado.")
                    return resultado == "victoria"

                combatiente = self.obtener_siguiente_turno()

        return self.finalizar_combate() == "victoria"