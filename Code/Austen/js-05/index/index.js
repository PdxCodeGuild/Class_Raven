// simple function to test connections between html elements and this script
function test(){
  alert('it just works')
}

// define api url
let URL = 'https://favqs.com'

// define target element

// format quotes and return a template
function formatQuote(data){
  let quote = data.body
  let author = data.author
  let template = `<div class="quote"><span class="quote-body">"${quote}"</span></br><span class="author">${author}</span></div>`
  return template
}
// request qotd from favqs api
const QOTD = () => axios.get(URL + '/api/qotd')
  // create template with requested quote
  .then(
    function (response){
      let target = document.getElementById('quotes-target')
      let data = response.data.quote
      let template = formatQuote(data)
      target.innerHTML = template

})
  .catch(
    function (error){
      console.log(error)
    })

function showForm(){
  let target = document.getElementById('form-target')
  let form = document.getElementById('search-form')
  target.innerHTML = form.innerHTML
}
// determine search type
function getType(){
  let author = document.getElementById('author').checked
  let tag = document.getElementById('tag').checked
  if (author === true){
    return 'author'
  }
  if (tag === true){
    return 'tag'
  }
}
function searchQuotes(){

  let term = document.getElementById('term').value
  let type = getType()
  let request = axios.get(URL + '/api/quotes',{
        headers: {
          'Authorization': `Token token=${FAVQS_API_KEY}`,
          'Content-Type': 'application/json'
        },
        params: {
          'filter': term,
          'type': type
        },
    })
    .then(
      function (response){
        let target = document.getElementById('quotes-target')
        target.innerHTML = ''
        let quotes = response.data.quotes
        quotes.forEach(quote => target.innerHTML += formatQuote(quote) + `</br>`)
    })}


// display qotd on initial load event
document.body.onload = QOTD
