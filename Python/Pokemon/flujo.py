from abc import ABC, abstractmethod
from os import path
from random import choice, randint, random, shuffle
from parametros import AUMENTO_DEFENSA, ENERGIA_ENTRENAMIENTO, GASTO_ENERGIA_BAYA, GASTO_ENERGIA_CARAMELO,\
    GASTO_ENERGIA_POCION, MAX_AUMENTO_ENTRENAMIENTO, MAX_AUMENTO_EXPERIENCIA,\
    MIN_AUMENTO_ENTRENAMIENTO, MIN_AUMENTO_EXPERIENCIA, PROB_EXITO_BAYA, PROB_EXITO_CARAMELO, PROB_EXITO_POCION
class LigaProgramon:
    def __init__(self):
        self.entrenadores = list()
        self.perdedores = list()
        self.ganadores = list()
        self.ronda_actual = 1
        self.campeon = ''
        self.bool = True #variable global, no me qudaba tiempo para pensar otra cosa
        self.menu_de_inicio()
    def abrir_entrenadores(self):
        titulo_menu_principal = ''
        ruta = path.join('entrenadores.csv')
        with open(ruta,'r') as f:
            lin = f.readlines()
            lineas = [e.strip().split(',') for e in lin]
            lineas.remove(lineas[0])
        for i in range(len(lineas)):
            titulo_menu_principal += f'[{i+1}] '+lineas[i][0]+': '
            a = lineas[i][1].split(';')
            for h in a:
                titulo_menu_principal += h+', '
            titulo_menu_principal += '\n'
            c = i + 2
        titulo_menu_principal += f'[{c}] salir'
        entrenador = [[lineas[i][0],(lineas[i][1].split(';')),lineas[i][2],lineas[i][3].split(';')] for i in range(len(lineas))]   
        programones = self.abrir_programones()
        objetos = self.abrir_objetos()
        entrenadores = []
        for e in entrenador:
            endor = Entrenador(e[0],e[2])
            for p in programones:
                if p.nombre in e[1]:
                    endor.programones.append(p)
            for o in objetos:
                if o.nombre in e[3]:
                    endor.objetos.append(o)
            entrenadores.append(endor)
        return titulo_menu_principal, entrenadores
    def menu_de_inicio(self):
        print(' ** Menu de inicio **')
        print('______________________')
        print('')
        print('Escoja que entrenador quiere utilizar')
        print('')
        titulo, entrenadores = self.abrir_entrenadores()
        for object in entrenadores:
            self.entrenadores.append(object)
        print(titulo)
        opcion = int(input())
        entrenador_escogido = entrenadores[opcion-1]
        a = self.menu_entrenador(entrenador_escogido)
        if opcion > len(self.entrenadores):
            print('gracias por jugar en DCCampeonato Programon')
    def menu_entrenador(self, entrenador_escogido):
        print('*** Menu Entrenador ***')
        print('')
        print('_______________________')
        print('')
        print('[1] Entrenamiento\n[2] Simular ronda\n[3] Resumen campeonato\n[4] Crear objeto')
        print('[5] Utilizar objeto\n[6] Estado entrenador\n[7] Volver\n[8] Salir')
        opcion = int(input())
        if opcion == 1:
            return self.menu_de_entrenamiento(entrenador_escogido)
        if opcion == 2:
            if self.ronda_actual > 4:
                print('Has ganado la LigaProgramon!!')
                return self.menu_de_entrenamiento(entrenador_escogido)  #REVISAR 
            else:
                self.simular_ronda(entrenador_escogido)
        if opcion == 3:
            print('Resumen campeonato') #no tuve tiempo para hacer que el print tenga la indentacion correcta
            print('------------------')
            participantes = 'Participantes: '
            for e in self.entrenadores:
                participantes += f'{e.nombre}, '
            print(participantes)
            print(f'Ronda actual: {self.ronda_actual}')
            ganadores = 'Participantes que siguen en la competencia: '
            for e in self.ganadores:
                ganadores += f'{e.nombre}, '
            print(ganadores)
        if opcion == 4:
            return entrenador_escogido.crear_objetos()
        if opcion == 5:
            return self.utilizar_objeto(entrenador_escogido)
        if opcion == 6:
            print(f'         **** Estado Entrenador ****           ')
            print(f'-----------------------------------------------')
            print(f'Nombre: {entrenador_escogido.nombre}')
            print(f'Energia: {entrenador_escogido.energia}')
            objetos_entrenador = ''
            for e in entrenador_escogido.objetos:
                objetos_entrenador += f' {e.nombre},'
            print(f'Objetos: {objetos_entrenador}')
            print(f'                               * Programones *                           ')
            print(f'-------------------------------------------------------------------------')
            print(f'        Nombre        |        Tipo        |        Nivel        |   Vida')
            programones_entrenador = ''
            for e in entrenador_escogido.programones:
                print(f' {e.nombre} |  {e.tipo} | {e.nivel} | {e._vida} ')
        if opcion == 7:
            return self.menu_de_inicio(self)
        if opcion == 8:
            return salir()
    def menu_de_entrenamiento(self, entrenador_escogido):
        print('*** Menu de Entrenamiento ***')
        print('')
        print('______________________________')
        print('')
        titulo_menu = ''
        contador = 1
        lista_programones = []
        indexador = 0
        for i in range(len(self.entrenadores)):
            if self.entrenadores[i] == entrenador_escogido:
                indexador = i
        for e in self.entrenadores[indexador].programones:
            titulo_menu += f'[{contador}] {e.nombre}\n'
            lista_programones.append(e)
            contador += 1
        titulo_menu += f'[{contador}] Volver\n'
        titulo_menu += f'[{contador + 1}] Salir'
        print(titulo_menu) 
        a = int(input())
        if a < len(lista_programones)+1:
            programon_escogido = lista_programones[a - 1] #aca se asigna el programon como objeto!!
        else:
            pass
        if entrenador_escogido.energia < ENERGIA_ENTRENAMIENTO:
            print(f'El entrenador no tiene suficiente energia para entrenar a un programon')
            return self.menu_entrenador(entrenador_escogido)
        else:
            print(entrenador_escogido)
            entrenador_escogido._energia -= ENERGIA_ENTRENAMIENTO
            programon_escogido.entrenamiento()
        return self.menu_entrenador(entrenador_escogido)
    def elegir_luchador(self,entrenador_ecogido):
        print('   *** Elige tu luchador   ***')
        print('------------------------------')
        for i in range(len(entrenador_ecogido.programones)):
            print(f'[{i+1}] {entrenador_ecogido.programones[i].nombre}')
            c = i + 2
        print(f'[{c}] Volver')
        print(f'[{c+1}] Salir')
        p = int(input())
        if p <= len(entrenador_ecogido.programones):
            programon_escogido = entrenador_ecogido.programones[p-1]
            return programon_escogido
        else:
            if p == c:
                return self.menu_de_entrenamiento(entrenador_ecogido)
            if p == c + 1:
                return salir()
    def abrir_programones(self):
        ruta = path.join('programones.csv')
        programones = []
        with open(ruta,'r') as f:
            programo = f.readlines()
            programon = [programo[i].strip() for i in range(len(programo))]
            programon.remove(programon[0])
            for a in programon:
                nombre, tipo, nivel, vida, ataque, defensa, velocidad = a.split(',')
                if tipo == 'planta':
                    prog = TipoPlanta(nombre, tipo, nivel, vida, ataque, defensa, velocidad)
                if tipo == 'fuego':
                    prog = TipoFuego(nombre, tipo, nivel, vida, ataque, defensa, velocidad)
                if tipo == 'agua':
                    prog = TipoAgua(nombre, tipo, nivel, vida, ataque, defensa, velocidad)
                programones.append(prog)
        return programones
    def abrir_objetos(self):
        objetos = []
        ruta = path.join('objetos.csv')
        with open(ruta,'r') as f:
            obje = f.readlines()
            objeto = [obje[i].strip() for i in range(len(obje))]
            objeto.remove(objeto[0]) 
            for a in objeto:
                nombre, tipo = a.split(',')
                if tipo == 'baya':
                    ob = Baya(nombre, tipo)
                if tipo == 'caramelo':
                    ob = Caramelo(nombre, tipo)
                if tipo == 'pocion':
                    ob = Pocion(nombre, tipo)
                objetos.append(ob)
        return objetos
    def resumen_campeonato(self):
        pass
    def simular_ronda(self, entrenador_escogido): #revisar
        programon_escogido = self.elegir_luchador(entrenador_escogido) #.nombre
        print(7*" "+f'ronda {self.ronda_actual}'+7*" ")
        print(21*'_')
        print('')
        if self.bool:
            peleas = [[self.entrenadores[i], choice(self.entrenadores[i].programones)] for i in range(len(self.entrenadores))\
                if self.entrenadores[i] != entrenador_escogido]
            shuffle(peleas)
            lista = [entrenador_escogido, programon_escogido]
            peleas.insert(0,lista)
            self.bool = False #se queda asi para que solo se use esa lista 1 vez
        else:
            peleas = [self.ganadores[i] for i in range(len(self.ganadores))]
            self.ganadores = []
        for i in range(1, len(peleas), 2):
            #hacer que termine
            print(f'{peleas[i-1][0].nombre} usando al programon {peleas[i-1][1].nombre}, se enfrenta a {peleas[i][0].nombre}')
            print(f'usando al programon {peleas[i][1].nombre}')
            ganador, perdedor, ganado = peleas[i-1][1].luchar(peleas[i][1])
            if i == 1 and not ganado:
                print('Perdiste, quieres jugar denuevo desde cero? (si, no)')
                opcion = input()
                if opcion.lower() == 'si':
                    return jugar_de_nuevo()
                if opcion.lower == 'no':
                    return salir()
                else:
                    print('Su input no es valido')
                    return salir()
            if ganado:
                print(f'{peleas[i-1][0].nombre} ha ganado la batalla')
                self.ganadores.append([peleas[i-1][0], peleas[i-1][1]])
                self.perdedores.append([peleas[i][0], peleas[i][1]])
            else:
                print(f'{peleas[i][0].nombre} ha ganado la batalla')
                self.ganadores.append([peleas[i][0], peleas[i][1]])
                self.perdedores.append([peleas[i-1][0], peleas[i-1][1]])
        self.ronda_actual += 1
        return self.menu_entrenador(entrenador_escogido)
    def utilizar_objeto(self,entrenador_escogido):
        print('Objetos disponibles')
        print('-------------------')
        contador = 1
        for e in entrenador_escogido.objetos:
            print(f'[{contador}] {e.nombre}')
            contador += 1
        print(f'[{contador+1}] Volver')
        print(f'[{contador+2}] Salir')
        opcion = int(input('Tiene que ser un numero: '))
        if opcion <= len(entrenador_escogido.objetos):
            objeto_escogido = entrenador_escogido.objetos[opcion]
            print('Escoga al programon que quiere beneficiar')
            for i in range(len(entrenador_escogido.programones)):
                print(f'[{i+1}] {entrenador_escogido.programones[i].nombre}')
            ipt = int(input("Solo debe escribir un numero: "))
            programon = entrenador_escogido.programones[ipt-1]
            print(f'Programon beneficiado: {programon}')
            print(f'Objeto utilizado: {objeto_escogido.nombre} (Tipo {objeto_escogido.tipo})')
            if objeto_escogido.tipo == 'baya':
                programon._vida += randint(1,10)
            if objeto_escogido.tipo == 'pocion':
                programon._ataque += randint(1,7)
            if objeto_escogido.tipo == 'caramelo':
                programon._ataque += randint(1,7)
                programon._vida += randint(1,10)
                programon._defensa += AUMENTO_DEFENSA
        elif opcion == len(entrenador_escogido.objetos) + 1:
            return self.menu_entrenador(entrenador_escogido)
        elif opcion == len(entrenador_escogido.objetos) + 2:
            return salir()
