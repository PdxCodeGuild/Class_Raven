/* Use the favqs.com api to show a random quote. To start, use https://favqs.com/api/qotd to GET a quote, then display it on the page.
The API also supports browsing quotes. */
let debugging = false;
let quoteNumber = 0;
let pageNumber = 1;
let timer1;
//if ctrl + shift + i is pressed, debugging will be toggled.
window.addEventListener("keydown", (event) => {
	if (event.code === "KeyI" && event.shiftKey) {
		debugging = !debugging;
		console.log("Debugging is now " + debugging);
	}
});

const headers = {
	Accept: "application/json",
	Authorization: `Token token=${FAVQS_API_KEY}`,
};

function backgroundImages() {
	let width = window.innerWidth; // Get the width of the window.
	let height = window.innerHeight; // This is the height of the screen.
	let deviceOrientation = window.orientation; // Doesn't actually do anything, just declaring the variable for later.

	if (width < height) {
		deviceOrientation = "portrait"; // If the width is less than the height, the device is in portrait mode.
	} else {
		deviceOrientation = "landscape"; // If the width is greater than the height, the device is in landscape mode.
	}

	let random = Math.floor(Math.random() * 10000) + 1;

	const url = `https://source.unsplash.com/random/${width}x${height}?sig=${random}&orientation=${deviceOrientation}&fit=fillmax&fill=blur`;
	fetch(url).then((data) => {
		let image = data.url;
		document.body.style.backgroundImage = `url(${image})`;
	});
}

function randomQuote() {
	clearTimeout(timer1);
	if (focus) {
		fetch("https://favqs.com/api/qotd", { headers })
			.then((response) => response.json())
			.then((data) => {
				debugging ? console.log(focus) : null;

				const author = data.quote.author;
				const quoteText = data.quote.body;
				const quoteLink = data.quote.url; // Link to the quote on favqs.com, will use later maybe.
				const quoteHTML = `<p><h4>${quoteText}</h4></p><p><i>&nbsp;-&nbsp;${author}</i></p>`;
				document.getElementById("quote").innerHTML = quoteHTML;

				timer1 = setTimeout(randomQuote, delayQuote());
				backgroundImages();
			});
	} else {
		clearTimeout(timer1);
	}
}
let focus = true;
//Pause randomQuote function if window is not active.
window.onblur = function () {
	debugging ? console.log("Window is not active.") : null;
	focus = false;
	clearTimeout(timer1);
};

//Resume randomQuote function if window is active.
window.onfocus = function () {
	debugging ? console.log("Window is active.") : null;
	focus = true;
	clearTimeout(timer1);
	randomQuote();
};
randomQuote();
function promiseTest() {
	let width = window.innerWidth;
	let height = window.innerHeight;
	let deviceOrientation = window.orientation;

	if (width < height) {
		deviceOrientation = "portrait";
	} else {
		deviceOrientation = "landscape";
	}
	let promise1 = fetch("https://favqs.com/api/qotd", { headers }).then(
		(response) => response.json()
	);
	let promise2 = fetch(
		`https://api.unsplash.com/photos/random?client_id=${UNSPLASH_API_KEY}&orientation=${deviceOrientation}`
	).then((response) => response.json());

	Promise.all([promise1, promise2]).then((values) => {
		data = values[0];
		data2 = values[1];

		const author = data.quote.author;
		const quoteText = data.quote.body;
		const quoteLink = data.quote.url; // Link to the quote on favqs.com, will use later maybe.
		const quoteHTML = `<p><h4>${quoteText}</h4></p><p><i>&nbsp;-&nbsp;${author}</i></p>`;
		const image = data2.urls.raw;

		document.body.style.backgroundImage = `url(${image}&orientation=${deviceOrientation}&fit=fillmax&fill=blur&w=${width}&h=${height})`;
		document.getElementById("quote").innerHTML = quoteHTML;
		setTimeout(promiseTest, delayQuote());
	});
}

function randomBackground() {
	let width = window.innerWidth;
	let height = window.innerHeight;
	let deviceOrientation = window.orientation;

	if (width < height) {
		deviceOrientation = "portrait";
	} else {
		deviceOrientation = "landscape";
	}

	fetch(
		`https://api.unsplash.com/photos/random?client_id=${UNSPLASH_API_KEY2}&orientation=${deviceOrientation}`
	)
		.then((response) => response.json())
		.then((data) => {
			const image = data.urls.raw;
			document.body.style.backgroundImage = `url(${image}&orientation=${deviceOrientation}&fit=fillmax&fill=blur&w=${width}&h=${height})`;
		});
}

