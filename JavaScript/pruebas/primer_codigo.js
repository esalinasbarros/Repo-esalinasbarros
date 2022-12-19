function primo(numero) {
    var cont = 0;
    for (let i = 1; i < numero + 1; i++) {
        if (numero % i === 0) {
            cont++;
        }
    }
    if (cont > 2) {
        return false;
    }
    else {
        return true;
    }
}
console.log(primo(11))

//Ciclo while
function utilizar_while() {
    var cont = 0;
    while (cont < 1000000) {
        cont++
        console.log(cont)
    }
}
utilizar_while()
console.log('termino')
