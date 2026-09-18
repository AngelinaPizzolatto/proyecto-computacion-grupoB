class Personaje():
    def __init__(self, nombre, salud=100, fuerza=80, defensa=50, nivel=1, experiencia=0):
        self.nombre = nombre
        self.salud = salud
        self.salud_max = salud
        self.fuerza = fuerza
        self.defensa = defensa
        self.nivel = nivel
        self.experiencia = experiencia
        
    def vive(self):
        return self.salud > 0
    
    def atacar(self, objetivo):
        danio = max(self.fuerza - objetivo.defensa //2,1)
        objetivo.recibir_danio(danio)
        return danio
    
    def recibir_danio(self,danio):
        self.salud = max(self.salud - danio, 0)
        
    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        while self.experiencia >= self._experiencia_para_subir():
            self.subir_nivel()
    
    def experiencia_para_subir(self):
        return self.nivel * 50
    
    def subir_nivel(self):
        self.experiencia -= self.experiencia_para_subir()
        self.nivel += 1
        self.fuerza += 5
        self.defensa += 3
        self.salud_max += 15
        self.salud = self.salud_max #esto es para que cuando se suba de nivel la salud se restablezca al 100%
    
class Rescatista(Personaje):
    def __init__(self,nombre = "Rescatista"):
        super().__init__(nombre, salud=110, fuerza=75, defensa=60)
#conocer mejor el mapa o atajos
#posee más calor corporal, lo que se traduce en más salud de lo normal

class Instructor(Personaje):
    def __init__(self, nombre= "Instructor"):
        super().__init__(nombre, salud=90, fuerza=90, defensa=55)
#tiene más fuerza y experiencia

class Rider(Personaje):
    def __init__(self, nombre= "Rider"):
        super().__init__(nombre, salud=95, fuerza=85, defensa=45)
#el rider al ser un profesional va a ser más rápido y puede defender al equipo mejor (ver como agregamos esto)