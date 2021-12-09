console.log("4556737586899855")

const cardTest = new String(prompt("Enter a 15 digit credit card number: "))
if (cardTest.length != 16) {
    alert("Incorrect Number of digits")
}


// Turn the string into a list
let cardList = []
for (num in cardTest) {
    cardList.push(parseInt(cardTest[num]))
}

const checkDigit = cardList.pop()

cardList = cardList.reverse()

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

cardNumSum %= 10

if (cardNumSum === checkDigit) {
    alert("Credit Card Valid!")
} else {
    alert("Credit Card Invalid!")
}

