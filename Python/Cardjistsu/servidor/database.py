from collections import deque
class DataBase():
    def __init__(self):
        self.jugador1 = 'jugador1'
        self.jugador2 = 'jugador2'
        self.oponete_jug1 = ''
        self.oponente_jug2 = ''
        self.llena = False
        self.usuarios = set()
        self.fila = deque()
        self.ids_jugadores = {1: '', 2: ''}
        self.cartas_jug1 = {}
        self.cartas_jug2 = {}
        self.confirmacion_jug1 = False
        self.confirmacion_jug2 = False
        self.jug1_jugar = False
        self.jug2_jugar = False
        self.carta_escogida_jug1 = {}
        self.carta_escogida_jug2 = {}
        self.ronda = 1
        self.cartas_trinfo_jug1 = []
        self.cartas_trinfo_jug2 = []
    def reset(self):
        self.jugador1 = 'jugador1'
        self.jugador2 = 'jugador2'
        self.oponete_jug1 = ''
        self.oponente_jug2 = ''
        self.llena = False
        self.usuarios = set()
        self.fila = deque()
        self.ids_jugadores = {1: '', 2: ''}
        self.cartas_jug1 = {}
        self.cartas_jug2 = {}
        self.confirmacion_jug1 = False
        self.confirmacion_jug2 = False
        self.jug1_jugar = False
        self.jug2_jugar = False
        self.carta_escogida_jug1 = {}
        self.carta_escogida_jug2 = {}
        self.ronda = 1
        self.cartas_trinfo_jug1 = []
        self.cartas_trinfo_jug2 = []
    def reset_jug1(self):
        self.jugador1 = 'jugador1'
        self.oponete_jug1 = ''
        self.llena = False
        self.cartas_jug1 = {}
        self.confirmacion_jug1 = False
        self.jug1_jugar = False
        self.carta_escogida_jug1 = {}
        self.cartas_trinfo_jug1 = []
    def reset_jug2(self):
        self.jugador2 = 'jugador2'
        self.oponete_jug2 = ''
        self.llena = False
        self.cartas_jug2 = {}
        self.confirmacion_jug2 = False
        self.jug2_jugar = False
        self.carta_escogida_jug2 = {}
        self.cartas_trinfo_jug2 = []
