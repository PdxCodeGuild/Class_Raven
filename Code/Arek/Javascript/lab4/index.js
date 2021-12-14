let addButton = document.querySelector('#add-task')
let row = document.querySelector('.row')
let idnum = 0
let completed = document.querySelector('#completed')


addButton.addEventListener('click', function () {
    
    
    task = prompt("Enter Task: ")
    // if cancel is clicked then a card will be created with 'null'
    // need to do input validation as well, the user enters nothing for prompt and presses ok.
    // It will make a card that is blank and too small
    
    var todo = document.createElement('div')
    //adding materialize classes to the new div
    todo.id = idnum
    todo.classList.add('todo')
    todo.classList.add('col')
    todo.classList.add('s12')
    todo.classList.add('m12')
    todo.classList.add('l10')
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
    idnum += 1
    console.log(todo.id)



    
       

    var delButton = todo.querySelector('#delete-task') //at first i had it as 'document.queryselector, that was just selecting the first element with that ID
    var doneButton = todo.querySelector('#task-done')

    delButton.addEventListener('click', function(event) {
        //console.log(event.target.parentNode.parentNode.parentNode)
        
        answer = confirm("Are you sure you want to delete this task? ")
        if (answer == true){
            completed.appendChild(todo)
            completed.removeChild(todo)
            row.removeChild(todo)
            
        }

    })

    doneButton.addEventListener('click', function(){
        // To send the completed ones to the bottom I just created a new container and appended the child to that parent
        todo.style.backgroundColor = '#cbcbcb'
        todo.style.textDecorationLine = 'line-through'
        todo.style.textDecorationStyle = ''
        completed.appendChild(todo)
        
            
        
        
        

    })
    

})





