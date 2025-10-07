// Determina si un número entero es múltiplo de 3, 5 o ambos.
let number = prompt("Introduce un número para saber si es multiplo de 3, de 5 o de ambos")
number = Number(number)
if (isNaN(number)) {
    console.log("Error: no has introducido un número");
} else if (number % 3 === 0 && number % 5 === 0) {
    console.log("Es divisible entre 3 y 5");
} else if (number % 3 === 0) {
    console.log("Es divisible entre 3");
} else if (number % 5 === 0) {
    console.log("Es divisible entre 5");
} else {
    console.log("Numero no divisible entre 3 o 5");
}