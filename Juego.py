import Narrativa
from Personaje import Rescatista, Instructor, Rider
from Sector import Sector
from Enemigo import generar_jefe
from Combate import Combate
from Interfaz import pausar, pedir_opcion
from Mochila import Mochila
from Item import BOTIQUIN, ANTIFUNGICO
from PilaCaidos import PilaCaidos

class Juego:
    def __init__(self):
        self.equipo = []
        self.mochila = Mochila()
        self.caidos = PilaCaidos()
        self.sectores = []
        self.desfibrilador = False

    def crear_equipo(self):
        self.equipo = [Rescatista(), Instructor(), Rider()]
        self.mochila = Mochila()
        self.caidos = PilaCaidos()
        self.desfibrilador = False
        self.mochila.guardar(BOTIQUIN)
        self.mochila.guardar(BOTIQUIN)
        self.mochila.guardar(ANTIFUNGICO)
        
    def crear_mapa(self):
        self.sectores = [
            Sector("Sendero del bosque muerto", "pista_verde", 1, Narrativa.TRANSICION_1),
            Sector("Campamento minero abandonado", "pista_amarilla", 1, Narrativa.TRANSICION_2),
            Sector("Cumbre del glaciar infectada", "pista_roja", 1, Narrativa.APARICION_YETI),
        ]
        
    def pelear(self, enemigos):
        nombres = []
        for enemigo in enemigos:
            nombres.append(enemigo.nombre)
        texto_nombres = ", ".join(nombres)
        print(f"¡Comienza el combate contra {texto_nombres}!")
        combate = Combate(self.equipo, enemigos, self.mochila, self.caidos)
        return combate.iniciar()

    def refugio(self):
        print(Narrativa.REFUGIO_MILITAR)
        for personaje in self.equipo:
            if personaje.vive():
                personaje.salud = personaje.salud_max
                personaje.estados_alterados.quitar("Necrosis")
        self.desfibrilador = True
        pausar()

    def acertijo(self, pista):
        texto, correcta = Narrativa.ACERTIJOS[pista]
        print(texto)
        if pedir_opcion("> ", 1, 3) == correcta:
            self.mochila.guardar(BOTIQUIN)
            print("Decisión correcta. Encuentran un Botiquín y lo guardan en la mochila")
        else:
            print("Decisión equivocada. Cada personaje vivo pierde 15 de salud")
            for personaje in self.equipo:
                if personaje.vive():
                    personaje.salud = max(personaje.salud - 15, 1)
        pausar()

    def segunda_oportunidad(self, jefe):
        if not self.desfibrilador:
            return False
        self.desfibrilador = False
        print(Narrativa.ADRENALINA_USADA)
        pausar()
        for personaje in self.equipo:
            personaje.salud = personaje.salud_max // 2
            personaje.estados_alterados.limpiar()
        while not self.caidos.esta_vacia():
            self.caidos.desapilar()
        return self.pelear([jefe])

    def recorrer_mapa(self):
        for sector in self.sectores:
            es_ultimo = sector is self.sectores[-1]
            if es_ultimo:
                self.refugio()

            print(f"\n{sector.nombre}")
            
            for i in range(sector.cantidad_encuentros):
                print(f"Encuentro {i + 1} de {sector.cantidad_encuentros}")
                if not self.pelear(sector.generar_horda()):
                    return False

            if es_ultimo and sector.texto_transicion:
                print(sector.texto_transicion)
                pausar()

            jefe = generar_jefe(sector.clave_enemigos)
            print(f"\n¡Aparece el jefe del sector: {jefe.nombre}!")
            if not self.pelear([jefe]) and not self.segunda_oportunidad(jefe):
                return False

            if not es_ultimo:
                print(sector.texto_transicion)
                pausar()
                self.acertijo(sector.clave_enemigos)
        return True
    
    def jugar(self):
        while True:
            self.crear_equipo()
            self.crear_mapa()
            print(Narrativa.INTRODUCCION)
            pausar()
            if self.recorrer_mapa():
                print(Narrativa.VICTORIA)
                break
            print(Narrativa.DERROTA)
            pausar()