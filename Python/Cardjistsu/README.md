# Tarea 3: DCCard-Jitsu 🐧🥋


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Mi tarea tiene algunos bugs, como cuando se salen los clientes de la sala de espera, y tratan de volver a entrar el programa tira un error. No pude crear los timers, asi que en vez de usar estos hay unos botones de confirmacion los cuales deben ser apretados por ambos jugadores para iniciar la partida o la ronda (para facilitar la correccion), sin embargo esto trae como consecuencia que una ronda puede durar infinito si esque el otro jugador no confirma su carta. Cuando realemente hay un error, el programa lo reconoce y lo muestra. Por ultimo, no hay cola de espera. El resto deberia funcionar bien, los jugadores púeden elegir cartas, la sala de espera se llena y se vacia correspondientemente, se pueden ganar fichas, y se puede ganar o perder la partida>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Networking: 26 pts (19%)
##### ✅ Protocolo	
##### ✅ Correcto uso de sockets		
##### ✅ Conexión	
##### ✅ Manejo de Clientes	
##### 🟠 Desconexión Repentina ## en general funciona bien, pero tiene errores
#### Arquitectura Cliente - Servidor: 31 pts (23%)			
##### ✅ Roles			
##### 🟠 Consistencia ## A veces se pierde el flujo del programa y no recibe muy bien los mensajes		
##### ✅ Logs ## Nota: no estan muy ordenados, pero mustran la informacion necesaria de lo que esta pasando con el programa
#### Manejo de Bytes: 27 pts (20%)
##### ✅ Codificación			
##### ✅ Decodificación			
##### ✅ Encriptación		
##### ✅ Desencriptación	
##### ✅ Integración
#### Interfaz Gráfica: 27 pts (20%)	
##### ✅ Ventana inicio		
##### ✅ Sala de Espera			
##### ✅ Ventana de juego							
##### ✅ Ventana final
#### Reglas de DCCard-Jitsu: 17 pts (13%)
##### ✅ Inicio del juego			
##### ✅ Ronda				
##### ✅ Termino del juego
#### Archivos: 8 pts (6%)
##### ✅ Parámetros (JSON)		
##### ✅ Cartas.py	
##### ✅ Cripto.py
#### Bonus: 8 décimas máximo
##### ❌ Cheatcodes	
##### ❌ Bienestar	
##### ❌ Chat

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```main.py``` en ```Cliente```
2. ```main.py``` en ```Servidor```
3. Nota: se deben ejecutar ambos por separado, es decir en distintos terminales
4. Nota: los archivos ya estan creados


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: ```(pyqtSignal, QObject) en Cliente/cliente.py e interfaz.py, (QApplication) en  cliente/main.py``` (debe instalarse)
2. ```PyQt5```: ```(pyqtSignal, QApplication, QPixmap, QMessageBox, uic) en cliente/frontend/(ventana_inicio.py, ventana_espera.py, ventana_juego.py)``` (debe instalarse)
3. ```json```: ```servidor/server.py, servidor/utils.py, cliente/backend/cliente.py``` 
4. ```random```: ```shuffle: cliente/backend/interfaz.py```
5. ```socket```: ```servidor/server.py, cliente/backend/cliente.py```
6. ```threading```: ```Thread y activeCount: servidor/server.py, cliente/backend/cliente.py```
7. ```math```: ```ceil: servidor/cripto.py, cliente/cripto.py```
8. ```sys```: ```servidor/(server.py, main.py), cliente/main.py, cliente/backend/cliente.py, cliente/frontend/(ventana_inicio.py, ventana_espera.py, ventana_juego.py)```
9. ```collections```: ```deque(): servidor/logica.py```
10. ```time```: ```sleep: cliente/backend/interfaz.py```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```cliente/backend```: Contiene a ```Interfaz```, ```Client```, (interpreta los mensajes del servidor y actualiza la interfaz de acuerdo a estos)...
2. ```cliente/frontend```: Contiene a ```SalaEspera```, ```VentanaInicio```, ```VentanaJuego``` Hecha para <interactuar con el usaurio>
3. ```cliente/frontend/assets```: Contiene a ```ventana_inicio_T3.ui```, ```sala_espera_T3.ui```, ```ventana_juego_T3.ui```, ```ventana_final.ui``` Son los archivos que corresponden a la interfaz
4. ```cliente/frontend/assets```: contiene todos los archivos que corresponden a las fotos que el usuario ve en el juego
5. ```cliente/parametros.json```: contiene los parametros que utiliza el programa
6. ```cliente/utils.py```: permite acceder a los parametros mediante la funcion ```data_json```, Nota: funcion sacada de la Actividad formativa 3
7. ```(cliente, servidor/(cripto.py, cartas.py)```: cripto.py encripta y desencripta los mensajes intercambiados entre el servidor y los clientes mediante las funciones ```encriptar, desencriptar``` y cartas.py entrega las cartas a los clientes que estan jugando mediante la funcion ```get_penguins```
8. ```cliente```: Contiene a ```main.py```, archivo a ejecutar
9. ```servidor```: Contiene a ```main.py```, archivo a ejecutar
10. ```servidor```: Contiene a ```Server``` y ```DataBase```, server actualiza a los clientes de manera asincronca y database almacena los datos de cada cliente
11. ```servidor/parametros.json```: contiene los parametros que utiliza el programa
2. ```servidor/utils.py```: permite acceder a los parametros mediante la funcion ```data_json```, Nota: funcion sacada de la Actividad formativa 3

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <La comunicacion entre el servidor y los clientes sera unicamente mediante diccionarios ya que facilita el proceso de procesamiento de mensajes> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...




-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<https://coderslegacy.com/python/pyqt5-qmessagebox/>: este hace \<es una casilla que advierte al usuario si el nombre que escogio esta bien o mal> y está implementado en el archivo <ventana_inicio.py> en las líneas <20 a 27>
2. \<https://coderslegacy.com/python/pyqt5-qmessagebox/>: este hace \<es una casilla que advierte al usuario si no escoge una carta> y está implementado en el archivo <ventana_juego.py> en las líneas <96 a 101>
3. \<https://coderslegacy.com/python/pyqt5-qmessagebox/>: este hace \<Le avisa al usuario que el servidor se desconecto> y está implementado en el archivo <interfaz.py> en las líneas <170 a 175>
4. \<https://note.nkmk.me/en/python-dict-get-key-from-value/>: este hace \<retorna la key de un value en un diccionario> y está implementado en el archivo <logica.py> en las líneas <189 y 190>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
