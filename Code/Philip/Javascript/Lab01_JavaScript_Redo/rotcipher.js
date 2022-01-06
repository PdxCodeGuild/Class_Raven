/*
Lab01 JavaScript Redo
Rot Cipher
By Philip Bartoo
12/11/21
PDX Code Guild

Directions:
Write a program that prompts the user for a string, and encodes it with ROT13. 
For each character, find the corresponding character, add it to an output string. 
Notice that there are 26 letters in the English language, so encryption is the same as decryption.
Allow the user to input the amount of rotation used in the encryption. (ROTN)
*/

//Prompt user for a word and store it as an Array variable
let wordArr = prompt("Enter Word to Encrypt: ").split("");
//Prompt user for a number to store in as an integer in a key variable
let key = parseInt(prompt("Enter a number: "));
//Create an empty string variable to hold the final cipher code
var cipher ='';
//Array variable to access index value of alphabet
const abcArr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
//For loop that increments by 1
for (i=0; i<wordArr.length; i++){
    //Using the user provided word, loop through each letter and determine its index in the alphabet array (abcArr)
    //Store that index result as a variable (offset)
    let offset = abcArr.indexOf(wordArr[i]);
    //Rotate the cipher by adding the key variable to the index variable, adjust for z by applying modulus of alphabet array
    offset = (offset + key) % abcArr.length;
    //Use the offset number to index the alphabet array and extract the new letter
    let update = abcArr[offset];
    //Add the encoded letter to the cipher string variable
    cipher = (cipher + update);
}
prompt('Your secret code is: ',cipher);

/*Note: In the course of completing this lab I discovered that much more computing power was available for the cipher using JavaScript. 
Using Flask and Python significantly limited the amount of letters and the amount of cipher rotation.
I suspect this has something to do with the html call from html, through Flask, to Python, but I'd like to further understand this.*/