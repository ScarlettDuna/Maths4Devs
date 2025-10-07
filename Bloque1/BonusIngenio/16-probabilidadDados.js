// Simula el lanzamiento de dos dados y calcula la probabilidad de obtener 7.
/* Cada dado tiene 6 caras, por lo que en teoria la probabilidad de caer en cada cara es de 1/6 Para que se den 7 hay varias opcion 6+1, 5+2, 4+3 y vice versa. 
Eso quiere decir que de las 36 posibles combinaciones de caer de los dos dados, solo 6 dan 7. la probabilidad de sacar 7 es de 6/36 */

const n = 100_000
let contador = 0

for (let i = 0; i < n; i++) {
    let dado1 = Math.floor(Math.random() * 6) + 1
    let dado2 = Math.floor(Math.random() * 6) + 1
    if (dado1 + dado2 === 7) contador += 1
}

console.log(`Probabilidad ≈ ${(contador / n * 100).toFixed(2)}%`);
