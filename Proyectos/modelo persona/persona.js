class Persona {
    constructor(edad, nombre, apellido, rut, sexo, tipo_sangre, direccion, comuna) {
        this.edad = edad;
        this.nombre = nombre;
        this.apellido = apellido;
        this.rut = rut;
        this.sexo = sexo;
        this.tipoSanguineo = tipo_sangre;
        this.direccion = direccion;
        this.comuna = comuna;
    }
    get age() {
        return this.age;
    }
    set age(age) {
        if (age < 0) {
            this.age = 0;
        } else {
            this.age = age;
        }
    }
    hablar(str) {
        console.log(this.name + "dijo" + str);
    }
    cambioDeDireccion(nueva_dir) {
        this.direccion = nueva_dir;
    }
}
let eduardo = new Persona(5, "Eduardo", "Salinas", 211518014, "hombre", "AB+", "Camino la loica 5054", "Lo barnechea")

class Skater {
    constructor(trucos, tabla, preferencia, persona) {
        this.trucos = trucos;
        this.tabla = tabla
        this.preferencia = preferencia;
        this.persona = persona
    }
    hacerTruco(truco) {
        console.log(this.name + "hizo un" + truco)
    }
}

let edo = new Skater(["flip", "ollie"], "pill", 8.25)












