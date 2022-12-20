function primos(array) {
    for (let i = 0; i < array.lenght; i++) {
        let cont = 0
        for (let j = 0; j < array[i]; j++) {
            console.log("hola")
            if (array[i] % j == 0) {
                cont++}
        if (cont > 2) {
            console.log(array[i] + ": Es un numero primo")
            return primos(array);}
        else{
            console.log(array[i] + ": No es un numero primo")
            return primos(array);
        }}
    
    }
    return;
};

let numeros = primos([1,2,3,4,5,6,7,8,9,80,7,65,34,53,23,65,34,68,69,45,32,337,35,2342,536,56,423,5346,3,62,53,6])