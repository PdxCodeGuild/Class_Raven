let numbers = [1,2,3,4,5,6,7,8,9]
let n = 2


// passing a named function to .map()
function addN(number, n){
  return number + n
}

numbers = numbers.map((number)=>addN(number, n))
console.log(numbers)

// passing an anonymous arrow function to map()
numbers = numbers.map((number) => number + n)
console.log(numbers)


// passing an anonymous function() to map()
numbers = numbers.map(function(number){
  return number + n
})
console.log(numbers)