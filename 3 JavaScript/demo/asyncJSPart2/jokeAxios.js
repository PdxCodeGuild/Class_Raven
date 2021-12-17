let button = document.querySelector('#button'),
  h1 = document.querySelector('#result')

// get a dad joke using Javascript's fetch() api

const headers = {
  Accept: 'application/json'
}

const url = 'https://icanhazdadjoke.com/'

// fetch(urlString, optionsObject)
axios
  .get(url, { headers: headers })
  // response is the HTTP response object
  .then(response => {
    // pull the joke out of data property of the response object
    h1.innerHTML = response.data.joke
  })
  .catch(error => console.log('error!', error))

