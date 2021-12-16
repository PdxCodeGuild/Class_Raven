let button = document.querySelector('#button'),
    h1 = document.querySelector('#result')


const url = `https://favqs.com/api/qotd`

const headers = {
    Accept: 'application/json'
}

button.addEventListener('click', ()=>{
    fetchQuote()
})

function fetchQuote(){
fetch(url, {
    method: 'GET',
    headers: headers
})
    .then(response => response.json())

    .then(result => {
        console.log(result.quote.id);
        console.log(result.quote.author);
        console.log(result.quote.body);

        h1.innerHTML = result.quote.body
    })

    .catch(error => console.log('error!', error))
}