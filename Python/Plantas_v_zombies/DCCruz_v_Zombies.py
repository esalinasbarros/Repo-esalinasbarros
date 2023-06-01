from PyQt5.QtWidgets import QApplication
from frontend.ventana_inicio import VentanaInicio
from frontend.ventana_postronda import VentanaPostRonda
from frontend.ventana_principal import VentanaPrincipal
from frontend.ventana_juego_dia import VentanaJuegoDia
from frontend.ventana_juego_noche import VentanaJuegoNoche
from backend.elementos import (Soles,PlantaClasica,PlantaAzul,ZombieClasico,
                                ZombieRapido,Girasol,PlantaPatata, 
                                Guisantes, GuisantesHielo, Grilla)
from backend.logica_inicio import LogicaInicio
from backend.logica_juego import LogicaJuego
from backend.logica_principal import LogicaPrincipal
from frontend.ventana_ranking import VentanaRanking

class DCCruz(QApplication):

    '''
    Codigo sacado del modulo DCCubitos de la AS3, pero con modificaciones
    '''
    def __init__(self, argv):
        super().__init__(argv)
        self.ventana_inicio = VentanaInicio()
        self.ventana_principal = VentanaPrincipal()
        self.ventana_post_juego = VentanaPostRonda()
        self.zombie_rapido = ZombieRapido()
        self.zombie_clasico = ZombieClasico()
        self.planta_clasica = PlantaClasica()
        self.girasol = Girasol()
        self.planta_papa = PlantaPatata()
        self.planta_azul = PlantaAzul()
        self.guisante = Guisantes()
        self.soles = Soles()
        self.grilla = Grilla()
        self.guisante_hielo = GuisantesHielo()
        self.ventana_juego_dia = VentanaJuegoDia()
        self.ventana_juego_noche = VentanaJuegoNoche()
        self.logica_inicio = LogicaInicio()
        self.logica_principal = LogicaPrincipal()
        self.logica_juego = LogicaJuego(self.soles,self.planta_clasica,self.planta_azul,self.zombie_clasico,
                                        self.zombie_rapido,self.girasol,self.planta_papa, 
                                        self.guisante, self.guisante_hielo)
        self.ventana_ranking = VentanaRanking()
        self.conectar_juego()
    def conectar_juego(self):
        self.logica_inicio.senal_abrir_ventana_principal.connect(self.ventana_principal.abrir_ventana)
        self.ventana_inicio.senal_enviar_login.connect(self.logica_inicio.comprobar_login)
        self.ventana_inicio.senal_ver_ranking.connect(self.ventana_ranking.init_gui)
        self.logica_inicio.senal_enviar_validacion.connect(self.ventana_inicio.validacion_login)
        self.ventana_principal.senal_enviar_theme.connect(self.logica_principal.theme)
        self.logica_principal.senal_iniciar_juego_dia.connect(self.ventana_juego_dia.init_gui)
        self.logica_principal.senal_iniciar_juego_noche.connect(self.ventana_juego_noche.init_gui)
        self.ventana_juego_dia.senal_activar_backend.connect(self.logica_juego.setear_zombies)
        self.ventana_juego_noche.senal_activar_backend.connect(self.logica_juego.setear_zombies)
        self.logica_juego.senal_aparecer_zombie.connect(self.ventana_juego_dia.aparecer_label_zombie)
        self.logica_juego.senal_aparecer_zombie.connect(self.ventana_juego_noche.aparecer_label_zombie)
        self.logica_juego.senal_mover_zombie.connect(self.ventana_juego_dia.mover_label_zombie)
        self.logica_juego.senal_mover_zombie.connect(self.ventana_juego_noche.mover_label_zombie)
        self.logica_juego.senal_mandar_lista_zombies.connect(self.ventana_juego_dia.recivir_lista_zombies)
        self.logica_juego.senal_mandar_lista_zombies.connect(self.ventana_juego_noche.recivir_lista_zombies)
        self.ventana_juego_dia.senal_verificar_posicion.connect(self.logica_juego.verificar_posicion)
        self.ventana_juego_noche.senal_verificar_posicion.connect(self.logica_juego.verificar_posicion)
        self.logica_juego.senal_enviar_verificacion_posicion.connect(self.ventana_juego_dia.recivir_verificacion_posicion)
        self.logica_juego.senal_enviar_verificacion_posicion.connect(self.ventana_juego_noche.recivir_verificacion_posicion)
        self.logica_juego.senal_aparecer_sol.connect(self.ventana_juego_dia.aparacer_label_sol)
        self.ventana_juego_dia.senal_verificar_pos_sol.connect(self.logica_juego.verificar_pos_sol)
        self.logica_juego.senal_verificar_sol.connect(self.ventana_juego_dia.desaparacer_label_sol)
        self.logica_juego.senal_mover_soles.connect(self.ventana_juego_dia.mover_labels_soles)
        self.logica_juego.senal_aparecer_guisante.connect(self.ventana_juego_dia.aparecer_label_guisantes)
        self.logica_juego.senal_aparecer_guisante.connect(self.ventana_juego_noche.aparecer_label_guisantes)
        self.logica_juego.senal_mover_guisante.connect(self.ventana_juego_dia.mover_label_guisantes)
        self.logica_juego.senal_mover_guisante.connect(self.ventana_juego_noche.mover_label_guisantes)
        self.ventana_juego_dia.senal_terminar_ronda.connect(self.logica_juego.pasar_ronda)
        self.ventana_juego_noche.senal_terminar_ronda.connect(self.logica_juego.pasar_ronda)
        self.logica_juego.senal_mostrar_ventana_post_ronda.connect(self.ventana_post_juego.init_gui)
        self.logica_juego.senal_pasar_ronda.connect(self.ventana_post_juego.actualizar_labels)
        self.ventana_post_juego.senal_pasar_ronda_dia.connect(self.ventana_juego_dia.empezar_ronda)
        self.ventana_post_juego.senal_pasar_ronda_noche.connect(self.ventana_juego_noche.empezar_ronda)
        self.ventana_post_juego.senal_actualizar_labels.connect(self.logica_juego.actualizar_labels)
        self.ventana_juego_dia.senal_pausa.connect(self.logica_juego.pausar_timers)
        self.ventana_juego_noche.senal_pausa.connect(self.logica_juego.pausar_timers)
        self.ventana_juego_dia.senal_despausar.connect(self.logica_juego.despausar)
        self.ventana_juego_noche.senal_despausar.connect(self.logica_juego.despausar)
        self.ventana_juego_dia.senal_salir.connect(self.ventana_inicio.init_gui)
        self.ventana_juego_noche.senal_salir.connect(self.ventana_inicio.init_gui)
        self.ventana_ranking.senal_volver.connect(self.ventana_inicio.init_gui)
        self.logica_juego.senal_sol_girasol.connect(self.ventana_juego_dia.aparecer_label_sol_girasol)
        self.logica_juego.senal_sol_girasol.connect(self.ventana_juego_noche.aparecer_label_sol_girasol)
        self.logica_juego.senal_eliminar_planta.connect(self.ventana_juego_dia.desaparecer_label_planta)
        self.logica_juego.senal_eliminar_planta.connect(self.ventana_juego_noche.desaparecer_label_planta)
        self.ventana_juego_dia.senal_colision_zombie_guisante.connect(self.logica_juego.colision_ZG)
        self.ventana_juego_noche.senal_colision_zombie_guisante.connect(self.logica_juego.colision_ZG)
        self.logica_juego.senal_eliminar_zombie.connect(self.ventana_juego_dia.desaparecer_zombie)
        self.ventana_post_juego.senal_volver.connect(self.ventana_inicio.init_gui)
        self.logica_inicio.mandar_usuario_a_ranking.connect(self.ventana_ranking.escribir_en_archivo)
    def iniciar_juego(self) -> None:
        self.ventana_inicio.show()