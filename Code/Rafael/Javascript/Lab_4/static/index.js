
/* ---- Complete/Incomplete ----*/
/* ---- Only one Let prefix,  DOM #targets the html id's  ----*/
let completeTodoSection = document.querySelector('#complete-todoListObject'),
    incompleteTodoSection = document.querySelector('#incomplete-todoListObject'),
    submitButton = document.querySelector('#submit'),
    inputField = document.querySelector('#text')
//console.log(typeof completeTodoSection)

let todoListObject = [
  {text: 'wash sand off vehicle',
  'complete': true },

  {text: 'get an external drive for laptop',
  'complete': false },
  {text: 'mail out holiday cards',
  'complete': true },

  {text: 'sell used video-card on ebay',
  'complete': false },

  {text: 'research recipes for Christmas day',
  'complete': false },
]
//console.log(todoListObject) //*** Array(5)0: {text: 'textValue1', complete: false}1: {text: 'textValue2', complete: true}2: {text: 'textValue3', complete: false}3: {text: 'textValue4', complete: true}4: {text: 'textValue5', complete: false}length: 5 ***

//console.log(typeof todoListObject) // *** object ***

/*---- To create a new todo item from button click with a 'click' event and pass a function for the input field for addTodo input value and make sure to add updateTodoList() to render  ----*/
submitButton.addEventListener('click', ()=>{
  //console.log(inputField.value) //To confirm button is working
  addTodo(inputField.value)
  /*-- Clears the input field text --*/
  inputField.value = ''
  updateTodoList()
})

/* passes a function to take out the text true/false and concatenate the current list and return a new list, completed is set to false boolean */
function addTodo(text){
  let newTodo = {
    text: text,
    completed: false
  }
    /*---- Add the new todo item to the list by concatenations ----*/
  todoListObject = todoListObject.concat(newTodo)

}

/*--- Complete & Incomplete button functionality, flips the complete and incomplete items*/
function toggleComplete(targetTodo){
  todoListObject = todoListObject.map((todo)=>{
    if(todo.text === targetTodo.text){
      return {
        text: todo.text,
        complete: !todo.complete
    }
    /*-- Otherwise return the todo value itself and keep it the same --*/
    } else {
       return todo 
    }  
  })
}

/* *filter* instead of *map* Array method to go through each delete item*/
function deleteTodo(targetTodo){
    todoListObject = todoListObject.filter(todo=>{
      if (todo.text === targetTodo.text){
          return false
      } else {
          return true
      }      
    })
}

/* ---- DOM elements below ----*/
/* ---- Function **generateTodoItem** return todoItem ----*/
function generateTodoItem(todo){
  /*  CRUD  */  
  let todoItem, crudButtons, completeButton, deleteButton;
  /* ----    DIV for HTML        ----*/
  todoItem = document.createElement('div');
  /* ----    ``````` not quotes ``````      ----*/
  todoItem.innerHTML = `<div>${todo.text}</div>`;
 
  /*--- Create CRUD Buttons ---*/
  crudButtons = document.createElement('div')

  /* ---- Create Additional Buttons CRUD **create, read, **update, **delete. These will be added to the function for Left todoItem  ----*/
   /* ---- *Complete Button* ----*/
  completeButton = document.createElement('button');
  completeButton.innerHTML = 'Complete';

  /*--- complete button eventListener to hook up html button and update todo list ---*/ 
  completeButton.addEventListener('click', ()=>{
      toggleComplete(todo)
      updateTodoList()
  })

   /* ---- *Delete Button* ----*/
  deleteButton = document.createElement('button');
  deleteButton.innerHTML = 'Delete';
/*--- delete button eventListener to hook up html button and update todo list ---*/ 
  deleteButton.addEventListener('click', ()=>{
    deleteTodo(todo)
    updateTodoList()
})
   /* ---- *CRUD Buttons* to display the buttons in the div from created buttons above ----*/
  crudButtons.appendChild(completeButton)
  crudButtons.appendChild(deleteButton)

  /* ---- *This will add the buttons to the TodoItem* ----*/
  todoItem.appendChild(crudButtons)

 /* ---- nReturning todoItem will update the Todo array  ----*/
  return todoItem
}

/* ---- CRUD  (create, Read, Update, Delete) ----*/
/* ----  Render a function for todoListObject  part of completeTodoSection above ----*/
/* ---- Function **updateTodoList** return todoItem ----*/
function updateTodoList(){
  let todoItem;

/* ---- Eliminate multiple re-listing of items when adding an item to the list ----*/
  completeTodoSection.innerHTML = incompleteTodoSection.innerHTML = ''

/* ---- Test to return todoItem index value ----*/
  //todoItem = generateTodoItem(todoListObject[0])
  
  /*---- Separate 2 items into Complete/Incomplete using a loop  ----*/
   /*---- Cycle through the todoListObject array via *forEach()*, pulls them into the variable and passes them through the function *(todo=>{})* ----*/
  todoListObject.forEach(todo=>{
      /*--- Indent ---*/
    todoItem = generateTodoItem(todo)
    //console.log(todo)

    /*--- Filters the todoListObject within the .forEach ---*/  
    /*--- if(todo[complete]){} "can be interchanged" when targeting keys or specific target todo[`key-${x}`]  ---*/ 
    if(todo.complete){
         /*---- You can pass multiple, if/else .add()  of complete and incomplete appends  ----*/
        todoItem.classList.add("complete", "todo-item" )
        completeTodoSection.appendChild(todoItem)
    }else{ 
            todoItem.classList.add("todo-item")
            incompleteTodoSection.appendChild(todoItem)
        }
    }) 
  
  /*---- Add Items ----*/
  todoItem.classList.add('todo-item')
  /*---- Add new items to the list ----*/
  incompleteTodoSection.appendChild(todoItem)  
}

/*---- renders and updates the list  ----*/
updateTodoList()