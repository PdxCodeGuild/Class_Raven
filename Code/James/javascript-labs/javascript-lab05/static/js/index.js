let button = document.querySelector('#button-quote'),
    button2 = document.querySelector('#button-page'),
    h1 = document.querySelector('#result'),
    h3 = document.querySelector('#author')
var pageNumber = pageNumber =1



const url = `https://favqs.com/api/quotes?page=${1}`

const headers = {
    Accept: 'application/json'
}
button2.addEventListener('click', ()=>{
    pageNumber +=1

})


button.addEventListener('click', ()=>{
    fetchQuote()
})

function fetchQuote(){
fetch(url, {
    method: 'GET',
    headers: headers
})

    .then(result => {
        // quotes = {
        //     id: result.quote.id,
        //     author: result.quote.author,
        //     quote: result.quote.body
        // }
        // console.log(result.quote.id);
        // console.log(result.quote.author);
        // console.log(result.quote.body);

        // h1.innerHTML = result.quote.body
        // h3.innerHTML = result.quote.author

        console.log(result);
    })

    .catch(error => console.log('error!', error))
}