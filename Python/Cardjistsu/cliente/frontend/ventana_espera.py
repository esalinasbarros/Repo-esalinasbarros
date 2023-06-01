from PyQt5 import uic
from utils import data_json
from os.path import join
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
import sys
window_name, base_class = uic.loadUiType(join(*data_json(
            "RUTA VENTANA ESPERA")))
###################################################################################################
class SalaEspera(window_name, base_class):
    senal_volver_ventana_inicio = pyqtSignal()
    senal_notificar_servidor = pyqtSignal(dict)
    senal_pasar_a_ventana_juego = pyqtSignal(str, str)
    senal_enviar_usuarios = pyqtSignal(dict)
    senal_enviar_msg = pyqtSignal(dict)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
    def init_gui(self):
        self.labels = {
            'jugador_1': self.label_jugador_1,
            'jugador_2': self.label_jugador_2,
            'boton_volver': self.label_boton_volver,
            'timer': self.label_timer}
        self.boton_iniciar.clicked.connect(
            self.mandar_solicitud_iniciar_juego)
    def abrir(self, jug1, jug2):
        self.show()
        self.labels['jugador_1'].setText(jug1)
        self.labels['jugador_2'].setText(jug2)
    def cerrar(self):
        self.hide()
    def actualizar_timer(self, num):
        self.labels['timer'].setText(num)
    def actualizar_labels(self):
        pass
    def borrar_label(self, num):
        self.labels[f'jugador_{num}'].setText(f'Jugador {num}')
    def mousePressEvent(self, event):
        if 160 < event.pos().x() <  341:
            if 440 < event.pos().y() < 511:
                self.cerrar()
                msg = {
                    'comando': 'cambio_a_sala_de_espera'
                    }
                self.senal_notificar_servidor.emit(msg)
                self.senal_volver_ventana_inicio.emit()
    def mandar_solicitud_iniciar_juego(self):
        msg = {}
        msg['comando'] = 'iniciar_juego'
        self.senal_enviar_msg.emit(msg)
    def entrar_juego(self):
        print('entrarjuego')
        self.cerrar()
        msg = {'comando': 'entrar_ventana_juego'}
        self.senal_enviar_usuarios.emit(msg)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    sala_espera = SalaEspera()
    sys.exit(app.exec_())