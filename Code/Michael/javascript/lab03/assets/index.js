let stringToEncrypt, intNumberRotations;

function getInput() {
	while (
		stringToEncrypt == "" ||
		stringToEncrypt == null ||
		stringToEncrypt == undefined ||
		stringToEncrypt == " "
	) {
		stringToEncrypt = prompt("Enter a string to be encrypted: ");
	}

	while (
		intNumberRotations == "" ||
		intNumberRotations == null ||
		intNumberRotations == undefined ||
		isNaN(intNumberRotations)
	) {
		intNumberRotations = parseInt(prompt("Enter the number of rotations: "));
	}
}

function rot13(str, rotations) {
	let result = "";
	for (let i = 0; i < str.length; i++) {
		let charCode = str.charCodeAt(i);
		if (charCode >= 65 && charCode <= 90) {
			charCode = ((charCode - 65 + rotations) % 26) + 65;
		} else if (charCode >= 97 && charCode <= 122) {
			charCode = ((charCode - 97 + rotations) % 26) + 97;
		} else if (charCode >= 48 && charCode <= 57) {
			charCode = ((charCode - 48 + rotations) % 10) + 48;
		}
		result += String.fromCharCode(charCode);
	}
	return result;
}

getInput();
alert(`Your string '${stringToEncrypt}'
has been encrypted to '${rot13(stringToEncrypt, intNumberRotations)}'`);