function delayQuote() {
	const wpm = 180;
	const quote = document.getElementById("quote").innerHTML;
	const quoteLength = quote.length;
	const words = quote.split(" ");
	const wordCount = words.length;
	const avgWordLength = quoteLength / wordCount;

	const delay = (quoteLength / avgWordLength / wpm) * 60000 + 2500;
	debugging ? console.log(delay) : null;
	return delay;
}

function searchQuotes(quoteNumber, pageNumber) {
	// Disable elements while fetching.
	document.getElementById("search-box").disabled = true;
	document.getElementById("search-box").style.cursor = "not-allowed";
	document.getElementById("search").disabled = true;
	document.getElementById("search").style.cursor = "not-allowed";
	document.getElementById("random-btn").disabled = true;
	document.getElementById("random-btn").style.cursor = "not-allowed";
	document.getElementById("left-btn").disabled = true;
	document.getElementById("left-btn").style.cursor = "not-allowed";
	document.getElementById("right-btn").disabled = true;
	document.getElementById("right-btn").style.cursor = "not-allowed";

	const searchTerm = document.getElementById("search-box").value;
	fetch(
		`https://favqs.com/api/quotes?filter=${searchTerm}&page=${pageNumber}`,
		{
			headers,
		}
	)
		.then((response) => response.json())
		.then((data) => {
			document.getElementById("search-box").disabled = false;
			document.getElementById("search-box").style.cursor = "auto";
			document.getElementById("search").disabled = false;
			document.getElementById("search").style.cursor = "auto";

			if (quoteNumber > data.quotes.length - 1) {
				quoteNumber = data.quotes.length - 1;
			}
			debugging ? console.log(quoteNumber, " quoteNumber") : null;
			let author;
			try {
				author = data.quotes[quoteNumber].author;
			} catch (error) {
				author = `Unknown [${error}]`;
			}

			const quoteText = data.quotes[quoteNumber].body;
			const quoteLink = data.quotes[quoteNumber].url; // Link to the quote on favqs.com, will use later maybe.
			const quoteHTML = `<p><h4>${quoteText}</h4></p><p><i>&nbsp;-&nbsp;${author}</i></p>`;
			debugging ? console.log(data) : null;

			if (data.quotes.length === 1) {
				document.getElementById("quote-result").innerHTML =
					"<p><h1>No quotes found.</h1></p>";
			} else {
				document.getElementById("quote-result").innerHTML = quoteHTML;
				document.getElementById("random-btn").disabled = false;
				document.getElementById("random-btn").style.cursor = "auto";
			}
			if (data.last_page === false) {
				//Enable right-btn
				document.getElementById("right-btn").disabled = false;
				document.getElementById("right-btn").style.cursor = "auto";
			} else {
				//Disable right-btn
				document.getElementById("right-btn").disabled = true;
				document.getElementById("right-btn").style.cursor = "not-allowed";
			}

			if (data.page === 1) {
				//Disable left-btn
				document.getElementById("left-btn").disabled = true;
				document.getElementById("left-btn").style.cursor = "not-allowed";
			} else {
				//Enable left-btn
				document.getElementById("left-btn").disabled = false;
				document.getElementById("left-btn").style.cursor = "auto";
			}
			pageNumber = data.page;
			backgroundImages();
			//randomBackground(); // Disabled because of lack of API key.
		});
}

// Event listeners
document.getElementById("search-box").addEventListener("keydown", (event) => {
	if (event.code === "Enter") {
		(quoteNumber = 0), (pageNumber = 1);
		searchQuotes(quoteNumber, pageNumber);
	}
});
// Event Listener for Search
document.getElementById("search").addEventListener("click", function (_event) {
	(quoteNumber = 0), (pageNumber = 1);
	searchQuotes(quoteNumber, pageNumber);
});
// Event Listener for Random
document
	.getElementById("random-btn")
	.addEventListener("click", function (_event) {
		//Random Number
		quoteNumber = Math.floor(Math.random() * 24);
		debugging ? console.log(quoteNumber) : null;
		searchQuotes(quoteNumber, pageNumber);
	});
// Event Listener for Next
document
	.getElementById("right-btn")
	.addEventListener("click", function (_event) {
		pageNumber++;
		debugging ? console.log(pageNumber) : null;
		searchQuotes(quoteNumber, pageNumber);
	});
// Event Listener for Previous
document
	.getElementById("left-btn")
	.addEventListener("click", function (_event) {
		pageNumber--;
		debugging ? console.log(pageNumber) : null;
		searchQuotes(quoteNumber, pageNumber);
	});

//promiseTest();  This fuction works, but because of API limitations and lack of API keys, I'm not using it.

backgroundImages();
