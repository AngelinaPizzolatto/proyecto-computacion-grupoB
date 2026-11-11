import random
import Narrativa
from Personaje import Personaje
from Item import ITEMS, REANIMACION

class Enemigo(Personaje):
    def __init__(self, nombre, salud, fuerza, defensa, experiencia_asignada, algun_item = None):
        super().__init__(nombre, salud, fuerza, defensa)
        self.experiencia_asignada = experiencia_asignada
        self.turnos_atacados = 0
        self.algun_item = algun_item
        
    def atacar(self,objetivo):
        danio = super().atacar(objetivo)
        self.turnos_atacados +=1
        if self.turnos_atacados == 3:
            estados_posibles = ["Congelamiento", "Ceguera", "Hipotermia", "Aturdimiento"]
            estado_aplicado = random.choice(estados_posibles)
            objetivo.estados_alterados.agregar(estado_aplicado)
            print(f"El {self.nombre} provocó '{estado_aplicado}' a {objetivo.nombre}")
            self.turnos_atacados = 0
        return danio
        
ENEMIGOS = {
    "pista_verde": [
        ("Alpinista novato", (25, 40), (10, 18), (5, 10)),
        ("Ankor - Lobo ártico hambriento", (20, 30), (8, 14), (8, 12)), #Lobo ártico (ataques rápidos)
    ],
    "pista_amarilla": [
        ("Guía zombie", (40, 55), (10, 15), (12, 18)),
        ("Nanuk - Oso polar mutado", (30, 42), (12, 16), (8, 12)),
    ],
    "pista_roja": [
        ("Médico", (55, 75), (14, 20), (16, 24)),
        ("Atlas - Alce gigante", (45, 65), (16, 22), (12, 18)),
    ],
}

INFECTADOS = ["Alpinista novato", "Guía zombie", "Médico"]

def generar_enemigo(pista):
    nombre,rango_salud, rango_fuerza, rango_defensa = random.choice(ENEMIGOS[pista])
    salud = random.randint(*rango_salud)
    fuerza = random.randint(*rango_fuerza)
    defensa = random.randint(*rango_defensa)
    experiencia = salud // 4
    item_drop = None
    if random.random() < 0.35:
        item_drop = random.choice(ITEMS)
    if nombre in INFECTADOS:
        return EnemigoInfectado(nombre, salud, fuerza, defensa, experiencia, item_drop)
    return Enemigo(nombre, salud, fuerza, defensa, experiencia, item_drop)

def generar_jefe(pista):
    if pista == "pista_verde":
        return EnemigoInfectado("Lobo alfa infectado", 70, 38, 12, 60, REANIMACION)
    if pista == "pista_amarilla":
        return EnemigoInfectado("Guía zombie mayor", 110, 50, 22, 100, REANIMACION)
    return Yeti()

class EnemigoInfectado(Enemigo):
    def __init__(self, nombre, salud, fuerza, defensa, experiencia_asignada, algun_item=None):
        super().__init__(nombre, salud, fuerza, defensa, experiencia_asignada, algun_item)

    def atacar(self, objetivo):
        danio = super().atacar(objetivo)
        
        if danio > 0 and random.random() < 0.30:  #probabilidad de contagiar la bacteria
            print(f"La bacteria del hielo de {self.nombre} infecta las heridas de {objetivo.nombre}")
            objetivo.estados_alterados.agregar("Necrosis")
        return danio

class Yeti(Enemigo):
    def __init__(self):
        super().__init__(nombre="Yeti", salud=220, fuerza=72, defensa=26,experiencia_asignada = 0)
        self.fase_avalancha = False
        
    def recibir_danio(self, danio):
        danio_final = super().recibir_danio(danio)
        
        if self.vive() and self.salud <= self.salud_max // 2 and not self.fase_avalancha:
            self.fase_avalancha = True
            self.fuerza += 15
            print(Narrativa.AVALANCHA)
        return danio_final