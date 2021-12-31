import Task from "./Task.js"

// document element shortcuts
  const doc = document;
  const tasklistELEM = doc.getElementById('tasks')
  const completeELEM = doc.getElementById('complete-tasks')

// tasklist array
  let masterlist = []

// draw tasks to document
  function drawTasks(tasks){
    tasklistELEM.innerHTML = ''
    completeELEM.innerHTML = ''
    masterlist.forEach(task => {
        if (task.complete === false){
          tasklistELEM.innerHTML += task.template
        };
        if (task.complete === true){
          completeELEM.innerHTML += task.template
        }
      }
    )
    masterlist.forEach(task => {
      if (task.complete === true){
        doc.getElementById(`task-${task.id}`).checked = true
        doc.getElementById(`label-${task.id}`).classList.add('complete')
      }
    })
  }
// create a new task and add it to the tasks array
  function addTask() {
    let task = prompt("enter the task name: ");
    task = {id: masterlist.length + 1, name: task, complete: false}
    task = new Task(task)
    masterlist.push(task)
    drawTasks()
  }
// change existing task.complete to 'trash'
  function removeTask() {
    let remove = prompt("enter the task to be removed: ")
    masterlist.forEach(task => {
      if (task.name === remove){
        task.complete = 'trash'
      }
    })
    drawTasks()
    doc.getElementById('deleted-tasks').classList.remove('visually-hidden')
  }
// update task status based on 'checked' attribute
  function updateTasks(event) {
    masterlist.forEach(task => {
      let taskELEM = doc.getElementById(`task-${task.id}`)
      task.complete = taskELEM.checked
    })
    event.preventDefault()
    drawTasks()
  }

// show deleted tasks for reference
  function showTrash(){
    doc.getElementById('show-trash').classList.toggle('visually-hidden')
    doc.getElementById('hide-trash').classList.toggle('visually-hidden')
    masterlist.forEach(task => {
      if (task.complete === 'trash'){
        doc.getElementById('trash').innerHTML += task.template
        doc.getElementById(`task-${task.id}`).classList.add('visually-hidden')
      }
    })
  }
  function hideTrash(){
    doc.getElementById('show-trash').classList.toggle('visually-hidden')
    doc.getElementById('hide-trash').classList.toggle('visually-hidden')
    doc.getElementById('trash').innerHTML = ''
  }
  // element event assignments
    doc.body.onload = drawTasks()
    doc.getElementById("add").onclick = addTask;
    doc.getElementById("remove").onclick = removeTask;
    doc.getElementById("tasklist").onsubmit = updateTasks;
    doc.getElementById("show-trash").onclick = showTrash
    doc.getElementById("hide-trash").onclick = hideTrash
