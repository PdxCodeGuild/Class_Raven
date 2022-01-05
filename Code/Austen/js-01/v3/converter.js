function convert(amount, from, to){
  let rates = {
    feet: 1,
    meters: 0.3048,
    miles: 1 / 5280,
    kilometers: 0.0003048
  };
  const round = (number, decimalPlaces) =>
    Number(Math.round(number + "e" + decimalPlaces) + "e-" + decimalPlaces);
  amount = parseInt(amount)
  let feet = amount / rates[from]
  let conversion = feet * rates[to]
  if (conversion > 99){
  conversion = round(conversion, 0)}
  if (conversion > 10){
  conversion = round(conversion, 1)}
  if (conversion > 1){
  conversion = round(conversion, 2)}
  if (conversion < 1){
  conversion = round(conversion, 4)}
  return `${conversion} ${to}`
}
function format(array){
  let string = ''
  let l = array.length
  for (let i = 0; i < l; i++){
    if (i === l-1){
      string += `and ${array[i]}.`
    }
    else {
      string += `${array[i]}, `
    }
  }
  return string
}



let options = ['feet', 'miles', 'meters', 'kilometers' ]
let string = format(options)
let from = prompt(`Welcome to the distance converter.\n   available units: ${string}\nEnter the starting unit:`);

let option = options.indexOf(from)
options.splice(option, 1)
string = format(options)
let amount = prompt(`How many ${from}: `);

let to = prompt(`Now what unit would you like to convert ${from} to?\n   available units: ${string}`);

let conversion = convert(amount, from, to)
document.getElementById('target').innerHTML = conversion
