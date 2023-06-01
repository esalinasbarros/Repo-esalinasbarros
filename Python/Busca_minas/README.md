# Tarea 0: Star Advanced 🚀🌌


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores
#### Programación Orientada a Objetos (18pts) (22%%)
##### 🟠 Menú de Inicio
##### 🟠 Funcionalidades		
##### 🟠 Puntajes
##### Nota: No utilize OOP para programar esta parte del juego, pero su funcionalidad es completa y correcta, por eso elegi 🟠. #####
#### Flujo del Juego (30pts) (36%) 
##### ✅ Menú de Juego
##### ✅ Tablero		
##### ✅ Bestias	
##### ✅ Guardado de partida		
#### Término del Juego 14pts (17%)
##### ✅ Fin del juego	
##### ✅ Puntajes	
#### Genera: 15 pts (15%)
##### ✅ Menús
##### ✅ Parámetros
##### 🟠 PEP-8
#### Bonus: 3 décimas
##### ❌ 
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```puntajes.txt``` en ```T0```
2. ```usuario.txt``` en ```T0/partidas```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```os```: ```os.path.join() / main.py: os.path.isfile() / main.py``` (debe instalarse)
2. ```random```: ```shuffle() / main.py ``` (debe instalarse)
3. ```string```: ```ascii_lowercase(); as L / main.py ``` (debe instalarse)
4. ```tablero```: ```print_tablero() / main.py ```
5. ```parametros```: ```POND_PUNT, PROB_BESTIA / main.py ```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```No se crearon modulos adicionales, el codigo se ejecuta 100% en el modulo main.py```



## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Supuse que el archivo puntajes.txt puede partir con mi nombre y mi puntaje, esto es ya que al crear el archivo y agregar un '\n' es bastante mas simple el proceso de guardar o printear los resultados> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>


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
1. \<https://www.w3schools.com/python/python_file_write.asp>: este hace \<crea un archivo con el nombre de usuario correspondiente> y está implementado en el archivo <main.py> en las líneas <190-194> y hace <explicación breve de que hace>
<Se busco en internet como crear un archivo>
2. \<https://es.stackoverflow.com/questions/213125/existe-una-manera-simple-de-convertir-una-lista-de-tipo-str-a-una-de-tipo-int><Pasa una lista de numeros en formato str() a una lista de numeros int()><linea 38 y 40, y linea 214>


## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/Syllabus/blob/master/Tareas/Descuentos.md).
