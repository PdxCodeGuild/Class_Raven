//Version 1 of lab5




let pageNumber = 1
let queryString = 'astronomy'
let url = "https://favqs.com/api/quotes"




let btn = document.querySelector('#button1')
btn.addEventListener('click', function(){

    function displayQuote(data){
        
            let quote = document.getElementById('quote-div')
            let newQuote = document.createElement('h1')
            
            newQuote.innerText = `
            "${data.quotes[Math.floor(Math.random()* data.quotes.length)].body}"\n\n
             
            `
            quote.appendChild(newQuote) 
        }
    axios({
        method: 'get',
        url: url,
        headers: {
            Authorization: `Token token=${FAVQS_API_KEY}`
        },
        params: {
            page: pageNumber,
            filter: queryString
        }
            
    })
    .then(function (response){
        console.log(response.data.quotes[Math.floor(Math.random()* response.data.quotes.length)].body)
        displayQuote(response.data)
        
    })
    .catch(function (error){
            console.log(error)
    })

})  





