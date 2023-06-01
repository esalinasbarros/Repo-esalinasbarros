from random import choice, randint
from PyQt5.QtCore import (QObject, QTimer, QRect)
from PyQt5.QtWidgets import QLabel, QWidget
from PyQt5.QtGui import QPixmap
from parametros import (ANCHO, DANO_MORDIDA, POS_INICIAL_ZOMBIE_X, 
                        POS_INICIAL_ZOMBIE_X, RUTAS_ELEMENTOS_JUEGO, RUTAS_FONDOS, RUTAS_PLANTAS, RUTAS_ZOMBIES_CAMINANDO, VELOCIDAD_GUISANTES, VELOCIDAD_ZOMBIE, VELOCIDAD_ZOMBIE_RAPIDO, 
                        VIDA_PLANTA, VIDA_ZOMBIE)

class Soles(QObject):
    def __init__(self):
        super().__init__()
        self.ancho = 50
        self.alto = 50
    def crear_label(self):
        ancho = self.ancho
        alto = self.alto
        return (ancho, alto)
class PlantaClasica(QObject):
    def __init__(self):
        super().__init__()
        self.tipo = 'planta_clasica'
        self._vida = VIDA_PLANTA
        self.posicion_plantada_x = int()
        self.posicion_plantada_y = int()
        self.x_guisante = 0
        self.y_guisante = 0
        self.carril = 0
        self.activo = True
        self.guisante = None
    def disparar(self):
        pass
    @property
    def vida(self):
        return self._vida
    @vida.setter
    def vida(self,x):
        if x > self.vida:
            self._vida = 0
        else:
            self._vida -= x
class PlantaAzul(QObject):
    def __init__(self):
        super().__init__()
        self.tipo = 'planta_hielo'
        self._vida = VIDA_PLANTA
        self.posicion_plantada_x = int()
        self.posicion_plantada_y = int()
        self.x_guisante = 0
        self.y_guisante = 0 
        self.carril = 0
        self.activo = True
        self.guisante = None
    def disparar(self):
        pass
    @property
    def vida(self):
        return self._vida
    @vida.setter
    def vida(self,x):
        if x > self.vida:
            self._vida = 0
        else:
            self._vida -= x
class Girasol(QObject):
    def __init__(self):
        super().__init__()
        self.tipo = 'girasol'
        self._vida = VIDA_PLANTA
        self.pos_x = 0
        self.pos_y = 0
        self.carril = 0
        self.activo = True
    def crear_label_sol(self):
        ancho = 50
        alto = 50
        a = randint(-50,50)
        b = randint(-50,50)
        x = self.pos_x + a
        y = self.pos_y + b
        return x, y, ancho, alto
    @property
    def vida(self):
        return self._vida
    @vida.setter
    def vida(self,x):
        if x > self.vida:
            self._vida = 0
        else:
            self._vida -= x
class PlantaPatata(QObject):
    def __init__(self):
        super().__init__()
        self.tipo = 'papa'
        self._vida = 2*VIDA_PLANTA
        self.posicion_plantada_x = int()
        self.posicion_plantada_y = int()
        self.carril = 0
        self.activo = True
    @property
    def vida(self):
        return self._vida
    @vida.setter
    def vida(self,x):
        if x > self.vida:
            self._vida = 0
        else:
            self._vida -= x
