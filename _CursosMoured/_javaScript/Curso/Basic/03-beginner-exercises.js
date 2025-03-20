
// 1. Escribe un comentario en una lÃ­nea.

//  Comentario de linea


// 2. Escribe un comentario en varias lÃ­neas.

/*
 comentario de varias lineas
 como ves en este ejemplo

*/



// 3. Declara variables con valores asociados a todos los datos de tipo primitivos.

let numero = 100; // Number
let texto = "Hola, mundo"; // String
let esVerdadero = true; // Boolean
let valorIndefinido; // Undefined
let valorNulo = null; // Null
let objetoPersona = { nombre: "Carlos", edad: 28 }; // Object
let listaNumeros = [1, 2, 3, 4, 5]; // Array

let simboloUnico = Symbol('id'); // Symbol
let numeroGrande = BigInt(9007199254740991); // BigInt



// 4. Imprime por consola el valor de todas las variables.

console.log(texto);
console.log(esVerdadero);
console.log(valorIndefinido);
console.log(valorNulo);
console.log(objetoPersona);
console.log(listaNumeros);
console.log(simboloUnico);
console.log(numeroGrande);


// 5. Imprime por consola el tipo de todas las variables.


console.log(typeof texto)
console.log(typeof esVerdadero)
console.log(typeof valorIndefinido)
console.log(typeof valorNulo)
console.log(typeof objetoPersona)
console.log(typeof listaNumeros)
console.log(typeof simboloUnico)
console.log(typeof numeroGrande)

// 6. A continuaciÃ³n, modifica los valores de las variables por otros del mismo tipo.

numero= 200
texto ="Adios"

// 7. A continuaciÃ³n, modifica los valores de las variables por otros de distinto tipo.


stringVar = 1000
numberVar = "Brais Moure"
booleanVar = "true"
nullVar = BigInt(1234567890123456)
undefinedVar = false
bigIntVar = 3.14159
symbolVar = null

// 8. Declara constantes con valores asociados a todos los tipos de datos primitivos.
const constString = "Soy una constante"
const constNumber = 37
const constBoolean = false
const constNull = null
const constUndefined = undefined
const constBigInt = BigInt(789654123)
const constSymbol = Symbol("constantSymbol")
// 9. A continuaciÃ³n, modifica los valores de las constantes.

console.log("no se puede modificar una constante  "  )

// 10. Comenta las lÃ­neas que produzcan algÃºn tipo de error al ejecutarse.consol


console.log(5+"5")

