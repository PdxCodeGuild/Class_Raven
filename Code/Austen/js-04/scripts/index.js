// document elements
  var doc = document;
  var body = doc.body;
  var main = doc.querySelector("main");
  var addBtn = doc.getElementById('add')
  var removeBtn = doc.getElementById('remove')
  var updateBtn = doc.getElementById('update')
  var tasklist = doc.getElementById("tasklist");
  var tasksSection = doc.getElementById("tasks");
  var completeSection = doc.getElementById("complete-tasks")
// tasklist arrays
  var tasks = [{id: 1, task: 'test', complete: false}];
  var complete = [];
  var templates = [];

// render structural styling to the page
  function load() {
    body.style.textAlign = "center";
    body.style.fontFamily = "consolas";
    main.style.margin = "4rem";
    main.style.marginTop = "1rem";
    main.style.minHeight = "75vh";
    addBtn.classList.add('btn-dark')
    removeBtn.classList.add('btn-dark')
    updateBtn.classList.add('btn-dark')
    tasklist.style.margin = "10%";
    tasklist.style.marginTop = "5%";
    tasklist.style.minHeight = "5vh";
    tasklist.style.border = "3px solid black";
    tasksSection.style.textAlign = "start";
    tasks.forEach((task) => drawTask(task));
  }

// create html template and render it to the page
  function drawTask(task, complete) {
    if (task.complete === false){
    let template = `
    <div>
      <label for="task-${task.id}" id="label-${task.id}">${task.task}</label>
      <input type="checkbox" name="task-${task.id}" id="task-${task.id}">
    </div>
    `;
    templates.push(template);
    tasksSection.innerHTML += template;}
  }

// create a new task and add it to the tasks array
  function addtask() {
    let task = prompt("enter the task name: ");
    task = {id: tasks.length + 1, task: task, complete: false}
    tasks.push(task);
    drawTask(task);
  }

// find and delete an existing task in the array
  function removetask() {
    let task = prompt("enter the task name: ");
    let index = tasks.indexOf(task);
    templates.splice(index, 1);
    tasksSection.innerHTML = "";
    templates.forEach((template) => (tasksSection.innerHTML += template));
  }

// mark tasks completed, add them to the complete array,
// and move them to the completed section on the page
  function updateTasklist(event) {
    tasks.forEach((task) => {
      let labelELEM = doc.getElementById(`label-${task.id}`)
      let taskELEM = doc.getElementById(`task-${task.id}`)
      if (taskELEM.checked){
        task.complete = true
        taskELEM.classList.add('visually-hidden')
        labelELEM.classList.add('visually-hidden')
      }
    });
    tasks.forEach((task) => {
      if (task.complete){
        complete.forEach((completeTask) => {
          if (task.id === completeTask.id){
            complete.pop(completeTask)
          }
        });
        complete.push(task)
        console.log(complete)
      }
    });
    completeSection.innerHTML = ''
    complete.forEach(task => {
      let template = `
      <div>
        <label style="text-decoration: line-through;" for="task-${task.id}" id="label-${task.id}">${task.task}</label>
        <input checked type="checkbox" name="task-${task.id}" id="task-${task.id}">
      </div>
      `
      console.log(task)
      completeSection.innerHTML += template
    })
    event.preventDefault();
  }

// assign functions to events
  body.onload = load();
  doc.getElementById("add").onclick = addtask;
  doc.getElementById("remove").onclick = removetask;
  tasklist.onsubmit = updateTasklist;
