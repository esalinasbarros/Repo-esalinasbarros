
from PyQt5 import uic
from parametros import RUTA_FRONTEND
from PyQt5.QtCore import pyqtSignal

window_name, base_class = uic.loadUiType(RUTA_FRONTEND['ventana postronda'])

class VentanaPostRonda(window_name, base_class):
    senal_pasar_ronda_dia = pyqtSignal()
    senal_pasar_ronda_noche = pyqtSignal()
    senal_actualizar_labels = pyqtSignal()
    senal_volver = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.puntaje_total = 0
        self.avanzar = True
        self.theme = ''
    def init_gui(self, tipo):
        self.theme = tipo
        self.setWindowTitle('Ventana Post Ronda')
        self.conectar_botones()
        self.mostrar_ventana()
    def mostrar_ventana(self):
        self.show()
    def actualizar_labels(self, ronda, soles, zombies, puntaje, bool):
        if bool:
            self.puntaje_total += puntaje
            self.label_ronda_actual.setText(f'{ronda}')
            self.label_soles_restantes.setText(f'{soles}')
            self.label_zombies_destruidos.setText(f'{zombies}')
            self.label_puntaje_ronda.setText(f'{puntaje}')
            self.label_puntaje_total.setText(f'{self.puntaje_total}')
            self.label_status.setText('Has derrotado a los zombies!')
            self.label_status.setStyleSheet('background-color: green;')
            self.avanzar = True
        else:
            self.puntaje_total += puntaje
            self.label_ronda_actual.setText(f'{ronda}')
            self.label_soles_restantes.setText(f'{soles}')
            self.label_zombies_destruidos.setText(f'{zombies}')
            self.label_puntaje_ronda.setText(f'{puntaje}')
            self.label_puntaje_total.setText(f'{self.puntaje_total}')
            self.label_status.setText('Haz perdido, los zombies te comieron los sesos')
            self.label_status.setStyleSheet('background-color: red;')
            self.avanzar = False
    def conectar_botones(self):
        self.boton_siguiente_ronda.clicked.connect(self.pasar_ronda)
        self.boton_salir.clicked.connect(self.salir)
    def pasar_ronda(self):
        if self.avanzar and self.theme == 'dia':
            self.senal_pasar_ronda_dia.emit()
            self.hide()
        if self.avanzar and self.theme == 'noche':
            self.senal_pasar_ronda_noche.emit()
            self.hide()
        else:
            self.label_status.setText('No puedes avanzar, perdiste')
    def salir(self):
        self.senal_volver.emit()
        self.hide()
