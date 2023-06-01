from PyQt5.QtCore import (QObject, pyqtSignal)
from PyQt5.QtWidgets import QMessageBox
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_espera import SalaEspera
from frontend.ventana_juego import VentanaJuego
from frontend.ventana_final import VentanaFinal
from os.path import join
from utils import data_json
from time import sleep
from random import shuffle
###################################################################################################
# no pasar los caracteres anteriores!!
class Interfaz(QObject):


    senal_mandar_msg_cliente = pyqtSignal(dict)
    senal_cargar_sala_espera = pyqtSignal(str, str)
    senal_sala_de_espera_llena = pyqtSignal()
    senal_eliminar_label_sala_espera = pyqtSignal(int)
    senal_mostrar_error = pyqtSignal(str)
    senal_cargar_ventana_juego = pyqtSignal(dict)
    senal_abrir_ventana_juego = pyqtSignal(dict)
    senal_ruta_foto_carta = pyqtSignal(str)
    senal_abrir_ventana_inicio = pyqtSignal()
    senal_cerrar_ventana_espera = pyqtSignal()
    senal_enviar_ruta_carta = pyqtSignal(int, str)
    senal_cambiar_carta_oponente = pyqtSignal(str)
    senal_abrir_ventana_ganador = pyqtSignal(str)
    senal_restaurar_carta_oponente = pyqtSignal()
    senal_crear_ficha = pyqtSignal(str, str, int, bool)
    senal_oponente_desconectado = pyqtSignal()
    senal_cerrar_ventana_juego = pyqtSignal()


    def __init__(self):


        super().__init__()
        self.ventana_inicio = VentanaInicio()
        self.ventana_de_espera = SalaEspera()
        self.ventana_juego = VentanaJuego()
        self.ventana_final = VentanaFinal()
        self.cartas = {}
        self.orden_cartas = []
        self.revolver_cartas_bool = True
    #    self.conectar_senales_ventanas()
#
#
    #def conectar_senales_ventanas(self):
    #    self.ventana_inicio.senal_comprobar_usuario.connect(
    #    self.comprobar_usuario)


    def abrir_ventana_inicio(self):
        '''
        si la abro con una señal no funciona
        '''
        self.ventana_inicio.abrir()


    def comprobar_usuario(self, usuario: str):
        msg = {'comando': 'usuario', 'usuario': usuario}
        self.enviar_mensaje(msg)


    def procesar_mensaje(self, msg: dict):
        '''
        cada diccionario contiene un comando
        accedible con la keyword 'comando'
        '''
        if msg['comando'] == 'comprobante_usuario':
            if msg['estado']:
                if not msg['llena']:
                    usr1 = msg['jugador1']
                    usr2 = msg['jugador2']
                    self.ventana_inicio.cerrar()
                    self.senal_cargar_sala_espera.emit(usr1, usr2)
                else:
                    self.senal_sala_de_espera_llena.emit()
            else:
                self.senal_mostrar_error.emit(msg['error'])

        elif msg['comando'] == 'timer':
            self.ventana_de_espera.actualizar_timer(
                msg['valor'])

        elif msg['comando'] == 'actualizar_interfaz':
            if msg['lugar'] == 'sala_de_espera':
                self.senal_eliminar_label_sala_espera.emit(msg['jugador'][0])

        elif msg['comando'] == 'abrir_interfaz':
            if msg['lugar'] == 'ventana_de_juego':
                self.cartas = msg['cartas']
                self.nombre = msg['nombre']
                info = {
                    'oponente': msg['oponente'],
                    'cartas': msg['cartas'],
                    'nombre': msg['nombre']}
                self.revolver_cartas()
                self.elegir_sprites_cartas()
                self.senal_cerrar_ventana_espera.emit()
                self.senal_abrir_ventana_juego.emit(info)
        elif msg['comando'] == 'resultado_ronda':
            if msg['gano']:
                ruta_opononente = self.ruta_carta_oponente(msg['carta_oponente'])
                self.senal_cambiar_carta_oponente.emit(ruta_opononente)
                sleep(5)
                self.elegir_sprites_cartas()
                self.eliminar_sprite_oponente()

            if not msg['gano']:
                ruta_opononente = self.ruta_carta_oponente(msg['carta_oponente'])
                self.senal_cambiar_carta_oponente.emit(ruta_opononente)
                sleep(5) #tiempo de "deliberacion"
                self.elegir_sprites_cartas()
                self.eliminar_sprite_oponente()
        elif msg['comando'] == 'ficha':
            color = msg['color']
            elemento = msg['elemento']
            numero = msg['numero']
            self.senal_crear_ficha.emit(
                color, elemento, numero, False
            )
        elif msg['comando'] == 'ficha_oponente':
            color = msg['color']
            elemento = msg['elemento']
            numero = msg['numero']
            self.senal_crear_ficha.emit(
                color, elemento, numero, True)
        
        elif msg['comando'] == 'ganador':
            if msg['ganador']:
                self.senal_abrir_ventana_ganador.emit('!Felicidades, has ganado¡')
            elif not msg['ganador']:
                self.senal_abrir_ventana_ganador.emit('Has perdido :(')
            self.senal_cerrar_ventana_juego.emit()
        elif msg['comando'] == 'desconexion':
            self.senal_oponente_desconectado.emit()
            self.ventana_inicio.abrir() #si la abro con señales se rompe el programa
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Tu oponente se desconecto")
            msgBox.setWindowTitle("Error de conexión")
            msgBox.setStandardButtons(QMessageBox.Ok)
            x = msgBox.exec_()


    def revolver_cartas(self):
        self.orden_cartas = [i for i in range(15)]
        shuffle(self.orden_cartas)


    def elegir_sprites_cartas(self):
        car = self.cartas
        for j in range(1, data_json("BARAJA PANTALLA") + 1):
            i = str(self.orden_cartas[j])
            llave = f"{car[i]['color']} {car[i]['elemento']} {car[i]['puntos']}"
            archivo = f"{car[i]['color']}_{car[i]['elemento']}_{car[i]['puntos']}.png"
            ruta = join(*data_json(llave), archivo)
            self.senal_enviar_ruta_carta.emit(j, ruta)


    def ruta_carta_oponente(self, carta):
        llave = f"{carta['color']} {carta['elemento']} {carta['puntos']}"
        archivo = f"{carta['color']}_{carta['elemento']}_{carta['puntos']}.png"
        ruta = join(*data_json(llave), archivo)
        return ruta


    def eliminar_sprite_oponente(self):
        self.senal_restaurar_carta_oponente.emit()


    def carta_escogida(self, key):
        llave = str(self.orden_cartas[int(key)])
        msg = {'comando': 'carta_escogida',
                'carta': self.cartas[llave],
                'nombre': self.nombre}
        self.orden_cartas.remove(int(llave))
        self.orden_cartas.append(int(llave))
        self.enviar_mensaje_con_id(msg)

    def esconder_ventanas(self):
        self.ventana_inicio.cerrar()
        self.ventana_de_espera.cerrar()
        self.ventana_juego.cerrar()
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText("El servidor se desconecto")
        msgBox.setWindowTitle("Error de conexión")
        msgBox.setStandardButtons(QMessageBox.Ok)
        x = msgBox.exec_()


    def enviar_mensaje_con_id(self, msg):
        msg['id'] = None
        self.senal_mandar_msg_cliente.emit(msg)


    def enviar_mensaje(self, msg: dict):
        '''
        manda el mensaje al modulo del cliente
        para enviarlo al servidor
        '''
        self.senal_mandar_msg_cliente.emit(msg)
