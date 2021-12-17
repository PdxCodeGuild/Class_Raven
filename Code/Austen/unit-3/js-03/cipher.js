var alphabet = "abcefghijklmnopqrstuvwxyz";
var capitols = alphabet.toUpperCase();

function rotate(char, rotations) {
  let index = alphabet.indexOf(char);
  index += parseInt(rotations);
  if (index > 25) {
    index -= 25;
  }
  let rot = alphabet.charAt(index);
  return rot;
}

let string = prompt("Enter the string to be run through the cipher:");
let rotations = prompt("How many rotations would you like to run?");
var ciphered = "";
for (let char of string) {
  if (alphabet.includes(char)) {
    char = rotate(char, rotations);
  }
  if (capitols.includes(char)) {
    char = char.toLowerCase();
    char = rotate(char, rotations);
    char = char.toUpperCase();
  }
  ciphered += char;
}
alert(ciphered);
