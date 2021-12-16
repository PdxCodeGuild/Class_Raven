//Version 1 of lab5

let url = "https://favqs.com/api/qotd"


let btn = document.querySelector('#button1')
btn.addEventListener('click', function(){

    function displayQuote(data){
        
            let quote = document.getElementById('quote-div')
            let newQuote = document.createElement('h1')
            
            newQuote.innerText = `
            "${data.quote.body}"\n\n  -${data.quote.author}
            `
            quote.appendChild(newQuote) 
        }

    fetch(url).then(function (response){
        return response.json() //.json() returns another promise so we have to use another .then to get the data from the
            //promise IT its fufilled
    }).then(function (data){
            // can manipulate the DOM right here with a function or hard coded in.
        displayQuote(data) //calls the displayQuote function to display the quoute on the screen 
        
    }).catch(function (error){
        alert(error) // this will alert and show the error if either of the two promises fail
    })
        
})





