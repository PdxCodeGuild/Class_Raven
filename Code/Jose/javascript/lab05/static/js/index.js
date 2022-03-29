let requestedinputText, searchButton, previousPageButton, nextPageButton, 
quoteText, quoteAuthor, quoteDiv, quoteDivAuthor, userSearch, pageNumber

searchButton = document.querySelector('#searchButton');
previousPageButton = document.querySelector('#previousPageButton');
nextPageButton = document.querySelector('#nextPageButton');
resultText = document.querySelector('#resultText');
resultAuthor = document.querySelector('#resultAuthor');

quoteNumber = 0;
pageNumber = 1;

let url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${requestedinputText}`

const headers = {
	Accept: 'application/json',
	Authorization: `Token token=${FAVQS_API_KEY}`
}



function fetchQuoteData() {
	requestedinputText = document.querySelector('#searchInput').value;
	
	fetch(`https://favqs.com/api/quotes?page=${pageNumber}&filter=${requestedinputText}`, {headers})
		.then((response) => response.json())
		.then((data) => {
			author = data.quotes[quoteNumber].author;
			quoteText = data.quotes[quoteNumber].body;
			resultText.innerHTML = quoteText;
			resultAuthor.innerHTML = author;
			amountofReturnedQuotes = data.quotes.length
			// Saving the data in a variable to use outside this scope
			returnedQuotes = data
			//console.log(returnedQuotes)
			//console.log(amountofReturnedQuotes)
		})
}

function nextPage() {
	if (quoteNumber < amountofReturnedQuotes-1){
		quoteNumber++
		author = returnedQuotes.quotes[quoteNumber].author;
		quoteText = returnedQuotes.quotes[quoteNumber].body;
		resultText.innerHTML = quoteText;
		resultAuthor.innerHTML = author;
	} else {
		alert("You've reached the end of the quotes!")
	}
}

function previousPage() {
	if (quoteNumber > 0) {
		quoteNumber--
		author = returnedQuotes.quotes[quoteNumber].author;
		quoteText = returnedQuotes.quotes[quoteNumber].body;
		resultText.innerHTML = quoteText;
		resultAuthor.innerHTML = author;
	} else {
		alert('This is the beginning of the quotes!')
	}
}


searchButton.onclick = function(){
	fetchQuoteData()
}

nextPageButton.onclick = function(){
	nextPage()
}

previousPageButton.onclick = function(){
	previousPage()
}

//quoteText = data.quote.body;
//quoteAuthor = data.quote.author;
//resultText.innerHTML = quoteText;
//resultAuthor.innerHTML = quoteAuthor;