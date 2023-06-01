from time import sleep
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt, QRect
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
from parametros import (RUTA_FRONTEND, RUTAS_PLANTAS, SOLES_INICIALES, SOLES_EXTRA, N_ZOMBIES,
                        RUTAS_PLANTAS, RUTAS_ELEMENTOS_JUEGO, COSTO_AVANZAR, LIMITE_X,
                        RUTAS_ZOMBIES_CAMINANDO, CHEATCODE_KIL, CHEATCODE_SUN, TECLA_PAUSA)

window_name_dia, base_class_dia = uic.loadUiType(RUTA_FRONTEND['ventana juego dia'])
    
class VentanaJuegoDia(window_name_dia, base_class_dia):
    senal_activar_backend = pyqtSignal(str)
    senal_verificar_posicion = pyqtSignal(int, int, str) #se manda la posicion, y devuelve un bool para ver si esta ocupada o no
    senal_verificar_pos_sol = pyqtSignal(int, int)
    senal_terminar_ronda = pyqtSignal(bool, str)
    senal_colision_zombie_guisante = pyqtSignal(int)
    senal_pausa = pyqtSignal()
    senal_chequear_colision_planta = pyqtSignal(int, int, int)
    senal_despausar = pyqtSignal()
    senal_salir = pyqtSignal()
    senal_verificar_colision_ZP = pyqtSignal(tuple, tuple)
    def __init__(self):
        super().__init__()
        self.theme = ''
        self.labels = {} #puntaje, nivel, soles
        self.botones = {} #Todos los botones en la ventana del juego
        self.grilla = []
        self.zombies_labels = {}
        self.habilitar_mouse = False #se activa cuando se tiene una planta seleccionada
        self.planta_a_comprar = None
        self.labels_soles = []
        self.labels_guisantes = []
        self.cheatcode = []
        self.labels_soles_girasoles = []
        self.id_guisantes = 1
        self.pausado = False
        self.setupUi(self)
        self.setMouseTracking(True)
    def init_gui(self):
        self.setWindowTitle('Jardin de la abuela')
        self.setear_botones()
        self.setear_labels()
        self.conectar_botones()
        self.empezar_ronda()
    def empezar_ronda(self):
        self.labels_zombies()
        self.setear_grilla()
        self.reset_labels()
        self.activar_backend()
        self.mostrar_ventana()
    def setear_botones(self):
        self.botones = {
        'comprar girasol': self.comprar_girasol,
        'comprar lanzaguisantes': self.comprar_lanzaguisantes,
        'comprar lanzaguisantes hielo': self.comprar_lanzaguisantes_hielo,
        'comprar papa': self.compra_papa,
        'boton pausar': self.boton_pausar,
        'boton salir': self.boton_salir,
        'boton avanzar': self.boton_avanzar,
        'boton iniciar': self.boton_iniciar}
    def setear_labels(self):
        self.labels = {
        'cantidad soles': self.label_cantidad_soles,
        'nivel': self.label_nivel, 
        'zombies destruidos': self.label_zombies_destruidos,
        'zombies restantes': self.label_zombies_restantes,
        'crazyruz': self.label_dueno_de_casa}
        self.labels['cantidad soles'].setText(f'{SOLES_INICIALES}')
        self.labels['zombies restantes'].setText(f'{N_ZOMBIES}')
    def labels_zombies(self):
        self.lista_labels_zombies = [QLabel('', self) for i in range(N_ZOMBIES)]
    def conectar_botones(self):
        self.botones['boton iniciar'].clicked.connect(self.activar_backend)
        self.botones['comprar girasol'].clicked.connect(self.aparecer_label_girasol)
        self.botones['comprar lanzaguisantes'].clicked.connect(self.aparecer_guisante)
        self.botones['comprar lanzaguisantes hielo'].clicked.connect(self.aparecer_guisante_hielo)
        self.botones['comprar papa'].clicked.connect(self.aparecer_label_papa)
        self.botones['boton avanzar'].clicked.connect(self.avanzar_ronda)
        self.botones['boton pausar'].clicked.connect(self.pausar)
        self.botones['boton salir'].clicked.connect(self.salir)
    def setear_grilla(self): 
        self.grilla = [[self.grid0_0, self.grid1_0, self.grid2_0, self.grid3_0, self.grid4_0,
                        self.grid5_0, self.grid6_0, self.grid7_0, self.grid8_0, self.grid9_0],
                        [self.grid0_1, self.grid1_1, self.grid2_1, self.grid3_1, self.grid4_1,
                        self.grid5_1, self.grid6_1, self.grid7_1, self.grid8_1, self.grid9_1]] #revisar si da problemas mas adelante
    def mostrar_ventana(self):
        self.show()
    def activar_backend(self):
        self.senal_activar_backend.emit('dia')
    def pausar(self):
        if not self.pausado:
            self.senal_pausa.emit()
        else:
            self.senal_despausar.emit()
    def recivir_lista_zombies(self, zombies):
        self.lista_zombies = zombies
    def enviar_verificacion_posicion(self, x, y):
        planta = self.planta_a_comprar[1]
        self.senal_verificar_posicion.emit(x, y, planta)
        self.habilitar_mouse = False
    def recivir_verificacion_posicion(self, bool, x, y, descuento):
        if not bool:
            self.plantar(x, y)
            self.labels['cantidad soles'].setText(str(int(self.labels['cantidad soles'].text()) - descuento))
        else:
            self.label = QLabel("posicion ocupada", self)
            self.label.setGeometry(150, 50, 500, 500)
            self.label.show()
            sleep(1.5)
            self.label.hide()
    def plantar(self, x, y):
        self.grilla[x][y].setPixmap(self.planta_a_comprar[0])
        self.grilla[x][y].setScaledContents(True)
        self.planta_a_comprar = None
    def aparecer_guisante(self): #mueve los guisantes
        if int(self.labels['cantidad soles'].text()) >= 100:
            self.planta_a_comprar = (QPixmap(RUTAS_PLANTAS['lanzaguisantes_1']), 'plantaclasica')
            self.habilitar_mouse = True
        else:
            self.label = QLabel('No te alcanzan los soles')
    def aparecer_guisante_hielo(self):
        if int(self.labels['cantidad soles'].text()) >= 150:
            self.planta_a_comprar = (QPixmap(RUTAS_PLANTAS['lanzaguisantesHielo_1']), 'plantahielo')
            self.habilitar_mouse = True
        else:
            self.label = QLabel('No te alcanzan los soles')
    def aparecer_label_girasol(self):
        if int(self.labels['cantidad soles'].text()) >= 50:
            self.planta_a_comprar = (QPixmap(RUTAS_PLANTAS['girasol_1']), 'girasol')
            self.habilitar_mouse = True
        else:
            self.label = QLabel('No te alcanzan los soles')
    def aparecer_label_papa(self):
        if int(self.labels['cantidad soles'].text()) >= 75:
            self.planta_a_comprar = (QPixmap(RUTAS_PLANTAS['papa_1']), 'papa')
            self.habilitar_mouse = True
        else:
            self.label = QLabel('No te alcanzan los soles')
    def aparacer_label_sol(self, x, y, ancho, alto): #solo se activara si es de dia
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap(RUTAS_ELEMENTOS_JUEGO['sol']))
        self.label.setGeometry(x, y, ancho, alto)
        self.label.setScaledContents(True)
        self.label.show()
        self.labels_soles.append(self.label)
    def avanzar_ronda(self):
        if int(self.labels['cantidad soles'].text()) >= COSTO_AVANZAR:
            self.labels['cantidad soles'].setText(str(int(self.labels['cantidad soles'].text()) - COSTO_AVANZAR))
            self.reset_labels()
            self.senal_terminar_ronda.emit(True, 'dia')
            self.hide()
    def aparecer_label_sol_girasol(self, sol):
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap(RUTAS_ELEMENTOS_JUEGO['sol']))
        self.label.setGeometry(sol[0], sol[1], sol[2], sol[3])
        self.label.setScaledContents(True)
        self.label.show()
        self.labels_soles_girasoles.append(self.label)
    def mover_labels_soles(self):
        for e in self.labels_soles:
            e.move(e.pos().x(), e.pos().y() + 1)
    def desaparacer_label_sol(self, cant_soles, x, y): #solo se activara si es de dia
        for e in self.labels_soles:
            if e.pos().x() <= x <= e.pos().x() + 50:
                if e.pos().y() <= y <= e.pos().y() + 50:
                    e.clear()
        num_soles = int(self.labels['cantidad soles'].text()) + cant_soles
        self.labels['cantidad soles'].setText(str(num_soles))
    def mover_label_zombie(self, id, pos):
        self.lista_labels_zombies[id].move(pos[0], pos[1])
        #self.senal_chequear_colision_planta.emit()
        if self.lista_labels_zombies[id].pos().x() <= LIMITE_X:
            self.senal_terminar_ronda.emit(False, 'dia')
        #for i in range(len(self.grilla)):
        #    for j in range(len(self.grilla[i])):
        #        rect_grilla = self.grilla[i][j].rect()
        #        rect_zombie = self.lista_labels_zombies[id].rect()
        #        if rect_grilla.intersects(rect_zombie):
        #            self.senal_chequear_colision_planta.emit(i, j, id)
    def desaparecer_zombie(self, id):
        self.lista_labels_zombies[id].clear()
        zom_destruidos = int(self.labels['zombies destruidos'].text()) + 1
        self.labels['zombies destruidos'].setText(str(zom_destruidos))
        if int(self.labels['zombies restantes'].text()) > 0:
            self.labels['zombies restantes'].setText(str(int(self.labels['zombies restantes'].text()) - 1))
        else:
            self.senal_terminar_ronda.emit(True, 'dia')
    def desaparecer_label_planta(self, i, j):
        self.grilla[i][j].clear()
    def aparecer_label_zombie(self, zombie, id):
        x, y, ancho, alto, tipo = zombie.label
        if tipo == 'clasico':
            self.lista_labels_zombies[id].setPixmap(QPixmap(RUTAS_ZOMBIES_CAMINANDO['zombienicowalker_1']))
        else:
            self.lista_labels_zombies[id].setPixmap(QPixmap(RUTAS_ZOMBIES_CAMINANDO['zombiehernanrunner_1']))
        self.lista_labels_zombies[id].setGeometry(x, y, ancho, alto)
        self.lista_labels_zombies[id].setScaledContents(True)
        self.lista_labels_zombies[id].show
    def keyPressEvent(self, event):
        tecla = event.text()
        self.cheatcode.append(tecla)
        if CHEATCODE_KIL == self.cheatcode:
            for e in self.lista_labels_zombies:
                e.clear()
                self.senal_terminar_ronda.emit(True, 'dia')
                self.cheatcode = []
            self.hide()
        if CHEATCODE_SUN == self.cheatcode:
            self.labels['cantidad soles'].setText(str(int(self.labels['cantidad soles'].text()) + SOLES_EXTRA))
            self.cheatcode = []
        if len(self.cheatcode) > 3:
            self.cheatcode = []
        if event.text() == TECLA_PAUSA and not self.pausado:
            self.senal_pausa.emit()
            self.pausado = True
        elif event.text() == TECLA_PAUSA and self.pausado:
            self.senal_despausar.emit()
            self.pausado = False  
    def aparecer_label_guisantes(self, x, y , ancho, alto, pixeles, id):
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap(pixeles))
        self.label.setGeometry(x, y, ancho, alto)
        print(self.label.rect())
        self.label.setScaledContents(True)
        self.labels_guisantes.append(self.label)
        self.label.show()
    def mover_label_guisantes(self, tup, id):
        self.labels_guisantes[id].move(tup[0],tup[1])
        self.chequear_colision_ZG(id)
    def chequear_colision_ZG(self, id):
        for i in range(len(self.lista_labels_zombies)):
            if self.labels_guisantes[id].pos().x() >= self.lista_labels_zombies[i].pos().x()\
                and self.labels_guisantes[id].pos().y() == self.lista_labels_zombies[i].pos().y() - 20:
                self.labels_guisantes[id].clear()
                self.senal_colision_zombie_guisante.emit(i)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.habilitar_mouse:
            x = event.pos().x()
            y = event.pos().y()
            self.enviar_verificacion_posicion(x, y)
        if event.button() == Qt.RightButton:
            x = event.pos().x()
            y = event.pos().y()
            self.senal_verificar_pos_sol.emit(x, y)
            for e in self.labels_soles_girasoles:
                if e.pos().x() <= x <= e.pos().x() + 50:
                    if e.pos().y() <= y <= e.pos().y() + 50:
                        e.clear()
                        num_soles = int(self.labels['cantidad soles'].text()) + 25
                        self.labels['cantidad soles'].setText(str(num_soles))
    def reset_labels(self):
        for e in self.grilla:
                for h in e:
                    h.clear()
        for e in self.lista_labels_zombies:
            e.clear()
        for e in self.labels_guisantes:
            e.clear()
        for e in self.labels_soles:
            e.clear()
    def salir(self):
        self.senal_salir.emit()
