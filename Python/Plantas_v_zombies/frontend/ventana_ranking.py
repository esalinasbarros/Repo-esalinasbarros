from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from parametros import RUTA_FRONTEND

window_name, base_class = uic.loadUiType(RUTA_FRONTEND['ventana ranking'])

class VentanaRanking(window_name, base_class):
    senal_volver = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.texto_escrito = ''
        self.setupUi(self)
    def init_gui(self):
        self.show()
        self.boton_volver.clicked.connect(self.volver)
    def escribir_en_archivo(self, texto):
        with open('puntajes.txt', 'a') as f:
            f.write(texto)
    def abrir_archivo(self):
        with open('puntajes.txt', 'r') as f:
            lineas = f.readlines()
            for e in lineas:
                self.texto_escrito += e
        self.label_3.setText(self.texto_escrito)
    def volver(self):
        self.hide()
        self.senal_volver.emit()