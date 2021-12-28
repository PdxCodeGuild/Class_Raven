let user_input = prompt("Enter: (rock, paper, scissors)");

user_input = user_input.toLowerCase();


const choices = ["rock", "paper", "scissors"]

compIndex = Math.floor(Math.random() * choices.length)
compChoice = choices[compIndex]

if (user_input === compChoice){
    resultText = `You and the computer chose ${user_input}, it's a tie.` 
}

if(user_input === choices[0]){
    if(compChoice === choices[1]){
        resultText = `You chose rock, the computer chose paper. You lose.`
    }
    if(compChoice === choices[2]){
        resultText = `You chose rock, the computer chose scissors. You win.`
    }
}

if(user_input === choices[1]){
    if(compChoice === choices[0]){
        resultText = `You chose paper, the computer chose rock. You win.`
    }
    if(compChoice === choices[2]){
        resultText = `You chose paper, the computer chose scissors. You lose.`
    }
}

if(user_input === choices[2]){
    if(compChoice === choices[0]){
        resultText = `You chose scissors, the computer chose rock. You lose.`
    }
    if(compChoice === choices[1]){
        resultText = `You chose scissors, the computer chose paper. You win.`
    }
}

alert(resultText)