from tablero import print_tablero
from parametros import POND_PUNT, PROB_BESTIA
import os
from random import shuffle
from string import ascii_lowercase as L
#Flujo del juego
def abrir_puntajestxt():
    # abre el archivo puntajes.txt y saca sus contenidos en forma de list()
    s = []
    f = open('puntajes.txt','r')
    a = f.readlines()
    for lineas in a:
        s.append(lineas.strip().split(','))
    for i in range (len(s)):
        int(s[i][1])
    f.close()
    return s
def guardar_puntaje(string):
    # abre el archivo puntajes.txt y agrega el puntaje mas reciente
    f = open('puntajes.txt','a')
    f.write('\n'+string)
    f.close()
    return
def cargar_partida(usuario,ruta):
    #abre el archivo correspondiente al usuario, y carga el tablero, luego retorna el menu del juego con el tablero cargado
    lista = []
    tabla_arbitraria = []
    tabla_real_arbitraria = []
    tabla = []
    tabla2 = []
    tabla_real = []
    tabla_real2 = []
    f = open(ruta,'r')
    a = f.readlines()
    for e in a:
        lista.append(e.strip('\n').split(':'))
    x = int(lista[0][0])
    y = int(lista[0][1])
    tablero = [lista[0][i] for i in range(len(lista[0])) if i > 1 and i < y + 2]
    tablero_real = [e for e in lista[1]]
    tablero_real.pop(len(tablero_real)-1)
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] != "'" and tablero[i][j] != '[' and tablero[i][j] != ']' and tablero[i][j] != ',':
                tabla_arbitraria.append(tablero[i][j])
        tabla.append(list(tabla_arbitraria))
        tabla_arbitraria = []
    for i in range(len(tabla)):
        for j in range(len(tabla[i])):
            if j % 2 == 0:
                tabla_arbitraria.append(tabla[i][j])
        tabla2.append(list(tabla_arbitraria))
        tabla_arbitraria = []    
    for i in range(len(tablero_real)):
        for j in range(len(tablero_real[i])):
            if tablero_real[i][j] != "'" and tablero_real[i][j] != '[' and tablero_real[i][j] != ']' and tablero_real[i][j] != ',':
                tabla_real_arbitraria.append(tablero_real[i][j])
        tabla_real.append(list(tabla_real_arbitraria))
        tabla_real_arbitraria = []
    for i in range(len(tabla_real)):
        for j in range(len(tabla_real[i])):
            if j % 2 == 0:
                tabla_real_arbitraria.append(tabla_real[i][j])
        tabla_real2.append(list(tabla_real_arbitraria))
        tabla_real_arbitraria = []
    return menu_del_juego(usuario,tabla_real2,x,y,ruta,tabla2)
def escribir_archivo(archivo,tablero,tablero_real,X,Y):
    #Guarda la informacion importante del tablero de un jugador, para luego poder ser cargado, retorna el menu principal
    casillas_descubiertas = 0
    lista_de_posiciones = []
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] != ' ':
                casillas_descubiertas += 1
                lista_de_posiciones.append('('+str(i)+','+str(j)+')')
    string = f'{X}:{Y}:'
    f = open(archivo,'wt')
    for e in tablero:
        string += str(e)+':'
    string += f'{str(casillas_descubiertas)}:'
    for e in lista_de_posiciones:
        string += str(e)+':'
    string.strip(':')
    string += '\n'
    for e in tablero_real:
        string += str(e)+':'
    print(string, file=f)
    f.close()
    return
def menu_del_juego(usuario,tablero_real,X,Y,archivo,tablero):
    #maneja el flujo del juego
    print_tablero(tablero)
    opciones = input('Selecione una opcion(1, 2 o 3):\nDesubrir un sector[1]\nGuardar partida[2]\nSalir[3]\nVer tablero completo[4]:\n ')
    if opciones == '1':
        return descubrir_sector(usuario,tablero_real,X,Y,archivo,tablero)
    elif opciones == '2': #ejemplo sacado de https://www.w3schools.com/python/python_file_write.asp desde linea 18 a linea 22
        nombre_archivo = str(usuario+'.txt')                    
        ruta_archivo = os.path.join("Partidas",nombre_archivo)
        escribir_archivo(ruta_archivo,tablero,tablero_real,X,Y)
        return menu_principal()
    elif opciones == '3':
        return final_del_juego()
    elif opciones == '4':
        print_tablero(tablero_real)
        return final_del_juego()
