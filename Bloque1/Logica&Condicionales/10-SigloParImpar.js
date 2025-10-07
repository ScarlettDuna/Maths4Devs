// Dado un año, determina si pertenece a un siglo par o impar.
function sigloParImpar(anio) {
    let siglo = Math.ceil(anio / 100)
    if (siglo % 2 === 0) {
        return "El siglo es par"
    } else {
        return "El siglo es impar"
    }
}
console.log(sigloParImpar(2015))
// Consideración el año 2015 es siglo 21