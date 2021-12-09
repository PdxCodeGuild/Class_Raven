function shuffle(password) {
  var shuffled = [];
  for (let s = 1; s < password.length; s++) {
    let index = Math.floor(Math.random() * password.length);
    let char = password.charAt(index);
    let newindex = Math.floor(Math.random() * password.length);
    char = { char: char, index: newindex };
    shuffled.push(char);
  }
  shuffled.sort();
  return shuffled;
}

function generate(length, charset) {
  var password = "";
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const special = "!@#$%^&*()_+";
  for (let u = 1; u <= charset.uppers; u++) {
    let index = Math.floor(Math.random() * letters.length);
    let char = letters.charAt(index);
    password += char;
  }
  for (let l = 1; l <= charset.lowers; l++) {
    let lowers = letters.toLowerCase();
    let index = Math.floor(Math.random() * lowers.length);
    let char = lowers.charAt(index);
    password += char;
  }
  for (let n = 1; n <= charset.numbers; n++) {
    let digit = Math.floor(Math.random() * 10);
    let char = Math.round(digit);
    password += char;
  }
  for (let s = 1; s <= charset.symbols; s++) {
    let index = Math.floor(Math.random() * special.length);
    let char = special.charAt(index);
    password += char;
  }
  while (password.length < length) {
    let fillers = letters + letters.toLowerCase() + "0123456789";
    let index = Math.floor(Math.random() * fillers.length);
    let char = fillers.charAt(index);
    password += char;
  }
  console.log(password);
  password = shuffle(password);
  console.log(password);

  return password;
}

alert("Welcome to the password generator.");
let length = prompt("How many characters should your password be?");
let upper = prompt("How many characters should be uppercase?");
let lower = prompt("How many characters should be lowercase?");
let number = prompt("How many characters should be numbers?");
let symbol = prompt("How many characters should be symbols?");
let charset = {
  uppers: upper,
  lowers: lower,
  numbers: number,
  symbols: symbol,
};
let password = generate(length, charset);
alert(password);
