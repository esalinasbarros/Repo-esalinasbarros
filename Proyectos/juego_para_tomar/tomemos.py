from random import randint
from os.path import join
class Tomemos:
    def __init__(self, jugadores, juegos):
        super.__init__()
        self._ronda = 0
        self.jugadores = jugadores
        self.ponderador_tragos = randint(1, 3)
        self.juegos = juegos
    def elegir_juego(self):
        juego = self.juegos[randint(0, len(self.juegos) - 1)]
        juego.empezar()
        
        

            
        
