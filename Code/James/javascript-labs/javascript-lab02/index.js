game = ['rock', 'sciccors', 'paper']


let user = prompt("Enter rock paper or scissors:    ")
// make user score part of the game list
console.log(`You chose ${user}`);


random = Math.floor(Math.random() *game.length)
let computer =  game[random]
console.log(`Computer chose ${computer}`);

if (user === computer){
    alert('tie');
}

else if (user === 'rock' && computer === 'paper'){
   alert('Computer wins!');
}
else if (user === 'rock' && computer === 'scissors'){
    alert('User wins!');
}
else if (user === 'paper' && computer === 'rock'){
    alert('User wins!');
}
else if (user === 'paper' && computer === 'scissors'){
    alert('Computer wins!');
}
else if (user === 'scissors' && computer === 'rock'){
    alert('Computer wins!');
}
else if (user === 'scissors' && computer === 'paper'){
    alert('User wins!');
}

console.log(computer);