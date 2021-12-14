var userChoice = prompt("Choose Rock,Paper, or Scissors: ")
var choices = ['rock','paper','scissors']
var enemyChoice = choices[Math.floor(Math.random()*choices.length)]

if (userChoice == enemyChoice){
    console.log("Its a tie")
}
else if (userChoice == 'rock' && enemyChoice == 'paper'){
    console.log("You lose")
}
else if (userChoice == 'rock' && enemyChoice == 'scissors'){
    console.log("You win")
}
else if (userChoice == 'paper' && enemyChoice == 'scissors'){
    console.log("You lose")
}
else if (userChoice == 'paper' && enemyChoice == 'rock'){
    console.log("You lose")
}
else if (userChoice == 'scissors' && enemyChoice == 'paper'){
    console.log("You win")
}
else if (userChoice == 'scissors' && enemyChoice == 'rock'){
    console.log("You lose")
}



