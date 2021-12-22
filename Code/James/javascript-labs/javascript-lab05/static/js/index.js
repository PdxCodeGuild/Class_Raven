let button = document.querySelector("#button-quote"),
  button2 = document.querySelector("#button-forward"),
  button3 = document.querySelector("#button-back"),
  h1 = document.querySelector("#result"),
  h3 = document.querySelector("#author"),
  pageNumber = 1,
  quotesContainer = document.querySelector("#quotes-container"),
  queryStringInput = document.getElementById('user-input'),
  currentPage = document.querySelector('#current-page'),
  button4 = document.querySelector("#button-search")
  quotesList = [],
  
  i = 0;
  
  
  const headers = {
    Accept: "application/json",
    Authorization: `Token token=${FAVQS_API_KEY}`,
  };
  
  button.addEventListener("click", () => {
    params.page = 1;
    getQuote();
  });
  
  button4.addEventListener("click", () => {
    // params.filter = queryString.value;
    getQuote(pageNumber, queryStringInput.value);
  });
  
  button3.addEventListener("click", () => {
    i -= 1;
    if (i > 0){
      h3.innerHTML = quotesList[i].author;
      h1.innerHTML = quotesList[i].body;
      console.log(i);
      
    }
    else {
      i = 0
      h3.innerHTML = quotesList[i].author;
      h1.innerHTML = quotesList[i].body;
      console.log(i);
    }
  });
  
  button2.addEventListener("click", () => {
    i += 1;
    
    //   if i is less than the total list length run this code black
    if (i < 25) {
      h3.innerHTML = quotesList[i].author;
      h1.innerHTML = quotesList[i].body;
      console.log(i);
    }
    
    //   else set i back to 0 and empty the quotes list then run the request function to start over with new list
    else if (i === 25) {
      params.page++;
      pageNumber++;
      getQuote(pageNumber);
    }
  });
  
  function getQuote(pageNumber, queryStringInput) {
    let params = {
      page: pageNumber,
      filter: queryStringInput
    };
    
    const url = `https://favqs.com/api/quotes`;
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
      quotesList = quotes;
      h3.innerHTML = quotes[0].author;
      h1.innerHTML = quotes[0].body;
    })
    // .then((result) => {
      //   for (let i = 0; i < quotesList.length; i++) {
        //     let quoteDiv = document.createElement("div");
        //     quoteDiv.innerHTML = `<h1 id='body'>${quotesList[i].body}</h1><h3 id="author">${quotesList[i].author}</h3>`;
        
        //     quotesContainer.appendChild(quoteDiv);
        //   }
    // })
    .catch((error) => console.log("error!", error));
}
