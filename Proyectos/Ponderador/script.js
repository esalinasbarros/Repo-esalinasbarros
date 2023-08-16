document.addEventListener('DOMContentLoaded', function () {
    // your code will go here
    const botonMas = document.querySelector('#mas');
    const wapper = document.querySelector('.wapper');
    botonMas.addEventListener('click', function () {
        const elementosX = document.querySelectorAll('.nota-y-p');
        const nuevoDiv = document.createElement('div');
        const longitud = elementosX.length + 1;
        nuevoDiv.classList.add('nota-y-p', 'trans');
        nuevoDiv.innerHTML = `<input type="text" id="nota${longitud}" placeholder="Ingrese nota ${longitud}">` +
        `<input type="text" id="porcentaje${longitud}" placeholder="Porcentaje de ponderacion" min="0" max="100">`

        botonMas.insertAdjacentElement('beforebegin', nuevoDiv);
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const botonCalcular = document.querySelector('.boton-calcular');
    botonCalcular.addEventListener('click', function () {
        const elementos = document.querySelectorAll('.nota-y-p');
        const notas = [];
        const notaAprobacion = document.querySelector('#nota-aprobacion').value;
        if (notaAprobacion === NaN) {
            notaAprobacion = 40;
        }
        let suma = 0;
        elementos.forEach(elemento => {
            //const nota = parseInt(document.querySelector(`#${elemento.id} input[type="text"]`).value);
            const nota = parseInt(document.querySelector(`#nota${elemento.id + 1}`).value);
            const porcentaje = parseInt(document.querySelector(`#porcentaje${elemento.id + 1}`).value);
            const notaPonderada = nota * (porcentaje / 100);
            notas.push(notaPonderada);
        });
        //const suma = notas.reduce((a, b) => a + b, 0);
        console.log(notas);
        for (let i = 0; i < notas.length; i++) {
           suma += notas[i];
        }
        const resultado = document.querySelector('.nota-total');
        resultado.textContent = suma.toString();
        if (resultado.textContent == 'NaN') {
            resultado.textContent = 'Ingrese notas y ponderaciones!';
        }
        if (suma >= notaAprobacion) {
            resultado.style.color = 'green';
        }else{
            resultado.style.color = 'red';
        }
    });
});
