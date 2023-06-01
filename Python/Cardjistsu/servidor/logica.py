from utils import data_json
from cartas import get_penguins
from database import DataBase
###################################################################################################
class Logica:


    def __init__(self, servidor):
        self.servidor = servidor
        self.database = DataBase()
        self.clientes = {}
        self.cont = data_json("CUENTA_REGRESIVA_INICIO")


    def procesar_mensaje(self, msg, id_cliente):
        '''
        si self.database.jugador1 y jugador2 se se llaman
        'jugador1' y 'jugador2' significa que hay cupos en
        la sala de espera, solo que no hay una fila
        '''
        respuesta = {}
        respuesta['estado'] = True #por default
        
        if msg['comando'] == 'usuario':
            if not self.database.llena:
                if msg['usuario'] not in self.database.usuarios:
                    if 1 <= len(msg['usuario']) <= 10:
                        if msg['usuario'].isalnum():
                            if self.database.jugador1 == 'jugador1':
                                self.database.ids_jugadores[1] = id_cliente
                                self.database.jugador1 = msg['usuario']
                                self.servidor.log(
                                f'{self.database.jugador1} he entrado a la sala de espera')
                                respuesta['llena'] = False
                                respuesta['comando'] = 'comprobante_usuario'
                                respuesta['estado'] = True
                                respuesta['jugador1'] = self.database.jugador1
                                respuesta['jugador2'] =  self.database.jugador2
                                #if self.database.ids_jugadores[1] == '':
                                #    return
                                self.servidor.enviar_mensaje_personal(respuesta,
                                    self.clientes[self.database.ids_jugadores[1]])

                            elif self.database.jugador1 != 'jugador1' and\
                                self.database.jugador2 == 'jugador2':
                                self.database.ids_jugadores[2] = id_cliente
                                self.database.jugador2 = msg['usuario']
                                respuesta['llena'] = False
                                respuesta['comando'] = 'comprobante_usuario'
                                respuesta['estado'] = True
                                respuesta['jugador1'] = self.database.jugador1
                                respuesta['jugador2'] =  self.database.jugador2
                                self.servidor.log(
                                f'{self.database.jugador2} he entrado a la sala de espera')
                                #if self.database.ids_jugadores[1] == '':
                                #    return
                                #if self.database.ids_jugadores[2] == '':
                                #    return
                                self.servidor.enviar_mensaje_personal(
                                    respuesta,
                                    self.clientes[self.database.ids_jugadores[1]])
                                self.servidor.enviar_mensaje_personal(
                                    respuesta,
                                    self.clientes[self.database.ids_jugadores[2]])
                                self.database.llena = True

                            elif self.database.jugador1 != 'jugador1' and\
                                self.database.jugador2 != 'jugador2':
                                self.database.llena = True

                            elif self.database.jugador1 == 'jugador1' and\
                                self.database.jugador2 != 'jugador2':
                                self.database.ids_jugadores[1] = id_cliente
                                self.database.jugador1 = msg['usuario']
                                self.database.llena = True
                                respuesta['comando'] = 'comprobante_usuario'
                                respuesta['estado'] = True
                                respuesta['jugador1'] = self.database.jugador1
                                respuesta['jugador2'] =  self.database.jugador2
                                #if self.database.ids_jugadores[1] == '':
                                #    return
                                #if self.database.ids_jugadores[2] == '':
                                #    return
                                self.servidor.log(
                                f'{self.database.jugador1} he entrado la sala de espera')
                                self.servidor.enviar_mensaje_personal(
                                    respuesta,
                                    self.clientes[self.database.ids_jugadores[1]])
                                self.servidor.enviar_mensaje_personal(
                                    respuesta,
                                    self.clientes[self.database.ids_jugadores[2]])

                        else:
                            respuesta['comando'] = 'comprobante_usuario'
                            respuesta['estado'] = False
                            respuesta['error'] = 'El nombre de usuario \
                                debe ser alphanumerico'
                            self.servidor.enviar_mensaje_personal(
                                respuesta,
                                self.clientes[id_cliente])

                    else:
                        respuesta['comando'] = 'comprobante_usuario'
                        respuesta['estado'] = False
                        respuesta['error'] = 'El nombre de usuario \
                            debe tener entre 1 y 10 caracter(es)'
                        self.servidor.enviar_mensaje_personal(
                            respuesta,
                            self.clientes[id_cliente])

                else:
                    print('usuario ocupao')
                    respuesta['comando'] = 'comprobante_usuario'
                    respuesta['estado'] = False
                    respuesta['error'] = 'Nombre de usuario ocupado'
                    self.servidor.enviar_mensaje_personal(
                        respuesta,
                        self.clientes[id_cliente])
                self.database.usuarios.add(msg['usuario'])
            else:
                print('llena')
                respuesta['comando'] = 'comprobante_usuario'
                respuesta['estado'] = False
                respuesta['error'] = 'Sala de espera llena'
                self.servidor.enviar_mensaje_personal(
                    respuesta,
                    self.clientes[id_cliente])
        

        if msg['comando'] == 'cambio_a_sala_de_espera':
            self.database.llena = False
            id_a_eliminar = self.get_keys_from_value(
                self.database.ids_jugadores, msg['id'])
            self.database.ids_jugadores[id_a_eliminar[0]] = ''
            #permite actualizar la interfaz y 
            #eliminar al cliente que no se salio

            if id_a_eliminar[0] == 1:
                self.servidor.log(
                f'{self.database.jugador1} se ha salido de la sala de espera')
                self.database.usuarios.remove(self.database.jugador1)
                self.database.reset_jug1()
                

            if id_a_eliminar[0] == 2:
                self.servidor.log(
                f'{self.database.jugador1} se ha salido de la sala de espera')
                self.database.usuarios.remove(self.database.jugador2)
                self.database.reset_jug2()

            mens = { 
                'comando': 'actualizar_interfaz',
                'lugar': 'sala_de_espera',
                'jugador': id_a_eliminar}
            for k, v in self.database.ids_jugadores.items():
                if self.database.ids_jugadores[k] != '':
                    self.servidor.enviar_mensaje_personal(
                        mens, self.clientes[self.database.ids_jugadores[k]])

        if msg['comando'] == 'iniciar_juego':
            id_de_confirmacion = self.get_keys_from_value(
                self.database.ids_jugadores, msg['id'])
            if id_de_confirmacion[0] == 1:
                self.database.confirmacion_jug1 = True
            if id_de_confirmacion[0] == 2:
                self.database.confirmacion_jug2 = True

        if msg['comando'] == 'carta_escogida':
            respuesta = self.procesar_carta_escogida(msg)
            if respuesta is not None and respuesta is not None:
                socket_ganador = self.clientes[respuesta[0]['id']]
                socket_perdedor = self.clientes[respuesta[1]['id']]
                self.servidor.enviar_mensaje_personal(respuesta[0], socket_ganador)
                self.servidor.enviar_mensaje_personal(respuesta[1], socket_perdedor)
        if self.database.confirmacion_jug1 and self.database.confirmacion_jug2:
            self.servidor.log(
                f'{self.database.jugador1} y {self.database.jugador2} han comenzado a jugar')
            self.abrir_sala_juego(cortar=False)
            self.database.confirmacion_jug1 = False
            self.database.confirmacion_jug2 = False
            self.database.llena = False
        else:
            self.abrir_sala_juego(cortar=True)
    def get_keys_from_value(self, d, val):
        return [k for k, v in d.items() if v == val]
    def checkear_sala_espera(self, id):
        respuesta = {}
        respuesta['comando'] = 'abrir_interfaz'
        respuesta['lugar'] = 'ventana_de_juego'
        id_jug = self.get_keys_from_value(
                self.database.ids_jugadores, id)
        if id_jug[0] == 1:
            respuesta['nombre'] = self.database.jugador1
            respuesta['oponente'] = self.database.jugador2
            a = get_penguins()
            self.database.cartas_jug1 = a
            respuesta['cartas'] = self.database.cartas_jug1
        if id_jug[0] == 2:
            respuesta['nombre'] = self.database.jugador2
            respuesta['oponente'] = self.database.jugador1
            b = get_penguins()
            self.database.cartas_jug2 = b
            respuesta['cartas'] = self.database.cartas_jug2
        return respuesta
    def abrir_sala_juego(self, cortar):
        if not cortar:
            for v in self.database.ids_jugadores.values():
                msg = self.checkear_sala_espera(v)
                self.servidor.enviar_mensaje_personal(msg, self.clientes[v])
    def procesar_carta_escogida(self, msg):
        if msg['nombre'] == self.database.jugador1:
            self.database.carta_escogida_jug1 = msg['carta']
            tipo = msg['carta']['elemento']
            nivel = msg['carta']['puntos']
            self.servidor.log(
            f'{self.database.jugador2} escogio una carta tipo {tipo} con {nivel} puntos')
            self.database.jug1_jugar = True
        if msg['nombre'] == self.database.jugador2:
            self.database.carta_escogida_jug2 = msg['carta']
            tipo = msg['carta']['elemento']
            nivel = msg['carta']['puntos']
            self.servidor.log(
            f'{self.database.jugador2} escogio una carta tipo {tipo} con {nivel} puntos')
            self.database.jug2_jugar = True
        if self.database.jug1_jugar and self.database.jug2_jugar:
            ganador = self.ganador(
                self.database.carta_escogida_jug1,
                self.database.carta_escogida_jug2)
            key_ganador = self.get_keys_from_value(
                self.database.ids_jugadores, ganador)
            respuesta_ganador = {'comando': 'resultado_ronda'}
            respuesta_perdedor = {'comando': 'resultado_ronda'}
            if key_ganador[0] == 1:
                self.servidor.log(f'{self.database.jugador1} gano la ronda')
                respuesta_ganador['nombre'] = self.database.jugador1
                respuesta_ganador['carta_oponente'] = self.database.carta_escogida_jug2
                respuesta_ganador['gano'] = True
                respuesta_ganador['id'] = ganador
                respuesta_perdedor['nombre'] = self.database.jugador2
                respuesta_perdedor['carta_oponente'] = self.database.carta_escogida_jug1
                respuesta_perdedor['gano'] = False
                respuesta_perdedor['id'] = self.database.ids_jugadores[2]
                self.database.cartas_trinfo_jug1.append(self.database.carta_escogida_jug1)
                self.checkear_tokens(1)
                color = self.database.carta_escogida_jug1['color']
                elemento = self.database.carta_escogida_jug1['elemento']
                largo = len(self.database.cartas_trinfo_jug1)
                mensaje = {'comando': 'ficha',
                            'color': color,
                            'elemento': elemento,
                            'numero': largo}
                mensaje_perdedor = {'comando': 'ficha_oponente',
                                    'color': color,
                                    'elemento': elemento,
                                    'numero': largo}
                socket_ganador = self.clientes[self.database.ids_jugadores[1]]
                socket_perdedor = self.clientes[self.database.ids_jugadores[2]]
                self.database.carta_escogida_jug1 = None
                self.database.carta_escogida_jug2 = None
                self.database.jug1_jugar = False
                self.database.jug2_jugar = False
            if key_ganador[0] == 2:
                self.servidor.log(f'{self.database.jugador2} gano la ronda')
                respuesta_ganador['nombre'] = self.database.jugador2
                respuesta_ganador['carta_oponente'] = self.database.carta_escogida_jug1
                respuesta_ganador['gano'] = True
                respuesta_ganador['id'] = ganador
                respuesta_perdedor['nombre'] = self.database.jugador1
                respuesta_perdedor['carta_oponente'] = self.database.carta_escogida_jug2
                respuesta_perdedor['gano'] = False
                respuesta_perdedor['id'] = self.database.ids_jugadores[1]
                self.database.cartas_trinfo_jug2.append(self.database.carta_escogida_jug2)
                self.checkear_tokens(2)
                color = self.database.carta_escogida_jug2['color']
                elemento = self.database.carta_escogida_jug2['elemento']
                largo = len(self.database.cartas_trinfo_jug2)
                mensaje = {'comando': 'ficha',
                            'color': color,
                            'elemento': elemento,
                            'numero': largo}
                mensaje_perdedor = {'comando': 'ficha_oponente',
                                    'color': color,
                                    'elemento': elemento,
                                    'numero': largo}
                socket_ganador = self.clientes[self.database.ids_jugadores[2]]
                socket_perdedor = self.clientes[self.database.ids_jugadores[1]]
                self.database.carta_escogida_jug1 = None
                self.database.carta_escogida_jug2 = None
                self.database.jug1_jugar = False
                self.database.jug2_jugar = False
            self.servidor.enviar_mensaje_personal(mensaje, socket_ganador)
            self.servidor.enviar_mensaje_personal(mensaje_perdedor, socket_perdedor)
            return respuesta_ganador, respuesta_perdedor
    def ganador(self, carta1, carta2):
        if carta1['elemento'] == carta2['elemento']:
            if carta1['puntos'] > carta2['puntos']:
                ganador = self.database.ids_jugadores[1]
            elif carta1['puntos'] < carta2['puntos']:
                ganador = self.database.ids_jugadores[2]
            elif carta1['puntos'] == carta2['puntos']:
                ganador = 'empate'
        if carta1['elemento'] == 'fuego' and carta2['elemento'] == 'nieve':
            ganador = self.database.ids_jugadores[1]
        elif carta1['elemento'] == 'fuego' and carta2['elemento'] == 'agua':
            ganador = self.database.ids_jugadores[2]
        elif carta1['elemento'] == 'nieve' and carta2['elemento'] == 'fuego':
            ganador = self.database.ids_jugadores[2]
        elif carta1['elemento'] == 'nieve' and carta2['elemento'] == 'agua':
            ganador = self.database.ids_jugadores[1]
        elif carta1['elemento'] == 'agua' and carta2['elemento'] == 'nieve':
            ganador = self.database.ids_jugadores[2]
        elif carta1['elemento'] == 'agua' and carta2['elemento'] == 'fuego':
            ganador = self.database.ids_jugadores[1]
        return ganador
    def checkear_tokens(self, jug):
        suma_fuego = 0
        suma_nieve = 0
        suma_agua = 0
        mensaje = {'comando': 'ganador', 'ganador': True}
        mensaje_perdedor = {'comando': 'ganador', 'ganador': False}
        ganador = None
        if jug == 1:
            for e in self.database.cartas_trinfo_jug1:
                if e['elemento'] == 'fuego':
                    suma_fuego += 1
                if e['elemento'] == 'nieve':
                    suma_nieve += 1
                if e['elemento'] == 'agua':
                    suma_agua += 1
            if suma_fuego == 3 or suma_agua == 3 or suma_nieve == 3:
                ganador = 1
            if suma_agua != 0 and suma_nieve != 0 and suma_fuego != 0:
                ganador = 1
        if jug == 2:
            for e in self.database.cartas_trinfo_jug2:
                if e['elemento'] == 'fuego':
                    suma_fuego += 1
                if e['elemento'] == 'nieve':
                    suma_nieve += 1
                if e['elemento'] == 'agua':
                    suma_agua += 1
            if suma_fuego == 3 or suma_agua == 3 or suma_nieve == 3:
                ganador = 2
            if suma_agua != 0 and suma_nieve != 0 and suma_fuego != 0:
                ganador = 2
        if ganador == 1:
            socket_ganador = self.clientes[self.database.ids_jugadores[1]]
            socket_perdedor = self.clientes[self.database.ids_jugadores[2]]
            
            self.servidor.enviar_mensaje_personal(mensaje, socket_ganador)
            self.servidor.enviar_mensaje_personal(mensaje_perdedor, socket_perdedor)
            self.database.reset()
        elif ganador == 2:
            socket_ganador = self.clientes[self.database.ids_jugadores[2]]
            socket_perdedor = self.clientes[self.database.ids_jugadores[1]]
            self.servidor.enviar_mensaje_personal(mensaje, socket_ganador)
            self.servidor.enviar_mensaje_personal(mensaje_perdedor, socket_perdedor)
            self.database.reset()    