let button = document.querySelector("#button-quote"),
  button2 = document.querySelector("#button-page"),
  h1 = document.querySelector("#result"),
  h3 = document.querySelector("#author"),
  pageNumber = 1,
  quotesList = [],
  i = 0;

const url = `https://favqs.com/api/quotes?page=${pageNumber}`;

const headers = {
  Accept: "application/json",
  Authorization: `Token token=${FAVQS_API_KEY}`,
};

button.addEventListener("click", () => {
  getQuote();
});

button2.addEventListener("click", () => {
  i += 1;

//   if i is less than the total list length run this code black
  if (i < 25) {
    h3.innerHTML = quotesList[i].author;
    h1.innerHTML = quotesList[i].body;
    console.log(i);
    // quotesList = []
  } 
  
//   else set i back to 0 and empty the quotes list then run the request function to start over with new list 
  else {
    i = 0;
    quotesList = [];
    getQuote();
  }
});

const params = {
  page: pageNumber,
};
function getQuote() {
  axios
    .get(url, {
      headers: headers,
      params: params,
    })

    .then((response) => {
    //   set i back to zero when function is called outside of the button 2 function
     i = 0;
      quotesList = [];
      let quotes = response.data.quotes;
      let data = response.data;
      console.log(data);
      console.log(quotes);
      quotes.forEach((quote) => {
        quotesList.push(quote);
        h3.innerHTML = quotes[i].author;
        h1.innerHTML = quotes[i].body;
      });
    })
    .catch((error) => console.log("error!", error));
}
