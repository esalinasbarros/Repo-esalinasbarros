import sys
from DCCruz_v_Zombies import DCCruz

'''
gran parte del codigo de todos los modulos esta sacado
de la AS3
'''

def hook(type_, value, traceback):
    print(type_)
    print(traceback)
sys.__excepthook__ = hook
juego = DCCruz(sys.argv)
juego.iniciar_juego()
sys.exit(juego.exec()) 
    