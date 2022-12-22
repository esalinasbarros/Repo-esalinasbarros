export default class Persona {
    constructor(edad, nombre, sexo, altura, x, y, peso) {
        this.edad = edad;
        this.nombre = nombre;
        this.sexo = sexo;
        this.altura = altura;
        this.posX = x;
        this.posY = y;
        this.peso = peso;
    }
    hablar(palabras) {
        console.log(`${this.nombre}: ${palabras}`);
    }
    caminar(x, y) {
        this.posX += x;
        this.posY += y;
        this.peso -= 0.2;
    }
    hacerDeporte(deporte, hrs) {
        calorias = 0;
        if (deporte == 'cardio') {
            calorias = 354 * hrs;
        } else {
            calorias = 400 * hrs;
        }
    }
    comer(comida) {
        console.log(`${this.nombre} esta comiendo ${comida}`); 
    }

}










