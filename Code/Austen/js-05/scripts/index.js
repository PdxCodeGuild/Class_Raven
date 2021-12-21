// simple function to test connections between html elements and this script
function test(){
  alert('it just works')
}

// define api url
let URL = 'https://favqs.com/'

// define target element
const target = document.getElementById('target')

// request qotd from favqs api
const QOTD = () => axios.get(URL + 'api/qotd').then(
  function (response){
  let data = response.data.quote
  let quote = data.body
  let author = data.author
  target.innerHTML = `<span class="quote-body">${quote}</span></br><span class="author">${author}</span>`
}).catch(
  function (error){
    console.log(error)
  }
)

// request the url with the user's search term
function searchQuote(){
  let term = prompt('search term: ')
  // const headers =
  const params = {
      filter: term
  }
// DOESNT FREAKING WORK FAVQ IS SO GOTDAMN ANNOYING
  axios.get(URL + 'quotes/',{
          headers: {
            'authorization': 'Token token:`${FAVQS_API_KEY}`',
            'content-type': 'application/json'
          },
          params: params
      }).then(function (response){
        console.log(response)
      })
}


// display qotd on initial load event
document.body.onload = QOTD
