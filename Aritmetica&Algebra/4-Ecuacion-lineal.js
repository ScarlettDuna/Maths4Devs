// Implementa una función que resuelva una ecuación lineal de la forma ax + b = 0.
function ecuacion_lineal(a, b){
    let x = - (b / a);
    return x; 
}
console.log(`La solución de "ax + b = 0" con a = 5 y b = 10 es ${ecuacion_lineal(5, 10)}`)