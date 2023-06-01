from PyQt5.QtCore import pyqtSignal, QObject, QTimer
from aparicion_zombies import intervalo_aparicion
from random import choice, randint
from backend.elementos import (Girasol, Grilla, Guisantes, GuisantesHielo, PlantaAzul, 
                                PlantaClasica, PlantaPatata, ZombieClasico, ZombieRapido)
from parametros import (ALTO_GRILLA, ANCHO_GRILLA, COSTO_AVANZAR, DANO_MORDIDA, DANO_PROYECTIL, 
                        GRILLA_CARRIL_1_Y, GRILLA_CARRIL_2_Y, 
                        INTERVALO_APARICION_SOLES, INTERVALO_DISPARO, 
                        INTERVALO_TIEMPO_MORDIDA, LIMITE_X, N_ZOMBIES, 
                        PONDERADOR_DIURNO, PONDERADOR_NOCTURNO, 
                        POS_INICIAL_GUISANTE_CARRIL1_Y, POS_INICIAL_GUISANTE_CARRIL2_Y, 
                        SOLES_INICIALES, TECLA_PAUSA)
class LogicaJuego(QObject):
    senal_aparecer_zombie = pyqtSignal(object, int)
    senal_mover_zombie = pyqtSignal(int, list)
    senal_mover_guisante = pyqtSignal(tuple, int) 
    senal_desaparecer_zombie = pyqtSignal()
    senal_aparecer_sol = pyqtSignal(int, int, int, int)
    senal_desaparecer_sol = pyqtSignal()
    senal_sol_girasol = pyqtSignal(tuple)
    senal_pasar_ronda = pyqtSignal(int, int, int, int, bool)
    senal_cambiar_puntaje = pyqtSignal
    senal_actualizar_zombies_destruidos = pyqtSignal()
    senal_actualizar_zombies_restantes = pyqtSignal()
    senal_actualizar_soles = pyqtSignal()
    senal_plantar_planta = pyqtSignal(tuple)
    senal_mandar_lista_zombies = pyqtSignal(list)
    senal_enviar_verificacion_posicion = pyqtSignal(bool, int, int, int)
    senal_verificar_sol = pyqtSignal(int, int, int)
    senal_mover_soles = pyqtSignal()
    senal_aparecer_guisante = pyqtSignal(int, int, int, int, str, int)
    senal_mostrar_ventana_post_ronda = pyqtSignal(str)
    senal_actualizar_labels = pyqtSignal()
    senal_eliminar_zombie = pyqtSignal(int)
    senal_eliminar_planta = pyqtSignal(int, int)
    def __init__(self, soles, planta, planta_hielo, zombie,
                zombie_rapido, girasol, papa, guisante, guisante_hielo):
        super().__init__()
        self.soles = soles
        self.planta = planta
        self.planta_hielo = planta_hielo
        self.zombie = zombie
        self.zombie_rapido = zombie_rapido
        self.girasol = girasol
        self.papa = papa
        self.guisante = guisante
        self.guisante_hielo = guisante_hielo
        self.timer_aparecer_zombie = QTimer()
        self.timer_mover_zombie = QTimer()
        self.timer_zombie_rapido = QTimer()
        self.timer_soles = QTimer()
        self.timer_disparo_planta = QTimer()
        self.timer_guisantes = QTimer() #Maneja el movimiento de los guisantes
        self.timer_comer = QTimer()
        self.timers_zombies = QTimer()
        self.timer_actualizar_juego = QTimer()
        self.timer_mover_soles = QTimer()
        self.timer_girasol = QTimer()
        self.cantidad_soles = SOLES_INICIALES
        self.zombies_destruidos = 0
        self.zombies_restantes = N_ZOMBIES
        self.planta_activa = True #permite que solo se inicien los timers de las plantas si hay alguna plantada en el mapa
        self.lista_soles = []
        self.puntaje = 0
        self.ronda = 1
        self.id_guisantes = 0
        self.zombies = []
        self.zombies_activos = []
        self.guisantes_activos = []
        self.zombies_comiendo = []
        self.gri1 = []
        self.gri2 = [] #Variable arbitraria
        self.grid = []
        self.theme = ''
        for i in range(10):
            a = Grilla()
            self.gri1.append(a)
        for i in range(10):
            a = Grilla()
            self.gri2.append(a)
        self.grid.append(self.gri1)
        self.grid.append(self.gri2)
        self.setear_posiciones_grilla()
    def setear_zombies(self, theme):
        self.theme = theme
        if theme == 'dia':
            self.intervalo = intervalo_aparicion(self.ronda, PONDERADOR_DIURNO)
        elif theme == 'noche':
            self.intervalo = intervalo_aparicion(self.ronda, PONDERADOR_NOCTURNO)
        for i in range(N_ZOMBIES):
            c = ZombieClasico()
            b = ZombieRapido()
            lista = [c, b]
            a = choice(lista)
            self.zombies.append([a, i]) #crea la lista de zombies activos y su id
        self.set_timers()
        self.iniciar_timers()
    def setear_posiciones_grilla(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if i == 0:
                    self.grid[i][j].pos_y = GRILLA_CARRIL_1_Y
                    self.grid[i][j].pos_x += ANCHO_GRILLA*j
                elif i == 1:
                    self.grid[i][j].pos_y = GRILLA_CARRIL_2_Y 
                    self.grid[i][j].pos_x += ANCHO_GRILLA*j
    def set_timers(self): #falta definir en los parametros los valores constantes
        self.timer_aparecer_zombie.setInterval(int(self.intervalo*10000))
        self.timer_aparecer_zombie.timeout.connect(self.aparecer_zombies)
        self.timer_mover_zombie.setInterval(800)
        self.timer_mover_zombie.timeout.connect(self.mover_zombies)
        self.timer_soles.setInterval(INTERVALO_APARICION_SOLES)
        self.timer_soles.timeout.connect(self.aparecer_sol)
        self.timer_mover_soles.setInterval(100)
        self.timer_mover_soles.timeout.connect(self.mover_labels_soles)
        self.timer_disparo_planta.setInterval(INTERVALO_DISPARO)
        self.timer_disparo_planta.timeout.connect(self.activar_plantas) #dispara los guisantes
        self.timer_guisantes.setInterval(100)
        self.timer_guisantes.timeout.connect(self.mover_guisantes)
        self.timer_comer.setInterval(INTERVALO_TIEMPO_MORDIDA)
        self.timer_comer.timeout.connect(self.zombies_comer)
        self.timer_girasol.setInterval(int(INTERVALO_APARICION_SOLES*0.5))
        self.timer_girasol.timeout.connect(self.girasol_activar) #activa los girasoles, falta definir la funcion
    def aparecer_sol(self):
        pos_x = randint(400, 1200)
        pos_y = randint(50, 500)
        ancho = self.soles.ancho
        alto = self.soles.alto
        self.senal_aparecer_sol.emit(pos_x, pos_y, ancho, alto)
        self.lista_soles.append([pos_x, pos_y])
    def cheatcodes(self):
        pass
    def iniciar_timers(self):
        self.timer_aparecer_zombie.start()
        self.timer_mover_zombie.start()
        self.timer_soles.start()
        self.timer_mover_soles.start()
        self.timer_comer.start()
    def iniciar_timers_plantas(self):
        self.timer_disparo_planta.start()
        self.timer_guisantes.start()
        self.timer_girasol.start()
    def despausar(self):
        self.timer_aparecer_zombie.start()
        self.timer_mover_zombie.start()
        self.timer_soles.start()
        self.timer_mover_soles.start()
        self.timer_disparo_planta.start()
        self.timer_guisantes.start()
        self.timer_girasol.start()
        self.timer_comer.start()
    def pausar_timers(self):
        self.timer_aparecer_zombie.stop()
        self.timer_mover_zombie.stop()
        self.timer_soles.stop()
        self.timer_mover_soles.stop()
        self.timer_disparo_planta.stop()
        self.timer_guisantes.stop()
        self.timer_girasol.stop()
        self.timer_comer.stop()
    def pasar_ronda(self, bool, tipo): #te avisa si el jugador puede pasar de ronda, se activa al apretar el boton de avanzar
        self.pausar_timers()
        if self.zombies_restantes == 0:
            self.senal_mostrar_ventana_post_ronda.emit(tipo)
            self.senal_pasar_ronda.emit(self.ronda, self.cantidad_soles, self.zombies_destruidos, self.puntaje, bool) #actualiza los labels de la ventana post ronda
        if bool:
            self.senal_mostrar_ventana_post_ronda.emit(tipo)
            self.senal_pasar_ronda.emit(self.ronda, self.cantidad_soles, self.zombies_destruidos, self.puntaje, bool)
        if not bool:
            self.senal_mostrar_ventana_post_ronda.emit(tipo)
            self.senal_pasar_ronda.emit(self.ronda, self.cantidad_soles, self.zombies_destruidos, self.puntaje, bool)
        self.resetear_juego()
    def aparecer_zombies(self):
        if len(self.zombies) > 0:
            self.senal_aparecer_zombie.emit(self.zombies[0][0], self.zombies[0][1])  
            self.zombies_activos.append(self.zombies.pop(0))
            self.senal_mandar_lista_zombies.emit(self.zombies_activos)
        else:
            self.timer_aparecer_zombie.stop()   
    def chequear_colision(self, zombie):
        if zombie.pos_x == LIMITE_X:
            self.pasar_ronda(False, 'nada')
    def mover_zombies(self): #cada vez que se mueva se revisar si choca con algo
        for zombie in self.zombies_activos:
            cambio_pos = zombie[0].mover()
            self.senal_mover_zombie.emit(zombie[1], cambio_pos)
            self.chequear_colision(zombie[0])
            #self.chequear_colision_zombie_planta(zombie[0])
    def verificar_posicion(self, x, y, p): #y entre 300 y 400 abajo y 300 y 200 arriba
        if p == 'plantaclasica':
            planta = PlantaClasica()
            descuento = 100
        if p == 'plantahielo':
            planta = PlantaAzul()
            descuento = 150
        if p == 'girasol':
            planta = Girasol()
            descuento = 50
        if p == 'papa':
            planta = PlantaPatata()
            descuento = 75
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if i == 0:
                    if self.grid[i][j].pos_x <= x <= self.grid[i][j].pos_x + ANCHO_GRILLA:
                        if self.grid[i][j].pos_y <= y <= self.grid[i][j].pos_y + ALTO_GRILLA:
                            self.senal_enviar_verificacion_posicion.emit(self.grid[i][j].ocupado, i,j, descuento)
                            planta.posicion_plantada_x = x
                            planta.posicion_plantada_y = y
                            planta.carril = 1
                            self.grid[i][j].planta = planta
                            self.grid[i][j].tipo = p
                            if not self.grid[i][j].ocupado:
                                self.grid[i][j].ocupado = True
                elif i == 1:
                    if self.grid[i][j].pos_x <= x <= self.grid[i][j].pos_x + ANCHO_GRILLA:
                        if self.grid[i][j].pos_y <= y <= self.grid[i][j].pos_y + ALTO_GRILLA:
                            self.senal_enviar_verificacion_posicion.emit(self.grid[i][j].ocupado, i, j, descuento)
                            planta.posicion_plantada_x = x
                            planta.posicion_plantada_y = y
                            planta.carril = 2
                            self.grid[i][j].planta = planta
                            self.grid[i][j].tipo = p
                            if not self.grid[i][j].ocupado:
                                self.grid[i][j].ocupado = True
        if self.planta_activa:
            self.iniciar_timers_plantas()
            self.planta_activa = False
        self.setear_plantas()
    def resetear_juego(self): #falta crear la senal para resetear el juego
        self.zombies_destruidos = 0
        self.zombies_restantes = N_ZOMBIES
        self.ronda += 1
        for e in self.grid:
            for h in e:
                h.vaciar()
        self.puntaje = 0
        self.planta_activa = True
        self.zombies_activos = []
        self.guisantes_activos = []
        self.lista_soles = []
        self.setear_zombies(self.theme)
    def verificar_pos_sol(self, x, y):
        for e in self.lista_soles:
            if e[0] <= x <= e[0] + 50:
                if e[1] <= y <= e[1] + 50:
                    self.cantidad_soles += 25
                    self.senal_verificar_sol.emit(25, x, y)
    def actualizar_labels(self):
        self.senal_actualizar_labels.emit()
    def mover_guisantes(self):
        for g in self.guisantes_activos:
            nueva_pos = g[0].mover()
            id = g[1]
            self.senal_mover_guisante.emit(nueva_pos, id)
    def activar_plantas(self):
        a = Guisantes()
        b = GuisantesHielo()
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].ocupado and self.grid[i][j].tipo != 'papa' and self.grid[i][j].tipo != 'girasol':
                    if self.grid[i][j].tipo == 'plantaclasica':
                        a.pos_x = self.grid[i][j].planta.x_guisante
                        a.pos_y = self.grid[i][j].planta.y_guisante
                        self.grid[i][j].planta.guisante = a
                        self.guisantes_activos.append([a, self.id_guisantes])
                        x, y, ancho, alto, pixeles = self.grid[i][j].planta.guisante.crear_label()
                        self.senal_aparecer_guisante.emit(x, y, ancho, alto, pixeles, self.id_guisantes)
                        self.id_guisantes += 1
                    if self.grid[i][j].tipo == 'plantahielo':
                        b.pos_x = self.grid[i][j].planta.x_guisante
                        b.pos_y = self.grid[i][j].planta.y_guisante
                        self.grid[i][j].planta.guisante = b
                        self.guisantes_activos.append([b, self.id_guisantes])
                        x, y, ancho, alto, pixeles = self.grid[i][j].planta.guisante.crear_label()
                        self.senal_aparecer_guisante.emit(x, y, ancho, alto, pixeles, self.id_guisantes)
                        self.id_guisantes += 1
    def girasol_activar(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                
                if self.grid[i][j].tipo == 'girasol' and self.grid[i][j].ocupado:
                    x, y, ancho, alto = self.grid[i][j].planta.crear_label_sol()
                    sol = (self.grid[i][j].pos_x + x, self.grid[i][j].pos_y + y, ancho, alto)
                    self.senal_sol_girasol.emit(sol)
    def setear_plantas(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j].tipo == 'plantaclasica':
                    if i == 0:
                        self.grid[i][j].planta.y_guisante = POS_INICIAL_GUISANTE_CARRIL1_Y
                        self.grid[i][j].planta.x_guisante = self.grid[i][j].pos_x + ANCHO_GRILLA
                    elif i == 1:
                        self.grid[i][j].planta.y_guisante = POS_INICIAL_GUISANTE_CARRIL2_Y
                        self.grid[i][j].planta.x_guisante = self.grid[i][j].pos_x + ANCHO_GRILLA
                if self.grid[i][j].tipo == 'plantahielo':
                    if i == 0:
                        self.grid[i][j].planta.y_guisante = POS_INICIAL_GUISANTE_CARRIL1_Y
                        self.grid[i][j].planta.x_guisante = self.grid[i][j].pos_x + ANCHO_GRILLA
                    elif i == 1:
                        self.grid[i][j].planta.y_guisante = POS_INICIAL_GUISANTE_CARRIL2_Y
                        self.grid[i][j].planta.x_guisante = self.grid[i][j].pos_x + ANCHO_GRILLA
    def colision_ZG(self, id):
        for e in self.zombies_activos:
            if id in e:
                e[0].vida -= DANO_PROYECTIL
                if e[0].vida <= 0:
                    self.zombies_destruidos += 1
                    self.zombies_restantes -= 1
                    self.senal_eliminar_zombie.emit(id)
                    self.zombies_activos.remove(e)
    #def chequear_colision_zombie_planta(self, i , j, id):
    #    if self.grid[i][j].ocupado:
    #        self.zombies_comiendo.append(self.zombies_activos.pop(self.zombies_activos))
    def zombies_comer(self):
        for e in self.zombies_comiendo:
            e[1].planta.vida -= DANO_MORDIDA
            if e[1].planta.vida <= 0:
                self.senal_eliminar_planta.emit(e[2],e[3])
                e[1].vaciar()
                self.zombies_comiendo.remove(e)
                self.zombies_activos.append(e[0])
    def mover_labels_soles(self):
        self.senal_mover_soles.emit()
    def salir(self):
        self.hide()
    def keyPressEvent(self, event):
        if event.key().lower() == TECLA_PAUSA:
            self.pausar_timers()
