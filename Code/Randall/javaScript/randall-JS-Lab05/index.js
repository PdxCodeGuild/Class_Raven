//Targets HTML items
let quoteDiv = document.querySelector("#quote")
let getQuoteBtn = document.querySelector("#getQuote")
let authorDiv = document.querySelector("#author")
let adderValue = document.querySelector('#adderValue')
	//API info
let headerObj = {
	headers: {
		Authorization: 'Token token="10f5d7e2de389a39e3c039e47742845d"'
	}
}
let url = "https://favqs.com/api/quotes"
getQuoteBtn.addEventListener("click", function() {
	let filterText = adderValue.value ? "&filter=" + adderValue.value + '&type=tag' : ''
	let adder = "?page=" + Math.floor(Math.random() * 26) + filterText
		//Ask API for specified category and returns json file
	let apigetwithsearchperams = fetch(url + adder, headerObj).then(function(response) {
		return response.json()
	}).then(function(data) {
		//Randomly pick quote from json file
		let ind = Math.floor(Math.random() * 25)
		quoteText = data.quotes[ind].body
		quoteAuthor = data.quotes[ind].author
		authorDiv.innerText = `-${quoteAuthor}`
		quoteDiv.innerText = `${quoteText}`
	})
})