$(document).ready(function () {
    let todoList = [
    {item : "This is the first item",
    complete : false},
    {item : "This item should be struck through because it is complete",
    complete : true},
    {item : "Go to the store",
    complete : false},
]

let $openList = $("#openList");
let $completeList = $("#completeList");
let $newTask = $("#newTask");

// Generates new todo based on button click
$newTask.click(()=>{
    addTodo()
    createTodoList()
  })

// Opens prompt to take in todo item, and adds it to the list of oustanding tasks
function addTodo() {
    let newTodo = prompt("Enter your todo item: ") // get new todo
    appendTodo(newTodo)
}

// Takes in a new todo from addTodo and appends it to todoList
function appendTodo(todo) {
    let newItem = {
      item: todo,
      complete: false
    }
    todoList = todoList.concat(newItem)
    createTodoList()
    
  }


// delete the todo entry to be removed entirely from the list 
function deleteTodo(todoToDelete){
    for(let i=0; i < todoList.length; i++) {
        if(todoList[i].item === todoToDelete.item){
            todoList.splice(i,1)
            return
        }
    }
}

// Allow the todo item to change to/from open & complete
function changeTodo(targetTodo) {
    for (let i=0; i < todoList.length; i++) {
        if(todoList[i].item === targetTodo.item) {
            todoList[i].complete = !todoList[i].complete
        }
        }
    }



// Create a todo item
function makeNewTodoItem(todo) {
   let $newTodoItem, $newButtons

    // new div for the item
    $newTodoItem = $(`<div>${todo.item}</div>`) 
    $newTodoItem.addClass("col-12 col-lg-6 offset-lg-3")

    $newButtons = makeNewButtons(todo) // make them buttons

    $newTodoItem.append($newButtons)
    console.log($newTodoItem)

    return $newTodoItem
}

// Create complete and delete buttons. Add to new div.
function makeNewButtons(todo) {
    let $buttons, $completeButton, $deleteButton

    $buttons = $('<a></a>')
    $buttons.addClass('mx-2')

    // make a new complete button with function to toggle complete/open
    $completeButton = $(`<button></button>`)
    $completeButton.addClass('bi bi-check-square')
    $completeButton.click(() => {
        changeTodo(todo)
        createTodoList()
    })

    // make a new delete button. add function to delete todo item on click
    $deleteButton = $(`<button></button>`)
    $deleteButton.addClass('bi bi-trash mx-1')
    $deleteButton.click(() => {
        deleteTodo(todo)
        createTodoList()
    })
    $buttons.append([$completeButton, $deleteButton])
    return $buttons
}

// Clear the Todo List
function clearTodoList() {
    $completeList.html('')
    $openList.html('')
}

// Update the Open and Complete lists
function createTodoList () {
    let $todoItem

    clearTodoList()
    todoList.forEach(todo => { // cycles through the todo list items and makes a new div item from makeNewTodoItem.
        $todoItem = makeNewTodoItem(todo)
        // filter the todo items into the completed or open lists
        if (todo.complete) {
            $completeList.append($todoItem)
            
        } else { 
            $openList.append($todoItem)
    }
 }); 
}

createTodoList()

})
