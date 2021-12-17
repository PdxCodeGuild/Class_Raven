var x = 1

while(x=1) {
var userInput = prompt("Welcome to Rock Paper Scissors. \n You will be playing against the computer. \n Please enter rock, paper, or scissors:").toLowerCase()

var computerOptions = ["rock", "paper", "scissors"]

if(computerOptions.includes(userInput)===false){
continue
}

console.log(userInput)

var randomIndex = Math.random()
randomIndex = randomIndex * 3
randomIndex = Math.floor(randomIndex)

var computerChoice = computerOptions[randomIndex]

console.log(computerChoice)

if(userInput===computerChoice){
alert("It's a tie!")
var YesorNo = prompt("Try again.. yes or no?")
if(YesorNo === 'no'){
break
}
}


else if(userInput==="rock" && computerChoice==="scissors"){
alert("You win!")
var YesorNo = prompt("Try again.. yes or no?")
if(YesorNo === 'no'){
break
}
}


else if(userInput==="paper" && computerChoice==="rock"){
alert("You win!")
var YesorNo = prompt("Try again.. yes or no?")
if(YesorNo === 'no'){
break
}
}


else if(userInput==="scissors" && computerChoice==="paper"){
alert("You win!")
var YesorNo = prompt("Try again.. yes or no?")
if(YesorNo === 'no'){
break
}
}

else if(userInput==="rock" && computerChoice==="paper"){
alert("Computer wins!")
var YesorNo = prompt("Try again.. yes or no?")
if(YesorNo === 'no'){
break
}
}


else if(userInput==="paper" && computerChoice==="scissors"){
alert("Computer wins!")
var YesorNo = prompt("Try again.. yes or no?")
if(YesorNo === 'no'){
break
}
}


else if(userInput==="scissors" && computerChoice==="rock"){
alert("Computer wins!")
var YesorNo = prompt("Try again.. yes or no?")
if(YesorNo === 'no'){
break
}
}

}