class Entrenador:
    def __init__(self,nombre,energia):
        self.nombre = nombre
        self._energia = int(energia)
        self.programones = list()
        self.objetos = list()
    @property
    def energia(self):
        return self._energia
    @energia.setter
    def energia(self,x):
        if self._energia - x < 0:
            self._energia = 0
        else:
            self._energia -= x
    def estado_entrenador(self):
        pass
    def crear_objetos(self):
        print(f'[1] Baya')
        print(f'[2] Poción')
        print(f'[3] Caramelo')
        print(f'[4] Volver')
        print(f'[5] salir')
        a = int(input())
        objetos = LigaProgramon().abrir_objetos()
        if a == 1:
            for e in objetos:
                if e.tipo == 'baya':
                    if e not in self.objetos:
                        b = random(0,1)
                        if b > PROB_EXITO_BAYA:
                            self.objetos.append(e)
                            self._energia -= GASTO_ENERGIA_BAYA
        if a == 2:
            for e in objetos:
                if e.tipo == 'pocion':
                    if e not in self.objetos:
                        b = random(0,1)
                        if b > PROB_EXITO_POCION:
                            self.objetos.append(e)
                            self._energia -= GASTO_ENERGIA_POCION
        if a == 3:
            for e in objetos:
                if e.tipo == 'caramelo':
                    if e not in self.objetos:
                        b = random(0,1)
                        if b > PROB_EXITO_CARAMELO:
                            self.objetos.append(e)
                            self._energia -= GASTO_ENERGIA_CARAMELO
        if a == 4:
            return LigaProgramon.menu_de_inicio(self)
        if a == 5:
            return salir()
