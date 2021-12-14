
// obtain number of characters from user 
prompt('Welcome to the password maker! Hit ok to continue')
let numNumbers= prompt("How many numbers do you want in your password?")
let numLetters= prompt("letters?")
let numPunct= prompt("punctuation characters?")

// list of alphabet(lower and upper) and list of punctuation
let letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
var punctuation = ['!', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']

// obtain list of random numbers based on how many user wants in password 
var finalnumbersList = []
for(var i=0; i<numNumbers; i++){
var w = Math.random() * 10
w = Math.floor(w)
finalnumbersList.push(w)
}
// console.log(finalnumbersList)

// obtain lists of random indexes for letters and punctuation based on how many user wants in password 
var lettersList = []
for(var i=0; i<numLetters; i++){
var x = Math.random() * 52
x= Math.floor(x)
lettersList.push(x)
}
// console.log(lettersList)

var punctList = []
for(var i=0; i<numPunct; i++){
var y = Math.random() * 30
y= Math.floor(y)
punctList.push(y)
}
// console.log(punctList)

// using lists of random indexes, loop through each to obtain random letters/punct based on how many user wants in password 
var finallettersList = []
lettersList.forEach(letterfunct);

function letterfunct(index) {
    finallettersList.push(letters[index])
}
// console.log(finallettersList)
// -------------------------------------------------------------------
var finalpunctList = []
punctList.forEach(punctfunct);

function punctfunct(index) {
    finalpunctList.push(punctuation[index])
}
// console.log(finalpunctList)


// combine lists of random number, letters, and punctuation characters 

const finalList = [].concat(finalnumbersList, finallettersList, finalpunctList)
// console.log(finalList)

// create list of random indexes again
var totalIndexes = finalList.length 
// console.log(totalIndexes)

var shuffledIndexes = []
while(shuffledIndexes.length<totalIndexes){
var z = Math.random() * (totalIndexes-1)
z = Math.round(z)
if(shuffledIndexes.includes(z)){
continue
}
shuffledIndexes.push(z)
}
// console.log(shuffledIndexes)

// shuffle final list of characters
var shuffledList = []

shuffledIndexes.forEach(shuffleFunction);

function shuffleFunction(index) {
    shuffledList.push(finalList[index])
}
// console.log(shuffledList)


// turn list into string and remove commas 
var finalPassword = shuffledList.toString()
finalPassword = finalPassword.replace(/,/g, '')
alert(`Your final password is ${finalPassword}`)

