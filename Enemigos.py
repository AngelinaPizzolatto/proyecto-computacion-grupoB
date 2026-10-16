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
        
ENEMIGOS = {
    #Después tenemos que cambiarle el nombre al diccionario de enemigos
    #y pensar en nombres para las 6 bestias o monstruos 
    "pista_verde": [
        ("Espectro de la ventisca", (25, 40), (10, 18), (5, 10)),
        ("Lobo corrupto de las nieves", (20, 30), (8, 14), (8, 12)),
    ],
    "pista_amarilla": [
        ("Gargola de hielo corrupta", (50, 70), (12, 20), (20, 30)),
        ("Sombre de la montaña", (35, 50), (15, 22), (10, 16)),
    ],
    "pista_roja": [
        ("Behemoth helado corrupto", (80, 110), (20, 28), (30, 40)),
        ("Guardian helado de las cumbres", (60, 90), (25, 35), (18, 25)),
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

class Yeti(Personaje):
    #el yeti será el último y más poderoso enemigo
    def __init__(self):
        super().__init__("Yeti", salud=250, fuerza=30, defensa=35)
        self.fase_avalancha = False
        self.experiencia_asignada = 100
        self.algun_item = None
        
    def recibir_danio(self, danio):
        super().recibir_danio(danio)
        if self.salud <= self.salud_max // 2 and not self.fase_avalancha:
            self.fase_avalancha = True
            self.fuerza += 15 # Aumenta su fuerza en la fase avalancha