class Objetos(ABC):
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.costo = 0 #arreglar despues
        self.prob_de_exito = 0 #ver despues
        self.tipo = tipo
    @abstractmethod
    def aplicar_objeto(self,objeto):
        pass
class Baya(Objetos):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        pass
    def aplicar_objeto(self, objeto):
        super().aplicar_objeto(objeto)
class Pocion(Objetos):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        pass
    def aplicar_objeto(self, objeto):
        super().aplicar_objeto(objeto)
class Caramelo(Objetos):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        pass
    def aplicar_objeto(self, objeto):
        super().aplicar_objeto(objeto)       
class Programones(ABC):
    def __init__(self, no, ni, vi, ata, de, vel):
        self.nombre = no
        self.nivel = int(ni)
        self._vida = int(vi)
        self._ataque = int(ata)
        self._defensa = int(de)
        self._velocidad = int(vel)
        self._experiencia = 0
        self.aumento_de_nivel = False
    @property
    def vida(self): #no puede ser mayor a 255
        print(f'La vida a aumentado a {self._vida}')
        return self._vida
    @vida.setter
    def vida(self,p):
        if (self._vida + p) > 255:
            self._vida = 255
        else:
            print(f'Aumento vida: {p}')
            self._vida += p
    @property
    def ataque(self):
        print(f'el ataque ha aumentado a {self._ataque}')
        return self._ataque
    @ataque.setter
    def ataque(self,p):
        if (self._ataque + p) > 190:
            self._ataque = 190
        else:
            print(f'Aumento ataque: {p}')
            self._ataque += p
    @property
    def defensa(self):
        print(f'La defensa ha aumentado a {self._defensa}')
        return self._defensa
    @defensa.setter
    def defensa(self,p):
        if (self._defensa + p) > 250:
            self._ataque = 250
        else:
            print(f'Aumento defensa: {p}')
            self._ataque += p
    @property
    def velocidad(self):
        print(f'La velocidad ha aumentado a {self._velocidad}')
        return self._velocidad
    @velocidad.setter
    def velocidad(self,p):
        if (self._velocidad + p) > 250:
            self._velocidad = 250
        else:
            print(f'Aumento velocidad: {p}')
            self._velocidad += p 
    @property
    def experiencia(self):
        print(f'La experiencia de {self.nombre} a aumentado a {self._experiencia}')
        return self._experiencia
    @experiencia.setter
    def experiencia(self,aumento):
        if (self._experiencia + aumento) > 100:
            self._experiencia = 0
            self.nivel += 1
            self.aumento_de_nivel = True
        else:
            self._experiencia += aumento
    @abstractmethod
    def entrenamiento(self):
        pass
    @abstractmethod
    def luchar(self,oponente):
        pass 
