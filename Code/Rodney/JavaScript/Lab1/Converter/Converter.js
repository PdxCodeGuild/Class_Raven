var x = 1

while(x=1) {
var userUnit = prompt("Please choose unit to convert to meters: \nFeet\nMiles\nKilometers\nYards\nInches").toLowerCase()

var listofUnits = ["feet", "miles", "meters", "kilometers", "yards", "inches"]

if(listofUnits.includes(userUnit)===false){
continue
}

var userDistance = prompt(`How many ${userUnit} do you want to convert to meters?`)

var converter = {feet: "0.3048", miles: "1609.34", meters: "1", kilometers: "1000", yards: "0.9144", inches: "0.0254"}

var conversionNumber = converter[userUnit]

var finalDistance = conversionNumber * userDistance

console.log(finalDistance)

var YesorNo = prompt(`Your conversion: ${userDistance} ${userUnit} equals ${finalDistance} meters.\n Do you want to try again?`).toLowerCase()
if(YesorNo === 'no'){
break
}
}

