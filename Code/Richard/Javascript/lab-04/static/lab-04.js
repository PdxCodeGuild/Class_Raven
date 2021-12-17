let task, create, vanish, finish, done, disappear

const incompleteTodosDiv= document.querySelector('#incomplete-todos')
const completeTodosDiv=document.querySelector('#complete-todos')

let incomplete = [
    "cut grass",
    "hide eggs",
    "fill baskets"
]

let complete = [
    "buy grass",
    "buy eggs",
    "buy baskets"
]

function loadTodo(){
    let todo, finish, vanish
    incompleteTodosDiv.innerHTML=''
    for (task of incomplete) {    
        todo = document.createElement("div")
        todo.innerText = task
        finish= document.createElement("button")
        finish.innerText='Done!'
        vanish=document.createElement("button")
        vanish.innerText="Delete"
        todo.appendChild(finish)
        todo.appendChild(vanish)
        incompleteTodosDiv.appendChild(todo)
    }
}

    
function loadDone (){
    for (task of complete) {
        todo = document.createElement("div")
        todo.innerText = task
        vanish=document.createElement("button")
        vanish.innerText="Delete"
        todo.appendChild(vanish)
        completeTodosDiv.appendChild(todo)
    }
}

create = document.querySelector('#create');
create.addEventListener('click', function createtodo() {incomplete.push(task=text.value); text.value=''; loadTodo()})

// disappear = document.querySelector('#vanish');
// disappear.addEventListener('click', function vanishTodo(){task=text.value;loadTodo(); text.value=''})

// done = document.querySelector('#finish');
// done.addEventListener('click', function finishTodo(){task=text.value;loadDone(); text.value=''})

loadTodo()
loadDone()








// function deleteTodo (){


// }
// for (task of incomplete) {
// containerDiv = document.querySelector('#todo-list')
// todo = document.createElement("div")
// todo.innerText = task
// console.log(todo.innerText)
// containerDiv.appendChild(todo)
// }

// console.log(document.getElementById('new-item-text').value)

// let incomplete = document.querySelector('#incomplete-todos')
// incomplete.innerHTML = '<h3>capture skunks</h3>'

// incomplete.push(value."#new-text-item") // add value from create button to incomplete todos
