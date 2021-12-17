

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

while (i=0){
    let q1 = parseInt(prompt('What is the distance in meters?'));

    let q2 = parseInt(prompt('What are the units'));

    let total = q1 * metersConvert[q2]

    console.log(typeof metersConvert)
    console.log(typeof ft)
    console.log(total + "Meters")
    console.log()

break

}

