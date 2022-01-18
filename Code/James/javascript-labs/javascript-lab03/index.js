'Credit Card Validation'
let user = prompt("Enter credit card digits: ")
console.log(user);



let userNumList = user.split('')

userNumList = userNumList.map((number)=> parseInt(number))

console.log(userNumList);

let lastDigit = userNumList.pop()


console.log(lastDigit);

let reverseList = userNumList.reverse()
console.log(reverseList);


for (let i = 0; i<reverseList.length; i+=2){
   reverseList[i] = reverseList[i]*2

}

console.log(reverseList);


for (let i = 0; i<reverseList.length; i++){
    if (reverseList[i]> 9){
        reverseList[i] = reverseList[i]-9
    }
}
console.log(reverseList);

let sum = reverseList.reduce((previousValue, currentValue)=>{
    return previousValue + currentValue

}, 0)
console.log(sum)

let sumDigit = Math.floor((sum / 1) % 10)
console.log(sumDigit);

if (sumDigit == lastDigit){
    alert('Valid!')
    
}









