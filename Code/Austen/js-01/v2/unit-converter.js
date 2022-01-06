const roundAccurately = (number, decimalPlaces) =>
  Number(Math.round(number + "e" + decimalPlaces) + "e-" + decimalPlaces);

function convert(unitFrom, unitTo, amount, rates) {
  for (let i = 0; i < rates.length; i++) {
    if (unitFrom === rates[i].name) {
      let unitrates = rates[i].rates;
      for (let i = 0; i < unitrates.length; i++) {
        if (unitTo === unitrates[i].name) {
          let rate = unitrates[i].rate;
          let calc = amount * rate;
          return roundAccurately(calc, 3);
        }
      }
    }
  }
}
let rates = [
  {
    name: "feet",
    rates: [
      { name: "inches", rate: 12 },
      { name: "meters", rate: 0.3048 },
    ],
  },
  { name: "meters", rates: [{ name: "feet", rate: 1 / 0.3048 }] },
];
alert("Welcome to the converter.");
let unitFrom = prompt("Unit from:\nenter 'feet' or 'meters': ");
let amount = prompt("Enter the number of " + unitFrom + ": ");
let unitTo = prompt(
  "What unit would you like to convert to?\nif you entered\n feet: enter 'inches' or 'meters'\n meters: enter 'feet'"
);
let output = convert(unitFrom, unitTo, amount, rates);
alert(amount + " " + unitFrom + " = " + output + " " + unitTo);
