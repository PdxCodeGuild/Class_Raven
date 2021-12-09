const x = 5
// console.log(x)
// x = 6

//var - gets global scope
//let - block scope
if (2 < 10) {
  var z = 10
  let y = 11
}
// console.log(z)
// console.log(y)

// Datatypes
let a = 5 // number
let b = 10.5 // number
let c = 'Hello' // string
let d = true // boolean
let e = null // null
let f // undefined
let fruits = ['apple', 'banana', 'orange'] // arrays
fruits[0] = 'pear'
// console.log(fruits) // [ "pear", "banana", "orange" ]
let person = {
  firstName: 'John',
  lastName: 'Doe',
  age: 46
}

// access values within objects
let key = 'firstName'
console.log(person['firstName'])
console.log(person[key])
console.log(person.firstName)



// pre/post increment
// console.log(a)
// console.log('my number is ' + a++)
// console.log('my number is ' + ++a)

// Math module
// Math.floor()
// Math.abs() // absolute value
// console.log(Math.random()) // random number between 0 - 1
// console.log(Math.random() * 100) // random number between 0 - 100



// random element from array
fruits = ['apple', 'banana', 'orange']

// generate random index
let randomIndex = Math.floor(Math.random() * fruits.length)
console.log(randomIndex, fruits[randomIndex])

// conditional statements
var number = 7
// if(number < 10){
//   console.log('x is less than 10')
// }

// logical operators &&, ||, !
// if(number < 10 && number > 5){
//   console.log('x is less than 10 and greater than 5')
// }

var game_on = false
// console.log(!game_on) // true - ! not

// beware of type coersion
// == vs ===

// == allows type coersion
// console.log(5 == '5') // true
// console.log(5 == 5) // true

// === doesn't allow type coersion
// console.log(5 === '5')
// console.log(5 === 5)

var temp = 90
// if(temp < 60){
//   console.log('cold')
// } else if(temp < 80){
//   console.log('warm')
// } else {
//   console.log('hot')
// }

// strings

// template literals
// console.log(`It is ${temp} degrees outside today.`)
// console.log('hello' + 'world')

// arrays
var numbers = [11, 22, 33]

numbers.push(44) //  add to the end of the array
numbers.unshift(77)

// console.log(numbers.length)
// console.log(numbers)

// loops
var i = 0
while (i < 10) {
  i++
  // console.log(i)
}

// for loops
// for(initialization; condition; increment)
for (let i = 0; i < 10; i++) {
  // console.log(i)
}

// iterate over a string or array
let string = 'hello'
i = 0
while (i < string.length) {
  // console.log(string[i])
  i++
}

for (let i = 0; i < string.length; i++) {
  // console.log(string[i])
}

// for-in iterates over the indices of the string
for (i in string) {
  // console.log(string[i])
}

// for-of iterates over the characters of the string
for (let char of string) {
  // console.log(char)
}

// functions
function add (a, b) {
  return a + b
}
// console.log(add(1,2)) // 3

// console.log(subtract(10, 5)) // error! function not defined
const subtract = function (a, b) {
  return a - b
}
// console.log(subtract(10, 5)) // 5

let firstName = prompt('What is your name?')
alert(firstName)
