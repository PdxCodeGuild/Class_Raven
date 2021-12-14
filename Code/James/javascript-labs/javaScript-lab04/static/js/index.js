<<<<<<< HEAD
let trash = document.querySelector("trash");

let completeTodoSection = document.querySelector("#complete-todos"),
  incompleteTodoSection = document.querySelector("#incomplete-todos"),
  submitButton = document.querySelector("#submit"),
  inputField = document.querySelector("#text");

let todos = [
  {
    text: "Mow the lawn",
    complete: false,
  },
  {
    text: "Walk the dog",
    complete: false,
  },
  {
    text: "Groceries",
    complete: true,
  },
];

submitButton.addEventListener("click", () => {
  addTodo(inputField.value);
  inputField.value = "";
  updateTodoList();
});

function addTodo(text) {
  let newTodo = {
    text: text,
    completed: false,
  };

  todos = todos.concat(newTodo);
}

function toggleComplete(targetTodo) {
  let newList = [];
  todos.forEach((todo) => {
    if (todo.text === targetTodo.text) {
      newList.push({
        text: todo.text,
        complete: !todo.complete,
      });
    } else {
      newList.push(todo);
    }
  });
  todos = newList
}


function deleteTodo(targetTodo) {
  let deleteList = []
  todos.forEach((todo) => {
    if (todo.text !== targetTodo.text) {
      deleteList.push(todo)
    }  
  });
  todos = deleteList
}

function generateTodoItem(todo) {
  let todoItem, crudButtons;

  todoItem = document.createElement("div");
  todoItem.innerHTML = `<div>${todo.text}</div>`;

  crudButtons = document.createElement("div");

  let completeButton = document.createElement("button");
  let iconComplete = '<i class="fas fa-check fa-lg"></i>';
  completeButton.innerHTML = iconComplete;
  completeButton.addEventListener("click", () => {
    toggleComplete(todo);
    updateTodoList();
  });

  let iconDelete = '<i class="far fa-trash-alt fa-lg"></i>';
  let deleteButton = document.createElement("button");
  deleteButton.innerHTML = iconDelete;
  deleteButton.addEventListener("click", () => {
    deleteTodo(todo);
    updateTodoList();
  });

  crudButtons.appendChild(completeButton);
  crudButtons.appendChild(deleteButton);
  todoItem.appendChild(crudButtons);

  return todoItem;
}

function updateTodoList() {
  let todoItem;

  completeTodoSection.innerHTML = incompleteTodoSection.innerHTML = "";

  todos.forEach((todo) => {
    todoItem = generateTodoItem(todo);

    if (todo.complete) {
      todoItem.classList.add("complete", "todo-item");
      completeTodoSection.appendChild(todoItem);
    } else {
      todoItem.classList.add("todo-item");

      incompleteTodoSection.appendChild(todoItem);
    }
  });
}

updateTodoList();
=======
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
>>>>>>> 5b26694b (prog)
