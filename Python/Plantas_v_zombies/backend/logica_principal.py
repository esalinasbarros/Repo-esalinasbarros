from PyQt5.QtCore import pyqtSignal, QObject
class LogicaPrincipal(QObject):
    senal_iniciar_juego_dia = pyqtSignal()
    senal_iniciar_juego_noche = pyqtSignal()
    def __init__(self):
        super().__init__()
    def theme(self, theme):
        if theme == 'jardin de abuela':
            self.senal_iniciar_juego_dia.emit()
        elif theme == 'salida nocturna':
            self.senal_iniciar_juego_noche.emit()
