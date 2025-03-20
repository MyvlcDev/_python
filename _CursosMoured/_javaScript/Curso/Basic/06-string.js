let myname= "Chato"
let greeting = "Hola, " + myname + " !"

console.log(greeting)
console.log(typeof greeting)
console.log(greeting.length)
console.log(greeting[1])
console.log(greeting[5])


console.log(greeting.toUpperCase())
console.log(greeting.toLowerCase())
console.log(greeting.indexOf("Chato"))
console.log(greeting.indexOf("Hola"))
console.log(greeting.indexOf("Lucas"))

console.log(greeting.includes("Chato"))
console.log(greeting.includes("Hola"))
console.log(greeting.includes("Lucas"))
console.log(greeting.slice(0,10 )) 
console.log(greeting.replace("Chato", "Vicente"))

let email = "xsync80@xsync80.com"

console.log(`Hola, ${myname}! Tu email es ${email} `) // se hace con el acento