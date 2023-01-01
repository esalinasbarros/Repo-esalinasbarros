from random import choice
def generador_cartas():
    tipos = ['Pic', 'Diamante', 'Corazon', 'Trebol']
    numeros = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
    return ' de '.join([choice(numeros), choice(tipos)])
