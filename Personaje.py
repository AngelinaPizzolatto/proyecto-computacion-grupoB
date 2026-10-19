from Estados import Estados
class Personaje():
    def __init__(self, nombre, salud=100, fuerza=80, defensa=50, nivel=1, experiencia=0):
        self.nombre = nombre
        self.salud = salud
        self.salud_max = salud
        self.fuerza = fuerza
        self.defensa = defensa
        self.nivel = nivel
        self.experiencia = experiencia
        self.estados_alterados = Estados()
        
    def get_fuerza(self):
        return self.fuerza
    
    def get_defensa(self):
        return self.defensa
    
    def get_salud_max(self):
        return self.salud_max
    
    def set_fuerza(self, nuevo_valor):
        if nuevo_valor < 0:
            self.fuerza = 0
        else:
            self.fuerza = nuevo_valor
    
    def set_defensa(self, nuevo_valor):
        if nuevo_valor < 0:
            self.defensa = 0
        else:
            self.defensa = nuevo_valor
        
    def set_salud_max(self, nuevo_valor):
        if nuevo_valor < 0:
            self.salud_max = 0
        else:
            self.salud_max = nuevo_valor
        
        
    def vive(self):
        return self.salud > 0
    
    def atacar(self, objetivo):
        estado_actual = self.estados_alterados.ver_tope()
        fuerza_efectiva = self.fuerza
        
        if estado_actual == "Aturdimiento":
            print(f"{self.nombre} fue aturdido por la Escarcha. Pierde su turno")
            return 0
        
        if estado_actual == "Hipotermia":
            dano_hipotermia = 5
            self.salud = max(self.salud - dano_hipotermia, 0)
            print(f"{self.nombre} sufre {dano_hipotermia} de daño por Hipotermia.")
            if not self.vive():
                print(f"{self.nombre} ha caído por la Hipotermia antes de poder atacar")
                return 0
            
        if estado_actual == "Ceguera":
            fuerza_efectiva = self.fuerza // 2
            print(f"{self.nombre} tiene Ceguera. Su ataque es demasiado débil")
        
        danio = max(self.fuerza - (objetivo.defensa //2), 1)
        objetivo.recibir_danio(danio)
        return danio
    
    def recibir_danio(self,danio):
        estado_actual = self.estados_alterados.ver_tope()
        if estado_actual == "Congelamiento":
            danio_extra = 5
            danio += danio_extra
            print(f"La armadura de {self.nombre} está frágil por el Congelamiento. Recibe {danio_extra} de daño extra")
        
        self.salud = max(self.salud - danio, 0)
        
    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        while self.experiencia >= self.experiencia_para_subir():
            self.subir_nivel()
    
    def experiencia_para_subir(self):
        return self.nivel * 50
    
    def subir_nivel(self):
        self.experiencia -= self.experiencia_para_subir()
        self.nivel += 1
        self.fuerza += 5
        self.defensa += 3
        self.salud_max += 15
        self.salud = self.salud_max 
    
class Rescatista(Personaje):
    def __init__(self,nombre = "Rescatista"):
        super().__init__(nombre, salud=110, fuerza=75, defensa=60)
        
    def primeros_auxilios(self,aliado):
        curacion = 30
        aliado.salud = min(aliado.salud + curacion, aliado.salud_max)
        return f"{self.nombre} aplicó primeros auxilios a {aliado.nombre} y recuperó {curacion} de calor corporal "

class Instructor(Personaje):
    def __init__(self, nombre= "Instructor"):
        super().__init__(nombre, salud=90, fuerza=90, defensa=55)
        self.esta_provocando = False

    def provocar(self):
        self.esta_provocando = True
        self.defensa += 15
        return f"{self.nombre} da un grito para atraer la atención y su defensa aumenta temporalmente"

class Rider(Personaje):
    def __init__(self, nombre= "Rider"):
        super().__init__(nombre, salud=95, fuerza=85, defensa=45)