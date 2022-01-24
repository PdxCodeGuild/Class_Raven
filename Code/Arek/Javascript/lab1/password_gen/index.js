

function createPassword(long){
    let newPassword = []
    let check = 0
    let masterList = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','"', "'",'!','@','#','$','%','^','&','*','(',')','-','_','.',',','/','{','}','~','?']
    
    while (check != long){
        newPassword.push(masterList[Math.floor(Math.random()*masterList.length)])
        check += 1
    }


    
    newPassword = newPassword.join('')
    return newPassword


}



var long = parseFloat(prompt("Enter the character length of that password: "))

console.log(createPassword(long))