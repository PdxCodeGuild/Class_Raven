console.log('Password Generator')
// let punctuation = `!"#$%&'()*+,-./:;<=>?@[\]^_{|}~`
// punctuation=[!, #, $, %, &, (, ), *, +, -, ., /, :, ;, <, =, >, ?, @, [, \, ], ^, _, {,|, }, ~]
// characters =`A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,1,2,3,4,5,6,7,8,9,0`

// let randomUpper = Math.floor(Math.random() * upper.length)
// let randomLower = Math.floor(Math.random() * lower.length)
// let randomNumber = Math.floor(Math.random() * number.length)
// let randomPunctuation = Math.floor(Math.random() * punctuation.length)

// let randomCharacter = Math.floor(Math.random() * characters.length)

var number = window.prompt('Enter desired number of characters in password\n>')

function generate(number){
    let characters =`abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"#$%&'()*+,-./:;<=>?@[\]^_{|}~` 
    let i=0
    let password=''
    while (i < number){
        let randomCharacter = characters.charAt(Math.floor(Math.random() * characters.length))//93
        password = password.concat(randomCharacter)
        i++
    }
    return password
}

alert(`Your generated password is:${generate(number)}`)