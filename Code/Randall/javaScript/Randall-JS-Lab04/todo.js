//Lab4 Todo in JS

//+ button that submits input to be added to the todo list
let add_bt = document.querySelector('#add_bt');
//user input
let todo_input = document.querySelector('#todo_input');
//the todo list
let list = document.querySelector('#todo_list');
//completed list with line through
let completed_list = document.querySelector('#completed_list');
//what happens when you click the + symbol
add_bt.onclick = function() {
    let text = todo_input.value;
    //if you didn't input anything, return nothing
    if (text === '') {
        return;
    }
    //blank list to add items to 
    todo_input.value = '';
    //adding a list item to the to do list
    let li = document.createElement('li');
    li.classList.add('todo_item');
    let text_div = document.createElement('div');
    text_div.innerHTML = text;

    //button with a check mark that deletes an item from the list
    let button_complete = document.createElement('button');
    //check mark
    button_complete.innerHTML = '&#x2713;';
    //function that moves li to the next div (completed) and puts line through
    button_complete.onclick = function() {
        list.removeChild(this.parentElement);
        let li = document.createElement('li');
        li.innerText = text;
        completed_list.appendChild(li);
    };
    //button with an x that deletes a li
    let button_remove = document.createElement('button');
    //x symbol
    button_remove.innerHTML = '&#x2715;';
    //deletes li
    button_remove.onclick = function() {
        list.removeChild(this.parentElement);
    };

    //appends list items to proper parent
    li.appendChild(text_div);
    li.appendChild(button_complete);
    li.appendChild(button_remove);
    list.appendChild(li);
}