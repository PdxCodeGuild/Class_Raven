/* Use the favqs.com api to show a random quote. To start, use https://favqs.com/api/qotd to GET a quote, then display it on the page.
The API also supports browsing quotes. */
let debugging = false; // Set this to true to see console.log() statements. Keybind: Shift + I
let quoteNumber = 0;
let pageNumber = 1;
let timer1;
let focus = true;

const headers = {
	Accept: "application/json", // This is the type of data that we are expecting back from the server.
	Authorization: `Token token=${FAVQS_API_KEY}`, // This is the key that we need to use to access the API.
};

// This is to change the background image every time the quote changes.
function backgroundImages() {
	let width = window.innerWidth; // Get the width of the window.
	let height = window.innerHeight; // This is the height of the screen.
	let deviceOrientation = window.orientation; // Doesn't actually do anything, just declaring the variable for later.

	if (width < height) {
		// If the width is less than the height, then the device is in portrait mode.
		deviceOrientation = "portrait";
	} else {
		// If the width is greater than the height, then the device is in landscape mode.
		deviceOrientation = "landscape";
	}

	let random = Math.floor(Math.random() * 10000) + 1; // This is to make sure that the background image is different every time.

	const url = `https://source.unsplash.com/random/${width}x${height}?sig=${random}&orientation=${deviceOrientation}&fit=fillmax&fill=blur`; // This is the url to the background image.
	fetch(url).then((data) => {
		// This is to fetch the background image.
		let image = data.url; // This is to get the url of the background image.
		document.body.style.backgroundImage = `url(${image})`; // This is to set the background image.
	});
}

// This is to get a random quote from the API.
function randomQuote() {
	clearTimeout(timer1); // This is to prevent the quote from changing when the window is not active.
	if (focus) {
		// This is to prevent the quote from changing when the window is not active.
		fetch("https://favqs.com/api/qotd", { headers }) // This is to fetch the quote from the API.
			.then((response) => response.json()) // This is to get the response from the API.
			.then((data) => {
				// This is to get the data from the API.
				debugging ? console.log(focus) : null;
				const author = data.quote.author; // This is to get the author of the quote.
				const quoteText = data.quote.body; // This is to get the quote.
				const quoteHTML = `<p><h4>${quoteText}</h4></p><p><i>&nbsp;-&nbsp;${author}</i></p>`; // This is to create the HTML for the quote.
				document.getElementById("quote").innerHTML = quoteHTML; // This is to display the quote on the page.
				timer1 = setTimeout(randomQuote, delayQuote()); // This is to set a timer to change the quote.
				backgroundImages(); // This is to change the background image every time the quote changes.
			});
	} else {
		clearTimeout(timer1); // This is to prevent the quote from changing when the window is not active. Probably not needed anymore.
	}
}

//This is the function that runs when the window is not active.
window.onblur = function () {
	debugging ? console.log("Window is not active.") : null;

	// The below is to prevent the quote from changing when the window is not active.
	focus = false;
	clearTimeout(timer1);
};

//This is the function that runs when the window is active.
window.onfocus = function () {
	debugging ? console.log("Window is active.") : null;
	focus = true; // This is to allow the quote to change when the window is active.
	clearTimeout(timer1); //This is to prevent the quote from changing when the window is not active. Probably not needed anymore.
	randomQuote(); //This is to start the quote changing when the window is active.
};

//This is a test function to see if promises work. Not using it, but does work.
function promiseTest() {
	let width = window.innerWidth; // Get the width of the window.
	let height = window.innerHeight; // This is the height of the screen.
	let deviceOrientation = window.orientation; // Doesn't actually do anything, just declaring the variable for later.

	if (width < height) {
		// If the width is less than the height, then the device is in portrait mode.
		deviceOrientation = "portrait";
	} else {
		// If the width is greater than the height, then the device is in landscape mode.
		deviceOrientation = "landscape";
	}
	let promise1 = fetch("https://favqs.com/api/qotd", { headers }).then(
		// This is to fetch the quote from the API.
		(response) => response.json() // This is to get the response from the API.
	);
	let promise2 = fetch(
		`https://api.unsplash.com/photos/random?client_id=${UNSPLASH_API_KEY}&orientation=${deviceOrientation}` // This is to fetch the background image.
	).then((response) => response.json()); // This is to get the response from the API.
	Promise.all([promise1, promise2]).then((values) => {
		// This is to get both the quote and the background image.
		data = values[0]; // This is to get the quote from the API.
		data2 = values[1]; // This is to get the background image from the API.
		const author = data.quote.author; // This is to get the author of the quote.
		const quoteText = data.quote.body; // This is to get the quote.
		const quoteHTML = `<p><h4>${quoteText}</h4></p><p><i>&nbsp;-&nbsp;${author}</i></p>`; // This is to create the HTML for the quote.
		const image = data2.urls.raw; // This is to get the url of the background image.
		document.body.style.backgroundImage = `url(${image}&orientation=${deviceOrientation}&fit=fillmax&fill=blur&w=${width}&h=${height})`; // This is to set the background image.
		document.getElementById("quote").innerHTML = quoteHTML; // This is to display the quote on the page.
		setTimeout(promiseTest, delayQuote()); // This is to set a timer to change the quote.
	});
}

