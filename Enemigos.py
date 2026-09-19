import random
from Personaje import Personaje

class Enemigo(Personaje):
    def __init__(self,nombre,salud,fuerza,defensa, experienci_asignada,algun_item):
        super.__init__(nombre,salud,fuerza,defensa)
        self.experiencia_asignada = experienci_asignada
        self.algun_item = algun_item
        
ENEMIGOS = {
    #Después tenemos que cambiarle el nombre al diccionario de enemigos
    #y pensar en nombres para las 6 bestias o monstruos 
    "pista_verde": [
        ("Monstruo1", (25, 40), (10, 18), (5, 10)),
        ("Monstruo2", (20, 30), (8, 14), (8, 12)),
    ],
    "pista_amarilla": [
        ("Monstruo3", (50, 70), (12, 20), (20, 30)),
        ("Monstruo4", (35, 50), (15, 22), (10, 16)),
    ],
    "pista_roja": [
        ("Monstruo5", (80, 110), (20, 28), (30, 40)),
        ("Monstruo6", (60, 90), (25, 35), (18, 25)),
    ],
}

def generar_enemigo(pista):
    nombre,rango_salud, rango_fuerza, rango_defensa = random.choice(ENEMIGOS[pista])
    salud = random.randint(*rango_salud)
    fuerza = random.randint(*rango_fuerza)
    defensa = random.randint(*rango_defensa)
    experiencia = salud // 4
    return Enemigo(nombre, salud, fuerza, defensa, experiencia)

class Yeti(Personaje):
    #el yeti será el último y más poderoso enemigo
    def __init__(self):
        super().__init__("Yeti", salud=250, fuerza=30, defensa=35)
        self.fase_avalancha = False
        
    def recibir_danio(self, danio):
        super().recibir_daño(danio)
        if self.salud <= self.salud_max // 2 and not self.fase_avalancha:
            self.fase_avalancha = True