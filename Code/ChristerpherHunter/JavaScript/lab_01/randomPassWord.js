
const pwLength = parseInt(prompt("Please enter the desired password Length: "))

let pwBank = [
    "abcdefghijklmnopqrstuvwxyz",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "012345678901234567890123456789",
    "!@#$%^&*()_-+=~{[}}><"
]

/**
 * 
 * @param {Array.<String>} shuffleItem
 */
function shuffler(shuffleItem) {

    rando = Math.random() * shuffleItem.length
    rando = Math.floor(rando)

    return shuffleItem[rando]
}

let password = new String

let i = 0
while (i < pwLength / 4) {

    password += (pwBank.map(shuffler))
    i++
}

password = password.replace(/,/g, '')
let psword = password.substr(0, pwLength)

alert(`Password:   ${psword}`)
