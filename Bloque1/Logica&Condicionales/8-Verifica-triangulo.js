// Verifica si tres longitudes pueden formar un triángulo válido.
/* la suma de las longitudes de dos lados cualesquiera siempre debe ser mayor que la longitud del tercer lado (Teorema de la Desigualdad Triangular) */

function teoDesigualdadTriangular(lado1, lado2, lado3) {
    if (lado1 + lado2 < lado3 || lado3 + lado2 < lado1 || lado1 + lado3 < lado2) {
        console.log("No pueden formar un triangulo");
    } else {
        console.log("Sí pueden formar un triángulo")
    }
}
teoDesigualdadTriangular(3, 4, 5)
teoDesigualdadTriangular(2, 3, 10)