function generate(length, charset, total) {
  // * sets available characters
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const special = "!@#$%^&*()_+";
  // * empty string to be added to
  var password = "";
  // * tracks the amount of characters added in each group
  var group1 = 0;
  var group2 = 0;
  var group3 = 0;
  var group4 = 0;
  // * distributes unspecified character types randomly
  if (total < length) {
    let amount = length - total;
    while (amount > 0) {
      let group = Math.floor(Math.random() * 4) + 1;
      if (group === 1) {
        charset.uppers += 1;
      }
      if (group === 2) {
        charset.lowers += 1;
      }
      if (group === 3) {
        charset.numbers += 1;
      }
      if (group === 4) {
        charset.symbols += 1;
      }
      amount -= 1;
    }
  }
  while (password.length < length) {
    // * randomly choose a set to pull from
    let group = Math.floor(Math.random() * 4) + 1;
    console.log(group);
    // * matches selected group and adds a random character if that group's quota isn't full
    if (group === 1) {
      if (group1 < charset.uppers) {
        let index = Math.floor(Math.random() * letters.length);
        let char = letters.charAt(index);
        password += char;
        group1 += 1;
      }
    }
    if (group === 2) {
      if (group2 < charset.lowers) {
        let lowers = letters.toLowerCase();
        let index = Math.floor(Math.random() * lowers.length);
        let char = lowers.charAt(index);
        password += char;
        group2 += 1;
      }
    }
    if (group === 3) {
      if (group3 < charset.numbers) {
        let index = Math.floor(Math.random() * 10);
        password += index;
        group3 += 1;
      }
    }
    if (group === 4) {
      if (group4 < charset.numbers) {
        let index = Math.floor(Math.random() * special.length);
        let char = special.charAt(index);
        password += char;
        group4 += 1;
      }
    }
  }
  // * prints the amount of characters pulled from each set for quick verification
  console.log(group1, group2, group3, group4);

  return password;
}

// * compares length and total then passes the larger number as the length to generate()
function getPassword(length, total, charset) {
  if (total > length) {
    alert(
      "You entered more characters than your desired length. Your generated password will contain " +
        total +
        " characters."
    );
    return generate(total, charset, total);
  } else {
    return generate(length, charset, total);
  }
}

// * collect and compile user input to pass to getPassword()
alert("Welcome to the password generator.");
let length = prompt("How many characters should your password be?");
let upper = prompt("How many characters should be uppercase?");
let lower = prompt("How many characters should be lowercase?");
let number = prompt("How many characters should be numbers?");
let symbol = prompt("How many characters should be symbols?");

// * get charset total to compare against user's desired length
let total =
  parseInt(upper) + parseInt(lower) + parseInt(number) + parseInt(symbol);

let charset = {
  uppers: upper,
  lowers: lower,
  numbers: number,
  symbols: symbol,
};

let password = getPassword(length, total, charset);

// * displays the generated password
alert(password);
