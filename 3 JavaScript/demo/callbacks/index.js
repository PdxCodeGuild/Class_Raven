// function add(a, b){
//   return a + b
// }
// const add = function(a, b) {
//   return a + b
// }

// // arrow function
// const add = (a, b) => {
//   return a + b
// }

// // return value on same line
// const add = (a, b) => a + b

// Arrow functions are the same as lambda functions in python
// add = lambda x: x ** 2
// add(2)


// -----------------------------------
// Callback functions

function eat (food) {
  console.log(`Yum, ${food}!`)
}

function cook (ingredients, callbackFunction) {
  let food

  switch (ingredients) {
    case 'broth, noodles':
      food = 'soup'
      break
    case 'flour, butter, sugar':
      food = 'cookies'
      break
    case 'meat, lettuce, tomato, bun':
      food = 'burger'
      break
    default:
      food = 'what is that?'
      break
  }

  callbackFunction(food)
}

// cook('broth, noodles', eat)
// cook('flour, butter, sugar', eat)
// cook('meat, lettuce, tomato, bun', eat)
// cook('', eat)

// callback functions with event listeners
// button.addEventlistener('click', function (event) {
//   console.log(event)
// })

// button.addEventlistener('click', event => {
//   console.log(event)
// })

// button.addEventlistener('click', event => console.log(event))

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

let squares = []

// run the callback function with each element in the array
numbers.forEach(number => {
  squares.push(number ** 2)
})

// console.log(squares)

// return a new value for each element from the callback function
// numbers = numbers.map(function(number){
//   return number ** 2
// })

numbers = numbers.map(number => number ** 2)
// console.log(numbers)


// return true if the number is desired, return false to filter the number
numbers = numbers.filter(number => number % 2 === 1) // filter out all the odd
// console.log(numbers)

// reduce will combine elements in the list based on a condition
sum = numbers.reduce((previousValue, currentValue) => {
  console.log(previousValue, currentValue)
  return previousValue + currentValue
}, 0)
// console.log(sum)