class TipoPlanta(Programones):
    def __init__(self, no, ti, ni, vi, ata, de, vel):
        super().__init__(no, ni, vi, ata, de, vel)
        self.tipo = ti
        self.xp = 0
    def entrenamiento(self):
        super().entrenamiento()
        aumento = randint(MIN_AUMENTO_EXPERIENCIA,MAX_AUMENTO_EXPERIENCIA)
        self.experiencia += aumento
        if self.aumento_de_nivel == True:
            aumento_atributos = randint(MIN_AUMENTO_ENTRENAMIENTO,MAX_AUMENTO_ENTRENAMIENTO)
            self._vida += aumento_atributos
            self._ataque += aumento_atributos
            self._defensa += aumento_atributos
            self._velocidad += aumento_atributos
            self.aumento_de_nivel = False
    def luchar(self,oponente):
        super().luchar(oponente)
        if oponente.tipo == 'fuego':
            ventaja_de_tipo = -1
            ventaja_de_tipo_oponente = 1
        else:
            ventaja_de_tipo = 1
            ventaja_de_tipo_oponente = -1
        perdedor = ''
        puntaje_de_victoria = max(0,(self._vida*0.2 + self.nivel * 0.3 + self._defensa * 0.15 + self._velocidad*0.2 + ventaja_de_tipo * 40))
        puntaje_de_victoria_oponente =  max(0,(oponente._vida*0.2 + oponente.nivel * 0.3 + oponente._defensa * 0.15 + oponente._velocidad * 0.2 + ventaja_de_tipo_oponente * 40))
        if puntaje_de_victoria > puntaje_de_victoria_oponente:
            ganador = self
            perdedor = oponente
            ganado = True
            return ganador, perdedor, ganado
        elif puntaje_de_victoria < puntaje_de_victoria_oponente:
            ganador = oponente
            perdedor = self
            ganado = False
            return ganador, perdedor, ganado
        else:
            ganador = choice(self, oponente)
            if ganador == self:
                ganado = True
            else:
                ganado = False
