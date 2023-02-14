#include <iostream>
#include <cmath>
using namespace std;

string comprobar_ganador(string jug1, string jug2) {
    int caso;
    if (jug1 == "piedra" && jug2 == "papel") {
        caso = 1;
    }

    if (jug1 == "piedra" && jug2 == "tijera") {
        caso = 2;
    }

    if (jug1 == "papel" && jug2 == "tijera") {
        caso = 1;
    }

    if (jug1 == "papel" && jug2 == "piedra") {
        caso = 2;
    }

    if (jug1 == "tijera" && jug2 == "papel") {
        caso = 2;
    }

    if (jug1 == "tijera" && jug2 == "piedra") {
        caso = 1;
    }

    if (jug1 == jug2) {
        caso = 3;
    }

    switch (caso) {
    case 1:
        return "Gano el jugador 2";
        break;
    case 2:
        return "Gano el jugador 1";
        break;
    case 3:
        return "Empate!";
        break;
    default:
        return "Ambos jugadores deben elejir Piedra, Papel o Tijera";
        break;
    }
}

int main() {
    string elegido1;
    string elegido2;
    int jugador_incial;

    cout << "Bienvenido a piedra, papel y tijera" << endl;
    cout << "Jugador 1: " << endl;
    cin >> elegido1;
    cout << "Jugador 2: " << endl;
    cin >> elegido2;
    cout << comprobar_ganador(elegido1, elegido2);
    return 0;
}