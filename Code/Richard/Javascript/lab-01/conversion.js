console.log('Distance Converter')

var distance = window.prompt('enter number of units\n>')

var userUnit = window.prompt('enter input unit \(in, ft, yd, mi, m, km\)\n>')

var outputUnit = window.prompt('enter output unit \(in, ft, yd, mi, m, km\)\n>')

function calculate(distance, userUnit, outputUnit) {
    let values = {'in':0.0254, 'ft':0.3048, 'm':1, 'yd':0.9144, 'km':1000, 'mi':1609.34}
    let output= distance * values[userUnit]
    let finalOutput = output / values[outputUnit]
    return finalOutput 
}
// console.log(`${calculate(distance, userUnit, outputUnit)} ${outputUnit}`)

alert(`${distance} ${userUnit}s ${calculate(distance, userUnit, outputUnit).toFixed(2)} ${outputUnit}`)