from os import path
RUTA_CRAZYRUZ = path.join('.','sprites','CrazyRuz','crazyRuz.png')
RUTAS_ELEMENTOS_JUEGO = {
    'guisante_2': path.join('.','sprites','Elementos de juego','guisante_2.png'),
    'guisante_3': path.join('.','sprites','Elementos de juego','guisante_3.png'),
    'guisante_1': path.join('.','sprites','Elementos de juego','guisante_1.png'),
    'guisanteHielo_1': path.join('.','sprites','Elementos de juego','guisanteHielo_1.png'),
    'guisanteHielo_2': path.join('.','sprites','Elementos de juego','guisanteHielo_2.png'),
    'guisanteHielo_3': path.join('.','sprites','Elementos de juego','guisanteHielo_3.png'),
    'logo': path.join('.','sprites','Elementos de juego','logo.png'),
    'sol': path.join('.','sprites','Elementos de juego','sol.png'),
    'texto_final': path.join('.','sprites','Elementos de juego','textoFinal.png')}
RUTA_FRONTEND = {
    'ventana_principal': path.join('.','Ventana_principal_T2.ui'),
    'ventana juego dia': path.join('.','ventana_dia_T2.ui'),
    'ventana juego noche': path.join('.','ventana_noche_T2.ui'),
    'ventana inicio': path.join('.','ventana_inicio.ui'),
    'ventana ranking': path.join('.','ranking_T2.ui'),
    'ventana postronda': path.join('.','ventana_postronda_T2.ui')}
RUTAS_FONDOS = {
    'fondo_menu': path.join('.','sprites','Fondos','fondoMenu.png'),
    'jardin_abuela': path.join('.','sprites','Fondos','jardinAbuela.png'),
    'salida_nocturna': path.join('.','sprites','Fondos','salidaNocturna.png')}
RUTAS_PLANTAS = {
    'girasol_1': path.join('.','sprites','Plantas','girasol_1.png'),
    'girasol_2': path.join('.','sprites','Plantas','girasol_2.png'),
    'lanzaguisantes_1': path.join('.','sprites','Plantas','lanzaguisantes_1.png'),
    'lanzaguisantes_2': path.join('.','sprites','Plantas','lanzaguisantes_2.png'),
    'lanzaguisantes_3': path.join('.','sprites','Plantas','lanzaguisantes_3.png'),
    'lanzaguisantesHielo_1': path.join('.','sprites','Plantas','lanzaguisantesHielo_1.png'),
    'lanzaguisantesHielo_2': path.join('.','sprites','Plantas','lanzaguisantesHielo_2.png'),
    'lanzaguisantesHielo_3': path.join('.','sprites','Plantas','lanzaguisantesHielo_3.png'),
    'papa_1': path.join('.','sprites','Plantas','papa_1.png'),
    'papa_2': path.join('.','sprites','Plantas','papa_2.png'),
    'papa_3': path.join('.','sprites','Plantas','papa_3.png')}
RUTAS_ZOMBIES_CAMINANDO = {
    'zombiehernanrunner_1':path.join('.','sprites','Zombies','Caminando','zombieHernanRunner_1.png'),
    'zombiehernanrunner_2':path.join('.','sprites','Zombies','Caminando','zombieHernanRunner_2.png'),
    'zombienicowalker_1':path.join('','sprites','Zombies','Caminando','zombieNicoWalker_1.png'),
    'zombienicowalker_2':path.join('','sprites','Zombies','Caminando','zombieNicoWalker_2.png')}
RUTAS_ZOMBIES_COMIENDO = {
    'zombiehernancomiendo_1': path.join('.','sprites','Zombies','Comiendo','zombieHernanComiendo_1.png'),
    'zombiehernancomiendo_2': path.join('.','sprites','Zombies','Comiendo','zombieHernanComiendo_2.png'),
    'zombiehernancomiendo_3': path.join('.','sprites','Zombies','Comiendo','zombieHernanComiendo_3.png'),
    'zombienicocomiendo_1': path.join('.','sprites','Zombies','Comiendo','zombieNicoComiendo_1.png'),
    'zombienicocomiendo_2': path.join('.','sprites','Zombies','Comiendo','zombieNicoComiendo_2.png'),
    'zombienicocomiendo_3': path.join('.','sprites','Zombies','Comiendo','zombieNicoComiendo_3.png')}
INTERVALO_DISPARO = 7000
VELOCIDAD_GUISANTES = 4
VIDA_PLANTA = 20
DANO_PROYECTIL = 5
RELENTIZAR_ZOMBIE = 0.9
INTERVALO_SOLES_GIRASOL = 750
CANTIDAD_SOLES = 1
PONDERADOR_NOCTURNO = 2
PONDERADOR_DIURNO = 1.5
VELOCIDAD_ZOMBIE = 4 #CAMBIAR
VELOCIDAD_ZOMBIE_RAPIDO = 1.5*VELOCIDAD_ZOMBIE
DANO_MORDIDA = 5
INTERVALO_TIEMPO_MORDIDA = 300
VIDA_ZOMBIE = 40
INTERVALO_APARICION_SOLES = 8500
PUNTAJE_ZOMBIE_DIURNO = 100
PUNTAJE_ZOMBIE_NOCTURNO = 150
SOLES_INICIALES = 100
N_ZOMBIES = 10
COSTO_AVANZAR = 500
MIN_CARACTERES = 3
MAX_CARACTERES = 15
POS_INICIAL_ZOMBIE_X = 1130
POS_INICIAL_ZOMBIE_Y = 300
POS_INICIAL_ZOMBIE_CARRIL2_Y = 200
POS_INICIAL_GUISANTE_CARRIL1_X = 100
POS_INICIAL_GUISANTE_CARRIL2_X = 100
POS_INICIAL_GUISANTE_CARRIL1_Y = 220
POS_INICIAL_GUISANTE_CARRIL2_Y = 320
PIXELES_AL_MOVER_ZOMBIE = 3
PIXELES_AL_MOVER_GUISANTE = 3
LIMITE_IZQUIERDA = 1300
LIMITE_X = 390
ANCHO = 1382
ALTO = 819
TECLA_PAUSA = 'p'
GRILLA_CARRIL_1_Y = 200
GRILLA_CARRIL_2_Y = 300
GRILLA_X = 390
ANCHO_GRILLA = 71
ALTO_GRILLA = 100
CHEATCODE_KIL = ['k','i','l']
CHEATCODE_SUN = ['s','u','n']
SOLES_EXTRA = 10000


