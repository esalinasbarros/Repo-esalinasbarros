from piramide.crear_piramide import generador_cartas
from random import shuffle
class Piramide():
    def __init__(self, jugadores):
        super.__init__()
        self.jugadores = jugadores
    def empezar(self):
        shuffle(self.jugadores)
        for jugador in self.jugadores:
            pass
    def mostrar_carta(self):
        pass
    