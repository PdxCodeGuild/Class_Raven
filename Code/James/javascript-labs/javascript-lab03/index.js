let user = prompt("Enter credit card digits: ")
console.log(user);





let userNumList = user.split('')

userNumList = userNumList.map((number)=> parseInt(number))

console.log(userNumList);

let lastDigit = userNumList.pop()

console.log(lastDigit);

let reverseList = userNumList.reverse()
console.log(reverseList);


for (let i = 1; i<reverseList.length; i+=2){
   reverseList[i] = Math.pow(reverseList[i], 2)

}

console.log(reverseList);

// console.log(reverseList);
// console.log(doubleOther);







