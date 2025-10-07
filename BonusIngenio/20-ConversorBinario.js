// Dado un número, devuelve su representación en binario sin usar funciones predefinidas.
function convertirBinario(numero){
    let binNum = ""
    while (numero > 1){
        let div = numero % 2
        binNum = div + binNum 
        numero = Math.floor(numero / 2)
    }
    binNum = numero + binNum
    return binNum
}
console.log(convertirBinario(255))