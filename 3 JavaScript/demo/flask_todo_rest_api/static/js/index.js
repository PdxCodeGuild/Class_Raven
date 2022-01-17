let todoItemTemplate = document.querySelector('#todo-item-template'),
  incompleteTodoList = document.querySelector('#incomplete-todos'),
  completeTodoList = document.querySelector('#complete-todos'),
  newTodoInput = document.querySelector('#new-todo-input'),
  addTodoButton = document.querySelector('#add-todo-button')


// all the api calls will use these
const BASE_URL = 'http://localhost:5000'
const headers = {
  'Content-Type': 'application/json'
}

// get all the todos from the api (only called when the page first loads)
function fetchTodos () {
  let url = BASE_URL + '/todos'

  axios
    .get(url, { headers: headers })
    .then(response => renderTodos(response.data.todos))
    .catch(error => console.log(error))
}

// call the api with the current value of the input field to create a new todo item
function createTodo () {
  let url = BASE_URL + '/todos/create'

  // get the current value from the input field
  let newTodoText = newTodoInput.value
  axios
    .post(url, { text: newTodoText }, { headers: headers })
    .then(response => renderTodos(response.data.todos))
    .catch(error => console.log(error))
}

// when the button is clicked get the text from the input field and create a new todo
addTodoButton.addEventListener('click', createTodo)

// call the api with the id of the clicked todo to toggle it
function toggleComplete (todoId) {
  let url = BASE_URL + '/todos/toggle-complete'

  axios
    .post(url, { todoId: todoId }, { headers: headers })
    .then(response => renderTodos(response.data.todos))
    .catch(error => console.log(error))
}

// call the api with the id of the clicked todo to delete it
function deleteTodo (todoId) {
  let url = BASE_URL + '/todos/delete'

  axios
    .post(url, { todoId: todoId }, { headers: headers })
    .then(response => renderTodos(response.data.todos))
    .catch(error => console.log(error))
}

function renderTodos (todos) {
  let todo,
    templateContent,
    newTodoItem,
    todoText,
    crudIcons,
    completeIcon,
    restoreIcon,
    deleteIcon

  // reset the innerHTML of the todo lists
  incompleteTodoList.innerHTML = completeTodoList.innerHTML = ''

  for (todo of todos) {
    // create a div for the new todo item
    newTodoItem = document.createElement('div')

    // create a copy of the template's inner content
    templateContent = todoItemTemplate.content.cloneNode(true)

    // add the content to the newTodoItem div
    newTodoItem.appendChild(templateContent)

    // select the inner elements of the todo item
    todoText = newTodoItem.querySelector('.todo-text')
    crudIcons = newTodoItem.querySelector('.crud-icons')
    deleteIcon = newTodoItem.querySelector('.crud-icon.delete')
    completeIcon = newTodoItem.querySelector('.crud-icon.complete')

    // set the todo text
    todoText.innerHTML = todo.text

    // attach the todo id to the html element
    deleteIcon.dataset.todoId = completeIcon.dataset.todoId = todo.id

    // when the complete icon is clicked, toggle the clicked todo item's complete value
    completeIcon.addEventListener('click', event => {
      // event.target is the element that was clicked
      // dataset.todoId is targeting the data-todo-id attribute on the html element
      let todoId = event.target.dataset.todoId

      // call the api function
      toggleComplete(todoId)
    })

    // when the complete icon is clicked, delete the clicked todo item
    deleteIcon.addEventListener('click', event => {
      // event.target is the element that was clicked
      // dataset.todoId is targeting the data-todo-id attribute on the html element
      let todoId = event.target.dataset.todoId

      // call the api function
      deleteTodo(todoId)
    })

    if (!todo.complete) {
      // add the newTodoItem to the incomplete list
      incompleteTodoList.appendChild(newTodoItem)
    } else {
      // add line-through style
      todoText.classList.add('complete-todo')

      // replace the complete and delete icons with the restore icon
      crudIcons.innerHTML = `<i class="fas fa-undo-alt crud-icon restore" title="restore"></i>`

      // apply the toggle event listener to the restore icon
      restoreIcon = crudIcons.querySelector('.crud-icon.restore')

      // add the id to the restore icon
      restoreIcon.dataset.todoId = todo.id

      restoreIcon.addEventListener('click', event => {
        // event.target is the element that was clicked
        // dataset.todoId is targeting the data-todo-id attribute on the html element
        let todoId = event.target.dataset.todoId

        // call the api function
        toggleComplete(todoId)
      })

      // add the new todo item to the complete list
      completeTodoList.appendChild(newTodoItem)
    }
  }
}

// load the todos from the database
fetchTodos()