class ZombieClasico(QObject): #La posicion en Y no cambia nunca, solo depende del carril en el que el zombie est
    def __init__(self):
        super().__init__()
        self.tipo = 'clasico'
        self.fase = 1
        self._vida = VIDA_ZOMBIE
        self.ataque = DANO_MORDIDA
        self.velocidad = VELOCIDAD_ZOMBIE
        self.activo = True
        self._pos_x = POS_INICIAL_ZOMBIE_X
        self.rect = QRect()
        self.alto = 70
        self.ancho = 70
        self.carril = choice([1,2])
        if self.carril == 1:
            self.pos_y = 300
        elif self.carril == 2:
            self.pos_y = 200
        self.label = self.crear_label()
    def crear_label(self):
        x = self.pos_x
        y = self.pos_y
        ancho = self.ancho
        alto = self.alto
        tipo = self.tipo
        fase = self.fase
        return [x, y, ancho, alto, tipo]
    @property
    def pos_x(self):
        return self._pos_x
    @pos_x.setter
    def pos_x(self, x):
        if self.pos_x - x <= ANCHO - 1000:
            self.pos_x = POS_INICIAL_ZOMBIE_X
            self.eliminar_label() #falta definir esta funcion
        else:
            self.pos_x = self.pos_x - x
    def comer(self):
        pass
    def mover(self):
        self._pos_x -= self.velocidad
        return [self.pos_x, self.pos_y]
    @property
    def vida(self):
        return self._vida
    @vida.setter
    def vida(self,x):
        if x > self.vida:
            self._vida = 0
        else:
            self._vida -= x
    def eliminar_label(self):
        pass
class ZombieRapido(QObject):
    label = []
    def __init__(self):
        super().__init__()
        self.tipo = 'rapido'
        self.fase = 1
        self._vida = VIDA_ZOMBIE
        self.ataque = DANO_MORDIDA
        self.velocidad = int(VELOCIDAD_ZOMBIE_RAPIDO)
        self.activo = True
        self._pos_x = POS_INICIAL_ZOMBIE_X
        self.rect = QRect()
        self.alto = 70
        self.ancho = 70
        self.carril = choice([1,2])
        if self.carril == 1:
            self.pos_y = 300
        elif self.carril == 2:
            self.pos_y = 200
        self.label = self.crear_label()
    def crear_label(self):
        x = self.pos_x
        y = self.pos_y
        ancho = self.ancho
        alto = self.alto
        tipo = self.tipo
        fase = self.fase
        return [x, y, ancho, alto, tipo]
    @property
    def pos_x(self):
        return self._pos_x
    @pos_x.setter
    def pos_x(self, x):
        if self.pos_x - x <= ANCHO - 1000:
            self.pos_x = POS_INICIAL_ZOMBIE_X
            self.eliminar_label() #falta definir esta funcion
        else:
            self.pos_x = self.pos_x - x
    def comer(self):
        pass
    def mover(self):
        self._pos_x -= self.velocidad
        return [self.pos_x, self.pos_y]
    @property
    def vida(self):
        return self._vida
    @vida.setter
    def vida(self,x):
        if x > self.vida:
            self._vida = 0
        else:
            self._vida -= x
    def eliminar_label(self):
        pass
class Guisantes(QObject):
    def __init__(self):
        super().__init__()
        self.pos_x = 0 #puede no ser property porque no importa si el guisante se pasa de largo
        self.pos_y = 0 #250 o 350 dependiendo del carril
        self.ancho = 50
        self.alto = 50
        self.rect = QRect()
        self.pixeles = RUTAS_ELEMENTOS_JUEGO['guisante_1']
    def crear_label(self):
        return self.pos_x, self.pos_y, self.ancho, self.alto, self.pixeles
    def mover(self):
        self.pos_x += VELOCIDAD_GUISANTES
        return (self.pos_x, self.pos_y)
class GuisantesHielo(QObject):
    def __init__(self):
        super().__init__()
        self.pos_x = 0 #puede no ser property porque no importa si el guisante se pasa de largo
        self.pos_y = 0 #250 o 350 dependiendo del carril
        self.ancho = 50
        self.alto = 50
        self.rect = QRect()
        self.pixeles = RUTAS_ELEMENTOS_JUEGO['guisanteHielo_1']
    def crear_label(self):
        return (self.pos_x, self.pos_y, self.ancho, self.alto, self.pixeles)
    def mover(self):
        self.pos_x += VELOCIDAD_GUISANTES
        return (self.pos_x, self.pos_y)
class Grilla(QObject):
    def __init__(self):
        super().__init__()
        self.ocupado = False
        self.planta = None
        self.pos_x = 390
        self.rect = QRect()
        self.pos_y = int()
        self.tipo = ''
    def vaciar(self):
        self.ocupado = False
        self.planta = None
        self.tipo = ''

