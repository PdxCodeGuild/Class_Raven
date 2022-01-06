let nextPageButton = document.getElementById("nextPageButton");
let result = document.getElementById("result") // target for templated quotes
let bootstrapQuoteTemplate = document.getElementById("bootstrapQuoteTemplate")
let submitButton = document.getElementById("searchTopic") // Search button 
let previousButton = document.getElementById("previousPageButton") // Previous button
let pageNumberValue = document.getElementById("pageNumberValue") 
let queryString = "running" // search topic input field
let quoteTemplate = document.querySelector("#bootstrapQuoteTemplate") // update when the time comes: "bootstrapQuoteTemplate"

let pageNumber, newQuote;

pageNumber = 1;

let url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`

const headers = {
    Authorization: `Token token=${FAVQS_API_KEY}`
}

const params = {
    page: pageNumber,
    filter: queryString
}

// to replace processInfo and processAuthors
function newProcess (response) {
    let fullQuote = response.data.quotes.map((quote) => ({quote:quote.body, author:quote.author}))
    return fullQuote
}

// Takes in a single array of {body, author} and fills template
function newFillTemplate (quote) {
    let newQuote = document.createElement('div') // create div for a new quote
    let newTemplate = quoteTemplate.content.cloneNode(true) // copy template from index.html
    newQuote.appendChild(newTemplate) // add the content to the div
    let quoteText = newQuote.querySelector('.blockquote') // select the inner element of the quote template 
    let quoteAuthor = newQuote.querySelector('#quote-author')
    quoteText.innerHTML = quote.quote // set the quote text
    quoteAuthor.innerHTML = quote.author
    result.appendChild(quoteText)
    result.appendChild(quoteAuthor)
    return
}

function lastPage (jsonOutput) {
    if (jsonOutput.data.last_page) {
        // True means this is the last page. Deactivate the Next Button.
        deactivateTheButton(nextPageButton)
        return 
    } else if (!jsonOutput.data.last_page){
        // False means this is NOT the last page. Re-activate the button.
        buttonReactivation(nextPageButton);
        return 
    } else {
        console.log('did not read last page info')
    } return
}

function lockPreviousPage (pageNumber) {
    if (pageNumber <=1 ) {
        deactivateTheButton(previousButton)
        return
    } else {
        previousButtonReactivation(previousButton)
        return
    }
}

function activateTheButton (button) {
    button.addEventListener('click', pageActivation)
}

function pageActivation () {
    url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`
    getQuotes(url)
}

function buttonReactivation (button) {
    button.setAttribute('class', 'btn btn-outline-primary btn-block my-2')
    button.addEventListener('click', pageActivation)
}

function previousButtonReactivation (button) {
    button.setAttribute('class', 'btn btn-outline-primary btn-block my-2')
    button.addEventListener('click', previousButtonActivation)
}

function previousButtonActivation () {
    pageNumber = pageNumber-2
    url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`
    getQuotes(url)
}

// reformats the next page button to outline red. Also removes 'click' event listener
function deactivateTheButton (button) {
    button.removeAttribute("class")
    button.setAttribute('class', 'btn btn-outline-danger btn-block my-2 disabled')
    button.removeEventListener("click", pageActivation)
    button.removeEventListener('click', previousButtonActivation)
}

function getQuotes (url) {
    axios
    .get(
    url,
    {
        headers: headers
    })
    .then( response => {
        pageNumberValue.innerHTML = `-- Page ${pageNumber} --`
        lockPreviousPage(pageNumber)
        pageNumber++
        console.log(url)
        result.innerHTML = '' // clear result area
        lastPage(response) // disables next page button if there are no additional pages remaining
        response = newProcess(response)
        
        response.forEach(item => {
            newFillTemplate(item)
        })
        
    })
    .catch(error => console.log('error!', error))
}

getQuotes(url)
activateTheButton(nextPageButton)

submitButton.addEventListener('click', ()=>{
    pageNumber = 1;
    console.log(pageNumber)
    queryString = document.getElementById("topicText").value
    url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`
    getQuotes(url)
})