class TipoFuego(Programones):
    def __init__(self, no, ti, ni, vi, ata, de, vel):
        super().__init__(no, ni, vi, ata, de, vel)
        self.tipo = ti
        self.xp = 0
    def entrenamiento(self):
        aumento = randint(MIN_AUMENTO_EXPERIENCIA,MAX_AUMENTO_EXPERIENCIA)
        self.experiencia += aumento
        if self.aumento_de_nivel == True:
            aumento_atributos = randint(MIN_AUMENTO_ENTRENAMIENTO,MAX_AUMENTO_ENTRENAMIENTO)
            self._vida += aumento_atributos
            self._ataque += aumento_atributos
            self._defensa += aumento_atributos
            self._velocidad += aumento_atributos
            self.aumento_de_nivel = False
        return super().entrenamiento()
    def luchar(self, oponente):
        super().luchar(oponente)
        if oponente.tipo == 'agua':
            ventaja_de_tipo = -1
            ventaja_de_tipo_oponente = 1
        else:
            ventaja_de_tipo = 1
            ventaja_de_tipo_oponente = -1
        perdedor = ''
        puntaje_de_victoria = max(0,(self._vida*0.2 + self.nivel * 0.3 + self._defensa * 0.15 + self._velocidad * 0.2 + ventaja_de_tipo * 40))
        puntaje_de_victoria_oponente =  max(0,(oponente._vida*0.2 + oponente.nivel * 0.3 + oponente._defensa * 0.15 + oponente._velocidad*0.2 + ventaja_de_tipo_oponente * 40))
        if puntaje_de_victoria > puntaje_de_victoria_oponente:
            ganador = self
            perdedor = oponente
            ganado = True
            return ganador, perdedor, ganado
        elif puntaje_de_victoria < puntaje_de_victoria_oponente:
            ganador = oponente
            perdedor = self
            ganado = False
            return ganador, perdedor, ganado
        else:
            ganador = choice(self, oponente)
            if ganador == self:
                ganado = True
            else:
                ganado = False
class TipoAgua(Programones):
    def __init__(self, no, ti, ni, vi, ata, de, vel):
        super().__init__(no, ni, vi, ata, de, vel)
        self.tipo = ti
        self.xp = 0
    def entrenamiento(self):
        aumento = randint(MIN_AUMENTO_EXPERIENCIA,MAX_AUMENTO_EXPERIENCIA)
        self.experiencia += aumento
        if self.aumento_de_nivel == True:
            aumento_atributos = randint(MIN_AUMENTO_ENTRENAMIENTO,MAX_AUMENTO_ENTRENAMIENTO)
            self._vida += aumento_atributos
            self._ataque += aumento_atributos
            self._defensa += aumento_atributos
            self._velocidad += aumento_atributos
            self.aumento_de_nivel = False
        return super().entrenamiento()
    def luchar(self,oponente):
        super().luchar(oponente)
        if oponente.tipo == 'planta':
            ventaja_de_tipo = -1
            ventaja_de_tipo_oponente = 1
        else:
            ventaja_de_tipo = 1
            ventaja_de_tipo_oponente = -1
        perdedor = ''
        puntaje_de_victoria = max(0,(self._vida*0.2 + self.nivel * 0.3 + self._defensa * 0.15 + self._velocidad + ventaja_de_tipo * 40))
        puntaje_de_victoria_oponente =  max(0,(oponente._vida*0.2 + oponente.nivel * 0.3 + oponente._defensa * 0.15 + oponente._velocidad * 0.2 + ventaja_de_tipo_oponente * 40))
        if puntaje_de_victoria > puntaje_de_victoria_oponente:
            ganador = self
            perdedor = oponente
            ganado = True
            return ganador, perdedor, ganado
        elif puntaje_de_victoria < puntaje_de_victoria_oponente:
            ganador = oponente
            perdedor = self
            ganado = False
            return ganador, perdedor, ganado
        else:
            ganador = choice(self, oponente)
            if ganador == self:
                ganado = True
            else:
                ganado = False
if __name__ == '__main__':
    liga = LigaProgramon()
    def salir():
        print('Gracias por jugar Liga Programon!!!')
        print('Quieres jugar de nuevo?')
        a = input()
        if a.lower() == 'si':
            return jugar_de_nuevo()
        return
    def jugar_de_nuevo():
        liga = LigaProgramon()




