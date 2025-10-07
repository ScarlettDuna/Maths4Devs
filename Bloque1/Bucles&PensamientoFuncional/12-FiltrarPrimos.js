// Filtra los números primos de una lista.
let numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let primos = numeros.filter(num => {
    if (num === 1) return false;
    if (num === 2 || num === 3) return true;

    for (let i = 2; i <= num / 2; i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
});
console.log(primos)