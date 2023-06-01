from PyQt5 import uic
from utils import data_json
from os.path import join
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QApplication, QMessageBox)
import sys
window_name, base_class = uic.loadUiType(join(*data_json(
            "RUTA VENTANA JUEGO")))
###################################################################################################
class VentanaJuego(window_name, base_class):

    
    senal_elegir_carta = pyqtSignal(str)
    senal_pedir_siguiente_carta = pyqtSignal()


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.carta = None
        self.labels = {
            'jugador': self.label_nombre_jugador,
            'oponente': self.label_nombre_oponente,
            'carta_oponente': self.carta_oponente,
            'carta_jugador': self.carta_jugador}
        self.cartas = {
            1: self.carta_1,
            2: self.carta_2,
            3: self.carta_3,
            4: self.carta_4,
            5: self.carta_5}
        self.fichas = {
            '1': self.token_1,
            '2': self.token_2,
            '3': self.token_3,
            '4': self.token_4,
            '5': self.token_5,
            '6': self.token_6,
            '7': self.token_7,
            '8': self.token_8,
            '9': self.token_9,
            '11': self.token_11,
            '10': self.token_10,
            '12': self.token_12,
            '13': self.token_13,
            '14': self.token_14,
            '15': self.token_15,
            '1_o': self.token_1_o,
            '2_o': self.token_2_o,
            '3_o': self.token_3_o,
            '4_o': self.token_4_o,
            '5_o': self.token_5_o,
            '6_o': self.token_6_o,
            '7_o': self.token_7_o,
            '8_o': self.token_8_o,
            '9_o': self.token_9_o,
            '10_o': self.token_10_o,
            '11_o': self.token_11_o,
            '12_o': self.token_12_o,
            '13_o': self.token_13_o,
            '14_o': self.token_14_o,
            '15_o': self.token_15_o,}
        self.boton_seleccionar_carta.clicked.connect(
            self.enviar_carta_escogida)
        self.rutas_cartas = {}


    def mostrar_baraja(self, num, ruta):
        self.cartas[num].setPixmap(QPixmap(ruta))
        self.cartas[num].setScaledContents(True)
        self.rutas_cartas[num] = ruta
            

    def abrir(self, info):
        self.labels['jugador'].setText(info['nombre'])
        self.labels['oponente'].setText(info['oponente'])
        self.show()


    def cerrar(self):
        self.hide()


    def cambiar_carta_oponente(self, ruta):
        pix = QPixmap(ruta)    
        self.labels['carta_oponente'].setPixmap(pix)
        
    def crear_label_ficha(self, color, elemento, numero, oponente):
        if not oponente:
            pix = QPixmap(join(*data_json(f'{color} {elemento}'), f'{elemento}_{color}.png'))
            self.fichas[str(numero)].setPixmap(pix)
            self.fichas[str(numero)].setScaledContents(True)
        if oponente:
            pix = QPixmap(join(*data_json(f'{color} {elemento}'), f'{elemento}_{color}.png'))
            self.fichas[f'{str(numero)}_o'].setPixmap(pix)
            self.fichas[f'{str(numero)}_o'].setScaledContents(True) 

    def restaurar_carta_oponente(self):
        pix = QPixmap(join(*data_json("BACK"))) 
        self.labels['carta_oponente'].setPixmap(pix)
        self.labels['carta_jugador'].setPixmap(pix)

    def enviar_carta_escogida(self):
        if self.carta is not None:
            self.senal_elegir_carta.emit(str(self.carta))
            pix = QPixmap(self.rutas_cartas[self.carta])
            self.labels['carta_jugador'].setPixmap(pix)
            self.carta = None
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Debes escoger una carta")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()
            #codigo sacado de https://coderslegacy.com/python/pyqt5-qmessagebox/

    def mousePressEvent(self, event):
        if 540 < event.pos().y() < 651:
            if 50 < event.pos().x() < 455:
                carta = ((event.pos().x() - 50) // 81) + 1
                self.carta = carta

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_juego = VentanaJuego()
    sys.exit(app.exec_())