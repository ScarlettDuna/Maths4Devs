// Crea una función que determine si una cadena es un palíndromo (se lee igual al derecho y al revés).
function palindromo(palabra) {
    let letras = palabra.split("")
    let mitad = Math.floor(letras.length / 2)
    let esPalindromo = true
    for (let i = 0; i < mitad; i++){
        if (letras[i] !== letras.at(-(i + 1))) {
            esPalindromo = false
        }
    }
    return esPalindromo
}


let palabra = "reconocer"
console.log(`¿La palabra "${palabra}" es palíndromo? ${palindromo(palabra)}`)