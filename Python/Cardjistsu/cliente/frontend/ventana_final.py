from PyQt5 import uic
from utils import data_json
from os.path import join
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QMessageBox, 
                            QApplication)
import sys
window_name, base_class = uic.loadUiType(join(*data_json(
            "RUTA VENTANA FINAL")))
class VentanaFinal(window_name, base_class):

    senal_volver_inicio = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def init_gui(self, text):
        self.show()
        self.boton_volver.clicked.connect(self.volver)
        self.label_status.setText(text)
    def volver(self):
        self.hide()
        self.senal_volver_inicio.emit()