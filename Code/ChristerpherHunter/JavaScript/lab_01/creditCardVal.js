const cardTest = "4556737586899855"

// Turn the string into a list
let cardList = []
for (num in cardTest) {
    cardList.push(parseInt(cardTest[num]))
}
console.log(cardList)

const checkDigit = cardList.pop()

console.log(checkDigit)

cardList = cardList.reverse()
console.log(cardList)

let cardNumSum = 0

for (odd in cardList) {
    if (odd % 2 == 0) {
        cardList[odd] *= 2
        if (cardList[odd] > 9) {
            cardList[odd] -= 9
        }
    }
    cardNumSum += cardList[odd]
}

console.log(cardList)
console.log(cardNumSum)

cardNumSum %= 10

console.log(cardNumSum)

if (cardNumSum === checkDigit) {
    alert("Credit Card Valid!")
} else {
    alert("Credit Card Invalid!")
}

