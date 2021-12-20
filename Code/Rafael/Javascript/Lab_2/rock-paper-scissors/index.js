/* Lab:01 Rock,Paper, Scissors 1 of 3 */


const rps = ['Rock', 'Paper', 'Scissors']
/*console.log(typeof rps)*/

const values = Object.values(rps)
const pc = values[Math.floor(Math.random() * 3)] 
/* console.log(pc); */

var human = []

console.log(rps)
/*console.log(typeof rps)*/


for (choice in human){
    /* console.log(typeof choice) */
    console.log(choice)
    }

var human = prompt("Enter your selection: 'Rock' 'Paper' or 'Scissors' ")

if (human == pc){
    console.log("Computer picked: ", pc)
    console.log("You picked: ", human)
    console.log("It is a tie.\n")
}
if ( human == 'Rock' && pc == 'Paper'){
    console.log("Computer picked: ", pc)
    console.log("You picked: ", human )
    console.log("Paper covers rock: You lost.\n")
}
if (human == 'Rock' && pc == 'Scissors'){
    console.log("Computer picked: ", pc)
    console.log("You picked: ", human)
    console.log("You crushed the Scissors: You won!\n")
}
if (human == 'Paper' && pc == 'Rock'){
    console.log("Computer picked: ", pc)
    console.log("You picked: ", human)
    console.log("Paper covers Rock : You won!\n")
}
if (human == 'Paper' && pc == 'Scissors'){
    console.log("Computer picked: ", pc)
    console.log("You picked: ", human)
    console.log("Scissors cut the Paper: You lost.\n")
}
if (human == 'Scissors' && pc == 'Rock'){
    console.log("Computer picked: ", pc)
    console.log("You picked: ", human)
    console.log("Scissors got crushed by Rock: You lost.\n")
}
if (human == 'Scissors' && pc == 'Paper'){
    console.log("Computer picked: ", pc)
    console.log("You picked: ", human)
    console.log("You cut the Paper: You won!\n")

}

