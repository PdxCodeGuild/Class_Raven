/* Use the favqs.com api to show a random quote. To start, use https://favqs.com/api/qotd to GET a quote, then display it on the page.
The API also supports browsing quotes. */

const headers = {
	Accept: "application/json",
	Authorization: `Token token=${FAVQS_API_KEY}`,
};

function randomQuote() {
	fetch("https://favqs.com/api/qotd", { headers })
		.then((response) => response.json())
		.then((data) => {
			const author = data.quote.author;
			const quoteText = data.quote.body;
			const quoteLink = data.quote.url; // Link to the quote on favqs.com, will use later maybe.
			const quoteHTML = `<p><h4>${quoteText}</h4></p><p><i>&nbsp;-&nbsp;${author}</i></p>`;
			document.getElementById("quote").innerHTML = quoteHTML;
			console.log(data);
		});
}

randomQuote();

//setInterval(randomQuote, 15000);

let randomNumber = Math.floor(Math.random() * (15000 - 5000 + 1)) + 5000;
setInterval(randomQuote, randomNumber);
