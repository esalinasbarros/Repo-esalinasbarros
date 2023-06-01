import socket
from threading import Thread
from PyQt5.QtCore import (pyqtSignal, QObject)
from cripto import (encriptar, desencriptar)
import json
from backend.interfaz import Interfaz
import sys
###################################################################################################
class Client(QObject):
    senal_abrir_ventana_inicio = pyqtSignal()
    senal_procesar_mensaje = pyqtSignal(dict)
    senal_esconder_ventanas = pyqtSignal()
    
    def __init__(self, host, port):
        super().__init__()
        self.interfaz = Interfaz()
        self.host = host
        self.port = port
        self.socket_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conectado = False
        self.id = int()
        self.cont = 10
        self.iniciar_cliente()
    def iniciar_cliente(self):
        try:
            self.socket_cliente.connect((self.host, self.port))
            self.conectado = True
            self.comenzar_a_escuchar() 
            self.conectar_senales()
        except ConnectionError as e:
            print(f"\n-ERROR: El servidor no está inicializado. {e}-")
            self.socket_cliente.close()
        except ConnectionRefusedError as e:
            print(f"\n-ERROR: No se pudo conectar al servidor.{e}-")
            self.socket_cliente.close()
    def conectar_senales(self):
        self.interfaz.abrir_ventana_inicio()
    def comenzar_a_escuchar(self):
        try:
            self.senal_abrir_ventana_inicio.emit()
            thread = Thread(target=self.recivir_mensaje, 
                                    daemon=True)
            thread.start()
        except ConnectionError as e:
            self.socket_cliente.close()
    def recivir_mensaje(self):
        while self.conectado:
            bytes_mensaje = bytearray()
            mensaje = bytearray()
            try:
                bytes_largo_mensaje = self.socket_cliente.recv(4)
                largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder = 'big')
                while len(bytes_mensaje) < largo_mensaje:
                    bytes_n_chunk = self.socket_cliente.recv(4)
                    chunk = self.socket_cliente.recv(32)
                    bytes_mensaje.extend(chunk)
                largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder='big')
                for i in range(largo_mensaje):
                    mensaje.extend(bytes_mensaje[i].to_bytes(1, byteorder='little'))
                msg_des = desencriptar(mensaje)
                msg_dec = msg_des.decode()
                msg_original = json.loads(msg_dec)
                if msg_original['comando'] == 'id':
                    self.id = msg_original['id']
                self.interfaz.procesar_mensaje(msg_original)
            except json.decoder.JSONDecodeError:
                print('el servidor se desconecto')
                self.conectado = False
                self.socket_cliente.close()
                self.senal_esconder_ventanas.emit()
                sys.exit()
            except ConnectionResetError:
                self.senal_esconder_ventanas.emit()
    def notificar_cambio_ventana(self, msg: dict):
        msg['id'] = self.id
        self.enviar_mensaje(msg)
    def enviar_mensaje(self, mensaje):
        try:
            if mensaje['id'] is None:
                mensaje['id'] = self.id
        except KeyError:
            pass
        try:
            print('se mando desde cliente')
            mensaje_a_mandar = bytearray()
            msg_json = json.dumps(mensaje)
            msg_codificado = msg_json.encode()
            msg_encriptado = encriptar(msg_codificado)
            largo = len(msg_encriptado)
            largo_bytes = largo.to_bytes(4, byteorder='big')
            mensaje_a_mandar.extend(largo_bytes)
            n_chunks = largo // 32
            n = 1
            for i in range(0, len(msg_encriptado)):
                if i % 32 == 0 and i > 0:
                    mensaje_a_mandar.extend(n.to_bytes(4, byteorder = 'little'))
                    mensaje_a_mandar.extend(msg_encriptado[i - 32: i])
                    n += 1
            index_chunk_incompleto = n_chunks * 32
            mensaje_a_mandar.extend(n.to_bytes(4, byteorder = 'little'))
            bytes_a_rellenar = 32 - \
                (len(msg_encriptado[index_chunk_incompleto: len(msg_encriptado)]))
            mensaje_a_mandar.\
                extend(msg_encriptado[index_chunk_incompleto: len(msg_encriptado)])
            for i in range(bytes_a_rellenar):
                mensaje_a_mandar.extend(b'\x00')
            self.socket_cliente.sendall(mensaje_a_mandar)
        except json.decoder.JSONDecodeError:
            print('el servidor esta desconectado')
            self.senal_esconder_ventanas.emit()
        except BrokenPipeError as e:
            print('el servidor esta desconectado')
            self.socket_cliente.close()
            

                
        
        
    