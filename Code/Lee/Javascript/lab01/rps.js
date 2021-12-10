/* Lee Colburn
Lab 1 Javascript
Rock, Paper, Scissors */

let options = ['rock', 'paper', 'scissors']

function randint(a, b) {
    return Math.floor(a + Math.random()*(b-a+1))
}

function randomChoice(arr) {
    let i = randint(0, arr.length-1)
    return arr[i]
}

function game (){
    let userChoice = prompt("Enter 'rock', 'paper', or 'scissors': ")
    let computerChoice = randomChoice(options);
    console.log("You chose", userChoice);
    console.log("Computer chose", computerChoice);
    result (userChoice, computerChoice)
}

function result (user, computer){
    if (user == computer){
        console.log("You tied!")
        return
    } else if (user == 'rock') {
        if (computer == 'paper') {
            console.log("The computer's paper covers your rock - you lose!")
            return
        } else if (computer == 'scissors') {
            console.log("The computer's scissors are crushed by your rock - you win!")
            return
        }
    } else if (user == 'paper') {
        if (computer == 'scissors') {
            console.log("The computer's scissors cuts your paper - you lose!")
            return
        } else if (computer == 'rock') {
            console.log("The computer's rock is covered by your paper - you win!")
            return
        }
    } else if (user == 'scissors') {
        if (computer == 'rock') {
            console.log("The computer's rock crushes your scissors - you lose!")
            return
        } else if (computer == 'paper') {
            console.log("The computer's paper is cut by your scissors - you win!")
            return
        }
    }
    return
}


let continueGame = 0

while (continueGame < 1) {
    game()
    let repeater = prompt("Input 'yes' if you'd like to continue the game")
    if (repeater != 'yes'){
        continueGame++
    } 
}

