let addButton = document.querySelector('#add-task')
let row = document.querySelector('.row')


addButton.addEventListener('click', function () {
    task = prompt("Enter Task: ")
    let todo = document.createElement('div')
    todo.classList.add('todo')
    todo.innerHTML = `
        
        <div class=" col s10 card purple">
            <div class="card-content black-text">  
                <p>
                    ${task}
                        
                </p>
                    
            </div>
        </div>
        
        
        <a id='delete-task' class='col s1 btn-small waves-effect waves-light black'>
            <i class=' material-icons center'>delete</i>
        </a>
        
                `
        
    row.appendChild(todo)

})