let completeTodoSection = document.querySelector('#complete-todos'),
  incompleteTodoSection = document.querySelector('#incomplete-todos'),
  submitButton = document.querySelector('#submit'),
  inputField = document.querySelector('#text')

let todos = [
  {
    text: 'Flip the compost',
    complete: false
  },
  {
    text: 'Prune the grapes',
    complete: false
  },
  {
    text: 'Clean the gutters',
    complete: true
  }
]

// create new todo item on button click
submitButton.addEventListener('click', ()=>{
  addTodo(inputField.value)
  inputField.value = '' // clear the field
  updateTodoList()
})

function addTodo(text){
  let newTodo = {
    text: text,
    completed: false
  }
  // add the new todo item to the list
  todos = todos.concat(newTodo)
}

// flip the target todo's complete value
function toggleComplete(targetTodo){
  todos = todos.map((todo)=>{
    if(todo.text === targetTodo.text){
      return {
        text: todo.text,
        complete: !todo.complete
      }
    } else {
      return todo
    }
  })
}

// delete a todo item from the list
function deleteTodo(targetTodo){
  todos = todos.filter(todo=>{
    if(todo.text === targetTodo.text){
      return false
    } else {
      return true
    }
  })

  // todos = todos.filter(todo => todo.text !== targetTodo.text)
}


function generateTodoItem (todo) {
  let todoItem, crudButtons, completeButton, deleteButton

  // create a new div for the todo item
  todoItem = document.createElement('div')
  todoItem.innerHTML = `<div>${todo.text}</div>`

  crudButtons = document.createElement('div')

  // add a complete button
  completeButton = document.createElement('button')
  completeButton.innerHTML = 'Complete'
  completeButton.addEventListener('click', ()=>{
    toggleComplete(todo)
    updateTodoList()
  })
  

  // add a delete button
  deleteButton = document.createElement('button')
  deleteButton.innerHTML = 'Delete'
  deleteButton.addEventListener('click', ()=>{
    deleteTodo(todo)
    updateTodoList()
  })

  // add the buttons to the div
  crudButtons.appendChild(completeButton)
  crudButtons.appendChild(deleteButton)

  // add the buttons to the item
  todoItem.appendChild(crudButtons)

  return todoItem
}

function updateTodoList () {
  let todoItem

  // clear both lists
  completeTodoSection.innerHTML = incompleteTodoSection.innerHTML = ''

  todos.forEach(todo => {
    todoItem = generateTodoItem(todo)

    // filter the todos
    if (todo.complete) {
      todoItem.classList.add('complete', 'todo-item')
      completeTodoSection.appendChild(todoItem)
    } else {
      todoItem.classList.add('todo-item')
      // add the new item to the list
      incompleteTodoSection.appendChild(todoItem)
    }
  })
}

updateTodoList()
