#from curses.ascii import isalnum, isalpha
from PyQt5.QtCore import QObject, pyqtSignal
from parametros import *
class LogicaInicio(QObject):
    senal_enviar_validacion = pyqtSignal(bool,  str)
    senal_abrir_ventana_principal = pyqtSignal()
    senal_abrir_ranking = pyqtSignal()
    mandar_usuario_a_ranking = pyqtSignal(str)
    def __init__(self):
        super().__init__()
    def comprobar_login(self,texto):
        if texto.isalnum():
            if len(texto) <= MAX_CARACTERES:
                if len(texto) >= MIN_CARACTERES:
                    self.senal_enviar_validacion.emit(True, 'sin error')
                    self.mandar_usuario_a_ranking.emit(texto) 
                    self.senal_abrir_ventana_principal.emit()
                    return
                self.senal_enviar_validacion.emit(False, \
                    'El nombre de usuario debe contener al menos 3 caracteres')
                return 
            self.senal_enviar_validacion.emit(False, \
                'El nombre de usuario debe contener menos de 15 caracteres')
            return
        self.senal_enviar_validacion.emit(False, \
            'El nombre de usuario no puede contener caracteres especiales')
        return
    def ver_ranking():
        pass