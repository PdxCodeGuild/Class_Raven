//Version 1 of lab5





let queryString = document.getElementById('filterType').value
let url = "https://favqs.com/api/quotes"
let pageNumber = 1
let quoteNum = 0
let back = document.querySelector('#back-page')
let next = document.querySelector('#next-page')
let btn = document.querySelector('#button1')
let lastPage = false
let count = 0
let newQuote = document.createElement('div')

function displayQuote(data){
    console.log(data.quotes.length) - 1
    let pagenum = document.getElementById('page-number')
    let quote = document.getElementById('quote-div')
    
    
    
   
    pagenum.innerHTML = `
        <article>Page Number: ${pageNumber}</article>
        <article>Last Page = ${data.last_page}</article>
        
    `
    for (item of data.quotes){
        newQuote.innerHTML = `
            <h1>${item.body}</h1>
        
        
        `
        quote.appendChild(newQuote)
    }
    
    
    

      
}

function apiCall(){
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
        console.log(response.data)
        displayQuote(response.data)
        return response.data
        
    })
    .catch(function (error){
        console.log(error)
    })
}


btn.addEventListener('click', function(){
    
    console.log(queryString)
    apiCall()

    
})

back.addEventListener('click', function(){
    count = 0
    if (pageNumber === 0){
        stop()
    }
    else{
        quoteNum = 0
        pageNumber -= 1
        apiCall()
    }
    
})
next.addEventListener('click', function(){
    count = 0
    quoteNum = 0
    pageNumber += 1
    apiCall()
})









