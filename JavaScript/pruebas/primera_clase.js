
class Persona {
    constructor(edad, nombre, sexo, altura, x, y, peso) {
        this.edad = edad;
        this.nombre = nombre;
        this.sexo = sexo;
        this.altura = altura;
        this.posX = x;
        this.posY = y;
        this.peso = peso
    }
    hablar() {
        console.log(`${this.nombre} esta hablando`)
    }
    caminar(x, y) {
        this.posX += x
        this.posY += y
        this.peso -= 0.2
    }

}


