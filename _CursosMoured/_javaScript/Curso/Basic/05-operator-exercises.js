// 1. Crea una variable para cada operaciÃ³n aritmÃ©tica.
let a = 5
let b= 6

suma        =a+b
resta       =a-b
prod        =a*b
division    =a/b
mod         =a%b
exponente   =a**b             

// 2. Crea una variable para cada tipo de operaciÃ³n de asignaciÃ³n,
//  que haga uso de las variables utilizadas para las operaciones aritmÃ©ticas.

a -= resta // Resta con asignaciÃ³n
a *= prod // MultiplicaciÃ³n con asignaciÃ³n
a /= division // DivisiÃ³n con asignaciÃ³n
a %= mod // MÃ³dulo con asignaciÃ³n
a **= exponente

// 3. Imprime 5 comparaciones verdades con diferentes operadores de comparaciÃ³n.

console.log(7>5)
console.log(5<7)
console.log(5==5)
console.log(4!=5)
console.log(5>=4)

// 4. Imprime 5 comparaciones falsas con diferentes operadores de comparaciÃ³n.
console.log(7<5)
console.log(5>7)
console.log(5!=5)
console.log(4==5)
console.log(5==4)
// 5. Utiliza el operador lÃ³gico and.

console.log(5>3&&7>5)


// 6. Utiliza el operador lÃ³gico or.

console.log(5>3||7>5)

// 7. Combina ambos operadores lÃ³gicos.

console.log((5 > 3 && 10 > 5) || (5 < 3 && 10 > 5))


// 8. AÃ±ade alguna negaciÃ³n.

console.log(!5==7)

// 9. Utiliza el operador ternario.

let age = 18
let canVote = (age >= 18) ? "Puede votar" : "No puede votar"
console.log(canVote)

// 10. Combina operadores aritmÃ©ticos, de comparÃ¡ciÃ³n y lÃ³gicas.

let result = (5 + 3) * 2 > 10 && (4 * 2) === 8;
console.log(result)