class Personaje():
    def __init__(self,salud=100,calor=34,fuerza=80,nivel=0,experiencia=20):
        self.salud = salud
        self.calor = calor
        self.fuerza = fuerza
        self.nivel = nivel
        self.experiencia = experiencia
        
    def atacar(self):
        pass
    
    def recibir_danio(self):
        pass
    
    def subir_nivel(self):
        pass
    
class Rescatista(Personaje):
    def __init__(self):
        pass
        #super().__init__(salud,calor,fuerza,nivel,experiencia)
        #
#conocer mejor el mapa o atajos
#mayor calor / calor = 36
#mayor salud

class Instructor(Personaje):
    pass
#mayor experiencia
#más fuerza

class Rider(Personaje):
    pass
#este va a ser más rápido