var doc = document;
var body = doc.body;
var main = doc.querySelector("main");
var tasklist = doc.getElementById("tasklist");
var tasksSection = doc.getElementById("tasks");

var tasks = [];
var templates = [];

function load() {
  body.style.textAlign = "center";
  body.style.fontFamily = "consolas";
  main.style.margin = "4rem";
  main.style.marginTop = "1rem";
  main.style.minHeight = "75vh";
  tasklist.style.margin = "10%";
  tasklist.style.marginTop = "5%";
  tasklist.style.minHeight = "5vh";
  tasklist.style.border = "3px solid black";
  tasksSection.style.textAlign = "start";
}

function drawTask(task) {
  tasks.push(task);
  let template = `
  <div>
    <label for="task-${tasks.indexOf(task)}">${task}</label>
    <input type="checkbox" id="task-${tasks.indexOf(task)}">
  </div>
  `;
  templates.push(template);
  tasksSection.innerHTML += template;
}

function addtask() {
  let task = prompt("enter the task name: ");
  drawTask(task);
}

function removetask() {
  let task = prompt("enter the task name: ");
  let index = tasks.indexOf(task);
  templates.splice(index, 1);
  tasksSection.innerHTML = "";
  templates.forEach((template) => (tasksSection.innerHTML += template));
}

function updateTasklist(event) {
  let updatetasks = tasksSection.children;
  event.preventDefault();
}

body.onload = load();
doc.getElementById("add").onclick = addtask;
doc.getElementById("remove").onclick = removetask;
tasklist.onsubmit = updateTasklist;
