from tomemos import Tomemos
from jugadores import Jugador
print(__name__)
if __name__ == '__main__':
    numero_jugadores = int(input())
    lista_jugadores = []
    for i in range(numero_jugadores):
        lista_jugadores.append(Jugador(input()))
    juego = Tomemos(lista_jugadores)