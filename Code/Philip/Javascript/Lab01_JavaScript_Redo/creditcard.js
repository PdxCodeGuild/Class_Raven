/*
Lab 01 JavaScript Redo
Random Password Generator
By Philip Bartoo
12/10/2021
PDX Code Guild

Directions:
Let's write a function which returns whether a string containing a credit card number is valid as a boolean. The steps are as follows:
Convert the input string into a list of ints
Slice off the last digit. That is the check digit.
Reverse the digits.
Double every other element in the reversed list.
Subtract nine from numbers over nine.
Sum all values.
Take the second digit of that sum.
If that matches the check digit, the whole card number is valid.
For example, the worked out steps would be:
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5
4 5 5 6 7 3 7 5 8 6 8 9 9 8 5
5 8 9 9 8 6 8 5 7 3 7 6 5 5 4
10 8 18 9 16 6 16 5 14 3 14 6 10 5 8
1 8 9 9 7 6 7 5 5 3 5 6 1 5 8
85
5
Valid!'''
*/

//Prompt user for a Credit Card number and split it into an array
let numberArr = prompt("Enter a Credit Card Number: ").split("");
//Pop out the last digit and save as a variable for later
let lastNumber = numberArr.pop();
//Reverse the array and save as a variable
let reversedArr = numberArr.reverse();
//Loop through every other element in array and multiply the element by 2
for (let i=0; i<reversedArr.length; i += 2){
    reversedArr[i] *= 2;
    reversedArr.join(",");
}
//Loop through each element in array and subtract 9 if element value is greater than 9
for (let i=0; i<reversedArr.length; i++){
    if (reversedArr[i]>9) {
        reversedArr[i]-=9;
        reversedArr.join(",");
    }
}
//Set a variable to hold the sum and loop through and sum each element in the array, note that JavaScript will concatenate values if they aren't parsed as integers
var total = 0;
for (i=0; i<reversedArr.length; ++i) {
    total += parseInt(reversedArr[i]);
}
//Use modulus to pull the last digit of the sum
let lastDigit = total % 10
//Check if the lastDigit is equal to the lastNumber pulled out earlier, if they are equal the card is valid
if (lastDigit==lastNumber) {
    greeting = "Valid Card";
} else {
    greeting = "Card Not Valid";
}

//alert(reversedArr);
//alert(total);
//alert(lastDigit);
//alert(lastNumber);
alert(greeting);

/*Note: My first serious attempt at writing JavaScript and it was slow getting started as I was trying to understand the syntax.
Using the 'prompt' to check if the code was working at each step helped to confirm that each step was working as intended.
I will need to shift to the log in the future to get better error information and help troubleshooting.
The next step in this code set is to go through and delete excess code.
Major lessons learned included for loops, the need to parseInt to convert to integer, and JavaScript commands.*/


        

