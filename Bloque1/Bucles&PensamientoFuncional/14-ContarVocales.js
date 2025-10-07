// Dada una cadena de texto, devuelve la cantidad de vocales.
const palabra = "javascript";
let contador = 0
const vocales = ["a", "e", "i", "o", "u"]

palabra.split("").forEach(letra => {
    if (vocales.includes(letra.toLowerCase())) contador ++;
})
console.log(`La palabra ${palabra} tiene ${contador} vocales`)