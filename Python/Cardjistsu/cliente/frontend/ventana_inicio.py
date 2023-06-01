from PyQt5 import uic
from utils import data_json
from os.path import join
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import (QMessageBox, 
                            QApplication)
import sys
window_name, base_class = uic.loadUiType(join(*data_json(
            "RUTA VENTANA INICIO")))
class VentanaInicio(window_name, base_class):
    senal_comprobar_usuario = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def abrir(self):
        self.show()
    def cerrar(self):
        self.hide()
    def entrada_rechazada(self, texto):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setIcon(QMessageBox.Warning)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setInformativeText(texto) 
        x = msg.exec_()

    def mousePressEvent(self, event):
        if 280 < event.pos().x() < 351:
            if 210 < event.pos().y() < 281:
                if self.nombre_usuario.text() != '':
                    self.senal_comprobar_usuario.emit(self.nombre_usuario.text())
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana_inicio = VentanaInicio()
    sys.exit(app.exec_())