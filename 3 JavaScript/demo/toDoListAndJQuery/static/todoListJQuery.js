// run the code once the document object has loaded
$(document).ready(function () {
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

  let $incompleteTodoSection = $('#incomplete-todos') // document.querySelector('#incomplete-todos')
  let $completeTodoSection = $('#complete-todos'),
    $submitButton = $('#submit'),
    $inputField = $('#text')

  $submitButton.click(()=>{
    let text = $inputField.val() // get the value
    $inputField.val('')
    addTodo(text)
    updateTodoList()
  })

  function addTodo (text) {
    let newTodo = {
      text: text,
      completed: false
    }
    // add the new todo item to the list
    todos = todos.concat(newTodo)
  }

  // flip the target todo's complete value
  function toggleComplete (targetTodo) {
    todos = todos.map(todo => {
      if (todo.text === targetTodo.text) {
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
  function deleteTodo (targetTodo) {
    todos = todos.filter(todo => {
      if (todo.text === targetTodo.text) {
        return false
      } else {
        return true
      }
    })

    // todos = todos.filter(todo => todo.text !== targetTodo.text)
  }

  function generateTodoItem (todo) {
    let $completeButton, $deleteButton, $crudButtons, $todoItem

    // create the todo item element
    $todoItem = $(`<div>${todo.text}</div>`)

    $crudButtons = $('<div></div>')
    $crudButtons.addClass('crud-buttons') // jquery function to add classes

    // create complete button
    $completeButton = $(`<button>${'Complete'}</button>`)
    $completeButton.click(()=>{
      toggleComplete(todo)
      updateTodoList()
    })
    
    // create delete button
    $deleteButton = $(`<button>Delete</button>`)
    $deleteButton.click(()=>{
      deleteTodo(todo)
      updateTodoList()
    })

    // add the buttons to the container
    $crudButtons.append([$completeButton, $deleteButton])

    $todoItem.append($crudButtons)

    return $todoItem
  }

  function updateTodoList () {
    let $todoItem

    // set the innerHTML
    $incompleteTodoSection.html('')
    $completeTodoSection.html('')

    todos.forEach(todo => {
      $todoItem = generateTodoItem(todo)

      // filter the todos
      if (todo.complete) {
        $todoItem.addClass(['complete', 'todo-item'])
        $completeTodoSection.append($todoItem)
        $todoItem.hide().fadeIn(1000)
      } else {
        $todoItem.addClass('todo-item')
        // add the new item to the list
        $incompleteTodoSection.append($todoItem)
        $todoItem.hide().fadeIn(1000)
      }
    })
  }

  updateTodoList()
})
