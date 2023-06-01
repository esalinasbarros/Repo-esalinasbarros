# Tarea 1: DCCampeonato 🏃‍♂️🏆


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<La tarea parte instanciado entrendadores, programones y objetos dentro de la LigaProgramon para que estos puedan interactuar entre si.
La clase principal contiene todos los menus del juego ya que tuve un problema al intentar separar los menus de las clases. Es por esto mismo que la extension del archivo flujo.py contiene mas de 400 lineas. Luego de instanciar se le da la opcion al usuario de elegir un entrenador, el cual utilizara durante todo el juego, puedes ir cambiando entre los programones que tiene tu entrenador para entrenarlos, alimentarlos, pealear, etc.>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Programación Orientada a Objetos (18pts) (22%%)
##### 🟠 Diagrama
##### ✅ Definición de clases, atributos, métodos y properties		
##### ✅ Relaciones entre clases
#### Preparación programa: 11 pts (7%)			
##### ✅ Creación de partidas
#### Entidades: 28 pts (19%)
##### ✅ Programón
##### ✅ Entrenador		
##### ✅ Liga	
##### 🟠 Objetos		
#### Interacción Usuario-Programa 57 pts (38%)
##### ✅ General	
##### ✅ Menú de Inicio
##### ✅ Menú Entrenador
##### ✅ Menu Entrenamiento
##### ✅ Simulación ronda campeonato
##### ✅ Ver estado del campeonato
##### ✅ Menú crear objeto
##### ✅ Menú utilizar objeto
##### ✅ Ver estado del entrenador
##### 🟠 Robustez
###### Nota: los menus no estan a prueba de errores ya que no tuve tiempo de hacerlo y las indentaciones estan corridas al elegir una opcion en los menus ######
#### Manejo de archivos: 12 pts (8%)
##### ✅ Archivos CSV
##### ✅ Parámetros
#### Bonus: 5 décimas
##### ❌ Mega Evolución
##### ❌ CSV dinámico

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```flujo.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. '''parametros.py'''


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```path / flujo.py```
2. ```abc```: ```ABC / flujo.py, abstractmethod / flujo.py``` (debe instalarse)
3. ```random```: ```randint, shuffle, choice, random / flujo.py```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```flujo.py```: Contiene a ```LigaProgramon```, ```Entrenador```, ```Programon```,```TipoFuego```,```TipoAgua```,```TipoPlanta```,```Objetos```, ```Baya```, ```Pocion```, ```Caramelo```
2. ```parametros.py```: Hecha para <Guardar parametros para luego utilizarlos en el flujo del juego>

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Al crear un objeto, se puede crear el primer objeto disponible al iterar el archivo objetos.csv> 
2. <Al perder con tu programon, pierde el entrenador que escogiste y por lo tanto pierdes el juego> 
3. <No se debe 'printear' el campeon, solo se mostrara si esque gana el usuario, el resto ocurre como si el usuario no supiera>
PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


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
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