// This is to get a random background image from the API.
function randomBackground() {
	let width = window.innerWidth; // Get the width of the window.
	let height = window.innerHeight; // This is the height of the screen.
	let deviceOrientation = window.orientation; // Doesn't actually do anything, just declaring the variable for later.

	if (width < height) {
		// If the width is less than the height, then the device is in portrait mode.
		deviceOrientation = "portrait";
	} else {
		// If the width is greater than the height, then the device is in landscape mode.
		deviceOrientation = "landscape";
	}

	fetch(
		`https://api.unsplash.com/photos/random?client_id=${UNSPLASH_API_KEY2}&orientation=${deviceOrientation}`
	) // This is to fetch the background image.
		.then((response) => response.json()) // This is to get the response from the API.
		.then((data) => {
			// This is to get the background image from the API.
			const image = data.urls.raw; // This is to get the url of the background image.
			document.body.style.backgroundImage = `url(${image}&orientation=${deviceOrientation}&fit=fillmax&fill=blur&w=${width}&h=${height})`; // This is to set the background image.
		});
}

// This is to get a calculated delay for the quote changing.
function delayQuote() {
	const wpm = 180; // This is the average words per minute for humans.
	const quote = document.getElementById("quote").innerHTML; // This is to get the quote.
	const quoteLength = quote.length; // This is to get the length of the quote.
	const words = quote.split(" "); // This is to split the quote into words.
	const wordCount = words.length; // This is to get the number of words in the quote.
	const avgWordLength = quoteLength / wordCount; // This is to get the average length of the words in the quote.
	const delay = (quoteLength / avgWordLength / wpm) * 60000 + 2500; // This is to get the delay for the quote changing.
	debugging ? console.log(delay) : null;
	return delay; // This is to return the delay.
}

