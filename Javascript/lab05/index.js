let nextPageButton = document.getElementById("nextPageButton");
let result = document.getElementById("result")
let pageNumber, queryString, newQuote;

pageNumber = 1;
queryString = "Relationships";

// notice that the base url changes from /api/qotd to /api/quotes
const url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`


const headers = {
    // ... other headers

    Authorization: `Token token=${FAVQS_API_KEY}`
}

const params = {
    page: pageNumber,
    filter: queryString
}

function processInfo (response) {
    let cleanedResponse
    cleanedResponse = response.data.quotes.map((quote) => quote.body)
    return cleanedResponse
}

function generateList (quote) {
    let updatedListing = document.createElement('h3')
    updatedListing.innerHTML =  quote
    return updatedListing
}   

nextPageButton.addEventListener('click', ()=>{
    pageNumber++
    console.log(pageNumber)
})

axios
    .get(
    url,
    {
        headers: headers
    })
    .then( response => {
        response = processInfo(response)
        response.forEach(item => {
            newQuote = generateList(item)
            result.appendChild(newQuote)
        })
        
    })
    .catch(error => console.log('error!', error))