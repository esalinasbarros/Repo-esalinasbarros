from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from parametros import *
window_name, base_class = uic.loadUiType(RUTA_FRONTEND['ventana_principal'])
class VentanaPrincipal(window_name, base_class):
    senal_enviar_theme = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.theme = ''
        self.boton_jardin_de_abuela.clicked.connect(lambda: self.apretar_boton_inicio(theme = 'jardin de abuela'))
        self.boton_salida_ncturna.clicked.connect(lambda: self.apretar_boton_inicio(theme = 'salida nocturna'))
    def init_gui(self):
        self.setWindowTitle('Ventana Principal')
    def abrir_ventana(self):
        self.show()
    def apretar_boton_inicio(self,theme):
        if theme != '':
            self.senal_enviar_theme.emit(theme)
            self.hide()
        else:
            self.abrir_ventana