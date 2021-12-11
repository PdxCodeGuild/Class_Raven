console.log("Rock, Paper, Scissors")
function play() {
  let choice = window.prompt("choose... (rock, paper, or scissors)\n>")
  let computer = "";
  game = ["rock", "paper", "scissors"];
  computer = game[Math.floor(Math.random() * game.length)];
  if (computer === choice) {
    alert(`It's a tie!`);
  }
  if (choice === "rock" && computer == "scissors") {
    alert(
      `Your Rock broke the computers Scisssors!  You win! \(take that computer..\)`
    );
  }
  if (choice === "paper" && computer == "rock") {
    alert(
      `Your Paper wrapped the computers Scisssors!  You win! \(gotcha computer..\)`
    );
  }
  if (choice === "scissors" && computer == "paper") {
    alert(
      `Your Scissors cut the computers Paper!  You win! \(try printing now computer!\)`
    );
  }
  if (choice === "scissors" && computer == "rock") {
    alert(
      `The computer's Rock broke your Scisssors!  Computer wins! \(stay away from my cables human\)`
    );
  }
  if (choice === "rock" && computer == "paper") {
    alert(
      `The computer's paper covered your Rock!  Computer wins! \(Where is your rock now, human?  Do you even know?\)`
    );
  }
  if (choice === "paper" && computer == "scissors") {
    alert(
      `The computer's Scisssors cut your paper!  Computer wins! \(Silly human, all your base are belong to us!\)`
    );
  }
  return;
}

// let again = "yes";
// while (!["N", "NO"].includes(again.toUpperCase())) {
//   // while !== (again !== "n" || "N" || "no"|| "No") {

//   // }
//   choice = "";

//   while (choice !== "rock" || choice !== "scissors" || choice !== "paper") {
//     var choice = window.prompt("choose... (rock, paper, or scissors)\n>");
//     // if (choice == "rock" || "scissors" || "paper") {
//     //   break;
//     }
//   }

//   var again= window.prompt(`would you like to play again?`);
// }
play()
