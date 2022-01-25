/*
Lab 01 JavaScript Redo
Random Passworod Generator
By Philip Bartoo
12/12/2021
PDX Code Guild

Directions:
Let's generate a password of length n using a while loop and random.choice, this will be a string of random characters, e.g. a62xB95. 
Allow the user to enter the value of n, remember to convert its type to an int, as input returns a string. 
Hint: random.choice can be used to pick a character out of a string, as well as an element out of a list.
*/

//Prompt user fot the length of the password and store as a variable
let n = prompt('Enter the length of password: ');
//Ensure the variable is stored as an integer
n = parseInt(n);
//Create the array that holds the character options for the password generator
const characterArr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0'];
//Establish a string variable to store the results of the while loop
let randomPassword = '';
//Set initial increment at 0 for the while loop
var i = 0;
//While loop to select a character from the options above
while (i<n) {
    //Generate a random number to use to select an index in the character array; use floor operator, random and the length of the array to get a random whole number as the index value
    let randomCharacter = characterArr[Math.floor(Math.random() * characterArr.length)];
    //Add the selected random character to the random password response string
    randomPassword = (randomPassword + randomCharacter);
    i++;
}
prompt('Your random password is: ',randomPassword);

//Note: Lesson learned on this was to not use 'const' to store a variable that is expected to change. That variable should probably be stored outside the loop as well. Switching to 'let' or 'var' allows the program to run.
