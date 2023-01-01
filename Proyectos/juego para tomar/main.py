from tomemos import Tomemos
from jugadores import Jugador
from nuncanunca import YoNuncaNunca
if __name__ == 'main':
    numero_jugadores = int(input())
    lista_jugadores = []
    lista_juegos = []
    nunca = YoNuncaNunca()
    for i in range(numero_jugadores):
        lista_jugadores.append(Jugador(input()))
    juego = Tomemos(lista_jugadores, lista_juegos)