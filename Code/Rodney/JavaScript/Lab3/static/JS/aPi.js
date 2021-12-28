let submit,
  clear,
  ul,
  errorPage,
  pageNumber,
  li,
  queryString,
  nextPageButton,
  previousPageButton,
  pageDisplay,
  userInput;

ul = document.querySelector("#quote-result");
clear = document.querySelector("#clear");
errorPage = document.querySelector(".container1");
nextPageButton = document.querySelector("#nextpagebutton");
previousPageButton = document.querySelector("#previouspagebutton");
pageDisplay = document.querySelector("#pagenumber");
submit = document.querySelector("#search");
userInput = document.querySelector("#userinput");

const headers = {
  Authorization: `Token token=${FAVQS_API_KEY}`,
};

// ----------------------------------Submit Button ---------------------------------------
nextPageButton.disabled = true;
clear.disabled = true;
previousPageButton.disabled = true;

submit.addEventListener("click", function () {
  nextPageButton.disabled = false;
  clear.disabled = false;
  previousPageButton.disabled = false;
  submit.disabled = true;
  queryString = userInput.value;
  pageNumber = 1;
  let url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`;
  fetch(url, {
    method: "GET",
    headers: headers,
  })
    .then((response) => response.json())

    .then(function (result) {
        console.log(result)
      if (result.last_page === true) {
        nextPageButton.disabled = true;
        previousPageButton.disabled = true;
      }

      result.quotes.forEach((element) => {
        if (element.body === "No quotes found") {
          pageDisplay.innerHTML = "";
          nextPageButton.disabled = true;
          previousPageButton.disabled = true;
          li = document.createElement("li");

          li.appendChild(
            document.createTextNode("Sorry, no results for that search!")
          );
          ul.appendChild(li);
          pageDisplay.innerHTML = "";
        } else {
          pageDisplay.innerHTML = `Page: ${pageNumber}`;

          li = document.createElement("li");
          li.appendChild(
            document.createTextNode(`${element.author}: ${element.body}`)
          );
          ul.appendChild(li);
        }
      });
    });
});

//----------------------------------Next Button ---------------------------------------

nextPageButton.addEventListener("click", function () {
  nextPageButton.disabled = true;
  ul.innerHTML = "";
  li.innerHTML = "";
  pageNumber = pageNumber + 1;

  let url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`;
  fetch(url, {
    method: "GET",
    headers: headers,
  })
    .then((response) => response.json())

    .then(function (result) {
      if (result.last_page !== true) {
        nextPageButton.disabled = false;
      }
    })
    .catch(function (error) {
      errorPage.style.color = "red";
      errorPage.style.fontSize = "2rem";
      errorPage.style.display = "flex";
      errorPage.style.margin = "100px";
      errorPage.style.justifyContent = "center";
      errorPage.innerHTML = "Error - Please try again";
    });

  pageDisplay.innerHTML = `Page: ${pageNumber}`;

  url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`;
  fetch(url, {
    method: "GET",
    headers: headers,
  })
    .then((response) => response.json())

    .then(function (result) {
      result.quotes.forEach((element) => {
        li = document.createElement("li");
        li.appendChild(
          document.createTextNode(`${element.author}: ${element.body}`)
        );
        ul.appendChild(li);
      });
    });
});

// ----------------------------------Previous Button ---------------------------------------

previousPageButton.addEventListener("click", function () {
  nextPageButton.disabled = false;
  ul.innerHTML = "";
  li.innerHTML = "";

  if (pageNumber > 1) {
    pageNumber = pageNumber - 1;
  }
  pageDisplay.innerHTML = `Page: ${pageNumber}`;
  let url = `https://favqs.com/api/quotes?page=${pageNumber}&filter=${queryString}`;
  fetch(url, {
    method: "GET",
    headers: headers,
  })
    .then((response) => response.json())
    .then(function (result) {
      result.quotes.forEach((element) => {
        li = document.createElement("li");
        li.appendChild(
          document.createTextNode(`${element.author}: ${element.body}`)
        );
        ul.appendChild(li);
      });
    })
    .catch(function (error) {
      errorPage.style.color = "red";
      errorPage.style.fontSize = "2rem";
      errorPage.style.display = "flex";
      errorPage.style.margin = "100px";
      errorPage.style.justifyContent = "center";
      errorPage.innerHTML = "Error - Please try again";
    });
});

// ----------------------------------Error Message ---------------------------------------

clear.addEventListener("click", function () {
  submit.disabled = false;
  nextPageButton.disabled = true;
  clear.disabled = true;
  previousPageButton.disabled = true;
  ul.innerHTML = "";
  li.innerHTML = "";
  userInput.value = "";
  pageNumber = 1;
  pageDisplay.innerHTML = "Search cleared! ";
});
