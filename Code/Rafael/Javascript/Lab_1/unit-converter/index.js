

/*

//var meters = parseInt(prompt("Please enter meters:"));
let feet = meters / 0.3048;
console.log(feet + " feet");


let q1 = parseInt(prompt('What is the distance in meters?'));


let q2 = parseInt(prompt('What are the units'));

let metersConvert = {
    ft: 0.3048, 
    m: 1, 
    km: 1000, 
    mi: 1609.34 
};

//console.log(typeof metersConvert["mi"])

let mi = q1 * metersConvert.mi
let m = q1 * metersConvert.m
let km = q1 * metersConvert.km
let ft = q1 * metersConvert.mi   

if (q2 = 'km'){
    console.log(km)
}else if (q2 === 'm'){
    console.log(m)
}else if (q2 === 'mi'){
    console.log(mi)
}else if (q2 === 'ft'){
    console.log(ft)
}else{
    console.log(prompt('Try again, select either miles: "mi", meters: "m", kilometers: "km" or feet: "ft" after entering a distance'))
}  
    

//console.log(typeof metersConvert)
//console.log(typeof ft)
//console.log(metersConvert + "Meters")
//console.log()

*/


let metersConvert = {
    'ft': 0.3048, 
    'm': 1, 
    'km': 1000, 
    'mi': 1609.34    
}


let i = 0


while (i < 3){
    

    let q2 = prompt('What are the units to convert(choose either: "ft", "m", "km", "mi" ');
    let q1 = parseInt(prompt('What is the distance in meters?'));

    let total = q1 * metersConvert[q2]

    console.log(q1 + q2 + " " + "is =" + " " + total + " Meters")


    

    break

}


/*

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
*/