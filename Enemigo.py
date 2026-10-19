import random
from Personaje import Personaje
from Item import *
from Estados import *

class Enemigo(Personaje):
    def __init__(self, nombre, salud, fuerza, defensa, experiencia_asignada, algun_item = None):
        super().__init__(nombre, salud, fuerza, defensa)
        self.experiencia_asignada = experiencia_asignada
        self.algun_item = algun_item
        
    def get_algun_item(self):
        return self.algun_item
    
    def set_algun_item(self, algun_item):
        self.algun_item = algun_item
    
    def atacar(self,objetivo):
        danio = super().atacar(objetivo)
        self.turnos_atacados +=1
        if self.turnos_atacados == 3:
            estados_posibles = ["Congelamiento", "Ceguera", "Hipotermia", "Aturdimiento"]
            estado_aplicado = random.choice(estados_posibles)
            objetivo.estados_alterados.apilar(estado_aplicado)
            print(f"El {self.nombre} provocó '{estado_aplicado}' a {objetivo.nombre}")
            self.turnos_atacados = 0
        return danio
        
ENEMIGOS = {
    "pista_verde": [
        ("Alpinista novato", (25, 40), (10, 18), (5, 10)),
        ("Ankor: Lobo ártico hambriento", (20, 30), (8, 14), (8, 12)), #Lobo ártico (ataques rápidos)
    ],
    "pista_amarilla": [
        ("Guía zombie", (50, 70), (12, 20), (20, 30)), #Oso polar del norte (mucha salud, muchos golpes-quita mucha vida)
        ("Nanuk: Oso polar mutado", (35, 50), (15, 22), (10, 16)),
    ],
    "pista_roja": [
        ("Médico ", (80, 110), (20, 28), (30, 40)),
        ("Atlas: Alce gigante", (60, 90), (25, 35), (18, 25)),
    ],
}

def generar_enemigo(pista):
    nombre,rango_salud, rango_fuerza, rango_defensa = random.choice(ENEMIGOS[pista])
    salud = random.randint(*rango_salud)
    fuerza = random.randint(*rango_fuerza)
    defensa = random.randint(*rango_defensa)
    experiencia = salud // 4
    item_drop = random.choice(ITEMS + [None]) if 'ITEMS' in globals() else None
    return Enemigo(nombre, salud, fuerza, defensa, experiencia, item_drop)

def entregar_drop(enemigo, mochila):
    if enemigo.algun_item is not None:
        mochila.guardar(enemigo.algun_item)
        
def generar_jefe(pista):
    if pista == "pista_roja":
        return Yeti()

    jefe = generar_enemigo(pista)
    jefe.nombre = f"Jefe: {jefe.nombre}"
    jefe.salud = int(jefe.salud * 1.5)
    jefe.salud_max = jefe.salud
    jefe.fuerza = int(jefe.fuerza * 1.25)
    jefe.defensa = int(jefe.defensa * 1.2)
    jefe.experiencia_asignada *= 2
    return jefe

class AlpinistaInfectado(Enemigo):
    def __init__(self, nombre, salud, fuerza, defensa):
        super().__init__(nombre, salud, fuerza, defensa, experiencia_asignada=80, algun_item="Bacteria")
        
    def atacar(self, objetivo):
        danio = super().atacar(objetivo)
        
        if danio > 0 and random.random() < 0.30:  #probabilidad de contagiar la bacteria
            print(f"La bacteria del hielo de {self.nombre} infecta las heridas de {objetivo.nombre}")
            objetivo.estados_alterados.apilar("Necrosis")
        return danio

class Yeti(Enemigo):
    def __init__(self):
        super().__init__(nombre="Yeti", salud=250, fuerza=30, defensa=35,experiencia_asignada = 1000)
        self.algun_item = None
        self.fase_avalancha = False
        
    def recibir_danio(self, danio):
        super().recibir_danio(danio)
        
        if self.salud <= self.salud_max // 2 and not self.fase_avalancha:
            self.fase_avalancha = True
            self.fuerza += 15