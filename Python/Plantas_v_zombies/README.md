# Tarea 2: DCCruz vs Zombies :zombie::seedling::sunflower:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<La tarea esta bugueada, al pasar de ronda los labels no se actualizan bien, no hay colision entre los guisantes y los zombies, ni de los zombies con las plantas, pero estos
si caminan, los guisantes se mueves, y cada planta cumple con su funcion, de disparar, dar soles, etc. La ventana del ranking no guarda los nombres de los usuarios y sus puntajes, ya que al no poder perder de manera legitima, es imposible calcular el puntaje. Sin embargo hay aspectos que funcionan bien, como los botones, la conexion entre ventanas, la interaccion con el usuario, etc.>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Ventanas: 39 pts (40%)
##### ✅ Ventana de Inicio
##### ❌ Ventana de Ranking
##### ✅ Ventana principal
##### ✅ Ventana de juego	
##### 🟠 Ventana post-ronda #No se suman bien los labels al pasar de ronda
#### Mecánicas de juego: 46 pts (47%)			
##### 🟠 Plantas
##### 🟠 Zombies
##### ✅ Escenarios		
##### 🟠 Fin de ronda	
##### 🟠 Fin de juego	
#### Interacción con el usuario: 22 pts (23%)
##### ✅ Clicks	
##### ❌ Animaciones
#### Cheatcodes: 8 pts (8%)
##### ✅ Pausa
##### ✅ S + U + N
##### 🟠 K + I + L #Al apretar, aparece que es la ronda 10 y se buguea el juego completamente
#### Archivos: 4 pts (4%)
##### ✅ Sprites
##### ✅ Parametros.py
##### ✅ K + I + L
#### Bonus: 9 décimas máximo
##### ❌ Crazy Cruz Dinámico
##### ❌ Pala
##### ❌ Drag and Drop Tienda
##### ❌ Música juego
##### Nota: tuve que hacer una ventana para el escenario de dia y otra para el escenario de noche, por lo tanto las seńales se repiten mucho en el modulo DCCruz_v_Zombies.py
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```puntajes.txt``` en ```T2```



## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: ```setupUi, loadUitype, Qpixmap, QLabel, pyqtSignal, setPixmap, QObject, QTimer / frontend y backend ``` (debe instalarse)
2. ```random```: ```randint, choice / logica_juego.py ```
3. ```time```: ```sleep / ventana_juego_dia.py y ventana_juego_noche.py ```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```DCCruz```: Contiene a ```Todas las clases del backend y el frontend```, (ser general, tampoco es necesario especificar cada una)...
2. ```frontend```: Se encarga de implementar objectos al programa para que el usuario pueda interactuar con estos. Contiene cada ventana creada en Qt Designer 
3. ```backend```: Se encarga de conectar las ventanas entre si, los botones y de validar la interaccion entre el usuario y el juego. Es decir, las mecanicas del juego
4. ```elementos.py```: Contiene a cada elemento que hay en el juego, desde los zombies hasta los guisantes.
## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Los soles se deben mover al aparecer/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <La Tarea esta muy bugueada en algunos aspectos!! Ademas Los zombies al llegar al final del mapa a veces gatillan una perdida pero a veces no, esto depende de lo que este plantado (no se porque)>


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
1. \<Modulo logica_inicio.py linea(26, 32) https://coderslegacy.com/python/pyqt5-qmessagebox/ >



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
