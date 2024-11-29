let num1 = 10;
let num2 = 5;  
let operacion = "suma"; 

function realizarOperacion(num1, num2, operacion) {
    let resultado;

    if (operacion === "suma") {
        resultado = num1 + num2;
    } else if (operacion === "resta") {
        resultado = num1 - num2;
    } else if (operacion === "multiplicacion") {
        resultado = num1 * num2;
    } else if (operacion === "division") {
        if (num2 === 0) {
            return "Error: No se puede dividir entre cero";
        } else {
            resultado = num1 / num2;
        }
    } else {
        return "Operación no válida";
    }

    return resultado;
}
let continuar = true;

while (continuar) {
    num1 = parseFloat(prompt("Ingrese el primer número: "));
    num2 = parseFloat(prompt("Ingrese el segundo número: "));
    operacion = prompt("Ingrese la operación (suma, resta, multiplicacion, division): ");

    let resultado = realizarOperacion(num1, num2, operacion);

    alert("El resultado es: " + resultado);

    let respuesta = prompt("¿Desea realizar otra operación? (si/no): ").toLowerCase();

    if (respuesta !== "si") {
        continuar = false;
        alert("¡Hasta luego!");
    }
}