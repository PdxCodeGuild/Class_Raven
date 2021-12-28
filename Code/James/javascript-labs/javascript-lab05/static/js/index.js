let button = document.querySelector("#button-quote"),
  button2 = document.querySelector("#button-forward"),
  button3 = document.querySelector("#button-back"),
  h1 = document.querySelector("#result"),
  h3 = document.querySelector("#author"),
  pageNumber = 1,
  quotesContainer = document.querySelector("#quotes-container"),
  queryStringInput = document.getElementById("user-input"),
  currentPage = document.querySelector("#current-page"),
  button4 = document.querySelector("#button-search");
(quotesList = []), (i = 0);
quoteDiv = document.querySelector("#quoteDiv");

const headers = {
  Accept: "application/json",
  Authorization: `Token token=${FAVQS_API_KEY}`,
};

button.addEventListener("click", () => {
  getQuote();
});

button4.addEventListener("click", () => {
  // params.filter = queryString.value;
  getQuote(pageNumber, queryStringInput.value);
});

button3.addEventListener("click", () => {
  i -= 1;

  // if (quotesList.page !== 0)
  if (i > 0) {
    h3.innerHTML = quotesList.quotes[i].author;
    h1.innerHTML = quotesList.quotes[i].body;
    console.log(i);
  } else if (i === 0 && pageNumber !== 1) {
    pageNumber--;
    h3.innerHTML = quotesList.quotes[i].author;
    h1.innerHTML = quotesList.quotes[i].body;
    getQuote(pageNumber);
    console.log(i);
  }
});

button2.addEventListener("click", () => {
  i += 1;

  //   if i is less than the total list length run this code black
  if (i < 25) {
    h3.innerHTML = quotesList.quotes[i].author;
    h1.innerHTML = quotesList.quotes[i].body;
    console.log(i);
  } else if (quotesList.last_page === true) {
    alert("This is the last page");
  }

  //   else set i back to 0 and empty the quotes list then run the request function to start over with new list
  else if (i === 25) {
    pageNumber++;
    getQuote(pageNumber, queryStringInput.value);
  }
});

function getQuote(pageNumber, queryStringInput) {
  const url = `https://favqs.com/api/quotes`;

  params = {
    page: pageNumber,
    filter: queryStringInput,
  };
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
      console.log(data.page);
      quotesList = data;
      console.log(quotesList);
      console.log(quotesList.last_page);
      h3.innerHTML = quotes[0].author;
      h1.innerHTML = quotes[0].body;
    })

    .then((result) => {
      currentPage.innerHTML = quotesList.page;
    })
    .catch((error) => console.log("error!", error));
}
