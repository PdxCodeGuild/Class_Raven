/* Use the favqs.com api to show a random quote. To start, use https://favqs.com/api/qotd to GET a quote, then display it on the page.
The API also supports browsing quotes. */

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
	console.log(random);

	const url = `https://source.unsplash.com/random/${width}x${height}?sig=${random}&orientation=${deviceOrientation}&fit=fillmax&fill=blur`;
	fetch(url).then((data) => {
		let image = data.url;
		console.log(image);
		document.body.style.backgroundImage = `url(${image})`;
	});
}

function randomQuote() {
	fetch("https://favqs.com/api/qotd", { headers })
		.then((response) => response.json())
		.then((data) => {
			const author = data.quote.author;
			const quoteText = data.quote.body;
			const quoteLink = data.quote.url; // Link to the quote on favqs.com, will use later maybe.
			const quoteHTML = `<p><h4>${quoteText}</h4></p><p><i>&nbsp;-&nbsp;${author}</i></p>`;
			document.getElementById("quote").innerHTML = quoteHTML;
			setTimeout(randomQuote, delayQuote());
			backgroundImages();
			//randomBackground(); // Disabled because of lack of API key.
		});
}

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
			console.log(data);
			document.body.style.backgroundImage = `url(${image}&orientation=${deviceOrientation}&fit=fillmax&fill=blur&w=${width}&h=${height})`;
			console.log(document.body.style.backgroundImage);
		});
}

function delayQuote() {
	const wpm = 180;
	const quote = document.getElementById("quote").innerHTML;
	console.log(document.getElementById("quote"), "test");
	const quoteLength = quote.length;
	const words = quote.split(" ");
	const wordCount = words.length;
	const avgWordLength = quoteLength / wordCount;
	const delay = (quoteLength / avgWordLength / wpm) * 60000 + 2500;
	return delay;
}

function searchQuotes() {
	const searchTerm = document.getElementById("search").value;
	fetch(`https://favqs.com/api/quotes?filter=${searchTerm}`, { headers })
		.then((response) => response.json())
		.then((data) => {
			const author = data.quotes.author;
			const quoteText = data.quotes.body;
			const quoteLink = data.quotes.url; // Link to the quote on favqs.com, will use later maybe.
			const quoteHTML = `<p><h4>${quoteText}</h4></p><p><i>&nbsp;-&nbsp;${author}</i></p>`;
			document.getElementById("quote-result").innerHTML = quoteHTML;
			console.log(data);

			backgroundImages();
			//randomBackground(); // Disabled because of lack of API key.
		});
}

// Event Listener for Search
document.getElementById("search").addEventListener("click", function (event) {
	searchQuotes();
});

//promiseTest();  This fuction works, but because of API limitations and lack of API keys, I'm not using it.

randomQuote();
backgroundImages();
