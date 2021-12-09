function computerMove() {
	let computerChoice = Math.floor(Math.random() * 3);
	if (computerChoice == 0) {
		return "rock";
	} else if (computerChoice == 1) {
		return "paper";
	} else {
		return "scissors";
	}
}

function playRound(playerSelection, computerSelection) {
	if (playerSelection == computerSelection) {
		return "It's a tie!";
	} else if (playerSelection == "rock") {
		if (computerSelection == "paper") {
			return "You lose! Paper beats rock.";
		} else {
			return "You win! Rock beats scissors.";
		}
	} else if (playerSelection == "paper") {
		if (computerSelection == "scissors") {
			return "You lose! Scissors beats paper.";
		} else {
			return "You win! Paper beats rock.";
		}
	} else {
		if (computerSelection == "rock") {
			return "You lose! Rock beats scissors.";
		} else {
			return "You win! Scissors beats paper.";
		}
	}
}

function playGame() {
	let playerScore = 0;
	let computerScore = 0;
	let round = 1;

	while (playerScore < 5 && computerScore < 5) {
		let playerSelection = "";
		while (
			playerSelection != "rock" &&
			playerSelection != "paper" &&
			playerSelection != "scissors" &&
			playerSelection != "quit"
		) {
			playerSelection = prompt(
				`Round: ${round} - Score: ${playerScore}:${computerScore}
    Rock, paper, or scissors?`
			).toLowerCase();
		}

		if (playerSelection == "quit") {
			break;
		}
		let computerSelection = computerMove();
		let result = playRound(playerSelection, computerSelection);
		alert(result);
		if (result == "You win! Rock beats scissors.") {
			playerScore++;
		} else if (result == "You win! Paper beats rock.") {
			playerScore++;
		} else if (result == "You win! Scissors beats paper.") {
			playerScore++;
		} else if (result == "You lose! Rock beats scissors.") {
			computerScore++;
		} else if (result == "You lose! Paper beats rock.") {
			computerScore++;
		} else if (result == "You lose! Scissors beats paper.") {
			computerScore++;
		}
		round++;
	}
	if (playerScore > computerScore) {
		alert("You win!");
	} else {
		alert("You lose!");
	}
	playAgain();
}

function playAgain() {
	let playAgain = "ask";
	while (
		playAgain != "y" &&
		playAgain != "n" &&
		playAgain != "quit" &&
		playAgain != "q" &&
		playAgain != "yes" &&
		playAgain != "no"
	) {
		playAgain = prompt("Play again? (y/n)");
	}
	if (playAgain == "y" || playAgain == "yes") {
		playGame();
	} else {
		alert("Thanks for playing!");
	}
}

playGame();
