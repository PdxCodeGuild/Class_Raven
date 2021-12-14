let trash = document.getElementById('trash')
let container = document.getElementById('.container')
let add = document.getElementById('add')

// trash.addEventListener('click', function(){
//     trash.classList.add('grow')
// })

// trash.addEventListener('click', function (){
//     let list = document.createElement('div')
//     list.classList.add('list')
// })


add.addEventListener('click', function (){
    var txt = prompt('Task to do is..');
    add.innerHTML += '<li class=list-group-item'> + txt + '</li>'
})
