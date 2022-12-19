
class Persona {
    constructor(edad, nombre, sexo) {
        this.edad = edad;
        this.nombre = nombre;
        this.sexo = sexo;
    }
    hablar () {
        console.log(`${this.nombre} esta hablando`)
    }
}

class Skater extends Persona {
    constructor (edad, nombre , sexo) {
        super(edad, nombre, sexo)
        const fs = require('fs');
        fs.readFile('trucos.txt', 'utf-8', (err, data) => {
            if (err) {
                console.error(err);
                return;
            }
            else {
                this.trucos = data.split('\n')
            }
        })
    }
    hacerTruco(numeroDeTruco) {
        console.log(`${this.nombre} acaba de hacer un ${this.trucos[numeroDeTruco]}`)  
    }
    static comprobarTruco (truco) {
    }
}
Skater.hacerTruco(2)

