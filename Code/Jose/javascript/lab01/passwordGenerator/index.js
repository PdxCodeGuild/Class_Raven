let characters = [
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', 
';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
let currentCharacterAmount = 0
let password = ""

let characterAmount = parseInt(prompt("How many characters would you like to include in the password? (10, 13, 27, ect..): "));

randomIndex = Math.floor(Math.random() * characters.length)
randomChoice = characters[randomIndex]

while(currentCharacterAmount < characterAmount){
    randomIndex = Math.floor(Math.random() * characters.length)
    randomChoice = characters[randomIndex]
    password += randomChoice
    currentCharacterAmount++
}

alert(`Your password is: ${password}`)