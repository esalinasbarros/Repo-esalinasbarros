from PyQt5.QtWidgets import (QMessageBox)
from PyQt5.QtCore import (pyqtSignal)
from parametros import RUTA_FRONTEND
from PyQt5 import uic
window_name, base_class = uic.loadUiType(RUTA_FRONTEND['ventana inicio'])

class VentanaInicio(window_name, base_class):
    senal_enviar_login = pyqtSignal(str)
    senal_ver_ranking = pyqtSignal()
    senal_salir = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
    def init_gui(self):
        self.setWindowTitle('DCCruz vs. Zombies')
        self.show()
        self.boton_iniciar.clicked.connect(self.enviar_login)
        self.boton_ranking.clicked.connect(self.ranking)
        self.boton_salir.clicked.connect(self.salir)
    def enviar_login(self):
        self.senal_enviar_login.emit(self.label_usuario_edit.text())
        pass
    def validacion_login(self, bool, texto):
        if not bool:
            msg = QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Usuario no valido")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Cancel|QMessageBox.Ok)
            msg.setInformativeText(texto) # codigo sacado de https://coderslegacy.com/python/pyqt5-qmessagebox/
            x = msg.exec_()
        else:
            self.hide()
    def ranking(self):
        self.senal_ver_ranking.emit()
        self.hide()
    def salir(self):
        self.hide()

