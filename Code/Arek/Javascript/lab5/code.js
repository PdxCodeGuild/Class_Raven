//Version 1 of lab5





let queryString = document.getElementById('filterType').value
let url = "https://favqs.com/api/quotes"
let pageNumber = 0
let quoteNum = 0
let back = document.querySelector('#back-page')
let next = document.querySelector('#next-page')
let btn = document.querySelector('#button1')
let lastPage = false

function displayQuote(data){
    console.log(data.quotes.length) - 1
    let pagenum = document.getElementById('page-number')
    let quote = document.getElementById('quote-div')
    
    pagenum.innerHTML = `
        <article>Page Number: ${pageNumber}</article>
        <article>Last Page = ${data.last_page}</article>
        
    `
        
    quote.innerHTML = `
        <h1>${data.quotes[quoteNum].body}\n</h1>
        
         
        `
    quoteNum += 1
    
    

      
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
    quoteNum = 0
    pageNumber += 1
    apiCall()
})









