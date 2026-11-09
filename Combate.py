import random
from TurnosCombate import TurnosCombate
from Interfaz import pedir_opcion
from Item import ItemPermanente

class Combate:
    def __init__(self, equipo, enemigos, mochila):
        self.equipo = equipo
        self.enemigos = enemigos
        self.mochila = mochila
        self.orden_turnos = TurnosCombate()
        self.pendientes = []
        self.preparar_combate()

    def preparar_combate(self):
        self.orden_turnos = TurnosCombate()
        for enemigo in self.enemigos:
            if enemigo.vive():
                self.orden_turnos.encolar(enemigo)

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
        
        vivos = [p for p in self.equipo if p.vive()]
        if vivos:
            personaje = random.choice(vivos)
            danio = enemigo.atacar(personaje)
            print(f"{enemigo.nombre} ataca a {personaje.nombre} y causa {danio} de daño")
    
    def elegir_aliado(self, pregunta):
        vivos = [p for p in self.equipo if p.vive()]
        print(pregunta)
        for i, personaje in enumerate(vivos, 1):
            print(f"{i}. {personaje.nombre} - Salud: {personaje.salud}/{personaje.salud_max}")
        return vivos[pedir_opcion("> ", 1, len(vivos)) - 1]

    def recoger_drops(self):
        for enemigo in self.enemigos:
            item = enemigo.algun_item
            if isinstance(item, ItemPermanente):
                print(f"\n{enemigo.nombre} dejó {item.nombre}: {item.descripcion}")
                item.aplicar(self.elegir_aliado("¿Quién lo usa?"))
            elif item is not None:
                self.mochila.guardar(item)
                print(f"\n{enemigo.nombre} dejó {item.nombre}. Se guardó en la mochila")

    def finalizar_combate(self):
        if not any(e.vive() for e in self.enemigos):
            exp_ganada = sum(e.experiencia_asignada for e in self.enemigos)
            for personaje in self.equipo:
                if personaje.vive():
                    personaje.ganar_experiencia(exp_ganada)
            self.recoger_drops()
            return "victoria"
        if not any(p.vive() for p in self.equipo):
            return "derrota"
        return "en_curso"         
    
    def combate_terminado(self):
        equipo_vivo = any(p.vive() for p in self.equipo)
        enemigos_vivos = any(e.vive() for e in self.enemigos)
        return not equipo_vivo or not enemigos_vivos

    def elegir_personaje(self):
        self.pendientes = [p for p in self.pendientes if p.vive()]
        if not self.pendientes:
            self.pendientes = [p for p in self.equipo if p.vive()]
        print("¿Qué personaje actúa?")
        for i, personaje in enumerate(self.pendientes, 1):
            print(f"{i}. {personaje.nombre} - Salud: {personaje.salud}/{personaje.salud_max}{personaje.estados_alterados.texto()}")
        return self.pendientes.pop(pedir_opcion("> ", 1, len(self.pendientes)) - 1)

    def elegir_enemigo(self):
        vivos = [e for e in self.enemigos if e.vive()]
        print("¿A qué enemigo ataca?")
        for i, enemigo in enumerate(vivos, 1):
            print(f"{i}. {enemigo.nombre} - Salud: {enemigo.salud}/{enemigo.salud_max}")
        return vivos[pedir_opcion("> ", 1, len(vivos)) - 1]

    def turno_enemigos(self):
        self.preparar_combate()
        enemigo = self.obtener_siguiente_turno()
        while enemigo is not None:
            self.ejecutar_turno_enemigo(enemigo)
            enemigo = self.obtener_siguiente_turno()

    def aplicar_estados(self):
        for personaje in self.equipo:
            if personaje.vive():
                personaje.procesar_estados()

    def atacar_enemigo(self, personaje):
        objetivo = self.elegir_enemigo()
        danio = self.turno_jugador(personaje, objetivo)
        if danio:
            print(f"{personaje.nombre} ataca a {objetivo.nombre} y causa {danio} de daño")
        if not objetivo.vive():
            print(f"{objetivo.nombre} fue derrotado")

    def usar_item(self):
        if self.mochila.esta_vacia():
            print("La mochila está vacía")
            return False
        print("¿Qué ítem usás?")
        print("0. Volver")
        numero = 1
        for item in self.mochila.items:
            print(f"{numero}. {item.nombre}: {item.descripcion}")
            numero += 1
        opcion = pedir_opcion("> ", 0, len(self.mochila.items))
        if opcion == 0:
            return False
        item = self.mochila.items[opcion - 1]
        aliado = self.elegir_aliado(f"¿Quién usa {item.nombre}?")
        if item.aplicar(aliado):
            self.mochila.sacar(opcion - 1)
            return True
        return False

    def turno_personaje(self, personaje):
        while True:
            print(f"¿Qué hace {personaje.nombre}?")
            print("1. Atacar")
            print("2. Abrir mochila")
            if pedir_opcion("> ", 1, 2) == 1:
                self.atacar_enemigo(personaje)
                return
            if self.usar_item():
                return

    def iniciar(self):
        while not self.combate_terminado():
            personaje = self.elegir_personaje()
            self.turno_personaje(personaje)
            if not self.combate_terminado():
                self.turno_enemigos()
                self.aplicar_estados()

        return self.finalizar_combate() == "victoria"