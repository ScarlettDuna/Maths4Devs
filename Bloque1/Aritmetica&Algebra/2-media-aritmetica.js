// Dada una lista de números, devuelve su media aritmética.
const numeros = [10, 20, 30, 40, 50];
let total = 0;
for (let i = 0; i < numeros.length; i++) {
    total += numeros[i]
}
let media = total / numeros.length
console.log(media)