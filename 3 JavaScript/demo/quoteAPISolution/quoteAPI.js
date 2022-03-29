let quoteContainer = document.querySelector('#quotes'),
  pageChangeArrows = document.querySelector('#page-change-arrows'),
  searchButton = document.querySelector('#search-button'),
  searchQueryInput = document.querySelector('#search-query-input'),
  pageControls = document.querySelector('#page-controls'),
  previousPageArrow = document.querySelector('#previous-page-arrow'),
  nextPageArrow = document.querySelector('#next-page-arrow'),
  currentPageNumber = document.querySelector('#current-page-number')

// global state variables,
// these are manipulated at a global level
// because they are used in various places
let currentPage = 1
let searchQuery = ''

// Fetch the quote of the day from FAVQs api and render it on the page
function fetchQuoteOfTheDay () {
  let url = 'https://favqs.com/api/qotd'
  // let quotes = []

  // create an object for HTTP headers
  const headers = {
    'Content-Type': 'application/json'
  }

  // axios.get(url, configObject)
  axios
    .get(url, { headers: headers })
    .then(response => {
      quote = response.data.quote
      renderQuotes([quote])
      renderPageArrows([quote])
    })
    .catch(error => console.log(error))
}

// search for the filterQuery
function fetchQuotes (pageNumber = 1, filterQuery = '') {
  let url = 'https://favqs.com/api/quotes'
  let quotes, isLastPage

  // create an object for HTTP headers
  const headers = {
    'Content-Type': 'application/json',
    Authorization: `Token token=${FAVQ_API_KEY}`
  }

  // create an object for the URL query parameters
  const params = {
    page: pageNumber,
    filter: filterQuery
  }

  // axios.get(url, configObject)
  axios
    .get(url, {
      headers: headers,
      params: params
    })
    .then(response => {
      // pull the data out of the HTTP response
      quotes = response.data.quotes
      currentPage = response.data.page
      isLastPage = response.data.last_page

      //
      renderQuotes(quotes)
      renderPageArrows(quotes, pageNumber, isLastPage)
    })
    .catch(error => console.log(error))
}

// render the page navigation arrows based on the currentPage and
function renderPageArrows (quotes, pageNumber, isLastPage) {
  // hide the arrows unless there is more than one quote
  if (quotes.length < 2) {
    pageControls.style.display = 'none'
  } else {
    pageControls.style.display = 'flex'

    // hide the left arrow if we're on the first page
    if (pageNumber === 1) {
      previousPageArrow.style.display = 'none'
    } else {
      previousPageArrow.style.display = 'block'
    }

    // hide the right arrow if we're on the last page
    if (isLastPage) {
      nextPageArrow.style.display = 'none'
    } else {
      nextPageArrow.style.display = 'block'
    }
  }

  currentPageNumber.innerHTML = currentPage
}

function renderQuotes (quotes) {
  let quote, blockquote, cite
  quoteContainer.innerHTML = ''

  if (quotes[0].body.toLowerCase() === 'no quotes found') {
    quoteContainer.innerHTML = `<h1>No quotes found</h1>`
  } else {
    for (quote of quotes) {
      blockquote = document.createElement('blockquote')
      cite = document.createElement('cite')

      blockquote.classList.add('quote')

      blockquote.innerHTML = quote.body + '<br/>'

      cite.innerHTML = `- ${quote.author}`
      blockquote.appendChild(cite)

      quoteContainer.appendChild(blockquote)
    }
  }
}

// when the searchButton is clicked,
searchButton.addEventListener('click', function () {
  // set the searchQuery to the current value of the searchQueryInput,
  // reset the currentPage to 1
  searchQuery = searchQueryInput.value
  currentPage = 1

  // set loading message
  quoteContainer.innerHTML =
    '<h1><i class="fas fa-stroopwafel spinner"></i></h1>'

  // call the API with the new currentPage
  // number and previous searchQuery
  fetchQuotes(currentPage, searchQuery)
})

function handlePageChange (direction) {
  // set loading message
  quoteContainer.innerHTML =
    '<h1><i class="fas fa-stroopwafel spinner"></i></h1>'

  // change the currentPage based on the direction
  if (direction === 'previous') {
    currentPage--
  } else if (direction === 'next') {
    currentPage++
  }

  // call the API with the new currentPage
  // number and previous searchQuery
  fetchQuotes(currentPage, searchQuery)
}

// handlePageChange could also be defined like this
// using a ternary if/else operation and an arrow function:
// const handlePageChange = direction =>
//   fetchQuotes(direction === 'next' ? currentPage++ : currentPage--, searchQuery)

// when the previousPageArrow is clicked,
// call handlePageChange to decrease page number
previousPageArrow.addEventListener('click', () => handlePageChange('previous'))

// when the nextPageArrow is clicked,
// call handlePageChange to increase page number
nextPageArrow.addEventListener('click', () => handlePageChange('next'))

// load the initial quote
fetchQuoteOfTheDay()
