//Lab1 Random Password Generrator with JS

//n_characters is the number the user input.
let n_characters = prompt('Welcome to password generator! How many characters long would you like your password to be?');

//Function to call on
function random_element(array) {
	let random_index = Math.floor(Math.random() * array.length);
	return array[random_index];
}

//List PW is generated from. Blank space entered will randomly generate a space in the password.
let alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmn opqrstuvwxyz01234 56789!@#$%^&*( )~`-=_+';

//output starts an empty list
let output = '';
//Loops until password length = n_characters input
for(let i = 0; i < n_characters; ++i) {
    //appending to the output list a random character from the alphabet list
	output += random_element(alphabet);
}
//Displays the PW result
alert(output);