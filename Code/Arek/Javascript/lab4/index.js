let addButton = document.querySelector('#add-task')
let row = document.querySelector('.row')


addButton.addEventListener('click', function () {
    task = prompt("Enter Task: ")
    // if cancel is clicked then a card will be created with 'null'
    // need to do input validation as well, the user enters nothing for prompt and presses ok.
    // It will make a card that is blank and too small
    console.log(task)
    var todo = document.createElement('div')
    //adding materialize classes to the new div
    todo.classList.add('todo')
    todo.classList.add('col')
    todo.classList.add('s12')
    todo.classList.add('card')
    todo.style.color = 'black';
    

    todo.innerHTML =
     `
        <div class="card-content">  
            <p'>
                ${task}
                <a id='delete-task' class='btn-small waves-effect waves-light black'>
                    <i class=' material-icons center'>delete</i>
                </a>
                <a id='task-done' class='btn-small waves-effect waves-light'>
                    <i class=' material-icons center'>check</i>
                </a>
                        
            </p>
            
                    
        </div>
                `
    // IF THERE ARE TWO CARDS, YOU HAVE TO DELETE THE FIRST ONE TO BE ABLE TO DELETE THE ONES UNDER
        
    row.appendChild(todo)
    var delButton = document.querySelector('#delete-task')
    var doneButton = document.querySelector('#task-done')

    delButton.addEventListener('click', function() {
        answer = confirm("Are you sure you want to delete this task? ")
        if (answer == true){
            row.removeChild(todo)
        }

    })

    doneButton.addEventListener('click', function(){
        todo.style.backgroundColor = '#2b2b2b'
        //NEED TO FIND A WAY TO USE THE STRIKE() METHOD TO MAKE THE TEST
        // HAVE A LINE THROUGH IT

        // if you have more than one cards it will make them all yellow

    })

})




