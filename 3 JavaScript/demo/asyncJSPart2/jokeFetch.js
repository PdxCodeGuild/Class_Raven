let button = document.querySelector('#button'),
  h1 = document.querySelector('#result')

// get a dad joke using Javascript's fetch() api

const headers = {
  Accept: 'application/json'
}

const url = 'https://icanhazdadjoke.com/'

// fetch(urlString, optionsObject)

fetch(url, {
  method: 'GET',
  headers: headers
})
  // response is the HTTP response object, which is converted to JSON
  .then(response => response.json())
  // result is the JSON version of the response data
  .then(result => {
    // pull the joke text out of the result data and inject it into an h1
    h1.innerHTML = result.joke
  })
  // if an error is thrown in any of the .then() functions, .catch() is run
  .catch(error => console.log('error!', error))
