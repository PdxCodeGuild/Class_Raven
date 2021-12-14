let conversion_table = {
	meters: 1,
	feet: 0.3048,
	yards: 0.9144,
	kilometers: 1000,
	miles: 1609.34,
	inches: 0.0254,
};

function convert(value, from, to) {
	return (value * conversion_table[from]) / conversion_table[to];
}

function convert_prompt() {
	let value = "";
	let from = "";
	let to = "";
	let conversion_string = "";
	for (let unit in conversion_table) {
		conversion_string += "'" + unit + "', ";
	}
	while (isNaN(value) || value == "") {
		value = prompt("Enter a value to convert: ");
	}

	while (!conversion_table.hasOwnProperty(from)) {
		from = prompt(`Enter a unit to convert from: 
${conversion_string}`);
	}

	while (!conversion_table.hasOwnProperty(to)) {
		to = prompt(`Enter a unit to convert to: 
${conversion_string}`);
	}
	let result = convert(value, from, to).toFixed(4);
	alert(`${value} ${from} is equal to ${result} ${to}`);
}

convert_prompt();
