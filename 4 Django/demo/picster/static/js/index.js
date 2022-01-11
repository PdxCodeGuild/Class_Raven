let likeButtons = document.querySelectorAll('.like'),
    csrfToken = document.getElementsByName('csrfmiddlewaretoken')[0],
    followButtons = document.querySelectorAll('.follow');

console.log(followButtons);

const axios_config = {
   headers: {
    'Content-Type': 'application/json',
    'X-CSRFToken': csrfToken.value // include Django's CSRF token
  }, 
   xsrfHeaderName: 'X-CSRFToken' 
}

function handleLikeEvent(event){
  let picId, url, headers;

  // isolate the picId number from the end of the clicked element's id
  picId = event.target.id
  picId = picId.split('-')[1]

  // include the picId as a url parameter
  url = 'http://localhost:8000/like/' + picId


  // axios.post(url, data, config)
  axios.post(url, {}, axios_config)
    .then(response=>{
      console.log(response);
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





function handleFollowEvent(event){
  let userId1, userId2, url;

  userId1 = event.target.id // follow-14
  userId1 = userId1.split('-')[1] // 14

  url = 'http://localhost:8000/users/follow/' + userId1
  axios.post(url, {}, axios_config)
    .then(response=>{

      // pull the data from the response
      let isFollowing = response.data.isFollowing
      let followerCount = response.data.followerCount
      let followingCount = response.data.followingCount
      userId2 = response.data.follwerId

      // target the badge and follwer count of the clicked user
      // and the following count of the user who made the click
      let followBadge = document.querySelector(`#follow-${userId1}`)
      let followerCountElement = document.querySelector(`#follower-count-${userId1}`)
      let followingCountElement = document.querySelector(`#following-count-${userId2}`)

      // isFollowing is a boolean indicating if request.user is following the other user
      // render the green following badge if true, otherwise the yellow follow badge
      if(isFollowing){
        followBadge.classList.replace('bg-warning', 'bg-success')
        followBadge.innerHTML = 'Following'
      } else {
        followBadge.classList.replace('bg-success', 'bg-warning')
        followBadge.innerHTML = 'Follow'
      }

      // change the follower/following counts of the users
      followerCountElement.innerHTML = followerCount
      followingCountElement.innerHTML = followingCount

    })
    .catch(error=>console.log(error))
}


// apply click event to all followButtons
followButtons.forEach(followButton=>followButton.addEventListener('click', handleFollowEvent))