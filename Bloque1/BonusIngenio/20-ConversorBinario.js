// Dado un número, devuelve su representación en binario sin usar funciones predefinidas.
function convertirBinario(numero){
    if (numero === 0) return "0";
    let binNum = ""
    while (numero > 0){
        let div = numero % 2
        binNum = div + binNum 
        numero = Math.floor(numero / 2)
    }
    return binNum
}
console.log(convertirBinario(255))