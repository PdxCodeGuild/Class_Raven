let distance = parseInt(prompt("What is the distance? (3, 5, 9..):"));
let typeOfUnit = prompt("What type of unit?");

const units = {
"ft": 0.3048,
"mi": 1609.34,
"m": 1,
"km": 1000,
"yard": 0.9144,
"inch": 0.0254
}

let product = distance * units[typeOfUnit]

alert(`${distance}${typeOfUnit} is ${product}m`)
