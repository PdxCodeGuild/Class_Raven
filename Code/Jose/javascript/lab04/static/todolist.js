let todoInput, addTodo, iList, cList, todoText, completedButton, deleteButton, li, todoTextDiv

todoInput = document.querySelector('#todoInput');
addTodo = document.querySelector('#addTodo');
iList = document.querySelector('#incompletedList');
cList = document.querySelector('#completedList');


addTodo.onclick = function(){
    todoText = todoInput.value;
    todoInput.value = '';


    li = document.createElement('li');
    li.classList.add('todo');
    todoTextDiv = document.createElement('div');
    todoTextDiv.innerHTML = todoText;


    completedButton = document.createElement('button');
    completedButton.innerHTML = '&check;';

    completedButton.onclick = function(){
        iList.removeChild(this.parentElement);
        li = document.createElement('li');
        li.innerText = todoText;
        cList.appendChild(li);
    };

    deleteButton = document.createElement('button');
    deleteButton.innerHTML = '&cross;';
    deleteButton.onclick = function(){
        iList.removeChild(this.parentElement);
    };

    li.appendChild(todoTextDiv);
    li.appendChild(completedButton);
    li.appendChild(deleteButton);
    iList.appendChild(li);
};