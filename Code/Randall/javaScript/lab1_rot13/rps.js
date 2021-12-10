//Lab1 Rock Paper Scissors JS redo

var random_number = Math.random();
var user_choice = prompt('Enter your choice: rock, paper, or scissors: ');

computer_choice = '';
if ( random_number  <= 1/3 ) {
    var computer_choice = 'rock' }
    else if ( random_number >= 1/3 && random_number <= 2/3 ) {
        var computer_choice = 'paper' }
    else if ( random_number >= 2/3 ) {
        var computer_choice = 'scissors' }
    else { var computer_choice = 'Not a valod selection. Reload and try again.' };


if ( computer_choice === user_choice ) {
    alert('You tied!') }
    
    else if ( user_choice === 'rock' && computer_choice === 'scissors') {
        alert(`You win!`) }
    else if ( user_choice === 'rock' && computer_choice === 'paper') {
        alert('You lost!') }
    
    else if ( user_choice === 'paper' && computer_choice === 'rock') { 
        alert('You lost!') }
    else if (user_choice === 'paper' && computer_choice === 'scissors') { 
        alert('You lose!') }

    else if (user_choice === 'scissors' && computer_choice === 'paper') {
        alert('You win!') }
    else if ( user_choice === 'scissors' && computer_choice === 'rock') { 
        alert('You lost!') }        
    else { alert('Error: Reload the program.')};