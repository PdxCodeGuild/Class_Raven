let button = document.querySelector('#button'),
  h1 = document.querySelector('#result')

// let promise = new Promise((resolve, reject)=>{
//   let number = Math.floor(Math.random() * 100)

//   // simulate API call with setTimeout
//   setTimeout(()=>{

//     if(number % 2 === 0){
//       resolve(`Yay! ${number} is even!!!`)
//     } else {
//       reject(`Oops! ${number} is odd!!!`)
//     }
//   }, 2000)
// })

// function add(a, b){
//   return a + b
// }

// const add = function(a,b){
//   return a + b
// }

// const subtract = (a, b) => {
//   return a + b
// }

// const add = (a, b) => a + b

function isEven (number) {
  return new Promise((success, error) => {
    // simulate API call with setTimeout
    setTimeout(function () {
      if (number % 2 === 0) {
        success(`Yay! ${number} is even!!!`)
      } else {
        error(`Oops! ${number} is odd!!!`)
      }
    }, 2000)
  })
}

button.addEventListener('click', () => {
  let number = Math.floor(Math.random() * 100)

  h1.style.color = 'black'
  h1.innerHTML = 'Thinking...'

  // isEven() returns a promise, so .then() and .catch() can be used after it
  isEven(number)
    .then(result => {
      // if the promise resolves, set the h1 to the resulting text
      h1.style.color = 'green'
      h1.innerHTML = result
    })
    .catch(error => {
      // if the promise is rejected, set the h1 to the error text
      h1.style.color = 'red'
      h1.innerHTML = error
    })
})
