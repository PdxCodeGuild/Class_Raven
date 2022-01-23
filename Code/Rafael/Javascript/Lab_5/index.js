// LAB:05 API - Class Raven - Rafael Medina
/*--- axios.post() to make an HTTP POST request, requires 2 parameters ---*/

let button = document.querySelector("#submit-btn"),
  h1 = document.querySelector(".result"),
  inputField = document.querySelector("#search"),
  clickRight = document.getElementById("#click-right"),
  clickLeft = document.getElementById("#click-left")

/**(Shorthand methods -Axios- )**
axios.request(config)
axios.get(url[, config])
axios.delete(url[, config])
axios.head(url[, config])
axios.options(url[, config])
axios.post(url[, data[, config]])
axios.put(url[, data[, config]])
axios.patch(url[, data[, config]])  
*/

/**  (for intellisense / autocomplete) while using CommonJS imports with require()  **/

let currentPage = 1
let searchQuery = ''
let quoteIndex = 0
let pageNumber = 1

const headers = {
  // ... other headers
  'Content-Type': 'application/json',
  Authorization: `Token token=${FAVQS_API_KEY}`,
};


function getQuote (pageNumber = 1, filterQuery = '') {
  let url = 'https://favqs.com/api/quotes'
  let quotes, isLastPage
  }





button.addEventListener("click", () => {
  /** -Axios- **/
  /*---"axios.request(config)
axios.get(url[, config]) "  ---*/
  const getQuote = () => {
    axios
      //const url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`
      //.get(`https://favqs.com/api/quotes`, {
        .get(`https://favqs.com/api/quotes?page=${pageNumber}&filter=${inputField.value}`, {
        headers: headers,
      })
      //.then(data => console.log(data.data.quote.body))
      .then((response) => {
        h1.innerHTML = response.data.quotes;
        currentPage = response.data.page;
        lastPage = response.data.last_page;
        console.log(response);
        console.log("current page: ", currentPage); // current page: 1
        console.log("last page: ", lastPage); //false
      })

      .catch((error) => console.log(error)); // Error 429 "too many requests" alert

    //console.log(getQuote)
  };
  getQuote();
});



function renderQuotes(quotes){
  let quote, blockquote, cite;
  h1.innerHTML = ''

  if (quotes[0].body.toLowerCase() === `<h1>'no quotes found'</h1>`){
  }
  else{
    for (quote of quotes){
      blockquote = document.createElement('blockquote')

      cite = document.createElement('cite')

      blockquote.innerHTML = quote.body + '<br>'
      cite.innerHTML = `- &{quote.author}`
      blockquote.appendChild(cite)

      h1.appendChild(blockquote)
    }
  }
  }


  button.addEventListener('click', function () {
    // set the searchQuery to the current value of the searchQueryInput,
    // reset the currentPage to 1
    searchQuery = inputField.value
    currentPage = 1
    // set loading message
    getQuote(currentPage, searchQuery)
  })



function pageSwitch(direction) {
  if (direction === "previous") {
    currentPage--;
  } else if (direction === "next") {
    currentPage++;
  }
  getQuote(currentPage, searchQuery)
}

clickLeft.addEventListener("click", () => pageSwitch("previous"));

clickRight.addEventListener("click", () => pageSwitch("next"));

// Input Fields

/*
button.addEventListener('click', ()=>{
  console.log("Test Response");
  console.log(axios) 
})
*/

/**(

function fetchQuote (){
  //data : {
                //firstName: 'John'    ,
                //lastName : 'Williams'
            
  const headers = {
    Accept: 'application/json'
    }
    const url = `https://favqs.com/api/quotes`
     // 'http://127.0.0.1:5500/index.html',
    
    return axios.get(url, {headers: headers})
    .then(response =>{
      console.log(response.data.quote.body)
    })

    .catch(error => console.log('error'. error))
            /*-- one advantage of axios is that you don't need to convert to JSON --*/
/*--
            }--*/
//          }
//          fetchQuote()

//  )
//  */
