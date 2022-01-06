/*
JavaScript Lab 05 Quote API
By Philip Bartoo
12/27/2021
PDX Code Guild

Directions:
Use the favqs.com api to show a random quote. To start, use https://favqs.com/api/qotd to GET a quote, then display it on the page.

{
  "id": 4,
  "author": "Albert Einstein",
  "body": "Make everything as simple as possible, but not simpler.",
  ...
}
Version 2

The API also supports browsing quotes.

You will need to sign up for an account, visit the API link at the very bottom of the page and generate an API key. 
The key will act like a username/password and authorize your API request when searching for quotes.

*/

//Variable for the button
let button = document.querySelector('#button');
//Variable for the token
let token = 'Your Token Here';
//Variable for the API URL
let url = 'https://favqs.com/api/quotes?page='
//Variable for the page number
let pageNumber
//Event listner for Get Quotes click
button.addEventListener('click', ()=>{
    //function to get a quote with initial page number
    function fetchQuote(pageNumber = 1) {
        //Using axios, submit the API request
        axios
            .get(url, {
                //Include headers witht he token
                headers: {
                    Authorization: `Token token=${token}`,
                    Accept: 'application/json'
                },
                //Include parameters for the page number
                params: pageNumber
            })
            //If successfull, grab the quotes data
            .then(data=>{
                //Establish variable for each quote
                let html = data.data.quotes.map(quotes => { 
                    //Grab the page number
                    page = data.data.page
                    //Return the quote body and author in a div
                   return`
                   <div class="quote">
                   <p>${quotes.body}</p>
                  <p class="author">-${quotes.author}</p>
                   </div>`
                }) 
                .join("");
                //Insert each quote div into html
                document.querySelector('#app').innerHTML=html;
            });     
    }
    //Call the function
    fetchQuote();
//Event listener for next page button click and logic to increment the page number by 1
let nextPageButton=document.querySelector('#next');
    nextPageButton.addEventListener('click', ()=>{
        pageNumber++
        fetchQuote()
    })
//Event listener for previous page button click and logic to decrement the page number by 1
    let previousPageButton=document.querySelector('#previous');
    previousPageButton.addEventListener('click', ()=>{
            pageNumber--;
            fetchQuote()
})
})