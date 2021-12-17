const rock = document.getElementById('rock')
const paper = document.getElementById('paper')
const scissors = document.getElementById('scissors')
const result = document.getElementById('result')

// apply click events to the buttons that will call the game function with different values
rock.addEventListener('click', ()=>{
  playRPS('rock')
})
paper.addEventListener('click', ()=>{
  playRPS('paper')
})
scissors.addEventListener('click', ()=>{
  playRPS('scissors')
})

function playRPS (player) {
  let choices, compIndex, comp, resultText

  // to calculate game outcomes
  const game = {
    rock: {
      lose: 'paper',
      win: 'scissors'
    },
    paper: {
      lose: 'scissors',
      win: 'rock'
    },
    scissors: {
      lose: 'rock',
      win: 'paper'
    }
  }

  // array of game choices
  choices = Object.keys(game)

  // calculate random index for computer choice
  compIndex = Math.floor(Math.random() * choices.length)

  // get the computer's choice
  comp = choices[compIndex]


  if(comp === player){
    resultText = `It's a tie! You and the computer both chose ${player}!`
  } else if(comp === game[player].lose) {
    resultText = `The computer's ${comp} defeats your ${player}! You lose!`
  } else if(comp === game[player].win) {
    resultText = `Your ${player} defeats the computer's ${comp}! You win!`
  }

  // set contents of results h1 to the result of the game
  result.innerHTML = resultText

}

