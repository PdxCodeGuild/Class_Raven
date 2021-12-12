let userInput = prompt('Enter password length: ')


let alphabet = "abcdefghijklmnopqrstuvwxyz".split('');
console.log(alphabet)

let punctuation = `!@#%^&*"><()_|{.,/;][$-=+}`.split('');
console.log(punctuation)

function generateArrayOfNumbers (numbers) {
    return [...Array(numbers).keys()].slice(0)
}

var numbers = generateArrayOfNumbers(10);
console.log(numbers)

var randomList = alphabet.concat(punctuation).concat(numbers)
// console.log(alphabet.concat(punctuation).concat(numbers))
console.log(randomList)


function randomPassword(randomList){
    return  Math.floor(Math.random() *randomList.length);
}

console.log(randomPassword(randomList))
let i = 0
var list = []

while (i < userInput){
    list.push(randomList[Math.floor(Math.random() *randomList.length)])
    
    i++
}

// function name(params) {
    
// }

console.log(list)
alert(`Your password is ${list}`)

// promp