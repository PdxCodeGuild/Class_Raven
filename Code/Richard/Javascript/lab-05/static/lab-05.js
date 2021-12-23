// Quote of the Day API Lab
let pageNumber = 1;
let queryString = "funny";
const quotesDiv = document.querySelector("#quotes-set");
const headers = {
  "Content-Type": "application/json",
  Authorization: `Token token=${FAVQS_API_KEY}`,
};

const params = {
  page: pageNumber,
  filter: queryString,
};

let quotes = [
  {
    id: 1,
    author: "Albert Einstein",
    body: "Make everything as simple as possible, but not simpler.",
  },
];

function displayQuotes(quotes) {
  let i, quote, quoteData, body, cite;
  quotesDiv.innerHTML = "";
  for (i in quotes) {
    quoteData = quotes[i];
    quote = document.createElement("div");
    body= document.createElement('blockquote');
    body.innerText = quoteData.body;
    quote.appendChild(body);

    cite=document.createElement('cite');
    cite.innerText = quoteData.author;
    quote.appendChild(cite);

    console.log(quoteData.body, quoteData.author);
    // quote.innerText = quoteData.body + quoteData.author;
    quote.id = "quote-${i}";
  

  console.log(quote.id);

  quotesDiv.appendChild(quote);
  }
}

displayQuotes(quotes);

getQotd = document.querySelector("#get-qotd");
getQotd.addEventListener("click", function getToday() {
  axios({
    method: "get",
    url: "https://favqs.com/api/qotd",
  }).then(function (response) {
    quotes.push(response.data.quote);
    displayQuotes(quotes);
  });
});

axios({
  method: "get",

  url: "https://favqs.com/api/quotes",
  headers: headers,
  params: params,
}).then(function (response) {
  console.log(response);
  displayQuotes(response.data.quotes);
});
