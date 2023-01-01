from tomemos import Tomemos
from jugadores import Jugador
from nuncanunca import YoNuncaNunca
from piramide.piramide import Piramide
if __name__ == 'main':
    numero_jugadores = int(input())
    lista_jugadores = []
    lista_juegos = [YoNuncaNunca(), Piramide()]
    for i in range(numero_jugadores):
        lista_jugadores.append(Jugador(input()))
    juego = Tomemos(lista_jugadores, lista_juegos)