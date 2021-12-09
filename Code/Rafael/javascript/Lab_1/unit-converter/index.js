
//var meters = parseInt(prompt("Please enter distance in meters to convert to feet:"));
//let feet = meters / 0.3048;
//console.log(feet + " feet");

let q2 = prompt('What are the units to convert(choose either: "ft", "m", "km", "mi" ');
let q1 = parseInt(prompt('What is the distance in meters?'));


let metersConvert = {
    ft: 0.3048, 
    m: 1, 
    km: 1000, 
    mi: 1609.34 
};

//console.log(typeof metersConvert["mi"])


// Placed this within the console log if & else if
//let mi = q1 * metersConvert.mi
//let m = q1 * metersConvert.m
//let km = q1 * metersConvert.km
//let ft = q1 * metersConvert.mi   

if (q2 == 'km'){
    console.log(alert(q1 * 1000 + ' meters'))
}else if (q2 == 'm'){
    console.log(alert(q1 * 1 + ' meters'))
}else if (q2 == 'mi'){
    console.log(alert(q1 * 1609.34 + ' meters'))
}else if (q2 == 'ft'){
    console.log(alert(q1 * 0.3048 + ' meters'))
}else{
    console.log(prompt('Try again, select either miles: "mi", meters: "m", kilometers: "km" or feet: "ft" after entering a distance'))
}  
    

//console.log(typeof metersConvert)
//console.log(typeof ft)
//console.log(metersConvert + "Meters")
//console.log()