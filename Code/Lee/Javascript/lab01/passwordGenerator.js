/* Lee Colburn
Lab 1 Javascript
Random Password Generator */

function randint(a, b) {
    return Math.floor(a + Math.random()*(b-a+1))
}

function randomChoice(arr) {
    let i = randint(0, arr.length-1);
    return arr[i]
}

function getChars(desiredLength, array){
    let passIndex=0;
    let charString = '';
    array = array.split('')
    while (passIndex < desiredLength){
       let choice = randomChoice(array)
       let choiceIndex = array.indexOf(choice)
       if (choiceIndex > -1) {
        array.splice(choiceIndex, 1); // omg this was painful. This essentially pops out the value from the array of eligible password characters. The prevents duplication of values for the final password output. 
      }
       charString =charString + choice
       
       ++passIndex
    }
    return charString
}

function generatePassword(numberLength, specialLength, upperLength, lowerLength){
    let passNumbers, passSpecial, passUpper, passLower, numPass, specialPass, upperPass, lowerPass, finalPass

    passNumbers = '0123456789';
    passSpecial = '!#$%&*+,-.=>?@[]^_`~';
    passUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    passLower = 'abcdefghijklmnopqrstuvwxyz';
    numPass = getChars(numberLength, passNumbers)
    specialPass = getChars(specialLength, passSpecial) 
    upperPass = getChars(upperLength, passUpper) 
    lowerPass = getChars(lowerLength, passLower)
    finalPass = numPass + specialPass + upperPass + lowerPass 
    console.log(finalPass)
    finalPass = getChars(finalPass.length, finalPass)
    return finalPass
}

function shuffleWord (word){
    var shuffledWord = '';
    word = word.split('');
    while (word.length > 0) {
      shuffledWord +=  word.splice(word.length * Math.random() << 0, 1);
    }
    return shuffledWord;
}

let numberLength=prompt('Enter an integer value for Numbers:')
let specialLength=prompt('Enter an integer value for your special chars:')
let upperLength=prompt('Enter an integer value for your uppercase chars:')
let lowerLength=prompt('Enter an integer value for your lowercase:')
let finalPassword = generatePassword(numberLength, specialLength, upperLength, lowerLength)
finalPassword = shuffleWord(finalPassword)

alert("Password: " + finalPassword)
