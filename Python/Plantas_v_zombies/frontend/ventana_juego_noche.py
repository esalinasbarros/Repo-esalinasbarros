from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel
from parametros import (RUTA_FRONTEND, RUTAS_PLANTAS, SOLES_INICIALES, SOLES_EXTRA, N_ZOMBIES,
                        RUTAS_PLANTAS, RUTAS_ELEMENTOS_JUEGO, COSTO_AVANZAR, LIMITE_X,
                        RUTAS_ZOMBIES_CAMINANDO, CHEATCODE_KIL, CHEATCODE_SUN, TECLA_PAUSA)
window_name_noche, base_class_noche = uic.loadUiType(RUTA_FRONTEND['ventana juego noche'])
    
class VentanaJuegoNoche(window_name_noche, base_class_noche):
    senal_activar_backend = pyqtSignal(str)
    senal_verificar_posicion = pyqtSignal(int, int, str) #se manda la posicion, y devuelve un bool para ver si esta ocupada o no
    senal_terminar_ronda = pyqtSignal(bool, str)
    senal_colision_zombie_guisante = pyqtSignal(int)
    senal_pausa = pyqtSignal()
    senal_despausar = pyqtSignal()
    senal_salir = pyqtSignal()
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
        'boton iniciar': self.boton_iniciar  
        }
    def setear_labels(self):
        self.labels = {
        'cantidad soles': self.label_cantidad_soles,
        'nivel': self.label_nivel, 
        'zombies destruidos': self.label_zombies_destruidos,
        'zombies restantes': self.label_zombies_restantes,
        'crazyruz': self.label_dueno_de_casa 
        }
        self.labels['cantidad soles'].setText(f'{SOLES_INICIALES}')
        self.labels['zombies restantes'].setText(f'{N_ZOMBIES}')
    def labels_zombies(self):
        self.lista_labels_zombie = [QLabel('', self) for i in range(N_ZOMBIES)]
        
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
        self.grilla = [[self.grid0_0, self.grid0_1, self.grid0_2, self.grid0_3, self.grid0_4,
                        self.grid0_5, self.grid0_6, self.grid0_7, self.grid0_8, self.grid0_9],
                        [self.grid1_0, self.grid1_1, self.grid1_2, self.grid1_3, self.grid1_4,
                        self.grid1_5, self.grid1_6, self.grid1_7, self.grid1_8, self.grid1_9]] #revisar si da problemas mas adelante
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
    def avanzar_ronda(self):
        if int(self.labels['cantidad soles'].text()) > COSTO_AVANZAR:
            self.labels['cantidad soles'].setText(str(int(self.labels['cantidad soles'].text()) - COSTO_AVANZAR))
            self.reset_labels()
            self.senal_terminar_ronda.emit(True, 'noche')
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
    def mover_label_zombie(self, id, pos):
        self.lista_labels_zombie[id].move(pos[0], pos[1])
        if self.lista_labels_zombies[id].pos().x() <= LIMITE_X:
            self.senal_terminar_ronda.emit(False, 'dia')
    def desaparecer_zombie(self, id):
        self.lista_labels_zombie[id].clear()
        zom_destruidos = int(self.labels['zombies destruidos'].text()) + 1
        self.labels['zombies destruidos'].setText(str(zom_destruidos))
        if int(self.labels['zombies restantes'].text()) > 0:
            self.labels['zombies restantes'].setText(str(int(self.labels['zombies restantes'].text()) - 1))
        else:
            pass #crear señal que te haga ganar la ronda
    def aparecer_label_zombie(self,zombie, id):
        x, y, ancho, alto, tipo = zombie.label
        if tipo == 'clasico':
            self.lista_labels_zombie[id].setPixmap(QPixmap(RUTAS_ZOMBIES_CAMINANDO['zombienicowalker_1']))
        else:
            self.lista_labels_zombie[id].setPixmap(QPixmap(RUTAS_ZOMBIES_CAMINANDO['zombiehernanrunner_1']))
        self.lista_labels_zombie[id].setGeometry(x, y, ancho, alto)
        self.lista_labels_zombie[id].setScaledContents(True)
        self.lista_labels_zombie[id].show
    def keyPressEvent(self, event):
        tecla = event.text()
        self.cheatcode.append(tecla)
        if CHEATCODE_KIL == self.cheatcode:
            for e in self.lista_labels_zombie:
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
    def desaparecer_label_planta(self, i, j):
        self.grilla[i][j].clear()              
    def aparecer_label_guisantes(self, x, y , ancho, alto, pixeles, id):
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap(pixeles))
        self.label.setGeometry(x, y, ancho, alto)
        self.label.setScaledContents(True)
        self.labels_guisantes.append(self.label)
        self.label.show()
    def desaparecer_label_guisantes(self):
        pass
    def mover_label_guisantes(self, tup, id):
        self.labels_guisantes[id].move(tup[0],tup[1])
        for i in range(len(self.lista_labels_zombie)):
            rect_guisante = self.labels_guisantes[id].rect() #manda el id del zombie que choca
            rect_zombie = self.lista_labels_zombie[i].rect()
            if rect_guisante.intersects(rect_zombie):
                self.labels_guisantes[id].clear()
            self.senal_colision_zombie_guisante.emit(id)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.habilitar_mouse:
            x = event.pos().x()
            y = event.pos().y()
            self.enviar_verificacion_posicion(x, y)
        if event.button() == Qt.RightButton:
            x = event.pos().x()
            y = event.pos().y()
            #self.senal_verificar_pos_sol.emit(x, y)
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
        for e in self.lista_labels_zombie:
            e.clear()
        for e in self.labels_guisantes:
            e.clear()
        for e in self.labels_soles:
            e.clear()
    def salir(self):
        self.senal_salir.emit()