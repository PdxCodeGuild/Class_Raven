let username = document.querySelector('#username'),
  fullName = document.querySelector('#full-name'),
  email = document.querySelector('#email'),
  phone = document.querySelector('#phone'),
  address = document.querySelector('#address'),
  websiteLink = document.querySelector('#website-link'),
  loadingModal = document.querySelector('#loading-modal'),
  button = document.querySelector('#button');


button.addEventListener('click', ()=>{
  // generate random userId
  let userId = Math.floor(Math.random() * 10) + 1

  // show the loading modal
  loadingModal.style.display = 'block';

  // call the api
  fetchUser(userId)
})


function fetchUser (userId) {
  let url = `https://jsonplaceholder.typicode.com/users/${userId}`

  // simulate a longer API response time with setTimeout
  setTimeout(() => {
    $.ajax({
      url: url,
      success: function (response) {
        // set the CSS display property to 'none'
        loadingModal.style.display = 'none'

        // hide the loading modal
        // send the response to the callback function
        setContent(response)
        
      },
      error: function (error) {
        loadingModal.style.color = 'red'
        loadingModal.innerHTML = `<h1>${error.status} ${error.statusText}</h1>`
      }
    })
  }, 1000)
}

function setContent (response) {
  console.log(response)
  username.innerHTML = response.username
  fullName.innerHTML = response.name
  email.innerHTML = response.email
  phone.innerHTML = response.phone
  websiteLink.innerHTML = response.website

  address.innerHTML = `
  ${response.address.street} </br>
  ${response.address.suite} </br>
  ${response.address.city} </br>
  ${response.address.zipcode} </br>
  `
}

fetchUser(3)

// console.log('A')
// setTimeout(function(){
//   console.log('B')
// }, 1000)
// console.log('C')

// console.log('A')
// setTimeout(function(){
//   console.log('B')

//   setTimeout(()=>{
//     console.log('C')
//   }, 1000)

// }, 1000)
// console.log('D')

// call the callback every time interval
// let count = 0;
// let timer = setInterval(() => {

//   console.log(count)
//   count++
//   if(count > 3){
//     console.log('end!')
//     clearInterval(timer)
//   }
// }, 1000);
