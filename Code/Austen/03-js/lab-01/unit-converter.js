function convert(unitFrom, unitTo, amount) {
  if (unitFrom === "feet") {
    if (unitTo === "inches") {
      var output = amount * 12;
    }
    if (unitTo === "meters") {
      var output = Math.round(amount * 0.3048);
    }
  }
  if (unitFrom === "meters") {
    if (unitTo === "feet") {
      var output = Math.round(amount / 0.3048);
    }
  }
  return output;
}

alert("Welcome to the converter.");
let unitFrom = prompt("What unit would you like to enter?");
let amount = prompt("Enter the number of " + unitFrom + ": ");
let unitTo = prompt("What unit would you like to convert to?");
let output = convert(unitFrom, unitTo, amount);
alert(amount + " " + unitFrom + " = (approx.) " + output + " " + unitTo);
