let user = prompt("Enter credit card digits: ")
console.log(user);



// let test = [1, 2, 4, 5]
// console.log(test);

let userNum = parseInt(user)

console.log(userNum);


let userNumList = user.split('')

console.log(userNumList);

let lastDigit = parseInt(userNumList.pop())

let reverseList = userNumList.reverse()


console.log(reverseList);

