let trash = document.getElementById('trash')
let container = document.getElementById('.container')
let add = document.getElementById('add')
let text = document.getElementById('#text')
// trash.addEventListener('click', function(){
//     trash.classList.add('grow')
// })

// trash.addEventListener('click', function (){
//     let list = document.createElement('div')
//     list.classList.add('list')
// })


add.addEventListener('click', function (){
    var txt = prompt('Task to do is..');
    text.innerHTML += '<li class=list-group-item'> + txt + '</li>'
})
