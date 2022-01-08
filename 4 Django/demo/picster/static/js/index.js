let likeButtons = document.querySelectorAll('.like'),
    csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0];


function handleLikeEvent(event){
  let picId, url, headers;

  // isolate the picId number from the end of the clicked element's id
  picId = event.target.id
  picId = picId.split('-')[1]

  // include the picId as a url parameter
  url = 'http://localhost:8000/like/' + picId

  headers = {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrfToken.value // include Django's CSRF token
  }

  // axios.post(url, data, config)
  axios.post(url, {}, { headers: headers, xsrfHeaderName: 'X-CSRFToken' })
    .then(response=>{

      const isLiked = response.data.isLiked // true if the current user is in the list of likes, else false
      const likeButton = document.querySelector(`#like-${picId}`) // heart icon
      const likeCount = document.querySelector(`#like-count-${picId}`) // like count element

      // change the pic's like count
      likeCount.innerHTML = response.data.likeCount

      // if the pic is liked, render red heart, otherwise, render heart outline
      if(isLiked){
        likeButton.classList.remove('far')
        likeButton.classList.add('fas', 'text-danger')
      } else {
        likeButton.classList.remove('fas', 'text-danger')
        likeButton.classList.add('far')
      }

    })
    .catch(error=>console.log(error))

}

// apply the click event listener to each likeButton
likeButtons.forEach(likeButton =>
  likeButton.addEventListener('click', handleLikeEvent)
)
