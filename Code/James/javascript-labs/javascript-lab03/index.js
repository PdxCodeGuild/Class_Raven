let user = prompt("Enter credit card digits: ")
console.log(user);





let userNumList = user.split('')

userNumList = userNumList.map((number)=> parseInt(number))


console.log(userNumList);

// let lastDigit = parseInt(userNumList.pop())

let reverseList = userNumList.reverse()

// for (let i=0; i<reverseList.length; i++){
//     reverseList[i] === parseInt(reverseList[i])
    
// }


console.log(reverseList);

