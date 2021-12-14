// getElementById targets a div with the given id
// let button = document.getElementById('add-box-button')

// querySelector targets a particular CSS selector
let button = document.querySelector('#add-box-button')
let container = document.querySelector('.container')

// return a random integer between low and high
function randomInt(low, high) {
  low = Math.ceil(low);
  high = Math.floor(high);
  return Math.floor(Math.random() * (high - low + 1) + low)
}

// shift the button up and left 50% of its width in px
button.style.top = `calc(50% - ${button.offsetHeight / 2}px)`
button.style.left = `calc(50% - ${button.offsetWidth / 2}px)`

// apply a class to the button on hover
button.addEventListener('mouseenter', function () {
  button.classList.add('grow')
})

// remove the class when the mouse leaves the button
button.addEventListener('mouseleave', function () {
  button.classList.remove('grow')
})

// when the + button is clicked
button.addEventListener('click', function () {
  let box = document.createElement('div')
  box.classList.add('box')

  // apply style to the box
  box.style.height = window.innerWidth / 6 - 5 + 'px';
  box.style.width = window.innerWidth / 6 - 5 + 'px';
  box.style.display = 'flex';
  box.style.justifyContent = 'center';
  box.style.alignItems = 'center';

  // calculate and apply random RGB background color
  let r, g, b
  r = randomInt(0, 255)
  g = randomInt(0, 255)
  b = randomInt(0, 255)
  box.style.backgroundColor = `rgb(${r}, ${g}, ${b})`

  box.addEventListener('mousemove', function(event){
    // console.log(event)

    // find x and y position of the mouse based on the current event info
    let x = event.screenX
    let y = event.screenY

    // add content to the box
    box.innerHTML = `<h1>x: ${x} <br/> y: ${y}</h1>`
  })

  // clear text when mouse leaves
  box.addEventListener('mouseleave', function(){
    box.innerHTML = ''
  })


  // delete the box when clicked
  box.addEventListener('click', function(){
    container.removeChild(box)
  })

  // attach the box to the container's list of children
  container.appendChild(box)

  // scroll to the bottom of the screen
  window.scrollTo(0, document.body.scrollHeight)
})

// if the Esc key is pressed, delete all boxes
window.addEventListener('keyup', function(event){
  if(event.key === 'Escape') {
    // target all the boxes
    let boxes = document.querySelectorAll('.box')
    
    // remove all boxes
    for(let box of boxes){
      container.removeChild(box)
    }
  }

})