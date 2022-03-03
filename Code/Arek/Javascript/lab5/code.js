//Version 1 of lab5





let queryString = document.getElementById('filterType').value
let url = "https://favqs.com/api/quotes"
let pageNumber = 1
let quoteNum = 0
let back = document.querySelector('#back-page')
let next = document.querySelector('#next-page')
let btn = document.querySelector('#button1')
let lastPage = false

let newQuote = document.createElement('div')

function displayQuote(data){
    let count = 0
    console.log(data.quotes.length) - 1
    let pagenum = document.getElementById('page-number')
    let quote = document.getElementById('quote-div')
    let quoteList = []
    quote.innerHTML = ``
    
    
   
    pagenum.innerHTML = `
        <article>Page Number: ${pageNumber}</article>
        <article>Last Page = ${data.last_page}</article>
        
    `
    for (thing in data.quotes){
        quoteList.push(data.quotes[count].body)
        count += 1

    }
    count = 0
    for (item in quoteList){
       let newquote = document.createElement('div')
       newquote.innerHTML = `
        <h1>${quoteList[count]}</h1>
       `
        quote.appendChild(newquote)
        count += 1
    }
    console.log(quoteList)

    
    
    
    
    

      
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
    queryString = document.getElementById('filterType').value
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