// This is to search for quotes.
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
	) // This is to fetch the quotes from the API.
		.then((response) => response.json()) // This is to get the response from the API.
		.then((data) => {
			// This is to get the quotes from the API.
			// Enable elements after fetching.
			document.getElementById("search-box").disabled = false;
			document.getElementById("search-box").style.cursor = "auto";
			document.getElementById("search").disabled = false;
			document.getElementById("search").style.cursor = "auto";
			if (quoteNumber > data.quotes.length - 1) {
				// If the quote number is greater than the number of quotes, then set the quote number to the last quote.
				quoteNumber = data.quotes.length - 1; // This is to set the quote number to the last quote.
			}
			debugging ? console.log(quoteNumber, " quoteNumber") : null;
			let author; // This is to declare the author variable. Fixed an error, probably not needed anymore.
			try {
				// This is to try to get the author of the quote. Probably not needed anymore.
				author = data.quotes[quoteNumber].author; // This is to get the author of the quote.
			} catch (error) {
				// This is to catch an error. Probably not needed anymore.
				author = `Unknown [${error}]`; // This is to set the author to Unknown. Probably not needed anymore.
			}
			const quoteText = data.quotes[quoteNumber].body; // This is to get the quote.
			const quoteHTML = `<p><h4>${quoteText}</h4></p><p><i>&nbsp;-&nbsp;${author}</i></p>`; // This is to get the quote in HTML.
			debugging ? console.log(data) : null;
			if (data.quotes.length === 1) {
				// This is to check if there is only one quote. (If there is only one quote, it means no quotes, this is probably the wrong way to handle it and will cause errors, but time is short.)
				document.getElementById("quote-result").innerHTML =
					"<p><h1>No quotes found.</h1></p>"; // This is to display no quotes.
			} else {
				// This is to check if there is more than one quote.
				document.getElementById("quote-result").innerHTML = quoteHTML; // This is to display the quote.
				document.getElementById("random-btn").disabled = false; // This is to enable the random button.
				document.getElementById("random-btn").style.cursor = "auto"; // This is to set the cursor to auto.
			}
			if (data.last_page === false) {
				// This is to check if there are more quotes.
				//Enable right-btn
				document.getElementById("right-btn").disabled = false; // This is to enable the right button.
				document.getElementById("right-btn").style.cursor = "auto"; // This is to set the cursor to auto.
			} else {
				// This is to check if there are no more quotes.
				//Disable right-btn
				document.getElementById("right-btn").disabled = true; // This is to disable the right button.
				document.getElementById("right-btn").style.cursor = "not-allowed"; // This is to set the cursor to not-allowed.
			}

			if (data.page === 1) {
				// This is to check if the page is the first page.
				//Disable left-btn
				document.getElementById("left-btn").disabled = true; // This is to disable the left button.
				document.getElementById("left-btn").style.cursor = "not-allowed"; // This is to set the cursor to not-allowed.
			} else {
				// This is to check if the page is not the first page.
				//Enable left-btn
				document.getElementById("left-btn").disabled = false; // This is to enable the left button.
				document.getElementById("left-btn").style.cursor = "auto"; // This is to set the cursor to auto.
			}
			pageNumber = data.page; // This is to set the page number.
			//backgroundImages(); // This is too spammy. Need a better function, no time to write.
			//randomBackground(); // Disabled because of lack of API key.
		});
}

// Event listeners
document.getElementById("search-box").addEventListener("keydown", (event) => {
	// This is to listen for keydown events on the search box.
	if (event.code === "Enter") {
		// This is to check if the keydown event is enter.
		(quoteNumber = 0), (pageNumber = 1); // This is to reset the quote number and page number.
		searchQuotes(quoteNumber, pageNumber); // This is to search the quotes.
	}
});
// Event Listener for Search
document.getElementById("search").addEventListener("click", function (_event) {
	// This is to listen for click events on the search button.
	(quoteNumber = 0), (pageNumber = 1); // This is to reset the quote number and page number.
	searchQuotes(quoteNumber, pageNumber); // This is to search the quotes.
});
// Event Listener for Random
document
	.getElementById("random-btn")
	.addEventListener("click", function (_event) {
		// This is to listen for click events on the random button.
		quoteNumber = Math.floor(Math.random() * 24); // This is to get a random number between 0 and 23.
		debugging ? console.log(quoteNumber) : null;
		searchQuotes(quoteNumber, pageNumber); // This is to search the quotes.
	});
// Event Listener for Next
document
	.getElementById("right-btn")
	.addEventListener("click", function (_event) {
		// This is to listen for click events on the right button.
		pageNumber++; // This is to increment the page number.
		debugging ? console.log(pageNumber) : null;
		searchQuotes(quoteNumber, pageNumber); // This is to search the quotes.
	});
// Event Listener for Previous
document
	.getElementById("left-btn")
	.addEventListener("click", function (_event) {
		// This is to listen for click events on the left button.
		pageNumber--; // This is to decrement the page number.
		debugging ? console.log(pageNumber) : null;
		searchQuotes(quoteNumber, pageNumber); // This is to search the quotes.
	});
window.addEventListener("keydown", (event) => {
	// This is to listen for keydown events on the window.
	if (event.code === "KeyI" && event.shiftKey) {
		// If the key is I and shift is held down, toggle debugging.
		debugging = !debugging; // Toggle debugging.
		console.log("Debugging is now " + debugging); // Log the new value of debugging.
	}
});

window.addEventListener("resize", () => {
	// This is to listen for resize events on the window.
	backgroundImages(); // This is to change the background images.
	//This could be done better, but time constraints.
});

backgroundImages(); // This function to load a random background image when the page loads.
randomQuote(); //This is to start the quote changing when the page is loaded.
//promiseTest();  This fuction works, but because of API limitations and lack of API keys, I'm not using it.

// I'm doing too much. I have to stop this so I can turn it in.
