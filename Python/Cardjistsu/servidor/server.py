import socket
from threading import (Thread, activeCount)
import json
from logica import Logica
from cripto import (encriptar, desencriptar)
###################################################################################################
class Servidor:
    def __init__(self, host, port): 
        self.host = host
        self.port = port
        self.sockets_clientes = {}
        self.id_cliente = 0
        self.server_sock = None
        self.logica = Logica(self)
        self.nombres_usuarios = []
        self.ids = list()
        self.log('Inicializando servidor...')
        self.abrir_servidor()
    def abrir_servidor(self):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.bind((self.host, self.port))
        self.server_sock.listen()
        self.thread_aceptar()
    def thread_aceptar(self):
        thread = Thread(target=self.aceptar_clientes, daemon=True)
        thread.start()
    def aceptar_clientes(self):
        while True:
            try:
                socket_cliente, addr = self.server_sock.accept()
                thread_cliente = Thread(
                    target=self.escuchar_cliente,
                    args=(socket_cliente, self.id_cliente),
                    daemon=True)
                thread_cliente.start()
                self.sockets_clientes[self.id_cliente] = socket_cliente
                self.logica.clientes[self.id_cliente] = socket_cliente
                self.enviar_mensaje_personal(
                    {'comando': 'id',
                    'id': self.id_cliente},
                    socket_cliente)
                self.ids.append(self.id_cliente)
                self.id_cliente += 1
                self.log('nuevo cliente!')
                self.log(f'{activeCount() - 2} cliente(s) conectado(s)')
            except ConnectionError as e:
                self.log('[ERROR] El cliente no se pudo conectar')
    def escuchar_cliente(self, sock_cliente, id_cliente):
        try:
            while True:
                print()
                self.recibir_mensaje(sock_cliente, id_cliente)
        except ConnectionError as e:
            self.log("ocurrio un problema")
        except json.JSONDecodeError:
            self.log("Se desconecto un cliente")
            usr = self.logica.get_keys_from_value(
                self.logica.database.ids_jugadores, id_cliente)
            if usr[0] == 1:
                self.logica.database.reset_jug1()
                self.logica.database.reset_jug2()
                msg = {'comando': 'desconexion'}
                id = self.logica.database.ids_jugadores[2]
                self.enviar_mensaje_personal(msg, self.logica.clientes[id])
            if usr[0] == 2:
                msg = {'comando': 'desconexion'}
                self.logica.database.reset_jug2()
                self.logica.database.reset_jug1()
                id = self.logica.database.ids_jugadores[1]
                self.enviar_mensaje_personal(msg, self.logica.clientes[id])
            id = self.logica.database.ids_jugadores[2]
            self.log(f"Borrando socket del cliente con id: {id_cliente}.")
            sock_cliente.close()
            self.sockets_clientes.pop(id_cliente, None)
    def recibir_mensaje(self, sock_cliente, id_cliente):
        bytes_mensaje = bytearray()
        mensaje = bytearray()
        bytes_largo_mensaje = sock_cliente.recv(4)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder = 'big')
        while len(bytes_mensaje) < largo_mensaje:
            bytes_n_chunk = sock_cliente.recv(4)
            chunk = sock_cliente.recv(32)
            bytes_mensaje.extend(chunk)
        largo_mensaje = int.from_bytes(bytes_largo_mensaje, byteorder='big')
        for i in range(largo_mensaje):
            mensaje.extend(bytes_mensaje[i].to_bytes(1, byteorder='little'))
        msg_des = desencriptar(mensaje)
        msg_dec = msg_des.decode()
        msg_original = json.loads(msg_dec)
        self.logica.procesar_mensaje(msg_original, id_cliente)
    def enviar_mensaje_personal(self, mensaje, socket_cliente):
        try:
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
            socket_cliente.sendall(mensaje_a_mandar)
        except ConnectionResetError as e:
            print(f'socket de id: {self.sockets_clientes.get(socket_cliente)} esta cerrado')
    def enviar_mensaje_general(self, mensaje):
        for sockets in self.sockets_clientes.values():
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
            try:
                sockets.sendall(mensaje_a_mandar)
            except BrokenPipeError:
                self.sockets_clientes.pop(sockets)
                self.log('Se ha tratado de enviar un mensaje a un socket cerrado')
    def enviar_mensaje_jugadores(self, mensaje, id1, id2):
        '''
        Actualiza solo a los clientes que estan juganddo
        '''
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
        try:    
            self.sockets_clientes[id1].sendall(mensaje_a_mandar)
            self.sockets_clientes[id2].sendall(mensaje_a_mandar)
        except BrokenPipeError:
                self.log('Se ha tratado de enviar un mensaje a un socket cerrado')
    def log(self, str: str):
        print(str)

    
        
