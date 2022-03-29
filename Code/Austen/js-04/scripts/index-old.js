import Task from "./Task.js"

// document element shortcut
  var doc = document;
// tasklist arrays
  var tasklist = [new Task({id: 1, name: "test"})];
  var complete = [];
  var tasksSection = doc.getElementById("tasks");
  var completeSection = doc.getElementById("complete-tasks")



// create html template and render it to the page
  function drawTask(task) {
      if (task.complete === false){
      tasksSection.innerHTML += task.template;
    }
  }

// create a new task and add it to the tasks array
  function addtask() {
    let task = prompt("enter the task name: ");
    task = {id: tasklist.length + 1, name: task}
    task = new Task(task)
    tasklist.push(task);
    drawTask(task);
  }


// find and delete an existing task in the array
  function removetask() {
    let remove = prompt("enter the task name: ");
    }

// mark tasks completed, add them to the complete array,
// and move them to the completed section on the page

  function updateTasklist(event) {
    tasklist.forEach((task) => {
      let labelELEM = doc.getElementById(`label-${task.id}`)
      let taskELEM = doc.getElementById(`task-${task.id}`)
      if (taskELEM.checked){
        task.complete = true
        taskELEM.classList.add('visually-hidden')
        labelELEM.classList.add('visually-hidden')
      }
    });
    tasklist.forEach((task) => {
      if (task.complete){
        complete.forEach((completeTask) => {
          if (task.id === completeTask.id){
            complete.pop(completeTask)
          }
        });
        task = new Task({id: task.id, name: task.name, complete: true})
        complete.push(task)
        // console.log(complete)
      }
    });
    completeSection.innerHTML = ''
    complete.forEach(task => {

      completeSection.innerHTML += task.ctemplate
    })
    if (complete.length > 0){
    complete.forEach((task) => {
      let labelELEM = doc.getElementById(`label-${task.id}`)
      let taskELEM = doc.getElementById(`task-${task.id}`)
      if (taskELEM.checked === false){
        task.complete = false
        taskELEM.classList.add('visually-hidden')
        labelELEM.classList.add('visually-hidden')
      }
    });
    complete.forEach((task) => {
      if (task.complete === false){
        complete.forEach((completeTask) => {
          if (task.id === completeTask.id){
            complete.pop(completeTask)
          }
        });
        task = new Task({id: task.id, name: task.name, complete: true})
        // tasklist.push(task)
        console.log(tasklist)
      }
    });
    tasksSection.innerHTML = ''
    tasklist.forEach(task => {
      if (task.complete === false){
      tasksSection.innerHTML += task.template}
    })}
    event.preventDefault();
  }

// startup tasks and event assignments
  tasklist.forEach((task) => drawTask(task))
  doc.getElementById("add").onclick = addtask;
  doc.getElementById("remove").onclick = removetask;
  doc.getElementById("tasklist").onsubmit = updateTasklist;
