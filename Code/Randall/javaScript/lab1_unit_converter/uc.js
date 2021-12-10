//lab1 Unit Converter in JS

let units = ['ft', 'mi', 'km', 'yd', 'in', 'm'];
let distance = parseFloat(prompt("What is the distance"));

let start_unit = prompt(`What are the starting units? ${units} > `)
while (units.indexOf(start_unit) == -1) {
	start_unit = prompt(`Choose from: ${units} > `)
}
if ((start_unit) == "ft") {
	var convert = distance * 3.3048;
} else if ((start_unit) == "mi") {
	var convert = distance * 1609.34;
} else if ((start_unit) == "km") {
	var convert = distance * 1000;
} else if ((start_unit) == "m") {
	var convert = distance * 1;
} else if ((start_unit) == "in") {
	var convert = distance * 0.0254;
} else if ((start_unit) == "y") {
	var convert = distance * 0.9144;
}

let end_unit = prompt(`What are the end units? ${units}`)
while (units.indexOf(end_unit) == -1) {
	end_unit = prompt(`Choose from: ${units} > `)
}
if ((end_unit) == "ft") {
	var distance2 = convert * 3.280839895;
} else if ((end_unit) == "mi") {
	var distance2 = convert * 0.0006213689;
} else if ((end_unit) == "km") {
	var distance2 = convert * 0.001;
} else if ((end_unit) == "m") {
	var distance2 = convert * 1;
} else if ((end_unit) == "in") {
	var distance2 = convert * 39.37007874;
} else if ((end_unit) == "y") {
	var distance2 = convert * 1.0936132983;
}

alert(`${distance}${start_unit} is also ${distance2}${end_unit}`)