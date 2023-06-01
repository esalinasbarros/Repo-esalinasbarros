import sys
from backend.cliente import Client
from PyQt5.QtWidgets import QApplication
from utils import data_json
###################################################################################################
if __name__ == '__main__':
    HOST = data_json("HOST")
    PORT = data_json("PORT")

    try:

        app = QApplication(sys.argv)
        cliente = Client(HOST, PORT)

        #########################
        ######## Señales ########

        cliente.interfaz.ventana_inicio.senal_comprobar_usuario.connect(
            cliente.interfaz.comprobar_usuario) #envia msg al cliente

        cliente.interfaz.senal_mandar_msg_cliente.connect(
            cliente.enviar_mensaje) #envia msg al servidor

        cliente.interfaz.senal_cargar_sala_espera.connect(
            cliente.interfaz.ventana_de_espera.abrir)

        cliente.interfaz.ventana_de_espera.senal_volver_ventana_inicio.connect(
            cliente.interfaz.ventana_inicio.abrir)

        cliente.interfaz.ventana_de_espera.senal_notificar_servidor.connect(
            cliente.notificar_cambio_ventana)

        cliente.interfaz.senal_eliminar_label_sala_espera.connect(
            cliente.interfaz.ventana_de_espera.borrar_label)

        cliente.senal_esconder_ventanas.connect(
            cliente.interfaz.esconder_ventanas)

        cliente.interfaz.ventana_de_espera.senal_enviar_usuarios.connect(
            cliente.interfaz.enviar_mensaje_con_id)

        cliente.interfaz.senal_mostrar_error.connect(
            cliente.interfaz.ventana_inicio.entrada_rechazada)

        cliente.interfaz.senal_cargar_ventana_juego.connect(
            cliente.interfaz.ventana_juego.abrir)

        cliente.interfaz.ventana_de_espera.senal_enviar_msg.connect(
            cliente.interfaz.enviar_mensaje_con_id)

        cliente.interfaz.senal_abrir_ventana_juego.connect(
            cliente.interfaz.ventana_juego.abrir)

        cliente.interfaz.ventana_juego.senal_elegir_carta.connect(
            cliente.interfaz.carta_escogida)

        cliente.interfaz.senal_ruta_foto_carta.connect(
            cliente.interfaz.ventana_juego.mostrar_baraja)

        cliente.interfaz.senal_abrir_ventana_inicio.connect(
            cliente.interfaz.ventana_inicio.abrir)

        cliente.interfaz.senal_cerrar_ventana_espera.connect(
            cliente.interfaz.ventana_de_espera.cerrar)
            
        cliente.interfaz.senal_enviar_ruta_carta.connect(
            cliente.interfaz.ventana_juego.mostrar_baraja)

        cliente.interfaz.senal_cambiar_carta_oponente.connect(
            cliente.interfaz.ventana_juego.cambiar_carta_oponente)

        cliente.interfaz.senal_restaurar_carta_oponente.connect(
            cliente.interfaz.ventana_juego.restaurar_carta_oponente)

        cliente.interfaz.senal_crear_ficha.connect(
            cliente.interfaz.ventana_juego.crear_label_ficha)

        cliente.interfaz.senal_abrir_ventana_ganador.connect(
            cliente.interfaz.ventana_final.init_gui)

        cliente.interfaz.ventana_final.senal_volver_inicio.connect(
            cliente.interfaz.ventana_inicio.abrir)

        cliente.interfaz.senal_oponente_desconectado.connect(
            cliente.interfaz.ventana_juego.cerrar)
        
        cliente.interfaz.senal_cerrar_ventana_juego.connect(
            cliente.interfaz.ventana_juego.cerrar)

        sys.exit(app.exec_()) 
        
    except ConnectionError as e:
        print("Ocurrió un error.", e)
        cliente.socket_cliente.close()

    except KeyboardInterrupt:
        print("\nCerrando cliente...")
        sys.exit()   

    