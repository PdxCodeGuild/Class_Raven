

let abcObject = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];



console.log(typeof abcObject)
console.log(abcObject)


function rot13(output){

    let rotations = 13
    console.log(typeof rotations)

    
    var userInput = ''
    console.log(typeof userInput)

    

    for (let i of output){

    if (i = " "){
        var userInput = userInput + " "
    }

    else{
        var indexPosition = abcObject[i] + parseInt(rotations)
    }
    
    if (indexPosition < 26){
        let userInput = userInput + abcObject[indexPosition]
    }

    else{
        let userInput = userInput + abcObject[indexPosition % 26] 
    }

    
    var userInput = prompt("Enter text to cipher in lower-case english only: ");

    console.log(rot13(userInput))
    
    return userInput



}

}


