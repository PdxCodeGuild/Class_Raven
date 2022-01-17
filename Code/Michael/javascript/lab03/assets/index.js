let stringToEncrypt, intNumberRotations;

function getInput() {
	while (
		stringToEncrypt == "" ||
		stringToEncrypt == null ||
		stringToEncrypt == undefined ||
		stringToEncrypt == " "
	) {
		// Check if input is empty
		stringToEncrypt = prompt("Enter a string to be encrypted: ");
	}

	while (
		intNumberRotations == "" ||
		intNumberRotations == null ||
		intNumberRotations == undefined ||
		isNaN(intNumberRotations)
	) {
		// Check if input is empty
		intNumberRotations = parseInt(prompt("Enter the number of rotations: "));
	}
}

function rot13(str, rotations) {
	let result = "";
	for (let i = 0; i < str.length; i++) {
		let charCode = str.charCodeAt(i);
		if (charCode >= 65 && charCode <= 90) {
			// Uppercase
			charCode = ((charCode - 65 + rotations) % 26) + 65;
		} else if (charCode >= 97 && charCode <= 122) {
			// Lowercase
			charCode = ((charCode - 97 + rotations) % 26) + 97;
		} else if (charCode >= 48 && charCode <= 57) {
			// Numbers
			charCode = ((charCode - 48 + rotations) % 10) + 48;
		}
		result += String.fromCharCode(charCode); // Convert back to string
	}
	return result;
}

getInput();
alert(`Your string '${stringToEncrypt}'
has been encrypted to '${rot13(stringToEncrypt, intNumberRotations)}'`);
