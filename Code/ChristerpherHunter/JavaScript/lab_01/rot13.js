

let userString = "Hello World!"
userString = prompt("Please enter the word to be encrypted: ")

var n = 13
n = prompt("Please enter the rotation number: ")


const asciiLowerCase = "abcdefghijklmnopqrstuvwxyz"

function cleaner(userInput) {

    // Grab the index of the space and special chars
    let space = userString.indexOf(" ")
    
    // console.log(`Space Count: ${space}`)

    return space
}

function cleaner2(userInput) {

    let specChar = userString.match(/[!,."'?]/g)
    // console.log(`Special Character: ${specChar}`)

    return specChar
}

function smoother(userInput ,specChar) {

    // Clean the input
    userInput = userInput.replace(" ", "")
    userInput = userInput.replace(specChar, "")
    // console.log(`Input String: ${userInput}`)

    return userInput
}

// Loop through the string and on each iteration extract the letter
// store the corresponding alphabetical number
function addN(userInput, n = 13, alphabet = asciiLowerCase) {
    let wordCountList = 0
    let word = ""
    let space = 0
    let specChar = ""

    // Grab special information
    space = cleaner(userInput)
    specChar = cleaner2(userInput)
    
    // Strip the space and special char
    userInput = smoother(userInput ,specChar)
    // console.log(userInput)

    for (letter of userInput) {
        
        // Store the corresponding alphabetical letter to the number
        wordCountList = alphabet.indexOf(letter.toLowerCase())

        // Add 'n' to that number
        wordCountList += n

        // if over 26, assign the letter to the difference of 26 and the overage.
        if (wordCountList > 26) {
            wordCountList -= alphabet.length
        }
        word += alphabet[wordCountList]
    }

    // reassemble the word
    word = word.slice(0, space) + " " + word.slice(space, word.length) + specChar

    return word
}

let encrypted = addN(userString, 13)

alert(`Encrypted Message: ${encrypted}`)