def crear_tablero(X,Y):
    #Crea el tablero con las dimensiones especificadas por el usuario, ademas coloca los numeros en base a la posicion
    #de las bestias y no en base a la posicion escogida por el jugador
    tablero = []
    lista_appendeable = []
    numeros_aleatoreos = []
    numero_de_bestias = int(X * Y * PROB_BESTIA)
    for i in range(X):
        lista_appendeable.append(0)
    for i in range(Y):
        tablero.append(list(lista_appendeable))
    for i in range(X):
        for j in range(Y):
            numeros_aleatoreos.append((i,j))
    shuffle(numeros_aleatoreos)
    posiciones_de_bestias = [numeros_aleatoreos[i] for i in range(numero_de_bestias)]
    for e in posiciones_de_bestias:
        tablero[e[1]][e[0]] = 'N'
    for e in posiciones_de_bestias:
        y = e[1]
        x = e[0]
        if (y > 0 and y <= Y-1) and (x >= 0 and x <= X-1):
            if tablero[y - 1][x] != 'N':
                tablero[y - 1][x] += 1 #arriba
        if (y >= 0 and y < Y-1) and (x >= 0 and x <= X-1):
            if tablero[y + 1][x] != 'N':
                tablero[y + 1][x] += 1 #abajo
        if (x >= 0 and x < X-1) and (y >= 0 and y <= Y-1):
            if tablero[y][x + 1] != 'N':
                tablero[y][x + 1] += 1#derecha
        if (x > 0 and x <= X-1) and (y >= 0 and y <= Y-1): 
            if tablero[y][x - 1] != 'N':
                tablero[y][x - 1] += 1#izquierda
        if (x > 0 and x <= X-1) and (y > 0 and y <= Y-1):
            if tablero[y -1][x - 1] != 'N':
                tablero[y -1][x - 1] += 1 #arriba-izquierda
        if (x > 0 and x <= X-1) and (y >= 0 and y < Y-1): #abajo-izquierda
            if tablero[y + 1][x - 1] != 'N':
                tablero[y + 1][x - 1] += 1
        if (x >= 0 and x < X-1) and (y > 0 and y <= Y-1): #arriba-derecha
            if tablero[y -1][x + 1] != 'N':
                tablero[y -1][x + 1] += 1
        if (x >= 0 and x < X-1) and (y >= 0 and y < Y-1): #abajo-derecha
            if tablero[y + 1][x + 1] != 'N':
                tablero[y + 1][x + 1] += 1
    return tablero
def descubrir_sector(usuario,tablero_real,X,Y,archivo,tablero):
    #descubre una casilla en el tablero_real, luego la copia en el tablero y la muestra en pantalla
    posisiones_en_letras = {L[i]: i for i in range(X) if i < X}
    print(posisiones_en_letras)
    print('Indique que posicion del tablero quiere descubrir. Ej: (a,3)\n')
    x_arbitraria = (input())
    y = int(input())
    x = posisiones_en_letras[x_arbitraria]
    if int(x) >= int(X) or int(y) >= int(Y):
        print('Las cordenadas que eligio no son validas, intente denuevo')
        return descubrir_sector(usuario,tablero_real,X,Y,archivo,tablero)
    if tablero_real[y][x] != 'N':
        tablero[y][x] = tablero_real[y][x]
        print_tablero(tablero)
        return menu_del_juego(usuario,tablero_real,X,Y,archivo,tablero)
    if tablero_real[y][x] == 'N':
        print_tablero(tablero_real)
        casillas_descubiertas = 0
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                if tablero[i][j] != ' ' and tablero[i][j] != 'N':
                    casillas_descubiertas += 1
        puntaje = casillas_descubiertas * int(X * Y * PROB_BESTIA) * POND_PUNT
        print(f'Perdiste, tu puntaje fue de {puntaje}')
        string = usuario+','+str(puntaje)
        guardar_puntaje(string)
    return menu_principal()
def menu_principal():
    #consiste en el menu principal, da las opciones de crear, guardar partidas, ver el ranking y salirse del juego
    continuacion = True
    while continuacion:
        opciones_de_menu = input('Selecione una opcion(1,2,3 o 0):\nPartida Nueva[1]\nCargar partida[2]\nRevisar Ranking[3]\nSalir[0]:\n ')
        if opciones_de_menu == '1':
            X = int(input('Seleccione el ancho del tablero: '))
            Y = int(input('Seleccione el alto del tablero: '))
            if X < 3 or X > 15:
                print('El ancho del tablero debe estar dentro del intervalo [3,15]')
                X = int(input('Seleccione el ancho del tablero: '))
            if Y < 3 or Y > 15:
                print('El largo del tablero debe estar dentro del intervalo [3,15]')
                Y = int(input('Seleccione el alto del tablero: '))
            usuario = input('Indique su nombre de usuario: ')
            nombre_archivo = str(usuario+'.txt')                    
            ruta_archivo = os.path.join("Partidas",nombre_archivo)
            f = open(ruta_archivo,'x')
            f.close()
            tablero_real = crear_tablero(X,Y)
            tablero = []
            lista_appendeable = []
            for i in range(X):
                lista_appendeable.append(' ')
            for i in range(Y):
                tablero.append(list(lista_appendeable))
            puntaje = menu_del_juego(usuario,tablero_real,X,Y,ruta_archivo,tablero)
        if opciones_de_menu == '2':
            print('Indique su nombre de usuario')
            a = input()
            ruta = os.path.join("Partidas", a+'.txt')
            existencia_del_archivo = os.path.isfile(ruta)
            if existencia_del_archivo:
                partida_guardada = cargar_partida(a,ruta)
            else:
               print('No tiene ninguna partida guardada')
        if opciones_de_menu == '3':
            puntajes_top10 = abrir_puntajestxt()
            puntajes_top102 = [(int(puntajes_top10[i][1]), str(puntajes_top10[i][0])) for i in range(len(puntajes_top10))]
            puntajes_top102.sort(reverse=True)
            for i in range(len(puntajes_top102)):
                if i < 10:
                    print(puntajes_top102[i])
                elif i >= 10:
                    break
        if opciones_de_menu == '0':
            continuacion = False
    return final_del_juego()
print('Bienvenido a star advanced!')
partidas = menu_principal()
def final_del_juego():
    #se encarga de terminar el juego
    print("Gracias por jugar Star Advanced!")
    return 


 

        
    


