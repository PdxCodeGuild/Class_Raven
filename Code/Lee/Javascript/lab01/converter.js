/* Lee Colburn
Lab 1 Javascript
Unit Converter */

function getMeters(distance, unit) {
    if (unit == "feet"){
        let result=(distance * .3048)
        return result
    }
    else if (unit == "miles") {
        let result = (distance * 1609.34)
        return result
    }
    else if (unit == "meters") {
        let result = (distance * 1)
        return result
    }
    else if (unit == "kilometers") {
        let result = (distance * 1000)
        return result
    }
    else if (unit == "yards") {
        let result = (distance * .9144)
        return result
    }
    else if (unit == "inches") {
        let result = (distance * 0.0254)
        return result 
    }
}

function getCustom(meters, unit){
    if (unit == "feet"){
        let result=(meters / .3048)
        return result
    }
    else if (unit == "miles") {
        let result = (meters / 1609.34)
        return result
    }
    else if (unit == "meters") {
        let result = (meters / 1)
        return result
    }
    else if (unit == "kilometers") {
        let result = (meters / 1000)
        return result
    }
    else if (unit == "yards") {
        let result = (meters / .9144)
        return result
    }
    else if (unit == "inches") {
        let result = (meters / 0.0254)
        return result 
    }
}



let outputUnit = prompt('Enter the unit you would like to convert to ("feet", "miles", "meters", "kilometers", "yards", or "inches"): ')
let inputDistance = prompt('Enter the distance you would like to convert:')
let inputUnit = prompt('Enter the unit you are converting from ("feet", "miles", "meters", "kilometers", "yards", or "inches")')
let meterResult = getMeters(inputDistance, inputUnit)

if (outputUnit != "meters"){
    let meters = getMeters(inputDistance, inputUnit)
    let customResult = getCustom(meters, outputUnit)
    alert(inputDistance + " " + inputUnit + " is equal to " + customResult + " " + outputUnit)
} else {
    alert(inputDistance + " " + inputUnit + " is equal to " + meterResult + " " + outputUnit)
}




