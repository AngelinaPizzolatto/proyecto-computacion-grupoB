import random
from TurnosCombate import TurnosCombate
from Interfaz import pedir_opcion
from Item import ItemPermanente, ItemReanimacion

class Combate:
    def __init__(self, equipo, enemigos, mochila, caidos):
        self.equipo = equipo
        self.enemigos = enemigos
        self.mochila = mochila
        self.caidos = caidos
        self.orden_turnos = TurnosCombate()
        self.pendientes = []
        self.habilidades_usadas = []
        self.preparar_combate()

    def obtener_vivos(self, personajes):
        vivos = []
        for personaje in personajes:
            if personaje.vive():
                vivos.append(personaje)
        return vivos

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
        
        vivos = self.obtener_vivos(self.equipo)
        if vivos:
            personaje = random.choice(vivos)
            for candidato in vivos:
                if candidato.estados_alterados.tiene("Provocando"):
                    personaje = candidato
            danio = enemigo.atacar(personaje)
            print(f"{enemigo.nombre} ataca a {personaje.nombre} y causa {danio} de daño")
            self.registrar_caidos()

    def registrar_caidos(self):
        for personaje in self.equipo:
            if not personaje.vive() and not self.caidos.contiene(personaje):
                self.caidos.apilar(personaje)
                print(f"{personaje.nombre} ha caído")

    def elegir_aliado(self, pregunta):
        vivos = self.obtener_vivos(self.equipo)
        print(pregunta)
        numero = 1
        for personaje in vivos:
            print(f"{numero}. {personaje.nombre} - Salud: {personaje.salud}/{personaje.salud_max}{personaje.estados_alterados.texto()}")
            numero += 1
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
        if len(self.obtener_vivos(self.enemigos)) == 0:
            exp_ganada = 0
            for enemigo in self.enemigos:
                exp_ganada += enemigo.experiencia_asignada
            for personaje in self.equipo:
                if personaje.vive():
                    personaje.ganar_experiencia(exp_ganada)
            self.recoger_drops()
            return "victoria"
        if len(self.obtener_vivos(self.equipo)) == 0:
            return "derrota"
        return "en_curso"         
    
    def combate_terminado(self):
        equipo_vivo = len(self.obtener_vivos(self.equipo)) > 0
        enemigos_vivos = len(self.obtener_vivos(self.enemigos)) > 0
        return not equipo_vivo or not enemigos_vivos

    def elegir_personaje(self):
        self.pendientes = self.obtener_vivos(self.pendientes)
        if not self.pendientes:
            self.pendientes = self.obtener_vivos(self.equipo)
        print("¿Qué personaje actúa?")
        numero = 1
        for personaje in self.pendientes:
            print(f"{numero}. {personaje.nombre} - Salud: {personaje.salud}/{personaje.salud_max}{personaje.estados_alterados.texto()}")
            numero += 1
        return self.pendientes.pop(pedir_opcion("> ", 1, len(self.pendientes)) - 1)

    def elegir_enemigo(self):
        vivos = self.obtener_vivos(self.enemigos)
        print("¿A qué enemigo ataca?")
        numero = 1
        for enemigo in vivos:
            print(f"{numero}. {enemigo.nombre} - Salud: {enemigo.salud}/{enemigo.salud_max}")
            numero += 1
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
                self.registrar_caidos()

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
        if isinstance(item, ItemReanimacion):
            usado = item.aplicar(self.caidos)
        else:
            usado = item.aplicar(self.elegir_aliado(f"¿Quién usa {item.nombre}?"))
        if usado:
            self.mochila.sacar(opcion - 1)
            return True
        return False

    def usar_habilidad(self, personaje):
        if personaje in self.habilidades_usadas or personaje.estados_alterados.tiene("Aturdimiento"):
            print(f"{personaje.nombre} no puede usar su habilidad ahora")
            return False
        self.habilidades_usadas.append(personaje)
        print(personaje.usar_habilidad(self.equipo, self.enemigos))
        return True

    def turno_personaje(self, personaje):
        while True:
            print(f"¿Qué hace {personaje.nombre}?")
            print("1. Atacar")
            print("2. Abrir mochila")
            print("3. Usar habilidad")
            opcion = pedir_opcion("> ", 1, 3)
            if opcion == 1:
                self.atacar_enemigo(personaje)
                return
            if opcion == 2 and self.usar_item():
                return
            if opcion == 3 and self.usar_habilidad(personaje):
                return

    def iniciar(self):
        while not self.combate_terminado():
            personaje = self.elegir_personaje()
            self.turno_personaje(personaje)
            if not self.combate_terminado():
                self.turno_enemigos()
                self.aplicar_estados()

        return self.finalizar_combate() == "victoria"